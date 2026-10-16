"""Synchronize final conference metadata, PDF output and regression evidence.

Run only after the current formal build and tools/run_apa_tests.py succeed.
Historical migration report and ledgers are archived before replacing summaries.
"""
from project_paths import project_path
from pathlib import Path
import collections,copy,hashlib,json,re,shutil,subprocess,sys
ROOT=Path(__file__).resolve().parents[1];OUT=project_path('apa7_audit');BASE=project_path('tmp/conference9_baseline')
sys.path.insert(0,str(ROOT/'tools'))
from active_tex import scan_manuscript
from build_reference_inventory import balanced_entries
def j(p):return json.loads(p.read_text(encoding='utf-8'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def write(p,v):p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def esc(s):return str(s).replace('|','\\|').replace('\n',' ')
keys=['fatemi2024financialqa','hendrycks2021mmlu','khot2023decomposed_prompting','park2023generative_agents','wang2023self_consistency','wu2024autogen','tang2025llmmedqa','yao2023react','zhou2023least_to_most']
overlay=j(project_path('apa_reference_adaptations.json'))['records'];maps={r['key']:r for r in overlay}
refs=j(OUT/'reference_78_acceptance.json');refmap={r['key']:r for r in refs}
before=j(OUT/'conference9_before78.json');beforemap={r['key']:r for r in before}
change=j(OUT/'conference9_change_log.json');review={r['key']:r for r in change['reviews']}
for n in ['apa14_results.json','extended_results.json','font_evidence.json','extended_font_evidence.json','coverage_results.json']:
    shutil.copy2(project_path('tmp/apa7_regression')/n,OUT/n)
core=j(OUT/'apa14_results.json');extended=j(OUT/'extended_results.json');coverage=j(OUT/'coverage_results.json')
assert len(core)==14 and all(r['result']=='PASS' for r in core)
assert len(extended)==15 and all(r['result']=='PASS' for r in extended)
assert len(refs)==78 and all(r['format_result']=='PASS' for r in refs)
assert len(j(OUT/'reference_85_preview.json'))==85 and all(r['format_result']=='PASS' for r in j(OUT/'reference_85_preview.json'))
scan=scan_manuscript(ROOT);commands=[c.raw_command for c in scan.citations];cited={k for c in scan.citations for k in c.keys}
rawpool={k for t,k,r in balanced_entries((project_path('references.bib')).read_text(encoding='utf-8'))}
assert len(commands)==136 and len(cited)==78 and len(rawpool)==85
assert cited==set(refmap) and rawpool==set(maps)
manifest=j(BASE/'manifest.json');head=manifest['head']
gitblob=lambda n:subprocess.check_output(['git','show',head+':'+n],cwd=ROOT)
protected=['manuscript.tex','references.bib','cas-dc.cls','cas-common.sty','cas-model2-names.bst','change_timeline.jpg','classify.jpg','fig3_topology.pdf','fig_flow.jpg','fig_reference_corpus.pdf']
assert all(sha(project_path(n))==manifest['tracked'][n] for n in protected)
assert len(overlay)==85
oldoverlay=j(BASE/'apa_reference_adaptations.json')
assert all(r==next(x for x in oldoverlay['records'] if x['key']==r['key']) for r in overlay if r['key'] not in keys)
assert all(r['original']==next(x for x in oldoverlay['records'] if x['key']==r['key'])['original'] for r in overlay)
baseline_source=project_path('tmp/conference9_source_baseline');baseline_source.mkdir(parents=True,exist_ok=True)
for n in ['manuscript.tex','eswa-apa-config.tex','eswa-apa-sourcemap.tex']:(baseline_source/n).write_bytes(gitblob(n))
oldscan=scan_manuscript(baseline_source)
assert commands==[c.raw_command for c in oldscan.citations]
pending=[r['key'] for r in refs if r['metadata_result']=='PENDING']
assert set(pending)==set(keys)-{'park2023generative_agents'}
fields=['author','year','title','booktitle','editor','publisher','pages','eid','pagetotal','doi','url']
nine=[]
for k in keys:
    r=maps[k];actual=refmap[k]['actual'];expect=r['original']|r['updates']
    extra={'same_key':k in cited,'actual_format_pass':refmap[k]['format_result']=='PASS','formal_version_preserved':r['original']==next(x for x in oldoverlay['records'] if x['key']==k)['original']}
    if k=='park2023generative_agents':
        extra.update(article2='(Article 2)' in actual,internal_pages_not_printed='(pp. 1–22)' not in actual,full_publisher='Association for Computing Machinery' in actual,editors_displayed=all(s in actual for s in ['S. Follmer','J. Han','J. Steimle','N. H. Riche']),no_wrong_eid_pages=expect['eid']=='2' and expect['pages'] is None and expect['pagetotal']=='22')
    if k=='fatemi2024financialqa':extra.update(full_publisher='Association for Computing Machinery' in actual,publisher_pages='530–537' in actual)
    if k=='tang2025llmmedqa':extra.update(publisher_ieee='IEEE.' in actual,publisher_pages='(pp. 1–8)' in actual)
    if k=='wu2024autogen':extra.update(awadallah_AH='Awadallah, A. H.' in actual,author_count_14=len(expect['author'].split(' and '))==14,no_invented_publisher=not expect.get('publisher'))
    if k in ['wang2023self_consistency','zhou2023least_to_most']:extra.update(full_initials='Le, Q. V.' in actual and 'Chi, E. H.' in actual)
    if k=='yao2023react':extra['narasimhan_KR']='Narasimhan, K. R.' in actual
    if k in ['wang2023self_consistency','yao2023react','zhou2023least_to_most','khot2023decomposed_prompting']:extra['iclr2023_formal_name']='The eleventh International Conference on Learning Representations' in actual
    if k=='hendrycks2021mmlu':extra['iclr2021_unchanged']=r['updates']['booktitle']==next(x for x in oldoverlay['records'] if x['key']==k)['updates']['booktitle']
    assert all(extra.values()),(k,extra)
    nine.append({'key':k,'before_pdf':beforemap[k]['actual'],'after_pdf':actual,'final_fields':{f:expect.get(f) for f in fields},'field_review':review[k],'checks':extra,'format_result':'PASS','metadata_result':refmap[k]['metadata_result'],'pdf_pages':refmap[k]['pages']})
write(OUT/'conference9_acceptance.json',nine)
archive=OUT/'history/conference9_baseline_20261012';archive.mkdir(parents=True,exist_ok=True)
for n in ['APA7_MIGRATION_REPORT.md','apa7_audit/metadata_changes.json','apa7_audit/scope_validation.json','apa7_audit/final_checks.json']:
    src=BASE/n;dest=archive/Path(n).name
    if src.exists() and not dest.exists():shutil.copy2(src,dest)
scope=j(BASE/'apa7_audit/scope_validation.json')
scope.update(formal_pdf_sha256=sha(project_path('manuscript.pdf')),references_sha256=sha(project_path('references.bib')),pool_count=85,bbl_count=78,commands=136,bbl_duplicates=[],cited_key_set_identical=True,commands_identical=True,format_pass=78,metadata_pending=pending,configuration_sha256={n:sha(project_path(n)) for n in ['manuscript.tex','eswa-apa-config.tex','eswa-apa-sourcemap.tex','apa_reference_adaptations.json']},final_bbl_sha256=sha(project_path('manuscript.bbl')),followup_date='2026-10-12',followup_baseline=head,followup_protected_file_equality={n:True for n in protected},non_target_overlay_records_identical=True)
write(OUT/'scope_validation.json',scope)
warnings={}
for label,path in [('before',project_path('tmp/conference9_before_build/manuscript.log')),('after',project_path('manuscript.log'))]:
    text=path.read_text(encoding='utf-8',errors='replace');warnings[label]={'overfull':re.findall(r'Overfull[^\n]+',text),'underfull_count':text.count('Underfull'),'warnings':re.findall(r'[^\n]*Warning[^\n]*',text),'errors':re.findall(r'^!.*$',text,re.M)}
warnings['biber_warnings']=[l for l in (project_path('manuscript.blg')).read_text(encoding='utf-8',errors='replace').splitlines() if 'WARN' in l or 'ERROR' in l]
assert not warnings['after']['errors'] and not warnings['after']['warnings'] and not warnings['biber_warnings']
assert warnings['before']['overfull']==warnings['after']['overfull']
warnings['comparison_baseline']='tmp/conference9_before_build/manuscript.log; same APA branch before nine-paper follow-up'
write(OUT/'warning_comparison.json',warnings)
layout=j(OUT/'conference9_pdf_comparison.json')
assert all(r['text_identical'] and r['pixels_identical_72dpi'] for r in layout['pages'][:18])
assert all(r['image_rectangles_identical'] and not r['outside_page'] for r in layout['pages'])
for r in layout['pages']:
    r['result']='PASS';r['visual_review']='Six contact sheets for 22 pages inspected; pages 19-22 additionally inspected at full rendered resolution. Double columns, hanging indents, target entries, captions and figures have no introduced clipping or overlap.'
write(OUT/'conference9_pdf_comparison.json',layout)
write(OUT/'pdf_page_review.json',[dict(page=r['page'],result=r['result'],note=r['visual_review'],outside_page=r['outside_page'],render=r['render'],text_identical_to_followup_baseline=r['text_identical'],pixels_identical_to_followup_baseline=r['pixels_identical_72dpi']) for r in layout['pages']])
final={'date':'2026-10-12','core14_pass':14,'extended15_pass':15,'body_pages_1_to_18_unchanged_after_conference9_followup':[r['pixels_identical_72dpi'] for r in layout['pages'][:18]],'formal_pages':22,'formal_pdf_sha256':scope['formal_pdf_sha256'],'configuration_sha256':scope['configuration_sha256'],'bbl_sha256':scope['final_bbl_sha256'],'metadata_pending':pending,'conference9_extra_checks':'9/9 output checks passed; remaining metadata uncertainty retained','scope_protection_pass':True,'baseline_head':head}
subprocess.run([sys.executable,'-B','-m','unittest','discover','-s','tests','-p','test_active_tex_bibpatch.py'],cwd=ROOT,check=True)
final['scanner_patch_tests_pass']=3
write(OUT/'final_checks.json',final)
retrieval=j(OUT/'conference9_sources/retrieval_manifest.json')
for source in retrieval:
    if source['name'] in ['apa_publishers','apa_conference']:
        source['content_validation']='BLOCKED_CHALLENGE_NOT_USABLE'
        source['usable_publication_evidence']=False
        source['note']='HTTP 200 body is an Incapsula challenge, not APA guidance; guidance was consulted separately through web retrieval.'
write(OUT/'conference9_sources/retrieval_manifest.json',retrieval)
table=['# 会议论文逐条分类与 APA 适配','', '2026-10-12 更新。56 条会议记录全部保留，52 条在正文引用。新增九篇字段核查见 conference9_final_review.md；缺字段不自动等同确证不存在。','', '|key|正文引用|实际出版形态|输出类型|编辑者/出版社适配|未核实字段|证据|','|---|---|---|---|---|---|---|']
for r in overlay:
    if r['original_type']!='inproceedings':continue
    f=r['original']|r['updates'];urls=list(dict.fromkeys(x['url'] for x in r['evidence'] if x and x.get('url')))
    table.append('|'+ '|'.join(map(esc,[r['key'],'是' if r['cited'] else '否',r['classification'],r['target_type'],f.get('editor','未补填')+' / '+f.get('publisher','未补填'),'；'.join(r['pending']) or '无新增必要字段缺口','；'.join(urls)]))+'|')
(OUT/'conference_56_review.md').write_text('\n'.join(table)+'\n',encoding='utf-8')
table=['# 正式参考文献 78 条逐项输出验收','', '2026-10-12 当前 PDF：78/78 格式输出检查通过，8 篇仍有 editor 等出版字段待补证。PENDING 不是不存在字段的证明，PASS 仅针对列明的输出检查。','', '|序号|key|页码|输出检查|元数据|实际 PDF 输出|','|---|---|---|---|---|---|']
for r in refs:table.append('|'+ '|'.join(map(esc,[r['index'],r['key'],','.join(map(str,r['pages'])),r['format_result'],r['metadata_result'],r['actual']]))+'|')
(OUT/'reference_78_review.md').write_text('\n'.join(table)+'\n',encoding='utf-8')
report=['# ESWA 九篇会议文献最终核查与 APA 7 验收报告','', '核查日期：2026-10-12。目标分支：`codex/eswa-apa7-migration`；基线提交：`'+head+'`。开始时工作区干净，没有需暂存或覆盖的本地改动。核查阶段未创建 Git 提交或推送；完成后用户另行授权将本轮改动提交并推送当前分支，不合并 main。','', '**格式和范围回归已通过；编辑者缺证的会议文献由 9 篇降为 8 篇，不能宣称全部出版元数据严格验收已闭环。** Generative Agents 的编辑者和 Article 2 已有证据，AutoGen 正式署名已修正，其他缺字段仍按证据保留 PENDING。','', '## 1. 证据与判断边界','', '用户本消息实际提供 8 篇不同论文的官方文章级 BibTeX：MMLU 重复一次，Decomposed Prompting 未出现。清理 Markdown 链接、HTML 空白实体、复制产生的反斜线后，仅保存相关字段，见 `conference9_sources/user_supplied_bibtex_fields.json`；没有覆盖原库。Decomposed Prompting 另查作者官方 [DecomP-ODQA 仓库的 Citation](https://github.com/HarshTrivedi/DecomP-ODQA)，核对题名、7 人顺序、2023 和正式会名。','', 'DOI 三篇逐条请求出版商登记的 Crossref，确认题名、作者顺序、年份、会议和页码；另外获取 UIST/ICAIF 整卷 DOI 登记、UIST 30 页前置材料、ICLR 2021/2023 出版目录和 COLM 官方录用名单。原始响应、访问失败、SHA-256 见 `conference9_sources/retrieval_manifest.json`。ACM 直连 403、OpenReview API 403／BibTeX 端点 404 均明确保留；没有把这些失败当无编辑者证据。','', 'UIST 编辑者使用同卷 ACM 官方网页可检索的 Published In 栏，它明确使用 Editors 标签，卷 DOI `10.1145/3586183`、ISBN `9798400701320` 与该文一致。前置材料中的 General/Program/Proceedings Chairs 仅作核对，不直接转换成 editor。网页缓存观察单独记录于 `uist_acm_editor_observation.json`，区别于本机下载成功的完整响应。','', '按 [APA 官方会议录规则](https://apastyle.apa.org/style-grammar-guidelines/references/examples/conference-proceeding-references)，保留会议录章节形态，不改成演讲、网页或预印本。按 [APA 出版社规则](https://apastyle.apa.org/blog/publisher-locations-in-book-references)，ACM 两篇使用出版记录给出的 Association for Computing Machinery；不添加 New York 或会议举办地。出版社全称是该出版记录与 APA source 规则共同支持的选择，不声称所有简称一律禁止。','', '文章级 BibTeX、整卷登记或目录不含 editor，均不能证明整卷没有编辑者。本轮没有找到足以确证另外 8 篇无编辑者的资料，因此全部保留空值及 PENDING。六篇 OpenReview 会议文献也没有取得可信的会议录连续页码，不能由论文长度补填。ICLR 的晚出 POD/USB 目录没有作为新版本或新页码来源，保持原正式 OpenReview 版本。','', '## 2. 九篇逐项结果','', '|引用键|已确认／修正|最终 editor / publisher / locator|仍待核实|主要证据|','|---|---|---|---|---|']
links={
 'fatemi2024financialqa':'https://doi.org/10.1145/3677052.3698686',
 'hendrycks2021mmlu':'https://openreview.net/forum?id=d7KBjmI3GmQ',
 'khot2023decomposed_prompting':'https://github.com/HarshTrivedi/DecomP-ODQA',
 'park2023generative_agents':'https://doi.org/10.1145/3586183.3606763',
 'wang2023self_consistency':'https://openreview.net/forum?id=1PL1NIMMrw',
 'wu2024autogen':'https://colmweb.org/2024/AcceptedPapers.html',
 'tang2025llmmedqa':'https://ieeexplore.ieee.org/document/11228647',
 'yao2023react':'https://openreview.net/forum?id=WE_vluYUL-X',
 'zhou2023least_to_most':'https://openreview.net/forum?id=WZH7099tgfM'}
notes={
 'fatemi2024financialqa':'2 人署名、2024、题名、会名、530–537、DOI 一致；ACM → 全称',
 'hendrycks2021mmlu':'7 人、2021、题名、URL 一致；会名和原适配保持',
 'khot2023decomposed_prompting':'作者官方仓库补证；7 人、2023、题名、URL 一致；正式 ICLR 2023 会名',
 'park2023generative_agents':'6 人、2023、题名、DOI 一致；补 4 位编辑者、Article 2、总页数22；ACM → 全称',
 'wang2023self_consistency':'8 人顺序不变；Le, Q. → Q. V.；Chi, E. → E. H.；正式会名',
 'wu2024autogen':'正式 COLM 2024 的14人及顺序确认；Awadallah, A. → A. H.',
 'tang2025llmmedqa':'9 人及顺序、2025、题名、IJCNN、IEEE、1–8、DOI 一致；保留既有正确适配',
 'yao2023react':'7 人顺序不变；Narasimhan, K. → K. R.；正式会名',
 'zhou2023least_to_most':'11 人顺序不变；Schärli 转正常姓名编码；Le, Q. V.、Chi, E. H.；正式会名'}
for k in keys:
    f=maps[k]['original']|maps[k]['updates'];locator='Article 2（pagetotal=22，内部1–22不打印）' if k=='park2023generative_agents' else f.get('pages','空；PENDING')
    remaining='无本轮新增元数据缺项' if k=='park2023generative_agents' else 'editor；publisher；pages' if k=='wu2024autogen' else 'editor；pages' if k in ['hendrycks2021mmlu','khot2023decomposed_prompting','wang2023self_consistency','yao2023react','zhou2023least_to_most'] else 'editor'
    report.append('|'+ '|'.join(map(esc,[k,notes[k],('已补4人' if k=='park2023generative_agents' else 'editor空')+' / '+f.get('publisher','publisher空；PENDING')+' / '+locator,remaining,'[正式记录]('+links[k]+')']))+'|')
report += ['', '所有已有 DOI/URL 保持一致；无 DOI 的 OpenReview 文献保持无 DOI。出版社不得根据平台、赞助商或主办人猜填。Financial QA 的 530–537 和 LLM-MedQA 的 1–8 是官方登记／用户正式 BibTeX 提供的范围，非按实际 PDF 页数构造。','', '## 3. Generative Agents 的文章编号、编辑者和实现','', '[ACM 正式文章页](https://doi.org/10.1145/3586183.3606763) 同时显示 Article No. 2 与 Pages 1–22；用户导出为 articleno=2、numpages=22。Crossref 仅登记 page=1–22 而未带 Article 编号，故不能只依其 pages 字段作为最终定位方式。APA 官方在[有文章编号的期刊条目](https://apastyle.apa.org/style-grammar-guidelines/references/elements-list-entry)中以 Article 取代页码；将这个定位原则应用于 ACM 文章编号会议录是本项目有明确记录的适配判断，APA 的会议录示例页没有直接给出同款 ACM 示例。','', '实现：独立 overlay 设置 `eid=2`、`pages=null`、`pagetotal=22`；原始 `pages=1--22` 不动，并在九篇台账保留 internal_pages=1--22 和官方 articleno/numpages。使用 eid 是 biblatex 标准字段，articleno 是 ACM 导出字段，numpages 是篇幅字段；二者都不能混成起始页。','', '当前 biblatex-apa 9.20 的 inbook driver 不打印 eid，所以项目配置仅修补 booktitle 后的定位宏：有 eid 输出 Article 2，否则保持原有 pp. 页码逻辑。安装的 APA 样式和 CAS 文件均未修改；宏补丁失配会报错，不静默丢失编号。最终 PDF 明确显示 `(Article 2)`，不显示 pp. 1–22。','', '4 位 editor 依同卷 [ACM 明确的编辑者标签](https://doi.org/10.1145/3586183.3606810)补入 Sean Follmer、Jeff Han、Jürgen Steimle、Nathalie Henry Riche。复核出版商姓名拆分时，Crossref 对 Nathalie Henry Riche 有 Riche / Henry Riche 两种历史形式（证据另存 `henry_riche_name_crossref.json`）；本次采用 Riche, Nathalie Henry，输出 N. H. Riche，完整署名未少词。该拆分选择透明保留，不以程序委员会身份推断编辑者。','', '## 4. AutoGen 及 ICLR 的处理','', '用户正式 OpenReview BibTeX 与 [COLM 2024 官方录用名单](https://colmweb.org/2024/AcceptedPapers.html)均列 Ahmed Hassan Awadallah。overlay 使用 `Awadallah, Ahmed Hassan`，最终 PDF 为 `Awadallah, A. H.`；仍为正式 2024 版全部 14 位作者，不混用 2023 预印本名单。COLM 官网组织信息只能确认会议，不足以确定出版社或 editor，相关字段保持 PENDING。','', '仅四篇 ICLR 2023（Decomposed Prompting、Self-Consistency、ReAct、Least-to-Most）补正式会名 `The Eleventh International Conference on Learning Representations`。保留会议专名，APA sentence case 生成 `The eleventh International Conference on Learning Representations`；2021 MMLU 和其他年份/文献未修改。同 [ICLR 2023 出版目录](https://www.proceedings.com/80586.html)相符；该目录明确区分原出版者 ICLR 与晚出的 POD 版本，未把 Curran 机械当成原文出版社。','', '## 5. 官方 BibTeX 与原值差异','', '|引用键|字段|本轮前有效值|最终有效值|依据|','|---|---|---|---|---|']
for r in change['changes']:report.append('|'+ '|'.join(map(esc,[r['key'],r['field'],r['before'],r['after'],'[证据]('+r['evidence']+')']))+'|')
report += ['', '共14项字段适配，所有字段修正仅在项目 overlay 与自动生成的 sourcemap。`references.bib` SHA-256 始终为 `'+scope['references_sha256']+'`。所有现有引用键、原字段、旧 pending 和被替代的差异记录保留于 verification_history、metadata_changes.history 及 history/conference9_baseline_20261012。','', '## 6. 修改前后实际 APA 7 输出','', '“前”来自本机独立重建的改动前 APA 分支 PDF，而非旧根目录生成物或预测字符串；“后”来自本次正式 PDF。文本抽取保留链接断行空白，实际可点击 URI 和字形另由78条输出检查与原尺寸页面验证。题名内排版断字可能导致抽取连接差异，应以 PDF 字形和原题名对照。','']
for r in nine:report += ['### '+r['key'], '', '**修改前：** '+r['before_pdf'], '', '**修改后：** '+r['after_pdf'], '', '格式输出：PASS；元数据：'+r['metadata_result']+'；正式 PDF 第 '+','.join(map(str,r['pdf_pages']))+' 页。','']
report += ['## 7. 回归、完整性、编译和版面','', '|验收|本轮实际结果|','|---|---|','|APA 核心|14/14 PASS|','|APA 扩展|15/15 PASS|','|九篇专项 PDF 检查|9/9 PASS；只代表列明的输出，不把缺证升级为已核实|','|正式78条逐项输出|78/78 PASS|','|85条独立预览|85/85 PASS|','|文献池／正文来源／命令|85／78／136；集合、键、全部命令逐项一致|','|原研究内容、图表、CAS|字节／哈希保护全部通过；其余76条 overlay 逐记录一致|','|完整构建|pdfLaTeX → Biber → pdfLaTeX → pdfLaTeX，全部成功|','|双栏和页数|22→22；第1–18页文本与72dpi像素逐页完全一致；全部图像与位置完全一致|','|视觉检查|22页联系表检查，参考文献19–22页另看完整分辨率，未引入裁切、重叠、缩进或跨栏问题|','|冻结BBL重建|本机三次pdfLaTeX、不跑Biber；22页文本与像素全部一致；不代表投稿服务器兼容|',f"|Overfull|{len(warnings['before']['overfull'])}→{len(warnings['after']['overfull'])}；三条既有值完全一致|",f"|Underfull|{warnings['before']['underfull_count']}→{warnings['after']['underfull_count']}；未增加|",'|最终编译／Biber 警告和错误|0／0；无未定义引用或需重跑提示|','', '已有 Overfull 为123.62721pt（CAS前置宏内部）、0.76843pt、0.5575pt；它们与改动前完全一致，页面无越界，不为了清警告改研究内容或布局。细节见 warning_comparison.json、conference9_pdf_comparison.json、scope_validation.json、final_checks.json、conference9_acceptance.json。','', '当前正式 PDF SHA-256：`'+scope['formal_pdf_sha256']+'`；BBL SHA-256：`'+scope['final_bbl_sha256']+'`。构建产物与日志在根目录和 tmp/apa7_build；前版在 tmp/conference9_before_build。','', '本机复现时，将 PyMuPDF 放入 Python 环境后，执行 `python -B tools/generate_apa_sourcemap.py`、`powershell -File build.ps1`、`python -B tools/run_apa_tests.py`、`python -B tools/audit_apa_output.py --skip-scope`、`python -B tools/audit_apa_output.py --pool85`。本轮运行环境用仓库 tmp/apa7_vendor 的 PyMuPDF，不修改全局 Python。修正了原测试/冻结脚本写死的 D 盘 TeX 路径，并修正 PowerShell 的 Biber 日志重定向；默认从 PATH 找本机引擎。引用扫描器仅增加对5参数 bibmacro补丁的跳过，仍拒绝隐藏引用/输入。','', '## 8. PENDING 的关闭与保留','', '关闭：Generative Agents 的 editor 缺项（同卷出版社明确标注四位编辑者）；其出版定位采用 Article 2，有证据的出版社全称、作者中间名与四篇正式会名修正完成。','', '保留：Financial QA、MMLU、Decomposed Prompting、Self-Consistency、AutoGen、LLM-MedQA、ReAct、Least-to-Most 的 editor（8篇）；MMLU／四篇ICLR2023／AutoGen 的会议录分页（6篇）；AutoGen 出版社（1篇）。8篇不能因用户官方文章级 BibTeX 没有这些字段而强行关闭。后续需要原整卷出版署名页或明确编辑／无编辑声明；如有分页需有同版本正式记录。','', '既有 Attention 页码、未引用 GenMentor/XAgent 等限制仍留在原台账；不扩本轮范围。原研究声明、图中的历史快照、内容与引用支持关系未作新核查，不能把本轮格式/出版字段检查理解为全部研究论证再次验证。导师的真实性和格式验收可使用这份当前证据进入审核，但“全部元数据无待核实项”仍不满足。']
report.insert(report.index('|APA 扩展|15/15 PASS|')+1,'|引用扫描器补丁回归|3/3 PASS；保留真实正文引用，拒绝补丁内隐藏引用或输入|')
report.insert(report.index('## 2. 九篇逐项结果'),'补充访问边界：本机下载的两份 APA 页面虽然 HTTP 200，正文实际为 Incapsula 验证页，已在 retrieval_manifest 标记不可作为出版证据。格式指导另经网页检索读取，不能把这两个缓存文件当作完整 APA 指南。\n')
(OUT/'conference9_final_review.md').write_text('\n'.join(report)+'\n',encoding='utf-8')
migration=['# ESWA APA 第七版迁移与会议文献收尾当前验收','', '更新日期：2026-10-12。当前正式稿 `cas-dc + biblatex-apa + Biber`；完整中文逐篇报告见 [九篇最终核查](apa7_audit/conference9_final_review.md)。原2026-10-11迁移报告完整保存在 [历史报告](apa7_audit/history/conference9_baseline_20261012/APA7_MIGRATION_REPORT.md)，其旧哈希、9篇缺证和旧PDF说明均为历史状态。','', '**当前格式回归与范围保护已通过；全部78篇严格出版元数据验收仍未闭环：8篇会议文献的editor等字段继续PENDING。** 不因空字段推断不存在。','', '## 当前结果','', '- 原始85条references.bib、78篇正文来源、136处引用命令和全部引用键完整保留。','- APA 核心14/14、扩展15/15、78条实际输出78/78、85条独立预览85/85通过。','- Generative Agents补出版社明确标注的四位editor，使用eid=2打印Article 2，pagetotal=22仅保存篇幅；内部1–22不冒充连续论文集分页。','- AutoGen保留COLM2024的14人正式作者名单，Awadallah的Hassan修正为A. H.；Self-Consistency／Least-to-Most的Le、Chi及ReAct的Narasimhan中间名同期修正。','- 两篇ACM出版社采用Association for Computing Machinery；只四篇ICLR2023改正式The Eleventh会名。','- 四阶段正式构建成功，22页；前18页像素完全一致，图表/位置和CAS未变。三条既有Overfull一致，Underfull未增加，无最终Biber/biblatex警告。','- 冻结BBL本机重建22页全部文本/像素一致；ESWA服务器后端与包版本兼容仍待平台核实。','', '当前 PDF SHA-256：`'+scope['formal_pdf_sha256']+'`；原库SHA-256：`'+scope['references_sha256']+'`。所有当前配置哈希见 [final_checks.json](apa7_audit/final_checks.json)，逐篇before/after/证据/未决项见完整中文报告。','', '## 仍未确认的字段','', '|key|剩余未核实字段|','|---|---|']
for k in pending:migration.append('|'+k+'|'+esc('；'.join(maps[k]['pending']))+'|')
migration += ['', 'ICLR/OpenReview空页码、AutoGen空publisher和以上空editor均不补造。未引用记录与既有可选限制保持，不改变正式版本、内容论证或引用关系。原迁移文档中的完整测试规则、投稿源文件包与历史差异可追溯，但其旧验证hash不得当作当前hash。','', '## 审阅状态','', '核查完成后，用户已授权将本轮改动提交并推送至GitHub的codex/eswa-apa7-migration分支；不合并main。审阅以该分支的核查提交为准。修改仅涉及项目引用适配、受影响审计/报告及为本机验收所需的工具修正。']
(project_path('APA7_MIGRATION_REPORT.md')).write_text('\n'.join(migration)+'\n',encoding='utf-8')
print(json.dumps({'core14':14,'extended15':15,'references78':78,'pool85':85,'commands':136,'metadata_pending':len(pending),'field_changes':len(change['changes']),'overfull':len(warnings['after']['overfull']),'underfull_before':warnings['before']['underfull_count'],'underfull_after':warnings['after']['underfull_count'],'report':'apa7_audit/conference9_final_review.md'},ensure_ascii=False))
