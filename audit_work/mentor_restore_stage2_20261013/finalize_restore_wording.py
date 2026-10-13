from pathlib import Path
import json,hashlib,difflib
OUT=Path(__file__).resolve().parent;ROOT=OUT.parents[1]
p=ROOT/'manuscript.tex';data=p.read_bytes();s=data.decode('utf8').replace('\r\n','\n')
ops=json.loads((OUT/'operations.json').read_text(encoding='utf8'))
def change(ids,a,b):
 global s
 assert s.count(a)==1,(ids,s.count(a))
 at=s.index(a);ops.append(dict(ids=ids.split(','),before=a,after=b,line_at_operation=s[:at].count('\n')+1,reason='Final approved-boundary review'))
 s=s.replace(a,b,1)
change('D028','Hybrid architectures are useful when task requirements are heterogeneous or when the workflow must combine deliberation, controlled execution, and conditional review through changes in decision authority.', 'Hybrid architectures are useful when task requirements are heterogeneous or when the workflow must combine deliberation, controlled execution, and conditional review, provided that decision authority changes across stages or decision states.')
change('D042', '''The approach is examined for interpretive consistency using ten published
systems. This purposive sample contains both core QA studies and supporting
workflow examples; it does not evaluate performance, establish causal benefit,
or provide independent validation. The proposed labels and criterion profiles
are retained, while reported workflows are coded by decision authority.''', '''The approach is verified for interpretive consistency by comparing its
inferred architectures with ten published systems. This purposive sample was
selected because the systems report agent roles and control flow with enough
detail for coding and cover different domains, process structures, and risk
levels. The comparison does not evaluate system performance, establish causal
benefit, or claim external validity. It contains both core QA studies and
supporting workflow examples and is not independent validation. The proposed
labels and criterion profiles are retained, while reported workflows are
coded by decision authority.''')
change('D043', '''architecture. LegalGraphRAG and EduPlanner remain divergent. Du et al.'s
peer debate remains flat despite repeated rounds, and Financial Reflection
QA remains hierarchical despite critic feedback. Nine reported workflows''', '''architecture. LegalGraphRAG and EduPlanner remain divergent. Du et al.'s
peer debate is flat at the macro level but uses iterative convergence;
EduPlanner and Financial Reflection QA combine convergent objectives with
evaluator or critic feedback. These boundary cases show that competing
requirements can make a single categorical label insufficient and that a
multi-label description of control flow may sometimes be preferable,
provided that overall authority and local mechanisms are distinguished.
Financial Reflection QA remains hierarchical despite critic feedback.
Nine reported workflows''')
change('D050b','For example, \nAnthropic introduced','For example, Anthropic introduced')
new=s.replace('\n','\r\n').encode('utf8') if b'\r\n' in data else s.encode('utf8')
assert p.read_bytes()==data,'Concurrent edit; stop'
p.write_bytes(new)
(OUT/'candidate.tex').write_bytes(new)
(OUT/'operations.json').write_text(json.dumps(ops,ensure_ascii=False,indent=2),encoding='utf8')
before=(OUT/'protection/manuscript.tex').read_text(encoding='utf8')
(OUT/'before_after.patch').write_text(''.join(difflib.unified_diff(before.splitlines(True),s.splitlines(True),fromfile='pre_restore/manuscript.tex',tofile='restored/manuscript.tex')),encoding='utf8')
print('Final wording review applied; total operations',len(ops),hashlib.sha256(new).hexdigest())
