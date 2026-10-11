from pathlib import Path
import collections, hashlib, json, re, subprocess, sys
import fitz
HERE=Path(__file__).resolve().parent
ROOT=next(p for p in HERE.parents if (p/'manuscript.tex').exists())
sys.path.insert(0,str(ROOT/'tools'))
from build_reference_inventory import balanced_entries, parse_fields

def norm(s):
    # Undo typesetter's alphabetic line-end hyphenation for prose comparison.
    # Link targets, rather than this normalized text, verify URL identities.
    s=re.sub(r'(?<=[A-Za-z])-\n(?=[A-Za-z])','',s)
    return re.sub(r'\s+',' ',s).strip()
def pdftext(job): return '\n'.join(p.get_text() for p in fitz.open(HERE/(job+'.pdf')))
overlay={r['key']:r for r in json.loads((ROOT/'apa_reference_adaptations.json').read_text(encoding='utf-8'))['records']}
def adapted(k):
    f=next(parse_fields(r) for t,key,r in balanced_entries((HERE/'types_fixed.bib').read_text(encoding='utf-8')) if key==k)
    f.update(overlay[k]['updates']);return {k:v for k,v in f.items() if v is not None}
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
docs={j:pdftext(j) for j in ['probe','types_fixed','pool78','commands78']}
for j,t in docs.items(): (HERE/(j+'_extracted.txt')).write_text(t,encoding='utf-8')
raw=docs['probe']; text=norm(raw)
refs=text.split('References',1)[1]
labels=['TWO-P','TWO-T','THREE-FIRST','IDENTICAL','INITIALS','YAO','FINAL-P','FINAL-T','CORPORATE','NOTES','ALT','TEXT-NOTES']
cit={}
for i,l in enumerate(labels):
    end=labels[i+1]+':' if i+1<len(labels) else 'References'
    cit[l]=text.split(l+':',1)[1].split(end,1)[0].strip()
expected=dict(json.loads((HERE/'expected_rules.json').read_text(encoding='utf-8')))
rows=[]
def add(key,actual,ok,evidence):
    rows.append(dict(rule=key,expected=expected[key],actual=actual,result='PASS' if ok else 'FAIL',evidence=evidence))
add('parenthetical_two',cit['TWO-P'],cit['TWO-P']=='(Alpha & Beta, 2020).','probe.pdf page 1 TWO-P')
add('narrative_two',cit['TWO-T'],cit['TWO-T']=='Alpha and Beta (2020).','probe.pdf page 1 TWO-T')
add('three_first',cit['THREE-FIRST'],cit['THREE-FIRST']=='(Gamma et al., 2021).','probe.pdf page 1 THREE-FIRST')
add('corporate',cit['CORPORATE'],cit['CORPORATE']=='(Example Institute, 2024).','probe.pdf page 1 CORPORATE')
lists={int(m[2]):m[1] for m in re.finditer(r'(Name01, A\.,.*?\(2025\)\. List of (20|21) authors\.)',refs)}
n20=re.findall(r'Name\d\d',lists[20]); n21=re.findall(r'Name\d\d',lists[21])
add('reference_20_authors',lists[20],n20==[f'Name{i:02d}' for i in range(1,21)] and '& Name20' in lists[20] and '...' not in lists[20],'probe.pdf page 1 names20; 20 displayed names')
add('reference_21_authors',lists[21],n21==[f'Name{i:02d}' for i in range(1,20)]+['Name21'] and '...' in lists[21] and '&' not in lists[21],'probe.pdf page 1 names21; first 19 plus last')
a=re.search(r'Kappa, K\.,.*?\(2022a\)\. Alpha study\.',refs)[0]
b=re.search(r'Kappa, K\., Lambda, L\., & Mu, M\. \(2022b\)\. Beta study\.',refs)[0]
add('same_authors_same_year_letters',a+' / '+b,'2022a' in cit['IDENTICAL'] and '2022b' in cit['IDENTICAL'],'reversed source citation order; bibliography alphabetic title order')
two=re.search(r'Alpha, A\.,.*?https://doi.org/10\.1000/test\S*',refs)[0]
links=[link.get('uri') for p in fitz.open(HERE/'probe.pdf') for link in p.get_links() if link.get('uri')]
add('doi_precedence',two,'https://doi.org/10.1000/test' in links and not any('example.invalid' in u for u in links) and 'example.invalid' not in text,'probe.pdf text and hyperlink targets')
add('different_first_author_initials',cit['INITIALS'],cit['INITIALS']=='(J. Chen et al., 2024; W. Chen et al., 2024).','two real Chen records; no a/b')
add('et_al_disambiguation',cit['YAO'],cit['YAO']=='(Yao, Yu, et al., 2023; Yao, Zhao, et al., 2023).','two real Yao records; no a/b')
pp='(Hasan, Liang, Kahn, & Jones, 2015; Hasan, Liang, Kahn, & Weintraub, 2015).'
tt='Hasan, Liang, Kahn, and Jones (2015) and Hasan, Liang, Kahn, and Weintraub (2015).'
add('et_al_cannot_replace_one_person',cit['FINAL-P']+' / '+cit['FINAL-T'],cit['FINAL-P']==pp and cit['FINAL-T']==tt,'both parenthetical and narrative four-author boundary cases')
add('same_year_each_year_repeated',cit['IDENTICAL'],cit['IDENTICAL']=='(Kappa et al., 2022a, 2022b).','probe.pdf IDENTICAL')
page=fitz.open(HERE/'probe.pdf')[0]
spans=[s for b in page.get_text('dict')['blocks'] if 'lines' in b for l in b['lines'] for s in l['spans']]
volume=next(s for s in spans if s['text']=='8')
issue=next(s for s in spans if s['text'].startswith('(2)') and abs(s['bbox'][1]-volume['bbox'][1])<1)
journal=[s for s in spans if 'Italic' in s['font'] and ('Test' in s['text'] or 'Journal' in s['text']) and abs(s['bbox'][1]-volume['bbox'][1])<1]
fontproof=dict(journal=[dict(text=s['text'],font=s['font']) for s in journal],volume=dict(text=volume['text'],font=volume['font']),issue=dict(text=issue['text'],font=issue['font']),gap_pt=issue['bbox'][0]-volume['bbox'][2])
add('journal_volume_issue',fontproof,bool(journal) and 'Italic' in volume['font'] and 'Regular' in issue['font'] and abs(fontproof['gap_pt'])<0.1 and '10–20.' in two,'PDF font spans and positions, not plain text inference')
add('no_period_after_doi',two,two.endswith('https://doi.org/10.1000/test'),'probe.pdf entry ends at URL, not URL plus period')
(HERE/'apa14_results.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8')
(HERE/'font_evidence.json').write_text(json.dumps(fontproof,ensure_ascii=False,indent=2),encoding='utf-8')

fixed=norm(docs['types_fixed']).split('References',1)[1]
typedoc=fitz.open(HERE/'types_fixed.pdf')
typelinks={v['uri'] for p in typedoc for v in p.get_links() if v.get('uri')}
typespans=[s for p in typedoc for b in p.get_text('dict')['blocks'] if 'lines' in b for l in b['lines'] for s in l['spans']]
italic_tokens=['Society','GPT-4','LangGraph:','Introducing','Announcing','Making','CrewAI:','Dify:','RAGFlow:','Proceedings']
typefontproof={word:[dict(text=s['text'],font=s['font']) for s in typespans if word in s['text']] for word in italic_tokens}
assert all(any('Italic' in s['font'] for s in spans) for spans in typefontproof.values())
(HERE/'extended_font_evidence.json').write_text(json.dumps(typefontproof,ensure_ascii=False,indent=2),encoding='utf-8')
types=[]
def case(name,expect,actual,ok,before=None):
    types.append(dict(test=name,expected=expect,actual=actual,result='PASS' if ok else 'FAIL',before=before))
case('journal_real','The Knowledge Engineering Review, italic 10, roman (2), 115–152, canonical DOI','The Knowledge Engineering Review, 10(2), 115–152. https://doi.org/10.1017/S0269888900008122',all(s in fixed for s in ['The Knowledge Engineering Review','10(2), 115–152.','10.1017/S0269888900008122']),'The knowledge engineering review: original lowercase metadata')
case('book_real','Italic standalone title; one literal publisher name; no publisher city','Minsky, M. (1988). Society of mind. Simon and Schuster.', 'Society of mind. Simon and Schuster.' in fixed,'Simon; Schuster: original publisher parsed as two list items')
conf=re.search(r'Chen, J\.,.*?v1/2024\.acl-long\.381',fixed)[0]
case('conference_real','In initials-first editors (Eds.), italic proceedings title, (pp. 7066–7085), publisher, DOI',conf,all(s in conf for s in ['In L.-W. Ku, A. Martins, & V. Srikumar (Eds.)','(pp. 7066–7085).','Computational Linguistics.']),'No editors in original record; APA style maps inproceedings without editor/crossref to article and drops publisher')
pre=re.search(r'OpenAI\. \(2023\).*?arXiv\.2303\.08774',fixed)[0]
case('preprint_real','Italic GPT-4 technical report; arXiv named; DOI canonical; no journal volume/issue',pre,'GPT-4 technical report. arXiv.' in pre and 'https://doi.org/10.48550/' in pre)
for k,publisher,version,start in [('crewai2023','PyPI','0.1.0','Moura, J.'),('dify2024','GitHub','0.6.0','LangGenius, Inc.'),('ragflow2024','GitHub','0.6.0','InfiniFlow.')]:
    tail=next(s for s in fixed.split(start)[1:] if '[Computer software]' in s)
    actual=start+tail.split('TYPE')[0]
    # Terminate at repository URL via linked target and match post-title format.
    m=re.search(r'.*?\[Computer software\]\. '+publisher+r'\.',actual)
    actual=m[0]
    source=adapted(k)
    case('software_'+k,f'(Version {version}) [Computer software]. {publisher}.; URL; no mandatory retrieval date',actual+' '+source['url'],f'(Version {version}) [Computer software]. {publisher}.' in actual and source['url'] in typelinks and 'urldate' not in source,'(Computer software; Version ...) when incorrectly using type instead of entrysubtype')
for k,title,start in [('anthropic2024mcp','Introducing the Model Context Protocol','Anthropic.'),('google2025a2a','Announcing the Agent2Agent protocol (A2A)','Surapaneni, R.'),('langgraph2024','LangGraph: Multi-agent workflows','The LangChain Team.'),('langgraph2024interrupt','Making it easier to build human-in-the-loop agents with interrupt','The LangChain Team.')]:
    begin=fixed.index(title); snippet=fixed[max(0,begin-55):begin+370]
    retrieved='Retrieved October 11, 2026, from'
    source=adapted(k)
    datewords={'anthropic2024mcp':'November 25','google2025a2a':'April 9','langgraph2024':'January 23','langgraph2024interrupt':'December 14'}
    case('web_'+k,'Italic title; full known publication date; actual retrieval date 2026-10-11; full cited URL',snippet+' | Link: '+source['url'],retrieved in snippet and datewords[k] in snippet and source['url'] in typelinks and source['urldate']=='2026-10-11','Original database note/date/type need explicit mapping; initial test used evidenced 2026-10-10')
case('corporate_same_identity','Both verified LangChain pages use The LangChain Team and consistent 2024a/b labels','The LangChain Team (2024a, January 23) / (2024b, December 14)',all(s in fixed for s in ['The LangChain Team. (2024a, January 23)','The LangChain Team. (2024b, December 14)']),'Original records use LangChain Team vs The LangChain Team')
case('natbib_prenote_postnote','(see Alpha & Beta, 2020, p. 12) / Alpha and Beta (2020, p. 12)',cit['NOTES']+' / '+cit['TEXT-NOTES'],cit['NOTES']=='(see Alpha & Beta, 2020, p. 12).' and cit['TEXT-NOTES']=='Alpha and Beta (2020, p. 12).')
# Real 20/31-author names: check display order against input, not bbl author count.
for key,count,begin,year,tailtitle in [('ouyang2022instructgpt',20,'Ouyang, L.',2022,'Training language'),('brown2020gpt3',31,'Brown, T.',2020,'Language models')]:
    part=fixed.split(begin,1)[1].split(f'({year})',1)[0]
    record=next(parse_fields(r) for t,k,r in balanced_entries((HERE/'types_fixed.bib').read_text(encoding='utf-8')) if k==key)
    surnames=[x.split(',')[0] for x in record['author'].split(' and ')]
    wanted=surnames if count==20 else surnames[:19]+[surnames[-1]]
    positions=[(begin+part).find(n+',') for n in wanted]
    ok=all(x>=0 for x in positions) and positions==sorted(positions)
    if count>20: ok=ok and '...' in part and '&' not in part and all(n+',' not in part for n in surnames[19:-1])
    else: ok=ok and '& Lowe,' in part and '...' not in part
    case('real_author_list_'+str(count),'20: all names; 31: first 19 plus last, ellipsis and no final &',begin+part,ok)
(HERE/'extended_results.json').write_text(json.dumps(types,ensure_ascii=False,indent=2),encoding='utf-8')



from active_tex import scan_manuscript
active_keys={k for c in scan_manuscript(ROOT).citations for k in c.keys}
pool_keys={k for t,k,r in balanced_entries((ROOT/'references.bib').read_text(encoding='utf-8'))}
coverage={}
for job,wanted in [('pool78',active_keys),('commands78',active_keys),('pool85',pool_keys)]:
    got=set(re.findall(r'\\entry\{([^}]+)\}',(HERE/(job+'.bbl')).read_text(encoding='utf-8')))
    coverage[job]=dict(count=len(got),missing=sorted(wanted-got),extra=sorted(got-wanted))
    assert got==wanted,(job,coverage[job])
assert len(active_keys)==78 and len(pool_keys)==85
(HERE/'coverage_results.json').write_text(json.dumps(coverage,indent=2),encoding='utf-8')
print(json.dumps(dict(core_pass=sum(x['result']=='PASS' for x in rows),core_total=len(rows),extended_pass=sum(x['result']=='PASS' for x in types),extended_total=len(types),coverage=coverage),ensure_ascii=False))
if any(x['result']!='PASS' for x in rows+types): sys.exit(1)
