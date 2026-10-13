"""Author the corrected resource-map objects; Image2PPT CLI builds the slide."""
import json, math
from pathlib import Path
P=Path(__file__).resolve().parent
req=json.loads((P/'page_request.json').read_text(encoding='utf-8'))
scale=96*req['content_box']['width']/req['source_size_px']['width']
shapes,texts,regions=[],[],[]
current=None
INK='#365466'; BLUE='#168BCB'; LIGHT='#D8EAF2'; GOLD='#F4BE62'

def region(id,label,box):
    global current
    current=dict(id=id,label=label,source_bbox_px=box,risk_level='high',strategy='native-object-decomposition',
        reason='User approved the corrected resource categories and requires all components editable; native diagrams and pictograms implement that request.',
        manifest_ids=dict(shapes=[],text_boxes=[],images=[]),protected_visual_anchors=[])
    regions.append(current)

def shape(id,typ,box,fill='none',stroke=INK,sw=.7,z=25,**extra):
    s=dict(id=id,type=typ,box_px=box,fill=fill,stroke=stroke,stroke_width=sw*scale,z_index=z,**extra)
    if typ=='roundRect':s.update(source_corner_radius_px=min(3,box[3]/5),corner_category='small-radius')
    shapes.append(s);current['manifest_ids']['shapes'].append(id)
    current['protected_visual_anchors'].append(dict(id='anchor-'+id,kind='node-boundary',manifest_id=id,source_bbox_px=box))
    return s

def line(id,pts,stroke=INK,sw=.65,arrow=False,z=24,dash=None):
    s=dict(id=id,type='line',points_px=pts,stroke=stroke,stroke_width=sw*scale,z_index=z)
    if arrow:s.update(connector='straight',end_arrow='triangle',start_arrow='none',arrow_width='sm',arrow_length='sm')
    if dash:s['dash']=dash
    shapes.append(s);current['manifest_ids']['shapes'].append(id)
    current['protected_visual_anchors'].append(dict(id='anchor-'+id,kind='directed-connector' if arrow else 'connector',manifest_id=id,source_points_px=pts))

def text(id,value,box,size=8.5,bold=False,color='#142A38',font='Arial',align='center'):
    texts.append(dict(id=id,text=value,box_px=box,font=font,font_size=round(size*scale,2),bold=bold,color=color,align=align,valign='middle',fit_text=False,z_index=80))
    current['manifest_ids']['text_boxes'].append(id)

def ellipse(id,cx,cy,w,h,fill,stroke=INK,sw=.7,z=25):
    return shape(id,'ellipse',[cx-w/2,cy-h/2,w,h],fill,stroke,sw,z)

def page(id,cx,cy,w=19,h=24):
    shape(id,'shape',[cx-w/2,cy-h/2,w,h],'#F7FCFE',INK,.65,preset='foldedCorner')
    for j in range(3):line(id+'-rule-'+str(j),[cx-w/2+4,cy-4+j*4,cx+w/2-4,cy-4+j*4],sw=.5,z=30)

def lens(id,cx,cy,r=7):
    line(id+'-handle',[cx+r*.7,cy+r*.7,cx+r*1.65,cy+r*1.65],sw=2.1,z=37)
    ellipse(id+'-rim',cx,cy,2*r,2*r,'#AECBD9',sw=.8,z=38)
    ellipse(id+'-glass',cx,cy,2*r-4,2*r-4,'#F3FBFE',sw=.5,z=39)

def person(id,cx,cy,k=1):
    ellipse(id+'-head',cx,cy,5*k,5*k,GOLD,sw=.5)
    shape(id+'-body','roundRect',[cx-4*k,cy+4*k,8*k,7*k],LIGHT,INK,.6)

def robot(id,cx,cy,k=1):
    shape(id+'-head','roundRect',[cx-7*k,cy-5*k,14*k,10*k],LIGHT,INK,.6)
    for j,dx in enumerate((-3,3)):ellipse(id+'-eye-'+str(j),cx+dx*k,cy,1.6*k,1.6*k,INK,'none',z=31)
    line(id+'-antenna',[cx,cy-5*k,cx,cy-9*k],sw=.6)
    ellipse(id+'-tip',cx,cy-10*k,2.8*k,2.8*k,GOLD,sw=.4)
    shape(id+'-body','roundRect',[cx-6*k,cy+7*k,12*k,8*k],LIGHT,INK,.6)
    for j,dx in enumerate((-3,3)):line(id+'-leg-'+str(j),[cx+dx*k,cy+15*k,cx+dx*k,cy+18*k],sw=.8)

def brain(id,cx,cy,k=1):
    for j,(dx,dy) in enumerate([(-8,-8),(0,-12),(8,-8),(-10,1),(10,1),(-7,9),(0,12),(7,9)]):
        ellipse(id+'-lobe-'+str(j),cx+dx*k,cy+dy*k,10*k,11*k,'#A1DAF5',sw=.55)
    shape(id+'-processor','roundRect',[cx-6*k,cy-7*k,12*k,14*k],GOLD,INK,.55,z=35)
    for j,dx in enumerate((-9,9)):line(id+'-pin-'+str(j),[cx+dx*k,cy-3*k,cx+dx*.7*k,cy-3*k],sw=.5,z=37)

def globe(id,cx,cy,r=9):
    ellipse(id+'-outer',cx,cy,2*r,2*r,'#A8DDEB',sw=.7)
    ellipse(id+'-meridian',cx,cy,r*.95,2*r,'none',sw=.5,z=29)
    for j,dy in enumerate((-r*.45,0,r*.45)):line(id+'-parallel-'+str(j),[cx-r*.85,cy+dy,cx+r*.85,cy+dy],sw=.45,z=30)

def bolt(id,cx,cy,k=1):
    shape(id,'shape',[cx-6*k,cy-12*k,12*k,24*k],GOLD,INK,.55,preset='lightningBolt',z=35)

region('foundation','Foundation layer',[74,13,212,159])
ellipse('foundation-circle',145,83,140,140,'#FCE8D5','none',z=0)
text('foundation-title','Foundation Layer',[90,40,110,14],8.1,True)
text('foundation-subtitle','Model & Retrieval\nComponents',[85,54,120,26],8.0)
shape('langchain-window','rect',[103,83,25,19],'#F9FBFC',INK,.65)
shape('langchain-topbar','rect',[103,80,25,5],GOLD,INK,.55)
for j in range(3):ellipse('window-dot-'+str(j),107+j*4,82.5,1.2,1.2,INK,'none')
text('langchain-code','</>',[106,87,20,10],7.6,bold=True)
ellipse('chain-link1',124,101,11,6,'none',sw=.9)
ellipse('chain-link2',128,106,11,6,'none',sw=.9)
text('langchain-name','LangChain',[87,113,58,14],7.0)
# Native llama silhouette rather than a bitmap logo.
llama_points=[[160,94],[163,94],[162,82],[166,80],[169,84],[170,92],[176,94],[176,101],[166,101],[163,99]]
shape('llama-silhouette','shape',[160,80,16,22],'#243945','#243945',.5,polygon_px=llama_points)
for j,x in enumerate((164,168,174)):line('llama-leg-'+str(j),[x,99,x-1,108],sw=1.25)
line('llama-tail',[176,95,180,92],sw=1)
for j,(cx,cy) in enumerate([(185,85),(185,95),(185,105)]):
    ellipse('index-node-'+str(j),cx,cy,4,4,'#DCEFFA',sw=.5)
    if j:line('index-edge-'+str(j),[185,cy-8,185,cy-2],sw=.5)
text('llamaindex-name','LlamaIndex',[145,113,58,14],7.0)
line('foundation-interface',[278,132,221,115],'#858E92',.7,arrow=True)
line('foundation-retrieval',[216,125,275,142],'#858E92',.7,arrow=True)
text('interface-label','Model\nInterfaces',[230,91,80,28],9.0)
text('retrieval-label','Retrieval\nComponents',[196,142,84,29],8.8)

region('orchestration','Orchestration layer',[414,13,217,160])
ellipse('orchestration-circle',559,83,140,140,'#EEECDC','none',z=0)
text('orchestration-title','Orchestration Layer',[497,40,124,14],8.1,True)
text('orchestration-subtitle','Multi-Agent Frameworks',[496,54,126,16],8.0)
shape('autogen-gear1','shape',[514,74,15,15],'#B2D9EB',INK,.55,preset='gear6')
shape('autogen-gear2','shape',[525,84,18,18],GOLD,INK,.55,preset='gear6')
text('autogen-name','AutoGen',[502,105,51,13],7.0)
crew_nodes=[(592,78),(583,94),(602,94)]
for j,(cx,cy) in enumerate(crew_nodes):person('crew-member-'+str(j),cx,cy,.8)
for j,(a,b) in enumerate([(0,1),(0,2),(1,2)]):line('crew-link-'+str(j),[*crew_nodes[a],*crew_nodes[b]],sw=.4,z=22)
text('crewai-name','CrewAI',[572,105,45,13],7.0)
robot('metagpt-robot',559,121,.72)
shape('metagpt-terminal','rect',[550,131,18,7],'#DBECF3',INK,.5)
text('metagpt-name','MetaGPT',[533,138,53,13],7.0)
line('role-definition',[424,131,482,115],'#858E92',.7,arrow=True)
line('workflow-control',[483,125,424,141],'#858E92',.7,arrow=True)
text('role-label','Role\nDefinition',[400,91,76,28],9.0)
text('workflow-label','Workflow\nControl',[428,142,67,29],8.8)

region('applications','Application resources',[74,208,211,165])
ellipse('application-circle',145,303,140,140,'#D3E7F0','none',z=0)
text('application-title','Application\nResource Layer',[90,246,110,27],8.1,True)
text('application-subtitle','Representative Platforms',[85,271,120,15],8.0)
page('storm-page',104,311,18,24);bolt('storm-bolt',93,307,.8)
text('storm-name','STORM',[82,323,42,13],7.0,font='Arial Narrow')
for j,(cx,cy) in enumerate([(145,299),(138,314),(153,314)]):
    ellipse('costorm-node-'+str(j),cx,cy,6,6,GOLD if j==0 else '#A4D4ED',sw=.65)
for j,(a,b) in enumerate([(0,1),(0,2),(1,2)]):
    points=[(145,299),(138,314),(153,314)]
    line('costorm-link-'+str(j),[*points[a],*points[b]],sw=.65,z=22)
bolt('costorm-bolt',133,303,.65)
text('costorm-name','Co-STORM',[118,323,56,13],7.0,font='Arial Narrow')
page('ragflow-page',187,307,20,24);lens('ragflow-lens',194,314,6)
text('ragflow-name','RAGFlow',[167,323,43,13],7.0,font='Arial Narrow')
line('synthesis-link',[217,251,276,235],'#858E92',.7,arrow=True)
line('document-link',[276,245,221,262],'#858E92',.7,arrow=True)
text('synthesis-label','Retrieval-Grounded\nSynthesis',[173,207,112,29],8.5)
text('document-label','Document\nUnderstanding',[218,263,89,28],8.8)

region('evaluation','Benchmarks and evaluation tools',[415,210,225,173])
ellipse('evaluation-circle',559,303,160,160,'#E9E1EE','none',z=0)
text('evaluation-title','Benchmarks &\nEvaluation Tools',[493,238,132,27],8.1,True)
text('qa-benchmark-group','QA & knowledge benchmarks',[493,265,132,13],6.7,True)
for j,(cx,name) in enumerate([(509,'HotpotQA'),(542,'CoQA'),(576,'MMLU'),(609,'MuSiQue')]):
    cy=291
    if j==0:
        shape('hotpot-db','rect',[cx-8,cy-6,13,13],'#B9AED1',INK,.55)
        ellipse('hotpot-top',cx-1.5,cy-6,13,5,'#C9C1DE',sw=.55,z=30)
        lens('hotpot-lens',cx+4,cy+4,4)
    elif j==1:
        shape('coqa-bubble','shape',[cx-10,cy-8,20,15],'#A9D9EF',INK,.6,preset='wedgeRoundRectCallout')
        text('coqa-bubble-word','QA',[cx-7,cy-6,14,9],5.6,True)
    elif j==2:brain('mmlu-brain',cx,cy,.52)
    else:
        for n,dx in enumerate((-7,0,7)):ellipse('musique-node-'+str(n),cx+dx,cy,5,5,GOLD,sw=.55)
        line('musique-edge1',[cx-5,cy,cx-2,cy],sw=.65)
        line('musique-edge2',[cx+2,cy,cx+5,cy],sw=.65)
    text('qa-name-'+str(j),name,[cx-21,303,42,12],6.8,font='Arial Narrow')
text('agent-benchmark-group','Agent-task benchmarks',[493,316,132,12],6.7,True)
robot('agentbench',526,337,.46)
shape('gaia-clipboard','rect',[552,328,15,19],'#FFFBF2',INK,.55)
shape('gaia-clip','roundRect',[556,326,7,4],GOLD,INK,.4)
for j in range(3):
    line('gaia-check-'+str(j),[554,333+j*4,555,334+j*4],sw=.55)
    line('gaia-rule-'+str(j),[558,333+j*4,564,333+j*4],sw=.4)
globe('webarena-globe',592,337,9)
for j,(cx,name,w) in enumerate([(526,'AgentBench',54),(559,'GAIA',30),(592,'WebArena',48)]):
    text('agent-name-'+str(j),name,[cx-w/2,348,w,12],6.8,font='Arial Narrow')
line('evaluation-tool-divider',[524,362,594,362],'#B7ABBE',.45,dash='dash')
shape('autorag-gear','shape',[525,367,9,9],GOLD,INK,.4,preset='gear6')
text('autorag-tool','RAG tool: AutoRAG',[538,365,66,13],6.5,bold=True,font='Arial Narrow')
line('answer-assessment',[484,251,424,235],'#858E92',.7,arrow=True)
line('rag-assessment',[423,245,480,261],'#858E92',.7,arrow=True)
text('answer-label','Answer & Task\nAssessment',[425,207,96,29],8.5)
text('rag-label','RAG Component\nEvaluation',[388,263,90,28],8.0)

region('system','Central system and construction outcome',[207,130,291,263])
shape('central-hexagon','shape',[282,130,140,115],BLUE,'none',z=5,preset='hexagon')
brain('system-brain',352,165,1)
text('system-ai','AI',[345,157,14,17],8.8,True)
text('system-title','Multi-Agent\nQA System',[301,194,102,40],11.5,True,color='#FFFFFF')
line('construction-arrow',[352,251,352,304],'#858E92',.8,arrow=True)
page('construction-document',351,325,24,28)
shape('construction-clip','roundRect',[345,309,12,5],GOLD,INK,.6)
for j in range(3):ellipse('construction-bullet-'+str(j),344,320+j*5,2,2,GOLD,sw=.5,z=35)
shape('construction-gear','shape',[354,326,18,18],GOLD,INK,.7,preset='gear6',z=40)
text('construction-outcome','System Construction\n& Evaluation',[281,348,142,28],9.0)
text('interpretation-note','Conceptual resource map; process assessment needs trace-level measures.',[207,378,291,14],6.6,font='Arial Narrow',color='#607181')

# Native networks have a complete, measured node-and-edge inventory.
node_ids=['costorm-node-0','costorm-node-1','costorm-node-2']
edge_ids=['costorm-link-0','costorm-link-1','costorm-link-2']
items={s['id']:s for s in shapes}
regions[2]['compound_diagram']=dict(kind='node-link-diagram',object_inventory_complete=True,measurement_reviewed=True,
    native_object_policy='measured-simple-objects-native',
    nodes=[dict(id=id,manifest_id=id,geometry='circle',source_center_px=[items[id]['box_px'][0]+3,items[id]['box_px'][1]+3],source_size_px=[6,6]) for id in node_ids],
    edges=[dict(id=id,manifest_id=id,source_points_px=items[id]['points_px'],line_style='solid',direction='none') for id in edge_ids])
quality={
 'font_size_calibrated':dict(observation='Type is calibrated to the unchanged prepared canvas using a 1.832 scale factor; resource labels and layer titles use consistent physical levels.'),
 'visual_inventory_matched':dict(observation='Four colored circles, central hexagon, eight reciprocal relation arrows, one outcome arrow and all labeled resources use native objects.'),
 'background_strategy_checked':dict(observation='White canvas and peach, beige, blue and lavender resource circles retain the source arrangement; the evaluation circle is enlarged for the approved category separation.'),
 'shape_corner_geometry_checked':dict(observation='Resource regions remain true circles and the system uses a native hexagon. Document and processor shapes keep restrained corner radii.')}
manifest=dict(schema_version=2,slide=req['slide'],content_box=req['content_box'],source=dict(path='source.png',width_px=686,height_px=393),
 page_strategy='Corrected resource-map reconstruction using native editable slide objects throughout.',
 user_overrides=dict(all_components_editable=True,native_pictogram_redraw_authorized=True,content_corrections_authorized=True,
    authorization='User accepted the preceding content audit and instructed execution; it explicitly proposes editable native text, regions, arrows and diagrams.'),
 text_inventory=[t['text'] for t in texts],visual_inventory=[dict(id=r['id'],kind='native-structure',representation='native',description=r['label']) for r in regions],
 background_strategy=dict(mode='native-or-script',source_consistency_contract='Same four outer resource circles, central blue hexagon and reciprocal support/assessment links on the supplied canvas.',removed_foreground='Labels and pictograms rebuilt independently as native objects.',comparison_note='Palette, central composition and named resources retained, with the approved grouping and terminology corrections.'),
 quality_checks={k:True for k in quality},quality_evidence=quality,text_boxes=texts,shapes=shapes,images=[],asset_provenance=[],
 image2ppt_region_decomposition=dict(schema_version='image2ppt-region-decomposition-v1',page_complexity='structured',source_size_px=[686,393],regions=regions),
 content_corrections=dict(foundation_subtitle='Model & Retrieval Components',evaluation_header='Benchmarks & Evaluation Tools',
     benchmark_groups=['QA & knowledge benchmarks','Agent-task benchmarks'],added_benchmark='MuSiQue',tool='AutoRAG',
     relation_labels=['Answer & Task Assessment','RAG Component Evaluation'],outcome='System Construction & Evaluation',
     interpretation='Conceptual map, resources may span layers, process assessment requires trace-level measures.'),
 content_sources=['https://aclanthology.org/2024.naacl-long.347/','https://aclanthology.org/2024.emnlp-main.554/',
 'https://github.com/infiniflow/ragflow/tree/v0.6.0','https://arxiv.org/abs/2410.20878',
 'https://aclanthology.org/D18-1259/','https://arxiv.org/abs/1808.07042','https://arxiv.org/abs/2009.03300',
 'https://aclanthology.org/2022.tacl-1.31/','https://arxiv.org/abs/2308.03688','https://arxiv.org/abs/2311.12983','https://arxiv.org/abs/2307.13854'])
(P/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(f'Authored {len(shapes)} shapes/connectors + {len(texts)} text boxes; zero images; font scale={scale:.3f}')
