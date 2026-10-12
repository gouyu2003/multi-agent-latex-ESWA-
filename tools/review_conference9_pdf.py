"""Compare the independently rebuilt pre-follow-up PDF with the current PDF."""
from pathlib import Path
import hashlib,json,re
import pymupdf as fitz
from PIL import Image,ImageDraw
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'tmp/conference9_rendered';OUT.mkdir(parents=True,exist_ok=True)
before=fitz.open(ROOT/'tmp/conference9_before_build/manuscript.pdf')
after=fitz.open(ROOT/'manuscript.pdf')
assert len(before)==len(after)==22
rows=[];thumbs=[]
for i,p in enumerate(after):
    pix=p.get_pixmap(matrix=fitz.Matrix(1.5,1.5));pix.save(OUT/f'page_{i+1:02d}.png')
    thumb=Image.frombytes('RGB',[pix.width,pix.height],pix.samples);thumb.thumbnail((580,820));thumbs.append(thumb)
    spans=[s for b in p.get_text('dict')['blocks'] if 'lines' in b for l in b['lines'] for s in l['spans'] if s['text'].strip()]
    outside=[dict(text=s['text'],bbox=s['bbox']) for s in spans if s['bbox'][0]<0 or s['bbox'][2]>p.rect.width+.5 or s['bbox'][1]<0 or s['bbox'][3]>p.rect.height+.5]
    rows.append({'page':i+1,'text_identical':before[i].get_text()==p.get_text(),'pixels_identical_72dpi':before[i].get_pixmap().samples==p.get_pixmap().samples,'outside_page':outside,'image_rectangles_identical':before[i].get_image_info()==p.get_image_info(),'render':str((OUT/f'page_{i+1:02d}.png').relative_to(ROOT)).replace('\\','/'),'result':'PENDING_VISUAL_REVIEW'})
for start in range(0,len(thumbs),4):
    sheet=Image.new('RGB',(1200,1720),'#ddd');draw=ImageDraw.Draw(sheet)
    for offset,img in enumerate(thumbs[start:start+4]):
        x=(offset%2)*600+10;y=(offset//2)*860+25;sheet.paste(img,(x,y));draw.text((x,y-20),f'Page {start+offset+1}',fill='black')
    sheet.save(OUT/f'sheet_{start//4+1}.png')
record={'date':'2026-10-12','before':'tmp/conference9_before_build/manuscript.pdf','after':'manuscript.pdf','before_sha256':hashlib.sha256((ROOT/'tmp/conference9_before_build/manuscript.pdf').read_bytes()).hexdigest(),'after_sha256':hashlib.sha256((ROOT/'manuscript.pdf').read_bytes()).hexdigest(),'pages':rows}
(ROOT/'apa7_audit/conference9_pdf_comparison.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'pages':len(rows),'body_text_identical':all(r['text_identical'] for r in rows[:18]),'body_pixels_identical':all(r['pixels_identical_72dpi'] for r in rows[:18]),'images_and_positions_identical':all(r['image_rectangles_identical'] for r in rows),'outside':sum(len(r['outside_page']) for r in rows)},ensure_ascii=False))
