from pathlib import Path
import fitz,json,re
from PIL import Image,ImageDraw
ROOT=Path(__file__).resolve().parents[1];HERE=ROOT/'tmp/apa7_migration'; OUT=HERE/'rendered';OUT.mkdir(exist_ok=True)
rows=[]
for kind,path in [('before',HERE/'baseline_build/manuscript.pdf'),('after',ROOT/'manuscript.pdf')]:
 doc=fitz.open(path); previews=[]; texts=[]
 for i,p in enumerate(doc):
  image=p.get_pixmap(matrix=fitz.Matrix(1.5,1.5)); image.save(OUT/f'{kind}_{i+1:02d}.png')
  thumb=Image.frombytes('RGB',[image.width,image.height],image.samples);thumb.thumbnail((590,835));previews.append(thumb)
  spans=[s for b in p.get_text('dict')['blocks'] if 'lines' in b for l in b['lines'] for s in l['spans'] if s['text'].strip()]
  outside=[dict(text=s['text'],bbox=s['bbox']) for s in spans if s['bbox'][0]<0 or s['bbox'][2]>p.rect.width+.5 or s['bbox'][1]<0 or s['bbox'][3]>p.rect.height+.5]
  content=p.get_text();texts.append(content)
  rows.append(dict(version=kind,page=i+1,outside=outside,image_rectangles=[list(v['bbox']) for v in p.get_image_info()],captions=re.findall(r'(?:Table|Figure)\s+\d+[^\n]*',content),references='References' in content,body_lines=len(spans)))
 for start in range(0,len(previews),4):
  sheet=Image.new('RGB',(1200,1740),'#ddd');draw=ImageDraw.Draw(sheet)
  for offset,img in enumerate(previews[start:start+4]):
   x=(offset%2)*600+5;y=(offset//2)*870+25;sheet.paste(img,(x,y));draw.text((x,y-20),f'{kind}: page {start+offset+1}',fill='black')
  sheet.save(OUT/f'{kind}_sheet_{start//4+1}.png')
 (HERE/(kind+'_text.txt')).write_text('\n\n'.join(texts),encoding='utf-8')
(HERE/'pdf_page_metrics.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'pages':len(rows)//2,'reference_pages':[(r['version'],r['page']) for r in rows if r['references']],'captions':[(r['version'],r['page'],r['captions']) for r in rows if r['captions']],'outside':[(r['version'],r['page'],r['outside']) for r in rows if r['outside']]},ensure_ascii=False))
