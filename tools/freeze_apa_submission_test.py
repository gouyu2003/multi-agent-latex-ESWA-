"""Verify a same-level full-manuscript package with a matching prebuilt BBL.

This local test does not certify the ESWA submission server.
"""
from pathlib import Path
import hashlib,json,os,re,shutil,subprocess,sys
import fitz
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'tmp/apa7_migration'/('frozen_full_release' if '--release' in sys.argv else 'frozen_full_final' if '--final' in sys.argv else 'frozen_full')
if OUT.exists():raise SystemExit('Preserve existing evidence; use a fresh directory for another frozen test.')
OUT.mkdir(parents=True);sys.path.insert(0,str(ROOT/'tools'))
from active_tex import scan_manuscript
active='\n'.join(scan_manuscript(ROOT).active_texts.values())
figures=set(re.findall(r'\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}',active))
files=['manuscript.tex','references.bib','cas-dc.cls','cas-common.sty','eswa-apa-config.tex','eswa-apa-sourcemap.tex']+sorted(figures)
for name in files:shutil.copy2(ROOT/name,OUT/Path(name).name)
shutil.copy2(ROOT/'tmp/apa7_build/manuscript.bbl',OUT/'manuscript.bbl')
env=dict(os.environ,TEXINPUTS=str(OUT)+';',BIBINPUTS=str(OUT)+';',LC_ALL='C',LC_CTYPE='C',LANG='C');returncodes=[]
for i in range(1,4):
 p=subprocess.run([r'D:\texlive\2026\bin\windows\pdflatex.exe','-interaction=nonstopmode','-halt-on-error','-file-line-error','-recorder','manuscript.tex'],cwd=OUT,env=env,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
 (OUT/f'pass{i}.console.txt').write_bytes(p.stdout);returncodes.append(p.returncode)
 if p.returncode:print(p.stdout[-3000:].decode('utf-8','replace'));raise SystemExit(p.returncode)
original=fitz.open(ROOT/'manuscript.pdf');frozen=fitz.open(OUT/'manuscript.pdf')
assert len(original)==len(frozen),'Frozen package page count changed'
record=dict(files=files+['manuscript.bbl'],returncodes=returncodes,biber_run=False,pages=len(frozen),text_equal=[a.get_text()==b.get_text() for a,b in zip(original,frozen)],pixels_equal_72dpi=[a.get_pixmap().samples==b.get_pixmap().samples for a,b in zip(original,frozen)],source_hashes={n:hashlib.sha256((OUT/Path(n).name).read_bytes()).hexdigest() for n in files+['manuscript.bbl']})
(ROOT/'apa7_audit/frozen_submission_result.json').write_text(json.dumps(record,ensure_ascii=False,indent=2),encoding='utf-8')
assert all(record['text_equal']) and all(record['pixels_equal_72dpi']),'Frozen package differs from the formal PDF'
print(json.dumps({k:v for k,v in record.items() if k!='source_hashes'},ensure_ascii=False))
