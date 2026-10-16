"""Update active project paths after the recorded one-time file move."""
from pathlib import Path
import hashlib
import io
import json
import re
import tokenize

from organize_project_20261016 import ROOT, RECORD, EXACT, PREFIX

EDITS = []

def write(path, data):
    path = ROOT / path if isinstance(path, str) else path
    before = path.read_bytes()
    if before == data:
        return
    relative = path.relative_to(ROOT).as_posix()
    backup = RECORD / 'before_edit' / relative
    if backup.exists():
        raise RuntimeError('Edit backup already exists: ' + relative)
    backup.parent.mkdir(parents=True, exist_ok=True)
    backup.write_bytes(before)
    path.write_bytes(data)
    EDITS.append(dict(file=relative, before_sha256=hashlib.sha256(before).hexdigest(),
        after_sha256=hashlib.sha256(data).hexdigest(), backup=backup.relative_to(ROOT).as_posix()))

def text_write(path, text):
    path = ROOT / path if isinstance(path, str) else path
    original = path.read_bytes()
    newline = '\r\n' if original.count(b'\r\n') == original.count(b'\n') and b'\n' in original else '\n'
    write(path, text.replace('\r\n','\n').replace('\n',newline).encode('utf-8'))

DIRECTORIES = {old.rstrip('/'): new.rstrip('/') for old,new in PREFIX.items() if old != 'archive/ch'}
DIRECTORIES.update({'tmp/apa7_build':'build/latex', 'tmp/apa7_regression':'build/apa7_regression',
    'tmp/apa7_scanner_tests':'.cache/tests/apa7_scanner_tests',
    'tmp/reference_scan_tests':'.cache/tests/reference_scan_tests'})

def mapped(value):
    if value in EXACT:
        return EXACT[value]
    if value in DIRECTORIES:
        return DIRECTORIES[value]
    # Runtime output paths take precedence over the historical file manifest.
    for old,new in sorted(DIRECTORIES.items(), key=lambda item:len(item[0]), reverse=True):
        if value.startswith(old+'/'):
            return new + value[len(old):]
    for extension in ['pdf','bbl','aux','bcf','blg','log','out','run.xml','synctex.gz','fls','abs']:
        if value == 'manuscript.'+extension:
            return ('build/' if extension=='pdf' else 'build/latex/') + value
    return value

def update_python(path):
    original = path.read_text(encoding='utf-8-sig')
    changes = []
    # Change only complete Python string literals, never substrings in prose,
    # citation keys, stored hashes, or historical ledger JSON/CSV files.
    import ast
    offsets = [0]
    for line in original.splitlines(keepends=True): offsets.append(offsets[-1]+len(line))
    for token in tokenize.generate_tokens(io.StringIO(original).readline):
        if token.type != tokenize.STRING:
            continue
        try: value = ast.literal_eval(token.string)
        except (ValueError,SyntaxError): continue
        if not isinstance(value,str):continue
        new = mapped(value)
        if new != value:
            quote = token.string[:1]
            # All migrated path literals are ordinary single/double quoted strings.
            replacement = quote + new.replace('\\','\\\\').replace(quote,'\\'+quote) + quote
            changes.append((offsets[token.start[0]-1]+token.start[1], offsets[token.end[0]-1]+token.end[1],replacement))
    text = original
    for start,end,replacement in reversed(changes):text=text[:start]+replacement+text[end:]
    if path.name=='test_active_tex.py':
        # Synthetic fixture names stay local to their temporary fixture directory.
        text = text.replace('"build/latex/manuscript.aux"','"manuscript.aux"').replace('"build/latex/manuscript.bbl"','"manuscript.bbl"')
        text = text.replace('/ "tmp" / "reference_scan_tests"','/ ".cache" / "tests" / "reference_scan_tests"')
    if path.name=='test_active_tex_bibpatch.py':
        text=text.replace("/'tmp'/'apa7_scanner_tests'", "/'.cache'/'tests'/'apa7_scanner_tests'")
    if path.name=='generate_reference_figures.py':
        text=text.replace('ROOT / f"fig_reference_corpus.{suffix}"','ROOT / f"figures/figure1/fig_reference_corpus.{suffix}"')
        text=text.replace('ROOT / f"{stem}{suffix}"','ROOT / "archive/figures" / f"{stem}{suffix}"')
    text_write(path,text)

def main():
    if not (RECORD/'move_verification.json').exists():raise RuntimeError('Move verification is required first')
    if (RECORD/'edited_files.json').exists():raise RuntimeError('Paths already updated; do not rerun')
    # Exactly six literal includegraphics paths; the sixth is the disabled legacy figure.
    manuscript = (ROOT/'manuscript.tex').read_bytes()
    changed = manuscript
    replacements = []
    for old,new in EXACT.items():
        needle = ('{'+old+'}').encode('utf-8')
        if needle in changed and old.lower().endswith(('.pdf','.jpg','.png')):
            replacements.append(dict(old=old,new=new,count=changed.count(needle)))
            changed=changed.replace(needle,('{'+new+'}').encode('utf-8'))
    if sum(r['count'] for r in replacements)!=6:raise RuntimeError('Unexpected manuscript graphics path count: '+repr(replacements))
    write('manuscript.tex',changed)
    (RECORD/'manuscript_path_changes.json').write_text(json.dumps(replacements,indent=2)+'\n',encoding='utf-8')
    for path in sorted((ROOT/'tools').glob('*.py')):
        if path.name in {'organize_project_20261016.py','update_organized_paths_20261016.py'}:continue
        update_python(path)
    for path in sorted((ROOT/'tests').rglob('*.py')):update_python(path)
    build = (ROOT/'build.ps1').read_text(encoding='utf-8')
    build=build.replace("'tmp/apa7_build'","'build/latex'")
    start=build.index('    # Publish matching generated artifacts together; sources stay untouched.')
    end=build.index('\n} finally {',start)
    build=build[:start]+'''    # Keep auxiliary files in the build directory; publish only the final PDF.
    $publishedDirectory = Join-Path $projectRoot 'build'
    New-Item -ItemType Directory -Path $publishedDirectory -Force | Out-Null
    Copy-Item -LiteralPath (Join-Path $buildDirectory 'manuscript.pdf') -Destination (Join-Path $publishedDirectory 'manuscript.pdf')
'''.rstrip()+build[end:]
    text_write('build.ps1',build)
    text_write('.latexmkrc',(ROOT/'.latexmkrc').read_text().replace('tmp/apa7_build','build/latex'))
    attributes=(ROOT/'.gitattributes').read_text(encoding='utf-8')
    lines=[]
    for line in attributes.splitlines():
        if line.startswith('/'):
            pattern, sep, rule=line.partition(' ')
            path=pattern[1:]
            path=mapped(path)
            line='/'+path+sep+rule
        lines.append(line)
    text_write('.gitattributes','\n'.join(lines)+'\n')
    ignored='''# Generated build outputs and disposable dependency/preview caches
/build/
/.cache/
__pycache__/
*.py[cod]

# Editor-generated auxiliary files (including direct local TeX builds)
*.aux
*.log
*.out
*.toc
*.lof
*.lot
*.blg
*.bcf
*.run.xml
*.fls
*.fdb_latexmk
*.synctex*
*.nav
*.snm
*.vrb
/manuscript.abs
/manuscript.bbl
/manuscript.pdf

# Preserved local material previously ignored under tmp/ and audit_work/
/audits/references/baselines/
/audits/references/scripts/
/audits/revisions/baselines/
/audits/figures/figure1/baseline/
/audits/figures/figure5/history/
/audits/organization/20261016/before_edit/
/audits/revisions/mentor_restore_stage2_20261013/protection/
/audits/revisions/mentor_restore_stage2_20261013/concurrent_protection/
/audits/revisions/mentor_restore_stage2_20261013/pdf_review/
/audits/revisions/mentor_restore_stage2_20261013/q5_sources/
/audits/revisions/mentor_restore_stage2_20261013/candidate.tex
/audits/revisions/mentor_restore_stage2_20261013/compiled_text.txt
/audits/revisions/mentor_restore_stage2_20261013/mentor_original.tex
/audits/revisions/mentor_restore_stage2_20261013/restored_manuscript.pdf
/audits/figures/replacement_20261013/preview/
/audits/figures/replacement_20261013/before_manuscript.bbl
/audits/figures/replacement_20261013/before_manuscript.pdf
/audits/figures/replacement_20261013/before_manuscript.tex

# OS metadata and Office lock files
Thumbs.db
Desktop.ini
.DS_Store
~$*
'''
    text_write('.gitignore',ignored)
    (RECORD/'edited_files.json').write_text(json.dumps(EDITS,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print('Updated',len(EDITS),'active text files; original bytes saved in before_edit/.')

if __name__=='__main__':main()
