from pathlib import Path
import json,difflib
out=Path(__file__).resolve().parent;root=out.parents[1];p=root/'manuscript.tex';data=p.read_bytes();s=data.decode('utf8').replace('\r\n','\n')
a='''  LLM-MedQA against the v1 preprint, Sections~III-A--F and Algorithm~1,
  without a new check of the final conference PDF.'''
b='''  LLM-MedQA against the IJCNN 2025 paper, Sections~III-A--F and Algorithm~1
  (physical pages 3--6).'''
assert s.count(a)==1
ops=json.loads((out/'operations.json').read_text(encoding='utf8'));ops.append(dict(ids=['D048a'],before=a,after=b,line_at_operation=s[:s.index(a)].count('\n')+1,reason='Final IJCNN2025 local source found and independently re-read in current workspace'))
s=s.replace(a,b,1);new=s.replace('\n','\r\n').encode('utf8') if b'\r\n' in data else s.encode('utf8')
assert p.read_bytes()==data
p.write_bytes(new);(out/'candidate.tex').write_bytes(new);(out/'operations.json').write_text(json.dumps(ops,ensure_ascii=False,indent=2),encoding='utf8')
before=(out/'protection/manuscript.tex').read_text(encoding='utf8');(out/'before_after.patch').write_text(''.join(difflib.unified_diff(before.splitlines(True),s.splitlines(True),fromfile='pre_restore/manuscript.tex',tofile='restored/manuscript.tex')),encoding='utf8')
