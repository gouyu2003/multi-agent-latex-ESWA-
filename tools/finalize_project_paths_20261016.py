"""Finish path integration while preserving all original scripts and records."""
from pathlib import Path
import ast
import json
import re

from organize_project_20261016 import ROOT, RECORD, PREFIX

def write(relative, data):
    path = ROOT / relative
    if path.exists():
        old = path.read_bytes()
        if old == data:return
        backup = RECORD/'before_edit'/relative
        if not backup.exists():
            backup.parent.mkdir(parents=True,exist_ok=True)
            backup.write_bytes(old)
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_bytes(data)

def encode_like(text, original):
    newline='\r\n' if b'\n' in original and original.count(b'\r\n')==original.count(b'\n') else '\n'
    return text.replace('\r\n','\n').replace('\n',newline).encode('utf-8')

def route_script(relative):
    path=ROOT/relative
    backup=RECORD/'before_edit'/relative
    original=backup.read_bytes() if backup.exists() else path.read_bytes()
    text=original.decode('utf-8-sig').replace('\r\n','\n')
    if relative=='tools/freeze_apa_submission_test.py':
        text=text.replace("OUT=ROOT/'tmp/apa7_migration'", "OUT=ROOT/'build/frozen'")
        text=text.replace('for name in files:shutil.copy2(ROOT/name,OUT/Path(name).name)',
            "for name in files:\n target=OUT/name;target.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(ROOT/name,target)")
        text=text.replace("OUT/Path(n).name", "OUT/n")
    for old in ["WORK / 'stage2_sources'",'WORK / "stage2_sources"']:
        text=text.replace(old,"ROOT / 'audits/references/stage2_sources'")
    for name in ['before_reference_corrections_20261008.zip','before_stage2_completion_20261010.zip','before_triad_role_update_20261010.zip']:
        text=re.sub(r"WORK\s*/\s*(['\"])"+re.escape(name)+r"\1", "ROOT / 'audits/revisions/backups/"+name+"'",text)
    # ZIP member names and saved manifest keys remain exactly as originally stored.
    tree=ast.parse(text)
    lines=text.splitlines(keepends=True)
    offsets=[0]
    for line in lines:offsets.append(offsets[-1]+len(line))
    def position(line,col):
        return offsets[line-1]+len(lines[line-1].encode('utf-8')[:col].decode('utf-8'))
    changes=[]
    for node in ast.walk(tree):
        if isinstance(node,ast.BinOp) and isinstance(node.op,ast.Div) and isinstance(node.left,ast.Name) and node.left.id=='ROOT':
            if isinstance(node.right,ast.Constant) and node.right.value=='tools':continue
            right=ast.get_source_segment(text,node.right)
            changes.append((position(node.lineno,node.col_offset),position(node.end_lineno,node.end_col_offset),'project_path('+right+')'))
    for start,end,replacement in sorted(changes,reverse=True):text=text[:start]+replacement+text[end:]
    if changes:
        if relative.startswith('tests/'):
            bootstrap="sys.path.insert(0,str(ROOT/'tools'))"
            assert bootstrap in text,relative
            text=text.replace(bootstrap,bootstrap+'\nfrom project_paths import project_path',1)
        else:
            tree=ast.parse(text)
            imports=[n for n in tree.body if isinstance(n,ast.ImportFrom) and n.module=='__future__']
            first=tree.body[0]
            anchor=max([n.end_lineno for n in imports] or ([first.end_lineno] if isinstance(first,ast.Expr) and isinstance(first.value,ast.Constant) and isinstance(first.value.value,str) else [0]))
            parts=text.splitlines(keepends=True)
            parts.insert(anchor,'from project_paths import project_path\n')
            text=''.join(parts)
    if relative=='tools/test_active_tex.py':
        text=text.replace('/ "tmp" / "reference_scan_tests"','/ ".cache" / "tests" / "reference_scan_tests"')
    if relative=='tests/test_active_tex_bibpatch.py':
        text=text.replace("/'tmp'/'apa7_scanner_tests'", "/'.cache'/'tests'/'apa7_scanner_tests'")
    if relative=='tools/active_tex.py':
        text=text.replace('stem = Path(main).with_suffix("")','stem = Path(main).with_suffix("")\n    artifact_root = root / "build/latex" if (root / "build/latex" / stem.with_suffix(".aux")).exists() else root')
        text=text.replace('read_aux(root / m.group(2))','read_aux(artifact_root / m.group(2))')
        text=text.replace('read_aux(root / stem.with_suffix(".aux"))','read_aux(artifact_root / stem.with_suffix(".aux"))')
        text=text.replace('bbl = root / stem.with_suffix(".bbl")','bbl = artifact_root / stem.with_suffix(".bbl")')
    ast.parse(text)
    write(relative,encode_like(text,original))

def main():
    directories={old.rstrip('/'):new.rstrip('/') for old,new in PREFIX.items() if old!='archive/ch'}
    runtime={'tmp/apa7_build':'build/latex','tmp/apa7_regression':'build/apa7_regression',
             'tmp/apa7_scanner_tests':'.cache/tests/apa7_scanner_tests','tmp/reference_scan_tests':'.cache/tests/reference_scan_tests'}
    runtime['manuscript.pdf']='build/manuscript.pdf'
    for extension in ['bbl','aux','bcf','blg','log','out','run.xml','synctex.gz','fls','abs']:
        runtime['manuscript.'+extension]='build/latex/manuscript.'+extension
    (RECORD/'directory_mapping.json').write_text(json.dumps(dict(prefixes=directories,runtime=runtime),indent=2)+'\n',encoding='utf-8')
    manifest=json.loads((RECORD/'file_manifest.json').read_text(encoding='utf-8'))
    for row in manifest:
        if row['old'].startswith(('tools/','tests/')) and row['old'].endswith('.py') and row['old'] not in ['tools/organize_project_20261016.py','tools/update_organized_paths_20261016.py']:
            route_script(row['new'])
    # LaTeX Workshop is installed locally; direct its auto-build and viewer to the same output folder.
    settings={
        'latex-workshop.latex.outDir':'%DIR%/build/latex',
        'latex-workshop.latex.recipe.default':'first',
        'latex-workshop.latex.recipes':[{'name':'ESWA: pdfLaTeX + Biber','tools':['eswa-build']}],
        'latex-workshop.latex.tools':[{'name':'eswa-build','command':'powershell.exe',
            'args':['-NoProfile','-File','%DIR%/build.ps1']}],
    }
    write('.vscode/settings.json',(json.dumps(settings,indent=2)+'\n').encode('utf-8'))
    print('Integrated current paths; preserved original historical keys and ZIP member paths.')

if __name__=='__main__':main()
