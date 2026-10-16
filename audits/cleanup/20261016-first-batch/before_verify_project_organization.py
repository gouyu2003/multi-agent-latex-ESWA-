"""Verify the recorded reorganization, current build, and rendered PDF parity."""
from pathlib import Path
import hashlib
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
RECORD = ROOT / 'audits/organization/20261016'
sys.path.insert(0, str(ROOT / '.cache/python/apa7_vendor'))
from active_tex import scan_manuscript

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    import pymupdf as fitz
    rows = json.loads((RECORD/'file_manifest.json').read_text(encoding='utf-8'))
    changed, missing, lost_bytes = [], [], []
    for row in rows:
        path = ROOT / row['new']
        if not path.is_file():
            missing.append(row['new'])
        elif sha(path) != row['sha256']:
            backup = RECORD/'before_edit'/row['new']
            if not backup.is_file() or sha(backup) != row['sha256']:
                lost_bytes.append(row['new'])
            changed.append(dict(file=row['new'], before_sha256=row['sha256'], after_sha256=sha(path),
                                backup=backup.relative_to(ROOT).as_posix()))
    if missing or lost_bytes:
        raise AssertionError(dict(missing_files=missing, missing_original_backups=lost_bytes))
    changes = json.loads((RECORD/'manuscript_path_changes.json').read_text(encoding='utf-8'))
    before = (RECORD/'before_edit/manuscript.tex').read_bytes()
    expected = before
    for row in changes:
        expected = expected.replace(('{'+row['old']+'}').encode(), ('{'+row['new']+'}').encode())
    manuscript_only_paths_changed = expected == (ROOT/'manuscript.tex').read_bytes()
    assert manuscript_only_paths_changed, 'Unexpected manuscript edit beyond the recorded graphics paths'
    current_scan = scan_manuscript(ROOT)
    before_scan = scan_manuscript(ROOT, 'audits/organization/20261016/before_edit/manuscript.tex')
    commands = lambda scan:[(c.command,c.keys,c.raw_command) for c in scan.citations]
    assert commands(current_scan)==commands(before_scan), 'Citation commands changed'
    active='\n'.join(current_scan.active_texts.values())
    graphics=re.findall(r'\\includegraphics(?:\[[^\]]*\])?\s*\{([^}]+)\}',active)
    assert len(graphics)==5 and all((ROOT/p).is_file() for p in graphics), 'Current figure dependency missing'
    labels=re.findall(r'\\label\{([^}]+)\}',active)
    assert len(labels)==len(set(labels)), 'Duplicate active labels'
    expected_root={'.gitattributes','.gitignore','.latexmkrc','README.md','build.ps1','cas-common.sty','cas-dc.cls',
                   'eswa-apa-config.tex','eswa-apa-sourcemap.tex','manuscript.tex','references.bib'}
    assert {p.name for p in ROOT.iterdir() if p.is_file()}==expected_root, 'Unexpected root-level file'
    assert not any((ROOT/p).exists() for p in ['tmp','output','apa7_audit','audit_work','figure1_audit']), 'Old working directory remains'
    log=(ROOT/'build/latex/manuscript.log').read_text(encoding='utf-8',errors='replace')
    bad=[line for line in log.splitlines() if re.search(r'undefined|multiply defined|Rerun to get|Please \(re\)run|^!',line,re.I)]
    assert not bad, bad
    biber=(ROOT/'build/latex/manuscript.blg').read_text(encoding='utf-8',errors='replace')
    assert not re.search(r'\b(?:ERROR|WARN)\b',biber), 'Biber error or warning'
    old_bbl=(ROOT/'build/baseline_20261016/manuscript.bbl').read_text(encoding='utf-8')
    new_bbl=(ROOT/'build/latex/manuscript.bbl').read_text(encoding='utf-8')
    entries=lambda text:re.findall(r'\\entry\{([^}]+)\}\{([^}]+)\}',text)
    assert entries(old_bbl)==entries(new_bbl), 'Bibliography entries or their ordering changed'
    pages=[]
    with fitz.open(ROOT/'build/baseline_20261016/manuscript.pdf') as old_pdf, fitz.open(ROOT/'build/manuscript.pdf') as new_pdf:
        assert len(old_pdf)==len(new_pdf), 'Page count changed'
        for index,(old,new) in enumerate(zip(old_pdf,new_pdf),1):
            pages.append(dict(page=index,text_identical=old.get_text()==new.get_text(),
                              pixels_identical_72dpi=old.get_pixmap().samples==new.get_pixmap().samples))
    assert all(p['text_identical'] and p['pixels_identical_72dpi'] for p in pages), 'PDF rendering changed'
    record=dict(original_files=len(rows), moved_files=sum(r['old']!=r['new'] for r in rows),
        all_original_bytes_preserved=True, missing_files=[], edited_files=changed,
        manuscript_only_six_graphics_paths_changed=manuscript_only_paths_changed,
        citation_commands_unchanged=True,citation_commands=len(current_scan.citations),
        cited_sources=len({k for c in current_scan.citations for k in c.keys}),
        bibliography_entries=len({key for key,entry_type in entries(new_bbl)}), active_figures=graphics,active_labels_unique=True,
        root_files=sorted(expected_root),four_stage_build_clean=True,pages=pages,
        previous_overfull_count=(ROOT/'build/baseline_20261016/manuscript.log').read_text(errors='replace').count('Overfull'),
        current_overfull_count=log.count('Overfull'))
    (RECORD/'acceptance.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in record.items() if k not in ['edited_files','root_files','active_figures','pages']},indent=2))
    print('PDF parity:',len(pages),'pages, all text and rendered pixels identical.')

if __name__=='__main__':main()
