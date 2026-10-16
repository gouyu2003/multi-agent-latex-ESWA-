"""Inspect each actual bibliography paragraph, not just the minimal examples."""
from project_paths import project_path
from pathlib import Path
import argparse,collections,csv,hashlib,json,re,subprocess,sys
import fitz
ROOT=Path(__file__).resolve().parents[1];HERE=project_path('tmp/apa7_migration'); OUT=project_path('apa7_audit')
sys.path.insert(0,str(ROOT/'tools'))
from active_tex import scan_manuscript
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def norm(s):return re.sub(r'\s+',' ',re.sub(r'(?<=[A-Za-z])-\n(?=[A-Za-z])','',s)).strip()
def plain(s):return re.sub(r'[^\w]','',s).casefold()
data=json.loads((project_path('apa_reference_adaptations.json')).read_text(encoding='utf-8'))
rows={r['key']:r for r in data['records']}
parser=argparse.ArgumentParser()
parser.add_argument('--pool85',action='store_true')
parser.add_argument('--build-dir')
parser.add_argument('--pdf')
parser.add_argument('--output-stem')
parser.add_argument('--skip-scope',action='store_true')
parser.add_argument('--overlay',help='Reviewed overlay matching an archived PDF, for before/after evidence')
args=parser.parse_args()
if args.overlay:
 data=json.loads((project_path(args.overlay)).read_text(encoding='utf-8'))
 rows={r['key']:r for r in data['records']}
pool85=args.pool85
build=project_path(args.build_dir or ('tmp/apa7_regression' if pool85 else 'tmp/apa7_build')); job='pool85' if pool85 else 'manuscript'
bbl=(build/(job+'.bbl')).read_text(encoding='utf-8')
globaldata=bbl.split(r'\datalist[entry]{apa/global//global/global/global}',1)[1].split(r'\enddatalist',1)[0]
entries=list(re.finditer(r'\\entry\{([^}]+)\}\{([^}]+)\}.*?\\endentry',globaldata,re.S));keys=[m[1] for m in entries]
doc=fitz.open(project_path(args.pdf) if args.pdf else build/(job+'.pdf') if pool85 else project_path('manuscript.pdf')); paragraphs=[];current=None;inrefs=False
for pi,p in enumerate(doc):
 blocks=p.get_text('dict')['blocks']
 for block in blocks:
  if 'lines' not in block:continue
  for l in block['lines']:
   text=''.join(s['text'] for s in l['spans']); sizes=[s['size'] for s in l['spans']]
   if text.strip()=='References':inrefs=True;continue
   if not inrefs or not sizes or min(sizes)<7.5 or max(sizes)>8.5 or l['bbox'][1]>747:continue
   x=l['bbox'][0]
   if abs(x-51)<2 or abs(x-306.6)<2:
    current={'lines':[],'locations':[],'spans':[]};paragraphs.append(current)
   if current:
    current['lines'].append(text);current['locations'].append(dict(page=pi+1,bbox=l['bbox']));current['spans']+=l['spans']
assert len(paragraphs)==len(keys),(len(paragraphs),len(keys))
results=[]
for i,(entry,par) in enumerate(zip(entries,paragraphs),1):
 k=entry[1];r=rows[k];f=dict(r['original']);f.update(r['updates']);f={n:v for n,v in f.items() if v is not None}
 actual=norm('\n'.join(par['lines'])); checks={}
 checks['year']=bool(re.search(r'\('+f['year']+r'[a-z]?(?:\)|,)',actual))
 checks['title']=plain(f['title'].replace('{','').replace('}','')) in plain(actual)
 protected_tokens=re.findall(r'\{([^{}]+)\}',f['title'])
 if protected_tokens:
  compact_actual=re.sub(r'[^\w]','',actual)
  checks['protected_title_case']=all(re.sub(r'[^\w]','',token) in compact_actual for token in protected_tokens)
 chars=[];charfonts=[]
 for span in par['spans']:
  for c in span['text']:
   if c.isalnum() or c=='_':
    v=c.casefold();chars.extend(v);charfonts.extend([span['font']]*len(v))
 flat=''.join(chars)
 def fonts_for(value,start=0):
  token=plain(value);at=flat.find(token,start)
  return (set(charfonts[at:at+len(token)]),at+len(token)) if at>=0 else (set(),start)
 titlefonts,_=fonts_for(f['title'].replace('{','').replace('}',''))
 standalone=entry[2] in ['online','book','software']
 checks['title_font']=bool(titlefonts) and all(('Italic' in font)==standalone for font in titlefonts)
 if entry[2]=='inbook' and f.get('booktitle'):
  bookfonts,_=fonts_for(f['booktitle'].replace('{','').replace('}',''))
  checks['proceedings_italic']=bool(bookfonts) and all('Italic' in font for font in bookfonts)
 if entry[2]=='article':
  journal=f.get('journaltitle',f.get('journal',''));jf,end=fonts_for(journal)
  checks['journal_italic']=bool(jf) and all('Italic' in font for font in jf)
  if f.get('volume'):
   vf,end=fonts_for(f['volume'],end);checks['volume_italic']=bool(vf) and all('Italic' in font for font in vf)
   if f.get('number'):
    nf,_=fonts_for(f['number'],end);checks['issue_roman']=bool(nf) and all('Italic' not in font for font in nf)
 authorcount=int(re.search(r'\\name\{author\}\{(\d+)\}',entry[0])[1]); families=re.findall(r'family=\{(.*?)\},\s*familyi=',entry[0],re.S)[:authorcount]
 families=[re.sub(r'[{}]','',a) for a in families]
 authorpart=actual.split('('+f['year'],1)[0]
 want=families if authorcount<=20 else families[:19]+families[-1:]
 # Primary-source surname order is checked in the preserved source audit;
 # this verifies all APA-displayed names against the final Biber name list.
 normalizedauthor=plain(authorpart);pos=0;ordered=True
 for family in want:
  token=plain(family);at=normalizedauthor.find(token,pos)
  if at<0:ordered=False;break
  pos=at+len(token)
 checks['author_order_and_truncation']=ordered and ('...' in authorpart if authorcount>20 else '...' not in authorpart)
 if authorcount>20:checks['ellipsis_no_final_ampersand']='&' not in authorpart
 uri=[]
 for loc in par['locations']:
  for link in doc[loc['page']-1].get_links():
   if link.get('uri') and fitz.Rect(loc['bbox']).intersects(fitz.Rect(link['from'])):uri.append(link['uri'])
 uri=sorted(set(uri));doi=f.get('doi')
 if doi:
  expecteddoi='https://doi.org/'+re.sub(r'^https?://(?:dx\.)?doi.org/','',doi)
  checks['canonical_doi']=expecteddoi in uri
  checks['doi_only_source_url']=all(u==expecteddoi for u in uri)
  checks['doi_no_terminal_period']=not actual.endswith('.')
 elif f.get('url'):checks['source_url']=f['url'] in uri
 if r['classification']=='网页':checks['ESWA_actual_access_date']='Retrieved October 11, 2026, from' in actual
 if r['target_type']=='software':
  checks['software_descriptor']='[Computer software]' in actual
  if f.get('version'):checks['software_version']='Version '+f['version'] in actual
 if f.get('eid'):checks['article_identifier']='Article '+f['eid'] in actual
 checks['no_audit_annotation']=not any(s in actual for s in ['Accessed 10 October','accessed 10 October','No peer-reviewed paper','First released on PyPI'])
 critical=[x for x in r['pending'] if x.startswith('editor')]
 results.append(dict(index=i,key=k,type=entry[2],classification=r['classification'],expected={n:f.get(n) for n in ['author','year','date','title','journal','journaltitle','booktitle','editor','publisher','volume','number','pages','eid','doi','url','version','entrysubtype','urldate'] if f.get(n)},actual=actual,pages=sorted({l['page'] for l in par['locations']}),checks=checks,format_result='PASS' if all(checks.values()) else 'FAIL',metadata_result='PENDING' if critical else 'CHECKED_WITH_RECORDED_LIMITS',pending=r['pending'],source_evidence=r['evidence'],font_evidence=[dict(text=s['text'],font=s['font'],size=s['size']) for s in par['spans']],links=uri))
stem=args.output_stem or ('reference_85_preview' if pool85 else 'reference_78_acceptance')
(OUT/(stem+'.json')).write_text(json.dumps(results,ensure_ascii=False,indent=2),encoding='utf-8')
with (OUT/(stem+'.csv')).open('w',encoding='utf-8-sig',newline='') as file:
 writer=csv.DictWriter(file,fieldnames=['index','key','classification','pages','format_result','metadata_result','failed_checks','pending','actual']);writer.writeheader()
 for r in results:writer.writerow({n:r.get(n,'') for n in writer.fieldnames if n not in ['failed_checks','pending']}|{'failed_checks':','.join(k for k,v in r['checks'].items() if not v),'pending':' | '.join(r['pending'])})
if pool85 or args.skip_scope:
 print('POOL85 entries',len(keys),'format pass',sum(r['format_result']=='PASS' for r in results),'failures',[(r['key'],[k for k,v in r['checks'].items() if not v]) for r in results if r['format_result']=='FAIL']);sys.exit(0)
base=json.loads((HERE/'baseline/manifest.json').read_text(encoding='utf-8'));scan=scan_manuscript(ROOT)
before=(HERE/'baseline/manuscript.tex').read_text(encoding='utf-8');after=(project_path('manuscript.tex')).read_text(encoding='utf-8')
def body(s):return s[s.index(r'\begin{document}'):].replace(r'\bibliographystyle{cas-model2-names}'+'\n'+r'\bibliography{references}',r'\printbibliography')
scope={'baseline':base['head'],'branch':subprocess.check_output(['git','branch','--show-current'],cwd=ROOT).decode().strip(),'protected_changes':[n for n,h in base['tracked'].items() if n not in ['manuscript.tex','.gitignore','README.md'] and (not (project_path(n)).exists() or sha(project_path(n))!=h)],'body_except_bibliography_identical':body(before)==body(after),'commands_identical':base['commands']==[c.raw_command for c in scan.citations],'commands':len(scan.citations),'cited_key_set_identical':set(keys)==set(base['active_keys']),'bbl_count':len(keys),'bbl_duplicates':[k for k,n in collections.Counter(keys).items() if n>1],'references_sha256':sha(project_path('references.bib')),'pool_count':len(rows),'original_bib_identical':sha(project_path('references.bib'))==base['saved']['references.bib'],'formal_pdf_sha256':sha(project_path('manuscript.pdf')),'format_pass':sum(r['format_result']=='PASS' for r in results),'metadata_pending':[r['key'] for r in results if r['metadata_result']=='PENDING']}
scope['configuration_sha256']={n:sha(project_path(n)) for n in ['manuscript.tex','eswa-apa-config.tex','eswa-apa-sourcemap.tex','apa_reference_adaptations.json']}
scope['final_bbl_sha256']=sha(build/(job+'.bbl'))
# Byte equality includes the disabled historical blocks; do not normalize them.
before_bytes=(HERE/'baseline/manuscript.tex').read_bytes();after_bytes=(project_path('manuscript.tex')).read_bytes()
scope['disabled_history_byte_identical']=re.findall(rb'\\iffalse.*?\\fi\b',before_bytes,re.S)==re.findall(rb'\\iffalse.*?\\fi\b',after_bytes,re.S)
(OUT/'scope_validation.json').write_text(json.dumps(scope,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(scope,ensure_ascii=False));print('format failures',[(r['key'],[k for k,v in r['checks'].items() if not v]) for r in results if r['format_result']=='FAIL'])
