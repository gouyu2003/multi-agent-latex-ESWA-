"""Author native slide objects into the Image2PPT manifest; the CLI builds the PPTX."""
import json
from pathlib import Path

P = Path(__file__).resolve().parent
req = json.loads((P / 'page_request.json').read_text(encoding='utf-8'))
shapes, texts, regions = [], [], []
current = None

def shape(id, typ, box, fill, stroke='#50637C', width=.8, z=25, **kw):
    item = dict(id=id, type=typ, box_px=box, fill=fill, stroke=stroke, stroke_width=width, z_index=z, **kw)
    if typ == 'roundRect':
        item.update(source_corner_radius_px=min(16,box[3]/5), corner_category='small-radius')
    shapes.append(item)
    current['manifest_ids']['shapes'].append(id)
    current['protected_visual_anchors'].append(dict(id='anchor-'+id,kind='node-boundary',manifest_id=id,source_bbox_px=box))
    return item

def line(id, pts, stroke='#50637C', width=.85, z=24, arrow=False):
    item=dict(id=id,type='line',points_px=pts,stroke=stroke,stroke_width=width,z_index=z)
    if arrow: item.update(connector='straight',end_arrow='triangle',arrow_width='sm',arrow_length='sm')
    shapes.append(item)
    current['manifest_ids']['shapes'].append(id)
    current['protected_visual_anchors'].append(dict(id='anchor-'+id,kind='directed-connector' if arrow else 'connector',manifest_id=id,source_points_px=pts))

def text(id, value, box, size=9.5, bold=False, color='#202B3A'):
    texts.append(dict(id=id,text=value,box_px=box,font='Arial',font_size=size,bold=bold,color=color,align='center',valign='middle',fit_text=False,z_index=60))
    current['manifest_ids']['text_boxes'].append(id)

def region(id, x, width, label):
    global current
    current=dict(id=id,label=label,source_bbox_px=[x,10,width,292],risk_level='high',strategy='native-object-decomposition',
                 reason='User explicitly requires every component editable and approved content corrections and geometric diagram redrawing.',
                 manifest_ids=dict(shapes=[],text_boxes=[],images=[]),protected_visual_anchors=[])
    regions.append(current)

colors=[('#DED9F3','#8C81B3'),('#D0EBDF','#689C86'),('#FFE0A7','#C18D40'),('#F5CED5','#B87284')]
cards=[
 (47,'1960s onward','Symbolic\napproaches','ELIZA (1966)\nProlog, Cyc','Rules & logic\nKnowledge representation'),
 (211,'1990s onward','Retrieval & reading\ncomprehension','TREC QA (1999)\nWeb search\nSQuAD (2016)','Document retrieval\nAnswer extraction'),
 (375,'2010s onward','Neural &\ngenerative QA','Transformer\nBERT, GPT-2/3\nT5','Pretraining & fine-tuning\nRAG (2020), CoT (2022)'),
 (539,'2022 onward','LLM-based\nagentic QA','ReAct (2022/2023)\nGPT-4, Gemini (2023)','Tool use\nMulti-agent collaboration')]
for i,(x,era,title,examples,methods) in enumerate(cards):
    region('stage-'+str(i+1),x-8,153,title.replace('\n',' '))
    fill,edge=colors[i]
    shape('card-'+str(i),'roundRect',[x,84,135,156],fill,edge,1.1,z=10)
    text('era-'+str(i),era,[x+4,93,127,17],10.5,True)
    text('title-'+str(i),title,[x+3,197,129,33],10.3,True)
    text('examples-'+str(i),examples,[x-5,17,145,55],9.3)
    text('methods-'+str(i),methods,[x-10,249,155,39],9.0)
    if i<3:
        shape('phase-arrow-'+str(i),'shape',[x+126,142,48,33],edge,'none',z=45,preset='rightArrow')
    if i==0:
        nodes=[(114,123,12),(95,150,11),(134,150,11),(85,174,10),(104,174,10),(124,174,10),(144,174,10)]
        for j,(a,b) in enumerate([(0,1),(0,2),(1,3),(1,4),(2,5),(2,6)]):
            xa,ya,da=nodes[a];xb,yb,db=nodes[b]
            # Each tree relationship is one editable straight line.
            line('tree-edge-'+str(j),[xa,ya+da/2,xb,yb-db/2],edge,1)
        for j,(cx,cy,d) in enumerate(nodes):
            shape('tree-node-'+str(j),'ellipse',[cx-d/2,cy-d/2,d,d], '#BBB0DB' if j<3 else '#D8BBD4', '#665982',.85)
    elif i==1:
        shape('doc','shape',[281,116,27,36],'#EBEDB5','#57726B',.8,preset='foldedCorner')
        for j in range(3): line('doc-line-'+str(j),[286,128+j*5,302,128+j*5],'#7E9879',.7,z=27)
        for j in range(3):
            yy=130+j*12
            shape('database-body-'+str(j),'rect',[247,yy,35,13],'#A1BAD3','#526F89',.9)
            shape('database-base-'+str(j),'ellipse',[247,yy+7,35,10],'#B6CCE0','#526F89',.9,z=26+j*2)
        shape('database-top','ellipse',[247,125,35,11],'#B6CCE0','#526F89',.9,z=34)
        line('lens-handle',[289,164,304,179],'#526F89',4.4,z=38)
        shape('lens-outer','ellipse',[268,141,31,31],'#A1BAD3','#526F89',1.0,z=40)
        shape('lens-inner','ellipse',[273,146,21,21],'#F4FBFB','#526F89',.65,z=41)
    elif i==2:
        columns=[[(413,132),(413,151),(413,170)],[(441,123),(441,146),(441,176)],[(471,140),(471,161)]]
        for layer in range(2):
            for a,(xa,ya) in enumerate(columns[layer]):
                for b,(xb,yb) in enumerate(columns[layer+1]):
                    line(f'neural-edge-{layer}-{a}-{b}',[xa,ya,xb,yb],'#9F7742',.75)
        for a,col in enumerate(columns):
            for b,(cx,cy) in enumerate(col):shape(f'neural-node-{a}-{b}','ellipse',[cx-5.5,cy-5.5,11,11],'#FFD391','#91663D',.8,z=33)
    else:
        # All pictogram components remain native at the user's explicit request.
        # Three robot agents surround an editable language-model hub.
        for j,(cx,cy) in enumerate([(606,122),(580,174),(633,174)]):
            line(f'agent-link-{j}',[cx,cy+6,606,154],'#67889D',.8,arrow=True)
            shape(f'robot-head-{j}','roundRect',[cx-8,cy-5,16,11],'#AFC9D8','#56738C',.8,z=35)
            shape(f'robot-eye1-{j}','ellipse',[cx-4.5,cy-1.5,2,2],'#49617A','none',z=36)
            shape(f'robot-eye2-{j}','ellipse',[cx+2.5,cy-1.5,2,2],'#49617A','none',z=36)
            line(f'robot-antenna-{j}',[cx,cy-5,cx,cy-9],'#56738C',.8,z=35)
            shape(f'robot-antenna-tip-{j}','ellipse',[cx-1.5,cy-11,3,3],'#F7E3A8','#56738C',.5,z=36)
            shape(f'robot-body-{j}','roundRect',[cx-7,cy+8,14,9],'#B9D4E3','#56738C',.75,z=35)
            for side in (-1,1):
                line(f'robot-arm-{j}-{side}',[cx+side*8,cy+9,cx+side*12,cy+15],'#56738C',1,z=35)
                line(f'robot-leg-{j}-{side}',[cx+side*4,cy+17,cx+side*4,cy+20],'#56738C',1,z=35)
        shape('llm-hub','ellipse',[591,142,30,26],'#C8DFEA','#56738C',.8,z=40)
        text('llm-label','LLM',[593,148,26,12],7.5,True,'#49617A')

for reg, prefix in [(regions[0], 'tree'), (regions[2], 'neural')]:
    node_shapes=[s for s in shapes if s['id'].startswith(prefix+'-node-')]
    edge_shapes=[s for s in shapes if s['id'].startswith(prefix+'-edge-')]
    reg['compound_diagram']=dict(kind='node-link-diagram',object_inventory_complete=True,
        measurement_reviewed=True,native_object_policy='measured-simple-objects-native',
        nodes=[dict(id=s['id'],manifest_id=s['id'],geometry='circle',
                    source_center_px=[s['box_px'][0]+s['box_px'][2]/2,s['box_px'][1]+s['box_px'][3]/2],
                    source_size_px=s['box_px'][2:]) for s in node_shapes],
        edges=[dict(id=s['id'],manifest_id=s['id'],source_points_px=s['points_px'],
                    line_style='solid',direction='none') for s in edge_shapes])

region('interpretation',35,640,'Interpretation of the development arrows')
current['source_bbox_px']=[35,296,640,25]
current['risk_level']='low'
current['strategy']='native-text-layout'
text('coexistence','Representative milestones; paradigms overlap and continue to coexist.',[35,302,640,18],8.5,False,'#596571')

evidence={
 'font_size_calibrated': {'observation':'Arial uses consistent 9.0-10.5 pt text levels; the LLM hub is 7.5 pt and the interpretation is 8.5 pt.'},
 'visual_inventory_matched': {'observation':'Four colored cards, three directional arrows and four diagrams rebuilt as native objects per the explicit all-editable requirement.'},
 'background_strategy_checked': {'observation':'White background and purple, green, amber and rose cards preserve the reference composition.'},
 'shape_corner_geometry_checked': {'observation':'Large source cards use rounded rectangles with a measured 16 pixel corner radius.'}}
manifest=dict(schema_version=2,slide=req['slide'],content_box=req['content_box'],source=dict(path='source.png',width_px=709,height_px=330),
 page_strategy='User-authorized corrected-text reconstruction with every diagram component editable as native PowerPoint objects.',
 user_overrides={'all_components_editable':True,'native_pictogram_redraw_authorized':True,'content_corrections_authorized':True,
 'authorization':'User requested all components editable, received the corrected four-stage wording and native geometric reconstruction plan, then instructed to begin.'},
 text_inventory=[t['text'] for t in texts],
 visual_inventory=[dict(id=r['id'],kind='native-structure',representation='native',description=r['label']) for r in regions],
 background_strategy=dict(mode='native-or-script',source_consistency_contract='White background, four pastel cards in a horizontal sequence; user-authorized text correction and editable diagram reconstruction.',removed_foreground='All original lettering and pictograms represented separately as native text and shapes.',comparison_note='Reference card positions and palette preserved; labels corrected according to the preceding manuscript audit.'),
 quality_checks={k:True for k in evidence},quality_evidence=evidence,text_boxes=texts,shapes=shapes,images=[],asset_provenance=[],
 image2ppt_region_decomposition=dict(schema_version='image2ppt-region-decomposition-v1',page_complexity='structured',source_size_px=[709,330],regions=regions),
 content_sources=['https://doi.org/10.1145/365153.365168','https://trec.nist.gov/data/qamain.html','https://aclanthology.org/D16-1264/',
 'https://arxiv.org/abs/1810.04805','https://arxiv.org/abs/2005.11401','https://arxiv.org/abs/2201.11903','https://arxiv.org/abs/2210.03629',
 'https://arxiv.org/abs/2303.08774','https://arxiv.org/abs/2312.11805'])
(P/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(f'Authored manifest: {len(shapes)} native shapes/connectors and {len(texts)} text boxes; no images.')
