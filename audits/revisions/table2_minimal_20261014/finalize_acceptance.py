from pathlib import Path
import collections, hashlib, json, re, shutil, sys, xml.etree.ElementTree as ET
from pypdf import PdfReader

OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[1]
BUILD = ROOT/'tmp/table2_minimal_20261014_build'
sys.path.insert(0,str(ROOT/'tools'))
from active_tex import scan_manuscript

def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def dump(name,obj): (OUT/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2),encoding='utf8')
static = json.loads((OUT/'static_acceptance.json').read_text(encoding='utf8'))
manifest = json.loads((OUT/'protected_manifest.json').read_text(encoding='utf8'))
protected = {name:h for name,h in manifest.items() if not name.startswith('tmp/')}
changed = [name for name,h in protected.items() if sha(ROOT/name)!=h]
generated_concurrent = {f'manuscript.{ext}' for ext in ['pdf','aux','bcf','blg','log','synctex.gz']}
assert set(changed)-generated_concurrent=={'manuscript.tex'},changed
concurrent=[name for name in changed if name in generated_concurrent]
dump('concurrent_generated_changes.json', [dict(file=name,before_sha256=manifest[name],current_sha256=sha(ROOT/name),action='Preserved concurrent compiler output; this task did not publish to root') for name in concurrent])
before = (OUT/'before_manuscript.tex').read_bytes().decode('utf8')
after = (ROOT/'manuscript.tex').read_bytes().decode('utf8')
def region(text):
    label=text.index(r'\label{tab:9categories}')
    a=text.rfind(r'\begin{table*}',0,label)
    b=text.index(r'\end{table*}',label)+len(r'\end{table*}')
    return a,b,text[a:b]
a,b,new_table=region(after); x,y,old_table=region(before)
restored=after[:a]+old_table+after[b:]
restored=restored.replace('related mechanisms\r\ndo not define additional architecture classes.',
    'related mechanisms are shown separately\r\nand do not define additional architecture classes.',1)
assert restored==before,'Changes outside approved regions'
scan=scan_manuscript(ROOT)
cited={k for c in scan.citations for k in c.keys}
bbl=(BUILD/'manuscript.bbl').read_text(encoding='utf8')
bbl_keys=re.findall(r'\\entry\{([^}]+)\}',bbl)
bbl_lists=[]
for body in bbl.split(r'\datalist')[1:]:
    list_keys=re.findall(r'\\entry\{([^}]+)\}',body.split(r'\enddatalist',1)[0])
    assert len(list_keys)==78 and set(list_keys)==cited
    bbl_lists.append(len(list_keys))
assert len(set(bbl_keys))==78 and set(bbl_keys)==cited
bcf=ET.parse(BUILD/'manuscript.bcf')
compiled_cited={node.text for node in bcf.iter() if node.tag.endswith('}citekey')}
assert compiled_cited==cited
active='\n'.join(scan.active_texts.values())
refs=set(re.findall(r'\\(?:ref|eqref|autoref|pageref|cref|Cref)\*?\{([^}]+)\}',active))
labels=set(re.findall(r'\\newlabel\{([^}]+)\}',(BUILD/'manuscript.aux').read_text(encoding='utf8')))
assert not refs-labels,refs-labels
assert len(re.findall(r'\\label\{tab:9categories\}',active))==1
log=(BUILD/'manuscript.log').read_text(encoding='utf8',errors='replace')
undefined=re.findall(r'(?:Citation|Reference) [^\n]+undefined',log)
assert not undefined and 'There were undefined references' not in log
assert 'Please (re)run Biber' not in log and 'Rerun to get cross-references right' not in log
assert 'Float too large' not in log and 'Overfull \\vbox' not in log
ta=after[:a].count('\n')+1;tb=after[:b].count('\n')+1
table_over=[]
for match in re.finditer(r'Overfull \\hbox \(([^)]+)\).*?(?:at line (\d+)|at lines (\d+)--(\d+))',log,re.S):
    nums=[int(v) for v in match.groups()[1:] if v]
    if any(ta<=n<=tb for n in nums): table_over.append(match.group(0))
assert not table_over,table_over
blg=(BUILD/'manuscript.blg').read_text(encoding='utf8',errors='replace')
assert 'ERROR -' not in blg
q5=json.loads((ROOT/'audit_work/mentor_restore_stage2_20261013/q5_case_scores.json').read_text(encoding='utf8'))
assert q5['rating_counts']=={'broad':6,'partial':2,'divergent':2}
assert q5['source_counts']=={'Hierarchical':9,'Flat':1}
assert '\\includegraphics[width=0.80\\linewidth]{output/figure4_editable/20261013-161131-Figure4_architecture_selection/final/Figure4_architecture_selection_authority_v2.pdf}' in after
assert 'Figure4_architecture_selection_authority_v2.pdf' in (BUILD/'manuscript.fls').read_text(encoding='utf8')
reader=PdfReader(BUILD/'manuscript.pdf')
pages=[i+1 for i,p in enumerate(reader.pages) if 'Sub-paradigm' in p.extract_text() and 'Coordination' in p.extract_text()]
assert len(pages)==1,pages
page_text=reader.pages[pages[0]-1].extract_text()
assert 'degeneration' not in page_text
assert 'demonstrated' in page_text and 'AI User' in page_text and '(ICT)' in page_text
dest=ROOT/'output/pdf/table2_minimal_20261014.pdf'
dest.parent.mkdir(parents=True,exist_ok=True)
assert not dest.exists(),'Do not overwrite a prior PDF'
shutil.copyfile(BUILD/'manuscript.pdf',dest)
result=dict(pipeline=['pdfLaTeX pass1','Biber','pdfLaTeX pass2','pdfLaTeX pass3'],
    pdf_pages=len(reader.pages),table2_page=pages[0],pdf_sha256=sha(dest),
    bbl_entries=len(set(bbl_keys)),bbl_sort_lists_entry_counts=bbl_lists,compiled_citation_keys_match=True,cross_references_checked=len(refs),
    undefined_citations=0,undefined_cross_references=0,table2_overfull_hbox=0,float_too_large=False,
    biber_warnings=[line for line in blg.splitlines() if 'WARN -' in line],
    protected_non_temporary_files=len(protected),changed_existing_files=changed,
    root_pdf_unchanged=sha(ROOT/'manuscript.pdf')==manifest['manuscript.pdf'],
    concurrent_generated_changes=concurrent,task_published_to_root=False,
    q5_rating_counts=q5['rating_counts'],q5_source_counts=q5['source_counts'],
    figure4_authority_v2_used=True,output_pdf=str(dest),
    outside_table2_legacy_overfull_hbox=re.findall(r'Overfull \\hbox[^\n]*',log),
    visual_review='Pending final page preview inspection')
dump('compile_acceptance.json',result)
ledger=json.loads((OUT/'cell_verification.json').read_text(encoding='utf8'))
lines=['# Table 2 导师原版最小纠错执行报告','',
 '日期：2026-10-14。批准方案 A；仅修改 manuscript.tex 的 Table 2 与指定导语。不提交、不推送、不合并。', '',
 '## 实际修改与逐格验收','',
 '导师基线 f84c78b；执行前分支 codex/mentor-conservative-restore-stage2，HEAD 00f9b61。', '',
 '38 项 KEEP 均与导师原格逐字相同（只忽略空白、换行及分类显示格式）；九项必要纠错全部符合获批建议；R1C6 采用 Cost and aggregation sensitivity。六列表头、八机制行、原行序均保留。', '',
 '恢复 manager--executor 与 evidence-processing 两个独立行，取消两区分组及长篇 Hybrid 定义行。CAMEL / MDAgents 分类带特定工作流脚注；--- 不构成第四类。表注逐字包含 A hybrid architecture requires a demonstrated change in decision authority.。', '',
 '表前导语仅删除 are shown separately and；其余内容不变。caption 保留方案 A 已批准的 and related mechanisms。', '',
 '## 必要排版调整','',
 '第一轮恢复原列宽时，分类格 Hierarchical 加上脚注导致 1.22806 pt 超宽；窄列两端对齐也造成过大字间距。最终仅把 C1 从 1.4 cm 调至 1.5 cm，六列使用 raggedright / arraybackslash 左对齐。其余列宽、scriptsize、行距、table* 浮动环境与表中文字均未更改。Hierarchical 跨行数由导师原 3 修为 2。', '',
 '## 逐格导师原文与最终值','',
 '| 单元格 | 批准判定 | 导师原文 | 最终内容 |', '|---|---|---|---|']
for row in ledger:
    status='KEEP：逐字保留' if row['decision']=='KEEP' else ('R1C6：用户批准的最小修正' if row['decision']=='UNCERTAIN' else row['decision'])
    lines.append(f"| {row['id']} | {status} | `{row['mentor']}` | `{row['after']}` |")
lines += ['', '## 编译与一致性','',
 f"现有 APA7/Biber 流程完整通过：pdfLaTeX → Biber → pdfLaTeX → pdfLaTeX。PDF 共 {len(reader.pages)} 页；Table 2 在第 {pages[0]} 页。Biber 在沙箱内启动失败后，仅以沙箱外现有 Biber 重试成功，没有改配置或安装。", '',
 f"参考文献池85、实际引用78、核心13未变；BCF引用集合与有效源码一致，BBL含78条；{len(refs)}个唯一交叉引用目标均存在。恢复独立的两行引用后，引用命令由135变136，键出现仍为180，不增加文献。", '',
 'Q5评分6/2/2与来源9H/1F/0Hybrid、Triad的S归属均保留。所有其他正文、其他表格、hidden history、书目与现有图稿/PPTX/图稿PDF均按内容指纹保护；初次全量验证7662文件仅正文改变。最终再验525个非临时现有文件，除正文外检测到根目录6个编译产物并发更新，保留未回退，见concurrent_generated_changes.json。Figure 4 authority_v2路径保持，并由编译fls证实读取。', '',
 'Table 2无Overfull hbox、无过大浮动体；全文无未定义引用/交叉引用及待重运行提示。文档其他位置仍有两条已有超宽提示：标题123.62721 pt及未改正文0.5575 pt，未扩大范围处理。', '',
 '本轮脚本没有向根目录发布/复制编译产物。但根目录manuscript.pdf及aux/bcf/blg/log/synctex.gz在16:37:18被并发编译过程更新，其日志声明Output written on manuscript.pdf，与本轮独立输出目录不同。未将并发变化误报为字节不变，也未覆盖/还原。Git HEAD/分支/索引未动；本轮新PDF为 output/pdf/table2_minimal_20261014.pdf；完整修改补丁 before_after.patch；逐格结构化记录 cell_verification.json；编译检查 compile_acceptance.json。', '',
 '最终视觉检查结果将在 PDF 预览验收后补录。']
(OUT/'EXECUTION_REPORT.md').write_text('\n'.join(lines)+'\n',encoding='utf8')
print(json.dumps(result,ensure_ascii=False,indent=2))
