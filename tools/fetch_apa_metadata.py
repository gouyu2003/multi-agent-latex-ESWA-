"""Read official publication metadata; preserve responses for field evidence."""
from project_paths import project_path
from pathlib import Path
import concurrent.futures,hashlib,json,re,time,sys
import requests
ROOT=Path(__file__).resolve().parents[1]; OUT=project_path('tmp/apa7_migration/sources'); OUT.mkdir(parents=True,exist_ok=True)
sys.path.insert(0,str(ROOT/'tools'))
from build_reference_inventory import balanced_entries,parse_fields
records=[dict(key=k,type=t,fields=parse_fields(r)) for t,k,r in balanced_entries((project_path('references.bib')).read_text(encoding='utf-8'))]
def fetch(job):
 key,kind,url=job; path=OUT/(key+'__'+kind+'.txt')
 if path.exists(): return json.loads((OUT/(key+'__'+kind+'.json')).read_text(encoding='utf-8'))
 record=dict(key=key,kind=kind,url=url,started_utc=time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime()))
 try:
  response=requests.get(url,timeout=30,headers={'User-Agent':'ESWA-reference-format-audit/1.0 (read-only academic metadata validation)'})
  record.update(status=response.status_code,final_url=response.url,content_type=response.headers.get('Content-Type',''))
  path.write_text(response.text,encoding='utf-8'); record['sha256']=hashlib.sha256(path.read_bytes()).hexdigest()
 except Exception as e: record['error']=str(e)
 (OUT/(key+'__'+kind+'.json')).write_text(json.dumps(record,ensure_ascii=False,indent=2),encoding='utf-8')
 return record
jobs=[]
for row in records:
 k=row['key']; f=row['fields']; u=f.get('url',''); doi=f.get('doi','')
 if doi and not doi.startswith('10.48550'): jobs.append((k,'crossref','https://api.crossref.org/works/'+doi))
 if u and not u.startswith('https://doi.org/') and not 'arxiv.org' in u:
  if u.endswith('-Paper-Conference.pdf'): u=u.replace('/file/','/hash/').replace('-Paper-Conference.pdf','-Abstract-Conference.html')
  jobs.append((k,'page',u))
  if 'aclanthology.org' in u: jobs.append((k,'bib',u.rstrip('/')+'.bib'))
  if 'proceedings.neurips.cc' in u or 'proceedings.iclr.cc' in u:
   jobs.append((k,'bib',u.replace('Abstract-Conference.html','Bibtex-Conference.bib').replace('Abstract-Datasets_and_Benchmarks_Track.html','Bibtex-Datasets_and_Benchmarks_Track.bib').replace('Abstract.html','Bibtex.bib')))
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as ex:
 results=list(ex.map(fetch,jobs))
(OUT/'index.json').write_text(json.dumps(results,ensure_ascii=False,indent=2),encoding='utf-8')
for r in results:
 print(r['key'],r['kind'],r.get('status',r.get('error')))
print('sources',len(results),'success',sum(r.get('status')==200 for r in results))
if '--followup' in sys.argv:
 from urllib.parse import urljoin
 import html
 follow=[]
 for row in records:
  k=row['key']; u=row['fields'].get('url','')
  page=OUT/(k+'__page.txt')
  if not page.exists(): page=project_path('audit_work/stage2_sources')/(k+'__official_page.txt')
  if page.exists():
   body=page.read_text(encoding='utf-8')
   for href in re.findall(r'href=[\"\']([^\"\']*bibtex[^\"\']*)[\"\']',body,re.I):
    if 'proceedings.neurips.cc' in u or 'proceedings.iclr.cc' in u or k=='ouyang2022instructgpt':
     origin=u if not u.startswith('https://doi.org/') else 'https://proceedings.neurips.cc/'
     follow.append((k,'official_bib',urljoin(origin,html.unescape(href))))
     break
 for k,u in [('iclr_proceedings','https://iclr.cc/FAQ/Proceedings'),('ijcai2024','https://www.ijcai.org/proceedings/2024/bibtex/890'),('neurips2022','https://proceedings.neurips.cc/paper/2022'),('colm2024','https://colmweb.org/2024/papers.html')]: follow.append((k,'volume',u))
 with concurrent.futures.ThreadPoolExecutor(max_workers=8) as ex: rr=list(ex.map(fetch,follow))
 (OUT/'followup_index.json').write_text(json.dumps(rr,ensure_ascii=False,indent=2),encoding='utf-8')
 for r in rr: print(r['key'],r['kind'],r.get('status',r.get('error')))
