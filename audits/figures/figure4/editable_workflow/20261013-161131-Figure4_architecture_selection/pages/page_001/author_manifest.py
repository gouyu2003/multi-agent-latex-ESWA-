"""Author editable native objects into the Image2PPT page manifest."""
import json
from pathlib import Path
P=Path(__file__).resolve().parent
req=json.loads((P/'page_request.json').read_text(encoding='utf-8'))
shapes,texts,regions=[],[],[]
current=None
INK='#384C57'

def region(id,label,box,risk='high'):
    global current
    current=dict(id=id,label=label,source_bbox_px=box,risk_level=risk,
        strategy='native-object-decomposition',reason='User requires every component editable; diagram and pictograms are reconstructed as native shapes and text.',
        manifest_ids=dict(shapes=[],text_boxes=[],images=[]),protected_visual_anchors=[])
    regions.append(current)

def shape(id,typ,box,fill='none',stroke=INK,sw=.6,z=20,**extra):
    s=dict(id=id,type=typ,box_px=box,fill=fill,stroke=stroke,stroke_width=sw,z_index=z,**extra)
    if typ=='roundRect':s.update(source_corner_radius_px=min(6,box[3]/5),corner_category='small-radius')
    shapes.append(s);current['manifest_ids']['shapes'].append(id)
    current['protected_visual_anchors'].append(dict(id='anchor-'+id,kind='node-boundary',manifest_id=id,source_bbox_px=box))
    return s

def line(id,pts,stroke=INK,sw=.65,arrow=False,connector='straight',z=18,dash=None):
    s=dict(id=id,type='line',points_px=pts,stroke=stroke,stroke_width=sw,z_index=z)
    if arrow:s.update(connector=connector,start_arrow='none',end_arrow='triangle',arrow_width='sm',arrow_length='sm')
    if dash:s['dash']=dash
    shapes.append(s);current['manifest_ids']['shapes'].append(id)
    current['protected_visual_anchors'].append(dict(id='anchor-'+id,kind='directed-connector' if arrow else 'connector',manifest_id=id,source_points_px=pts))

def text(id,value,box,size=7,bold=False,align='center',font='Arial Narrow',runs=None,color='#172127'):
    t=dict(id=id,text=value,box_px=box,font=font,font_size=size,bold=bold,color=color,
           align=align,valign='middle',fit_text=False,z_index=70)
    if runs:t['runs']=runs
    texts.append(t);current['manifest_ids']['text_boxes'].append(id)

def diamond(id,cy,value,height=37):
    shape(id,'shape',[179,cy-height/2,197,height],'#BFDEEC','#6191A6',.8,preset='diamond')
    text(id+'-question',value,[194,cy-height/2+3,165,height-6],6.8)

def person(prefix,cx,cy,fill='#D8E4E7',scale=1):
    d=7*scale
    shape(prefix+'-head','ellipse',[cx-d/2,cy-d/2,d,d],fill,INK,.5)
    shape(prefix+'-shoulders','bezier',[cx-8*scale,cy+4*scale,16*scale,9*scale],
          'none',INK,.55,bezier_px=[[cx-8*scale,cy+13*scale,cx-8*scale,cy+2*scale,cx+8*scale,cy+2*scale,cx+8*scale,cy+13*scale]])

def card(id,y,fill,edge,title,rest,description):
    shape(id,'roundRect',[406,y,221,37],fill,edge,.75,z=11)
    header=title+' '+rest
    text(id+'-header',header,[416,y+4,179,12],7.4,align='left',
         runs=[dict(text=title+' ',bold=True),dict(text=rest,bold=False)])
    text(id+'-description',description,[416,y+16,181,18],6.5,align='left')

region('input','Input scenario',[180,20,200,42])
shape('input-card','roundRect',[186,26,186,31],'#EAEAEA','#969696',.75,z=10)
text('input-title','Input: Target QA Application Scenario',[193,29,172,12],8.2)
text('input-subtitle','(Assess Key Decision Factors)',[193,41,172,12],7.7)
line('input-to-q1',[279,57,279,72],arrow=True)

region('prescreen','Phase 1 pre-screening',[72,63,563,108])
shape('phase1-background','rect',[72,63,563,108],'#ECECEC','none',z=0)
text('phase1-label','Phase 1: Pre-screening',[78,66,130,15],8.1,True,'left')
diamond('q1',91,'Is task complexity low and\nspecialization requirement not\nhigh?',38)
diamond('q2',147,'Is it in fields with high safety &\ncompliance requirements like\nMedical/Legal?',38)
line('q1-true',[376,91,406,91],arrow=True)
line('q1-false',[279,110,279,128],arrow=True)
line('q2-true',[376,147,406,147],arrow=True)
line('q2-false',[279,166,279,184],arrow=True)
for id,label,x,y in [('q1T','T',383,77),('q1F','F',284,111),('q2T','T',383,133),('q2F','F',284,168)]:text(id,label,[x,y,10,12],7.4)
card('single',73,'#DFDFDF','#8F8F8F','Single-Agent','Low latency, low cost.',
     'Suitable for: Simple fact query,\nsingle-step reasoning tasks')
person('single-person',605,89,'#D9D9D9',1)
shape('latency-clock','ellipse',[612,77,10,12],'none',INK,.55)
line('clock-hand1',[617,80,617,83],sw=.5);line('clock-hand2',[617,83,620,86],sw=.5)
card('hitl',128,'#F6C9C4','#BA746D','Hybrid + HITL','Human review at key points.',
     'Suitable for: Medical diagnosis, legal consultation,\nfinancial risk control')
person('reviewer',595,142,'#F3DEDB',.85)
shape('reviewer-hair','bezier',[589,132,12,12],'none',INK,.55,bezier_px=[[589,140,588,128,602,129,601,139]])
line('reviewer-hand',[588,148,585,153],sw=.55)
shape('reviewer-ball','ellipse',[586,147,8,8],'none',INK,.55)
shape('gavel-head','shape',[609,131,11,5],'#F3DED9',INK,.55,preset='parallelogram')
line('gavel-handle',[614,137,619,143],sw=1.1)
shape('gavel-base','rect',[608,143,10,2],'#F3DED9',INK,.5)
shape('safety-shield','shape',[608,149,13,13],'#F3DED9',INK,.55,preset='pentagon',flip_v=True)
shape('safety-shield-inner','shape',[611,151,7,8],'none',INK,.4,preset='pentagon',flip_v=True)

region('selection','Phase 2 selection',[72,176,563,149])
shape('phase2-background','rect',[72,176,563,149],'#E4F4FB','none',z=0)
line('phase-divider',[72,175,635,175],'#6799B0',.85,dash='dash',z=5)
text('phase2-label','Phase 2: Selection',[78,179,123,15],8.1,True,'left')
diamond('q3',206,'Is task workflow highly standardized\nwith clear serial dependencies?',38)
diamond('q4',265,'Does task difficulty fluctuate widely with\ncomplex cross-domain multi-hop reasoning?',44)
line('q3-true',[376,206,406,206],arrow=True)
line('q3-false',[279,225,279,243],arrow=True)
line('q4-true',[376,265,406,265],arrow=True)
line('q4-false',[279,287,406,306],arrow=True,connector='elbow')
for id,label,x,y in [('q3T','T',383,193),('q3F','F',284,227),('q4T','T',383,251),('q4F','F',283,288)]:text(id,label,[x,y,10,12],7.4)
card('hierarchy',187,'#DDEBC5','#819D64','Hierarchical','Manager-Executor / RAG Pipeline',
     'Suitable for: Knowledge-intensive QA,\nlong document QA')
nodes=[('h-top',608,198),('h-mid',608,209),('h-left',599,218),('h-bottom',608,218),('h-right',617,218)]
line('h-line1',[608,201,608,206],sw=.55)
line('h-line2',[608,211,608,214],sw=.55)
line('h-left-edge',[608,212,599,214],sw=.5)
line('h-right-edge',[608,212,617,214],sw=.5)
for id,cx,cy in nodes:shape(id,'rect',[cx-4,cy-2.5,8,5],'#F0F6E5',INK,.5)
card('adaptive',246,'#FFE0B7','#C69958','Hybrid','Adaptive switching / Mesh network',
     'Suitable for: Large complexity span,\nmulti-hop reasoning')
network=[(600,256),(609,254),(618,257),(596,264),(607,264),(616,268),(603,274)]
edges=[(0,1),(1,2),(0,3),(0,4),(1,4),(2,4),(2,5),(3,4),(3,6),(4,5),(4,6),(5,6)]
for j,(a,b) in enumerate(edges):line('mesh-edge-'+str(j),[*network[a],*network[b]],sw=.45)
for j,(cx,cy) in enumerate(network):shape('mesh-node-'+str(j),'ellipse',[cx-2.5,cy-2.5,5,5],'#FFF3DF',INK,.5,z=28)
card('flat',288,'#CAE4F1','#6191A6','Flat','Multi-party debate / Role play / Group chat',
     'Suitable for: Open-domain QA,\nmulti-perspective verification')
shape('chat-left','shape',[596,296,18,11],'#E7F2F8',INK,.55,preset='wedgeRectCallout')
shape('chat-right','shape',[605,302,18,11],'#D9EAF3',INK,.55,preset='wedgeRectCallout',flip_h=True)
for j in range(2):line('chat-content-'+str(j),[599,299+j*3,610,299+j*3],sw=.4,z=30)

# Native network components are measured and protected individually.
for reg,node_prefix,edge_prefix in [(regions[2],'mesh-node-','mesh-edge-')]:
    ns=[s for s in shapes if s['id'].startswith(node_prefix)]
    es=[s for s in shapes if s['id'].startswith(edge_prefix)]
    reg['compound_diagram']=dict(kind='node-link-diagram',object_inventory_complete=True,measurement_reviewed=True,
        native_object_policy='measured-simple-objects-native',
        nodes=[dict(id=s['id'],manifest_id=s['id'],geometry='circle',source_center_px=[s['box_px'][0]+2.5,s['box_px'][1]+2.5],source_size_px=[5,5]) for s in ns],
        edges=[dict(id=s['id'],manifest_id=s['id'],source_points_px=s['points_px'],line_style='solid',direction='none') for s in es])

region('note','Decision rule note',[73,328,565,15],'low')
current['strategy']='native-text-layout'
text('decision-note','Note: Phase 1 judgment is a hard constraint; Phase 2 is a preferred recommendation, practice can be balanced with team capabilities & budget constraints.',[78,329,552,12],6.2,align='left')
quality={
 'font_size_calibrated':dict(observation='Arial Narrow reproduces the compact lettering. Phase headings are 8.1 pt, result headers 7.4 pt, question text 6.8 pt and explanatory text 6.5 pt.'),
 'visual_inventory_matched':dict(observation='Input, four diamond decisions, eight T/F labels, five colored result cards and the original icon subjects all have native editable representations.'),
 'background_strategy_checked':dict(observation='White canvas, gray Phase 1 and pale blue Phase 2 retain the source positions and dashed phase boundary.'),
 'shape_corner_geometry_checked':dict(observation='Input and result cards use small six-pixel corner radii; decision diamonds and phase rectangles retain their original geometry.')}
manifest=dict(schema_version=2,slide=req['slide'],content_box=req['content_box'],source=dict(path='source.png',width_px=654,height_px=346),
 page_strategy='Faithful flow and text reconstruction with all components native and editable at the user explicit request.',
 user_overrides=dict(all_components_editable=True,native_pictogram_redraw_authorized=True,
 authorization='User requested all components editable for Figure 4; the plan explicitly states pictograms are rebuilt from native shapes.'),
 text_inventory=[t['text'] for t in texts],visual_inventory=[dict(id=r['id'],kind='native-structure',representation='native',description=r['label']) for r in regions],
 background_strategy=dict(mode='native-or-script',source_consistency_contract='Same input card, four decision diamonds, two phases, five output cards and note on the original 654 by 346 canvas.',removed_foreground='Readable text and pictograms reconstructed individually as native components.',comparison_note='The phase/card positions and branch destinations correspond to the source.'),
 quality_checks={k:True for k in quality},quality_evidence=quality,text_boxes=texts,shapes=shapes,images=[],asset_provenance=[],
 image2ppt_region_decomposition=dict(schema_version='image2ppt-region-decomposition-v1',page_complexity='structured',source_size_px=[654,346],regions=regions))
(P/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(f'{len(shapes)} shapes/lines and {len(texts)} editable text boxes; zero pictures')
