"""Rebuild all APA gates with the current project configuration, in ignored tmp."""
from project_paths import project_path
from pathlib import Path
import shutil,subprocess,sys
ROOT=Path(__file__).resolve().parents[1]; OUT=project_path('tmp/apa7_regression');OUT.mkdir(parents=True,exist_ok=True)
for source in (project_path('tests/apa7')).iterdir():
 if source.is_file():shutil.copy2(source,OUT/source.name)
jobs=['probe','types_fixed','pool78','commands78','pool85']
for stage in ['pass1','biber','pass2','pass3']:
 subprocess.run([sys.executable,'-B',str(project_path('tools/build_apa_stage.py')),stage,str(OUT),*jobs],cwd=ROOT,check=True)
subprocess.run([sys.executable,'-B',str(OUT/'validate.py')],cwd=ROOT,check=True)
print('Rebuilt final-configuration APA tests:',OUT)
