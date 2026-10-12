"""Run one recorded build stage without changing TeX installation settings."""
from pathlib import Path
import json,os,shutil,subprocess,sys,time
ROOT=Path(__file__).resolve().parents[1]
def engine(name):
 found=shutil.which(name)
 if not found:raise SystemExit('Required TeX engine not found on PATH: '+name)
 return found
stage=sys.argv[1]; directory=Path(sys.argv[2]).resolve(); jobs=sys.argv[3:]
directory.mkdir(parents=True,exist_ok=True)
env=dict(os.environ,TEXINPUTS=str(directory)+';'+str(ROOT)+';',BIBINPUTS=str(directory)+';'+str(ROOT)+';',LC_ALL='C',LC_CTYPE='C',LANG='C')
results=[]
for job in jobs:
 if stage in ('biber','bibtex'): cmd=[engine(stage),job]; cwd=directory
 else:
  source=directory/(job+'.tex')
  if not source.exists(): source=ROOT/(job+'.tex')
  cmd=[engine('pdflatex'),'-interaction=nonstopmode','-halt-on-error','-file-line-error','-recorder','-output-directory='+str(directory),str(source)]; cwd=ROOT
 start=time.time(); p=subprocess.run(cmd,cwd=cwd,env=env,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
 (directory/(job+'.'+stage+'.console.txt')).write_bytes(p.stdout)
 r=dict(stage=stage,job=job,returncode=p.returncode,seconds=round(time.time()-start,2),command=cmd); results.append(r); print(json.dumps(r))
 if p.returncode: print(p.stdout[-4000:].decode('utf-8','replace')); break
(directory/('build_'+stage+'.json')).write_text(json.dumps(results,indent=2),encoding='utf-8')
if any(r['returncode'] for r in results): sys.exit(1)
