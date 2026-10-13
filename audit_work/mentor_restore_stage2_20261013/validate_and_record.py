from pathlib import Path
import csv,collections,difflib,hashlib,json,re,subprocess,sys
OUT=Path(__file__).resolve().parent;ROOT=OUT.parents[1]
sys.path.insert(0,str(ROOT/'tools'))
from active_tex import scan_manuscript
from build_reference_inventory import balanced_entries
def write(name,obj): (OUT/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2),encoding='utf8')
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
before=(OUT/'protection/manuscript.tex').read_text(encoding='utf8');after=(ROOT/'manuscript.tex').read_text(encoding='utf8')
ops=json.loads((OUT/'operations.json').read_text(encoding='utf8'));items=json.loads((OUT/'plan_items.json').read_text(encoding='utf8'))
replay=before
for o in ops:
 assert replay.count(o['before'])==1,(o['ids'],'non-unique replay')
 replay=replay.replace(o['before'],o['after'],1)
assert replay==after,'Unrecorded body modification: stop'
assert collections.Counter(x['class'] for x in items)=={'A':64,'B':25,'C':30}
assert all(any(x['id'] in o['ids'] for o in ops) for x in items if x['class']=='B')
QMAP={'D007':'Q1','D009b':'Q3','D010a':'Q3','D012':'Q2','D013b':'Q2'}
for x in items:
 if x['class']=='C' and x['id'] not in QMAP:QMAP[x['id']]='Q5' if x['id'] in ['D042','D043','D045a','D045b','D045c','D046b','D047b','D048a','D084b'] else 'Q4'
def final_excerpt(x):
 old=x['pre_restore_plan'] or ''
 if old.rstrip('\n') in after:return old.rstrip('\n'),[]
 related=[o for o in ops if any(k[:4]==x['block'] for k in o['ids']) or (old.strip() and (old.strip() in o['before'] or o['before'] in old))]
 excerpts=[]
 for o in related:
  new=o['after']
  for later in ops[ops.index(o)+1:]:
   if later['before'] in new:new=new.replace(later['before'],later['after'],1)
  if new and new not in excerpts:excerpts.append(new)
 return '\n\n'.join(excerpts) if excerpts else '[保留删除或格式成果；见保护验证及实际补丁]',[ops.index(o)+1 for o in related]
records=[];lines=['# 阶段二逐项实际执行记录','', '2026-10-13。导师基线 f84c78b；执行前 HEAD 6191a1b。119项：A64/B25/C30。', '', 'before/after 为实际片段或同段必要联动片段。表内移动的条目附完整共同操作，不能将同一表的联动重复当作新授权。完整顺序补丁见 operations.json 和 before_after.patch。','']
for x in items:
 excerpt,opnums=final_excerpt(x);applied=[i+1 for i,o in enumerate(ops) if x['id'] in o['ids']]
 status=('必要纠错成果保留；共享片段仅按批准B/C边界恢复' if x['class']=='A' else ('完整恢复' if x['id'] in ['D004','D011','D019','D025','D057','D078'] else '局部恢复') if x['class']=='B' else QMAP[x['id']]+'已执行'+('（保留当前已符合批准规则的片段）' if not applied else '（按批准方案联动）'))
 rec=dict(id=x['id'],category=x['class'],status=status,approved_decision=x['decision'],mentor=x['mentor'],before=x['pre_restore_plan'],after=excerpt,operation_numbers=applied or opnums)
 records.append(rec);lines.extend([f"## {x['id']} — {x['class']} — {status}",'',f"操作编号：{rec['operation_numbers']}。",'', '**before**','```tex',x['pre_restore_plan'] or '[无当前片段]','```','', '**after**','```tex',excerpt,'```',''])
write('execution_ledger.json',records);(OUT/'EXECUTION_LEDGER.md').write_text('\n'.join(lines),encoding='utf8')
scan0=scan_manuscript(OUT/'protection');scan=scan_manuscript(ROOT)
keys0={k for c in scan0.citations for k in c.keys};keys={k for c in scan.citations for k in c.keys};entries=balanced_entries((ROOT/'references.bib').read_text(encoding='utf8'))
roles={r['key']:r['evidence_role'] for r in csv.DictReader((ROOT/'literature_audit.csv').open(encoding='utf-8-sig'))}
assert len(entries)==85 and len(keys)==78 and keys==keys0
core=sorted(k for k in keys if roles[k]=='I');assert len(core)==13 and core==sorted(k for k in keys0 if roles[k]=='I') and roles['hu2024triad']=='S'
poolroles=dict(collections.Counter(roles[k] for _,k,_ in entries));citeroles=dict(collections.Counter(roles[k] for k in keys))
assert poolroles=={'I':13,'S':17,'B':46,'T':9};assert citeroles=={'I':13,'S':15,'B':42,'T':8}
preserved={}
for label,pat in [('all_figure_environments',r'\\begin\{figure\*?\}.*?\\end\{figure\*?\}'),('conclusion',r'\\section\{Conclusion\}(.*?)(?=\\section\*|\\printbibliography)'),('hidden_history',r'\\iffalse.*?\\fi'),('section_order',r'\\(?:sub)*section\{[^}]+\}'),('taxonomy_definition',r'This review classifies.*?Figure~\\ref\{fig:topology\}')]:
 a=re.findall(pat,before,re.S);b=re.findall(pat,after,re.S);assert a and a==b,label;preserved[label]=True
assert before[:before.index('review of multi-agent collaborative QA using')]==after[:after.index('review of multi-agent collaborative QA based')]
table=re.search(r'\\begin\{table\*\}.*?\\label\{tab:9categories\}.*?\\end\{table\*\}',after,re.S)[0]
assert table.count(r'\multicolumn{6}')==2 and table.count('    --- &')==5
assert all(r'\textbf{'+k+'}' in table for k in ['Flat','Hierarchical','Hybrid'])
assert r'\multirow' not in table
cases=json.loads((ROOT/'audit_work/case_classification_audit.json').read_text(encoding='utf8'))['cases']
rules={
 'tang2024medagents':dict(F1=True,F2=True,F3=True,locator='ACL 2024 §§2.1–2.5, Algorithm1, printed601–603',basis='各领域专家给出分析；全专家用同一yes/no提示审同一报告；no产生修改意见并进入更新后重审。t上限；固定报告修订和最终决策仍H。'),
 'tang2025llmmedqa':dict(F1=True,F2=True,F3=True,locator='正式IJCNN2025 §§III-A–F, Algorithm1, physical3–6；v1作补充',basis='question与option专家逐角色分析；共同报告交所有专家同规则Approve/Reject；Reject意见整合进修订并重投。Algorithm1有k上限；§III-F固定MakeDecision仍H。F1是角色贡献，不是统计独立；option分析可参照question分析。'),
 'legalgraphrag2026':dict(local_hybrid_authority_change=False,locator='批准方案：正式§4.3/Fig3, printed37459–37460',basis='Researcher→Auditor→Adjudicator固定不对称链；没有来源定位的决策权配置切换。'),
 'zhang2024eduplanner':dict(F2=False,locator='批准方案：v1 §III-C–E/Algorithms1–3；历史正式版定位未重新认证',basis='evaluator具有固定评分权，optimizer/analyst给出反馈；不是各专家对同一共同报告具同等复核权限。'),
}
ratings=[]
for c in cases:
 p=c['prior_proposed_label'];s=c['source_based_label'];local=rules.get(c['key'],{})
 score='broad' if p==s else 'partial' if p=='Flat' and all(local.get(k) is True for k in ['F1','F2','F3']) else 'divergent'
 ratings.append(dict(key=c['key'],name=c['name'],role=c['evidence_role'],proposed=p,source_overall=s,rating=score,evidence=local or dict(locator=c['locator'],basis=c['source_evidence'],version_boundary='沿用已批准方案/现有来源台账；本轮不声称再次核读全部原文')))
count=dict(collections.Counter(c['rating'] for c in ratings));sourcecount=dict(collections.Counter(c['source_overall'] for c in ratings));assert count=={'broad':6,'partial':2,'divergent':2};assert sourcecount=={'Hierarchical':9,'Flat':1}
vtable=after[after.index(r'\label{tab:validation}'):];vtable=vtable[:vtable.index(r'\end{tabularx}')]
assert vtable.count(r'$\checkmark$')==6 and vtable.count(r'$\triangle$')==2 and vtable.count(r'$\times$')==2
write('q5_case_scores.json',dict(rule='按批准Q5先整体类别，异类再局部机制；F1/F2/F3合取；资料不足不评分',cases=ratings,rating_counts=count,source_counts=sourcecount,denominator=10,independent_validation=False,performance_measurement=False))
ql=['# Q5来源再核查与逐例评分','', '2026-10-13。MedAgents正式ACL全文及LLM-MedQA正式IJCNN2025全文重新核读；其余八例沿用已批准方法证据及冻结P/S。','', '## F1/F2/F3证据','', '| 案例 | F1 | F2 | F3 | 定位与边界 |','|---|---|---|---|---|']
for k in ['tang2024medagents','tang2025llmmedqa']:
 x=rules[k];ql.append(f"| {k} | 成立 | 成立 | 成立 | {x['locator']}；{x['basis']} |")
ql+=['','MedAgents的全专家复核见Algorithm1 for i=1…n；LLM-MedQA的for each expert采用同一pvote。二者专家反对意见进入固定修订模型，后续轮次再审；达到上限时并不保证一致。LLM-MedQA算法的c_draft/current_draft/cc_draft名称不完全一致，§III-E及式(7)清楚说明修订与再次复核；本轮不执行原论文代码，也不据伪代码证明实现性能。','', '正式LLM-MedQA PDF SHA256：4c27d253f6df5b9834392cc4550db905b3e47eaf6e3732a414c76480398d226b。原本方案的不可重读限制在当前机器已解除。旧方案/旧台账保留原样，只在本轮记录及新表注更新。','', '[MedAgents ACL正式论文](https://aclanthology.org/2024.findings-acl.33.pdf)；[LLM-MedQA v1补充文本](https://arxiv.org/html/2501.05464v1)。正式IJCNN PDF位于用户本地10.10ziliao目录，保护副本及全文提取见q5_sources。','', '## 十案例','', '| 案例 | 角色 | P | S | 评分 | 依据 |','|---|---|---|---|---|---|']
for c in ratings:ql.append(f"| {c['name']} | {c['role']} | {c['proposed']} | {c['source_overall']} | {dict(broad='广泛一致',partial='部分一致',divergent='不一致')[c['rating']]} | {c['evidence']['basis']} |")
ql+=['','复算：6广泛一致、2部分一致、2不一致；9H/1F/0Hybrid，分母10。作者回顾性组织相容分析，非预测准确率、独立验证、实测性能或安全提升。']
(OUT/'Q5_SOURCE_RECHECK.md').write_text('\n'.join(ql),encoding='utf8')
mentor=(OUT/'mentor_original.tex').read_text(encoding='utf8')
def prose(t):
 t=re.sub(r'\\iffalse.*?\\fi','',t,flags=re.S);t=re.sub(r'(?m)(?<!\\)%.*','',t);t=re.sub(r'\\begin\{(figure\*?|table\*?|equation\*?)\}.*?\\end\{\1\}','',t,flags=re.S);t=re.sub(r'\\(?:cite\w*|ref|label|input|includegraphics)(?:\[[^\]]*\])*\{[^}]*\}','',t)
 return re.findall(r"[A-Za-z]+(?:[-'][A-Za-z]+)*",t)
metric={};a=prose(mentor)
for label,t in [('before',before),('after',after)]:
 b=prose(t);m=difflib.SequenceMatcher(None,a,b,autojunk=False);metric[label]=dict(tokens=len(b),changed_tokens=sum(i2-i1+j2-j1 for tag,i1,i2,j1,j2 in m.get_opcodes() if tag!='equal'),similarity=m.ratio())
assert metric['after']['changed_tokens']<metric['before']['changed_tokens']
write('mentor_prose_comparison.json',dict(method='去注释、iffalse、图/表/展示公式及cite/ref/label/input/includegraphics；按英文词元SequenceMatcher(autojunk=False)。只是可重复编辑距离代理指标，不是导师风格的定量证明。',mentor_tokens=len(a),metrics=metric))
(OUT/'mentor_to_restored.patch').write_text(''.join(difflib.unified_diff(mentor.splitlines(True),after.splitlines(True),fromfile='mentor_f84c78b/manuscript.tex',tofile='restored/manuscript.tex')),encoding='utf8')
manifest=json.loads((OUT/'protected_manifest.json').read_text());changes=[]
for x in manifest:
 p=ROOT/x['path'];assert p.exists(),('Missing protected file',x['path'])
 if sha(p)!=x['sha256']:changes.append(x['path'])
allowed_generated={'manuscript.pdf','manuscript.aux','manuscript.bbl','manuscript.bcf','manuscript.blg','manuscript.run.xml','manuscript.out','manuscript.log','manuscript.fls','manuscript.abs','manuscript.synctex.gz'}
concurrent=json.loads((OUT/'concurrent_changes.json').read_text(encoding='utf8')) if (OUT/'concurrent_changes.json').exists() else []
for x in concurrent:
 assert sha(ROOT/x['path'])==x['current_sha256'],('Concurrent file changed again; preserve new version',x['path'])
external={x['path'] for x in concurrent}
unexpected=[p for p in changes if p!='manuscript.tex' and p not in allowed_generated and p not in external];assert not unexpected,unexpected
write('static_acceptance.json',dict(pool=85,cited=78,core=core,pool_roles=poolroles,cited_roles=citeroles,cited_key_set_identical=True,citation_commands_before=len(scan0.citations),citation_commands_after=len(scan.citations),citation_key_appearances=sum(len(c.keys) for c in scan.citations),command_count_reason='Q4合并层级两行引用为一条命令，键出现次数180及唯一键78不变',protected_regions=preserved,all_changes_recorded=True,unauthorised_body_changes=False,protected_file_count=len(manifest),changed_existing_files=changes,concurrent_external_changes=concurrent,unexpected_protected_changes=unexpected,q4_three_classes_five_mechanisms=True,q5_counts=count,q5_source_counts=sourcecount,mentor_metrics=metric,head=subprocess.check_output(['git','rev-parse','HEAD']).decode().strip(),branch=subprocess.check_output(['git','branch','--show-current']).decode().strip()))
print('Static acceptance PASS; A64/B25/C30 recorded;',metric,'protected file changes',changes)
