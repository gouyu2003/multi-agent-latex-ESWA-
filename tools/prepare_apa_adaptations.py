"""Build a reviewed, per-key APA overlay from preserved official-source responses.

Does not write references.bib or the previous reference audit.
"""
from project_paths import project_path
from pathlib import Path
import hashlib,html,json,re,sys
ROOT=Path(__file__).resolve().parents[1]; SRC=project_path('tmp/apa7_migration/sources'); OUT=project_path('apa7_audit'); OUT.mkdir(exist_ok=True)
sys.path.insert(0,str(ROOT/'tools'))
from build_reference_inventory import balanced_entries,parse_fields
from active_tex import scan_manuscript
active={k for c in scan_manuscript(ROOT).citations for k in c.keys}
previous={r['key']:r for r in json.loads((project_path('audit_work/reference_field_audit.json')).read_text(encoding='utf-8'))}
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def readbib(p):
 b=p.read_text(encoding='utf-8'); entries=balanced_entries(b)
 return parse_fields(entries[0][2]) if entries else {}
def source(key,kind):
 p=SRC/(key+'__'+kind+'.txt'); j=p.with_suffix('.json')
 if not p.exists():return None
 meta=json.loads(j.read_text(encoding='utf-8')) if j.exists() else {}
 return dict(path=str(p.relative_to(ROOT)).replace('\\','/'),sha256=digest(p),url=meta.get('url',meta.get('bib_url','')),status=meta.get('status',200))
official={p.name.split('__')[0]:readbib(p) for p in SRC.glob('*__official_bib.txt')}
neurips={official[k]['year']:k for k in official if 'publisher' in official[k] and 'Neural Information' in official[k].get('booktitle','')}
brands=['GPT-4','AutoGen','MetaGPT','HotpotQA','CoQA','QuAC','BERT','LLaMA','ChatGLM','GLM','ChatGPT','HuggingGPT','Hugging Face','LONGAGENT','DSPy','GPTSwarm','AgentVerse','MDAgents','MemGPT','Self-RAG','Self-refine','MedAgents','ChatLaw','LegalBench','SWE-agent','SWE-bench','GitHub','CrewAI','Dify','LegalGraphRAG','EduPlanner','ReConcile','RAGFlow','XAgent','MuSiQue','AgentBench','GAIA','WebArena','AutoRAG','LangGraph','Wikipedia','LangChain','Model Context Protocol','Agent2Agent','A2A','AI','LLM','LLMs','NLP','RAG','ACM','EMNLP','IJCAI','IJCNN']
casefix={'Gptswarm':'GPTSwarm','Agentverse':'AgentVerse','Mdagents':'MDAgents','llms':'LLMs','Medagents':'MedAgents','Chatlaw':'ChatLaw','Legalbench':'LegalBench','Llm-medqa':'LLM-MedQA'}
def protect_title(value):
 s=value.replace('{','').replace('}','').rstrip('.')
 for old,new in casefix.items():s=re.sub(r'\b'+re.escape(old)+r'\b',new,s)
 for b in sorted(brands+['LLM-MedQA','ReAct','GLM-130B','GLM-4','AgentCoder','ChatDev'],key=len,reverse=True):
  s=re.sub(r'(?<![\w{])'+re.escape(b)+r'(?![\w}])',lambda m:'{'+m[0]+'}',s)
 return s
def proceedings_title(v):
 # APA sentence case; preserve institutions and official acronyms.
 for name in ['Association for Computational Linguistics','North American Chapter','International Conference on Learning Representations']:
  v=re.sub(re.escape(name),lambda m:'{'+name+'}',v,flags=re.I)
 for acronym in ['EMNLP','ACL','IJCAI-24','IJCNN','ACM','AI']:
  v=re.sub(r'(?<![\w{])'+acronym+r'(?![\w}])','{'+acronym+'}',v)
 return v
rows=[]; changes=[]; sources=[]
for typ,k,raw in balanced_entries((project_path('references.bib')).read_text(encoding='utf-8')):
 f=parse_fields(raw); updates={}; reasons={}; evidence=[]; pending=[]; target=typ; classification=typ
 def put(field,value,why,url=None):
  if value!=f.get(field): updates[field]=value;reasons[field]=dict(reason=why,evidence=url or f.get('url') or previous[k]['field_checks']['title'].get('evidence_url'))
 for kind in ['crossref','page','bib','official_bib']:
  s=source(k,kind)
  if s and s['status']==200:evidence.append(s)
 crosspath=SRC/(k+'__crossref.txt'); cross=json.loads(crosspath.read_text(encoding='utf-8'))['message'] if crosspath.exists() else {}
 put('title',protect_title(f['title']),'APA sentence case; protect documented proper names and acronyms; remove a title-final period from data')
 if typ=='inproceedings':
  target='incollection';classification='正式会议论文集文章'
  book=f['booktitle']; chosen=None
  if cross.get('type')=='journal-article':
   target='article';classification='期刊/连续出版物形式会议论文'
   put('journaltitle',cross['container-title'][0],'Publisher-deposited Crossref classifies this as a journal article','https://api.crossref.org/works/'+f['doi'])
   put('booktitle',None,'Transferred serialized conference title to journaltitle')
   if cross.get('issue'):put('number',cross['issue'],'Official serialized proceedings issue','https://api.crossref.org/works/'+f['doi'])
  else:
   if k in official:chosen=k
   elif 'neural information processing systems' in book.lower():chosen=neurips.get(f['year'])
   if chosen:
    b=official[chosen]; s=source(chosen,'official_bib')
    if not s or not s['url']:
     extras=SRC/(chosen+'_official__extra.json')
     if extras.exists():s=dict(path=str((SRC/(chosen+'__official_bib.txt')).relative_to(ROOT)),sha256=digest(SRC/(chosen+'__official_bib.txt')),url=json.loads(extras.read_text(encoding='utf-8')).get('bib_url'),status=200)
    if s:evidence.append(s)
    if b.get('editor'):
     ed=re.sub(r'(?<=[A-Z])\.(?=[A-Z])','. ',b['editor']).replace('U. Von Luxburg','von Luxburg, U.')
     put('editor',ed,'Official paper BibTeX / same proceedings volume explicitly credits these editors',s.get('url') if s else None)
    if b.get('publisher'):put('publisher',b['publisher'],'Official proceedings BibTeX publisher',s.get('url') if s else None)
    if k==chosen and not f.get('pages') and b.get('pages'):put('pages',b['pages'],'Previously missing page range now explicitly available in official BibTeX',s.get('url') if s else None)
   if 'Learning Representations' in book or 'learning representations' in book:
    year=f['year']; catalog=SRC/('iclr'+year+'__catalog.txt')
    if not catalog.exists():catalog=SRC/('iclr'+year+'_catalog__extra.txt')
    if catalog.exists() and 'International Conference on Learning Representations (ICLR)' in catalog.read_text(encoding='utf-8'):
     url='https://www.proceedings.com/'+{'2021':'80587','2023':'80586','2024':'80585','2025':'80508'}[year]+'.html'
     put('publisher','International Conference on Learning Representations','ICLR-linked publisher catalog distinguishes original publisher from POD publisher Curran',url)
     evidence.append(dict(path=str(catalog.relative_to(ROOT)),sha256=digest(catalog),url=url,status=200))
    if not chosen:pending.append('editor: official record supplies no editor; no unsupported editor was added')
   if k=='guo2024llm_multiagent_survey':
    b=readbib(SRC/'ijcai2024__volume.txt');put('editor',b['editor'],'Official IJCAI paper BibTeX editor','https://www.ijcai.org/proceedings/2024/bibtex/890')
    evidence.append(source('ijcai2024','volume'))
   acl=SRC/(k+'__bib.txt')
   if 'aclanthology.org' in f.get('url','') and acl.exists():
    b=readbib(acl)
    for field in ['editor','publisher']:
     if b.get(field):put(field,b[field],'Official ACL Anthology BibTeX '+field,f['url'].rstrip('/')+'.bib')
    book=b.get('booktitle',book)
   if 'mlr.press' in f.get('url',''):
    body=(SRC/(k+'__page.txt')).read_text(encoding='utf-8');b=readbib_text=html.unescape(re.search(r'<code[^>]*id="bibtex"[^>]*>(.*?)</code>',body,re.S)[1]);b=parse_fields(balanced_entries(b)[0][2])
    put('editor',b['editor'],'Official PMLR embedded BibTeX editors',f['url']);put('publisher',b['publisher'],'Official PMLR publisher',f['url'])
   if not f.get('publisher') and cross.get('publisher') and 'neural information processing systems' not in book.lower():
    put('publisher',cross['publisher'],'Publisher-deposited Crossref publication venue publisher','https://api.crossref.org/works/'+f['doi'])
   if k=='wu2024autogen':pending.append('editor/publisher/pages: COLM/OpenReview official accepted paper supplies no verified values; supplementation stopped')
   if not updates.get('editor',f.get('editor')) and not any(x.startswith('editor') for x in pending):
    pending.append('editor: primary publication registration has no editor field; absence of editorial credit is not established; supplementation stopped')
   put('booktitle',proceedings_title(book),'APA proceedings sentence case with institution/acronym protection')
   if not f.get('pages') and not updates.get('pages'):pending.append('pages: no confirmed pagination in consulted primary records; left empty')
 elif typ=='article' and 'arXiv' in f.get('journal',''):
  target='online';classification='预印本（保留既有版本）'
  put('journal',None,'Preprint server is a source, not a journal');put('organization','arXiv','Original record DOI/URL and prior verified selected arXiv version')
 elif typ=='article':
  classification='期刊论文'
  if cross.get('container-title'):put('journal',cross['container-title'][0],'Canonical journal capitalization from publisher-deposited Crossref','https://api.crossref.org/works/'+f['doi'])
  if cross.get('article-number'):
   put('eid',cross['article-number'],'Publisher-deposited article identifier','https://api.crossref.org/works/'+f['doi']);put('pages',None,'Article identifier is not a page range')
  if k=='zhang2024memory_survey':
   put('eid','155','Prior official article audit confirms Article 155, pages 155:1–155:47',f['url']);put('pages',None,'Use APA Article 155 rather than article-prefixed pagination')
 elif typ=='book':
  classification='书籍';put('publisher','{Simon and Schuster}','Preserve the existing single literal publisher; prevent and being parsed as list separator')
 elif typ=='misc':
  if k in ['anthropic2024mcp','google2025a2a','langgraph2024','langgraph2024interrupt']:
   target='online';classification='网页'
   dates={'anthropic2024mcp':'2024-11-25','google2025a2a':'2025-04-09','langgraph2024':'2024-01-23','langgraph2024interrupt':'2024-12-14'}
   put('date',dates[k],'Full publication date verified in official page and preserved validation evidence')
   put('urldate','2026-10-11','Actual successful HTTP 200 retrieval logged in this migration; ESWA requires web access date')
   if k.startswith('langgraph'):
    put('author','{The LangChain Team}','Exact official page byline; unify corporate identity across two publications')
    put('organization','LangChain','Official website identity')
   if k=='google2025a2a':put('organization','Google Developers Blog','Official website identity')
  else:
   target='software';classification='软件'
   put('entrysubtype','Computer software','APA bracketed description uses entrysubtype, not type')
   version={'crewai2023':'0.1.0','dify2024':'0.6.0','ragflow2024':'0.6.0'}.get(k)
   if version:put('version',version,'Preserved version explicitly verified in prior software release audit')
   else:
    put('urldate','2026-10-11','Actual successful repository access; unknown software version requires access date in ESWA');pending.append('version/date: unversioned XAgent; original year retained; not a verified release date')
   put('publisher','PyPI' if k=='crewai2023' else 'GitHub','Actual distribution/repository host, not inferred software creator')
  if f.get('howpublished'):put('howpublished',None,'Replaced legacy howpublished with structured source/type fields')
 if f.get('note'):
  put('annotation',f['note'],'Keep historical audit/access evidence out of printed bibliographic note');put('note',None,'Historical audit note is not an APA bibliographic element')
 row=dict(key=k,cited=k in active,original_type=typ,target_type=target,classification=classification,original=f,updates=updates,reasons=reasons,evidence=evidence,pending=pending,previous_audit=previous[k].get('existence_status'))
 rows.append(row)
 if target!=typ:changes.append(dict(key=k,field='ENTRYTYPE',old=typ,new=target,reason='Verified publication form / APA driver, not automatic inproceedings fallback',evidence=f.get('url')))
 for field,value in updates.items():changes.append(dict(key=k,field=field,old=f.get(field),new=value,**reasons[field]))
document={'references_sha256':digest(project_path('references.bib')),'records':rows}
(project_path('apa_reference_adaptations.json')).write_text(json.dumps(document,ensure_ascii=False,indent=2),encoding='utf-8')
(OUT/'metadata_changes.json').write_text(json.dumps(changes,ensure_ascii=False,indent=2),encoding='utf-8')
(OUT/'publication_classification.json').write_text(json.dumps([{n:r[n] for n in ['key','cited','original_type','target_type','classification','pending','evidence']} for r in rows],ensure_ascii=False,indent=2),encoding='utf-8')
print('overlay records',len(rows),'changes',len(changes),'pending records',sum(bool(r['pending']) for r in rows))
