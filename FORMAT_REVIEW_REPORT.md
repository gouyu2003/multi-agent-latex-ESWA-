# ESWA 排版与 APA 验证实施报告

## 当前状态

已完成用户最终确认的本轮范围：统一正文双栏、整理图5和表4、补表6正文引用，以及分别依据 APA7 和 ESWA 核查网页访问日期。

APA 独立样例未通过严格合规门槛。用户随后选择“本轮先完成排版、表6引用和访问日期核查，暂缓 APA 迁移”。局部 CAS/BibTeX 样式原型停留在 `tmp/format_review/apa_gate/`，没有接入正式论文。未运行 Biber，未迁移引用系统。**当前正式 PDF 仍使用原 CAS 引用样式，不能称为严格 APA 第七版或全部投稿要求已通过。**

恢复基线：Git 标签 `codex/eswa-format-baseline-20261010`，提交 `98732a209e1e7acac768fd76c7c296dc4c99ebbd`。建立标签时工作区干净。

## APA 独立最小样例

正式论文和原始参考文献未参与实验性样式切换。样例使用官方 `cas-dc`、`natbib`、BibTeX，引用两个真实 Chen 条目、两个真实 Yao 条目、真实长作者名单及合成边界案例。完整执行 pdfLaTeX → BibTeX → pdfLaTeX → pdfLaTeX。

原型仅在官方 CAS 样式的副本上尝试局部格式适配：年份括号、括号/叙述引用的连接词、20/21人作者名单以及 DOI 优先输出。原始 CAS 文件未修改。

14项检查通过8项，失败6项；**整体结果为 FAIL，不得称为严格 APA 第七版**。

| 检查 | 结果 | 实际问题或通过依据 |
|---|---|---|
| 两人括号引用 `&` | 通过 | `(Alpha & Beta, 2020)` |
| 两人叙述引用 `and` | 通过 | `Alpha and Beta (2020)` |
| 三人及以上首次引用 `et al.` | 通过 | 首次输出 `Gamma et al., 2021` |
| 机构作者 | 通过 | 机构名未被拆为个人姓名 |
| 20人参考文献名单 | 通过 | 全部20人 |
| 21人参考文献名单 | 通过 | 前19人、省略号、末位作者 |
| 相同作者名单同年分配 `a/b` | 通过 | Alpha study / Beta study 按题名分配后缀 |
| DOI 优先于重复 URL | 通过 | 仅输出规范 DOI URL |
| 不同首作者同姓的首字母消歧 | **失败** | J. Chen / W. Chen 被错误合并为 `Chen et al., 2024a,b` |
| 相同首作者、不同作者名单的 `et al.` 消歧 | **失败** | 两个 Yao 条目被错误合并为 `Yao et al., 2023a,b`，没有展开 Yu / Zhao |
| `et al.` 不可仅替代一人 | **失败** | 仅最后作者不同的四人名单仍被缩写并错误添加 `a/b` |
| 同年后缀的年份完整显示 | **失败** | 输出 `2022a,b`，没有输出 `2022a, 2022b` |
| 期刊、卷号斜体及期号 | **失败** | 局部原型仍沿用 CAS 的期刊/卷期输出，没有满足目标格式 |
| DOI 末尾不加句点 | **失败** | CAS 统一结尾标点仍附加句点 |

失败不是“BibTeX 在理论上不能实现 APA7”的证明。它表明当前 CAS 样式的局部修改不足以严格满足要求。首字母和作者前缀消歧需要跨条目比较真实作者身份，年份后缀不能继续根据缩写后的引用标签分配；合并引用还需要适配 natbib 的显示行为。继续实施意味着维护更完整的自定义样式和引用辅助逻辑，不能把仅修改标点的原型接入正式论文。

依据：

- [APA 作者—年份规则](https://apastyle.apa.org/style-grammar-guidelines/citations/basic-principles/author-date)
- [APA 相同 et al. 缩写的消歧](https://apastyle.apa.org/style-grammar-guidelines/citations/basic-principles/same-year-first-author)
- [APA 相同作者和年份](https://apastyle.apa.org/style-grammar-guidelines/citations/basic-principles/same-year-author)
- [APA 参考文献组成与作者名单](https://apastyle.apa.org/style-grammar-guidelines/references/elements-list-entry)
- [APA DOI 与 URL](https://apastyle.apa.org/style-grammar-guidelines/references/dois-urls)

原始证据：`tmp/format_review/apa_gate_results.json`、样例 `.tex/.bib/.bst/.bbl/.pdf` 和四阶段构建日志。该实验 PDF 仅用于检查，不是投稿文件。

## 替代路线与待决定事项

可以继续深度定制 BibTeX，也可以在确认后改用 `biblatex-apa` + Biber。后者由维护中的 APA7 专用样式处理多数规则，但仍必须先通过独立样例，不能把安装了样式当作已合规。

投稿兼容性需要另行验证：本地 TeX Live / Biber 与投稿系统版本可能不同；CAS 的文献标题、字号、超链接和命令兼容性需要检查。Elsevier 的官方说明列出标准 BibTeX 和 `.bbl` 提交方式，不足以确认该期刊系统可直接运行本地 Biber 配置，也不能据此断言其不支持 Biber。

- [CTAN：biblatex-apa](https://ctan.org/pkg/biblatex-apa)
- [Elsevier LaTeX 投稿说明](https://www.elsevier.support/publishing/answer/how-to-submit-a-latex-file-in-editorial-manager)

## 修改文件清单及前后差异

| 文件 | 本轮变化 |
|---|---|
| `manuscript.tex` | 移除有效正文中的两处单栏切换及其配套强制分页；图5改为跨栏；表4改为跨栏、自适应列宽和局部字号设置；补表6引用 |
| `references.bib` | 为3个网页条目补有证据的访问日期，更新另1个网页条目的最后访问日期；其余字段不变 |
| `FORMAT_REVIEW_REPORT.md` | 新增本报告，记录差异、APA门槛、访问日期依据、构建及逐页检查结果 |
| `manuscript.pdf` | 更新完整编译产生的 PDF，从23页变为22页；该文件为生成物，Git忽略规则保持原样 |
| 编译辅助文件 | 更新生成的 `.aux/.bbl/.log/.blg/.out/.abs`；仍使用原 BibTeX 路线 |

实验样例、基线快照、构建日志、页面图和机器验证结果均位于 Git 已忽略的 `tmp/format_review/`。没有把失败样式安装到正式目录，也没有修改官方模板或历史审计台账。

关键差异：

- 表1前：删除有效的 `\clearpage` 和 `\onecolumn`，表1保留跨栏，后续正文连续双栏。
- 图5：`figure` → `figure*`；最终宽度为 `0.94\textwidth`，实测约163.4 mm，按原比例显示。图内主要文字、图标和箭头在页面尺度复查中可辨认；原始 `classify.jpg` 未改。
- 表4：`table` → `table*`；`tabular` → `tabularx`；前两列为2.6 cm和2.0 cm，其余四列自适应。字号由 `\normalsize` 改为局部 `\small`，保留全部8个框架行、6列内容及引用。移除表前后栏位切换和强制分页。
- 表6：首次介绍相关资源的段落末尾新增 `Table~\ref{tab:benchmark_resources} summarizes these resources and their primary evaluation roles.`，没有新增研究结论。
- 引用系统：仍为 `natbib` + `cas-model2-names.bst`；原引用键、作者、年份、文献版本及85条文献池完整保留。

逐行差异：[before_after.patch](<D:/multi-agent review_joural/ESWA_Submission_caomodify/tmp/format_review/before_after.patch>)。

## 网页和软件访问日期核查

APA7 的一般规则只对未归档且设计为持续变化的内容要求访问日期；稳定的署日期文章、固定版本软件通常不要求。ESWA 所提供指南的 **Web references** 部分另要求网页引用提供完整 URL 和最后访问日期。因此，以下网页日期按 ESWA 要求处理，不宣称它们均为 APA7 的一般必填字段。[APA 日期规则](https://apastyle.apa.org/style-grammar-guidelines/references/elements-list-entry)、[ESWA 官方指南](https://www.sciencedirect.com/journal/expert-systems-with-applications/publish/guide-for-authors)

ESWA 官网本轮直接读取失败；指南依据为用户提供的官方复制文本，位置为 `C:/Users/ccbus/.codex/attachments/1e5c800f-f183-40c9-8efc-240c0c44032e/已粘贴的文本.txt`。该读取失败没有用于证明任何访问日期。

| 条目 | 分类与规则 | 本轮访问证据 | 正式文献处理 |
|---|---|---|---|
| `anthropic2024mcp` | 署日期公告网页：APA一般不要求日期，ESWA网页要求日期 | 成功读取所引公告 URL；另有历史检索日志记录同一 URL 于2026-10-10返回200 | 新增2026-10-10 |
| `google2025a2a` | 署日期博客网页：同上 | 成功读取所引 Google Developers Blog 页面及作者/日期信息 | 新增2026-10-10 |
| `langgraph2024` | 署日期博客网页：同上 | 成功读取所引 LangChain 页面，能确认题名与署名 | 新增2026-10-10 |
| `langgraph2024interrupt` | 署日期博客网页：同上 | 成功重新读取所引 interrupt 文章页面 | 将原2026-10-08更新为本次真实再访问的2026-10-10 |
| `crewai2023` | 固定版本软件0.1.0：APA一般不要求访问日期；ESWA软件示例未明确要求访问日期，不因包含URL就自动改判为网页引用 | 成功读取所引 PyPI 0.1.0 页面 | 不机械追加日期；访问事实仅保存在证据中 |
| `dify2024` | 固定版本软件0.6.0：APA一般不要求访问日期 | 成功读取所引 GitHub 0.6.0版本页面，保留明确版本依据 | 保留已有有据可查的2026-10-10；不称为APA一般必填 |
| `ragflow2024` | 固定版本软件0.6.0：同上 | 成功读取所引 GitHub v0.6.0版本页面 | 保留已有有据可查的2026-10-10；不称为APA一般必填 |

本次成功访问发生于2026-10-10，时区按 Asia/Shanghai 记录。没有把当前日期批量填入所有含 URL 的期刊、会议或软件条目；没有使用403、失败请求或近似 URL 替代实际所引网址的访问证据。

逐条证据：[web_access_evidence.json](<D:/multi-agent review_joural/ESWA_Submission_caomodify/tmp/format_review/web_access_evidence.json>)。完整工具读取记录保存在同目录的两个 `web_access_*tool_output.txt` 文件中。

## 构建与范围验证

基线和修改版分别完整执行 `pdfLaTeX → BibTeX → pdfLaTeX → pdfLaTeX`。修改版四个阶段均返回0，PDF为22页，图表编号保持一致。

| 验证 | 结果 |
|---|---|
| 有效源码引用键 | 78，和基线完全相同 |
| 编译 `.aux` 引用键 | 同一组78 |
| 编译 `.bbl` 文献条目 | 同一组78，无重复、无新增或缺失 |
| 文献池 | 原85条完整保留 |
| 未定义引用或交叉引用 | 0 |
| `Float too large` / `Overfull \vbox` | 0 |
| PDF文字超出纸张范围 | 0；同时进行了视觉检查，不能只用该指标替代版面复查 |
| 正文栏位 | 有效源码没有 `\onecolumn/\twocolumn`；第2—18页正文均检测到左右两栏文字，首页遵循CAS前置格式 |
| 官方模板、图片及其他原有受Git跟踪文件 | 除 `manuscript.tex`、`references.bib` 外，全部原有受Git跟踪文件SHA-256保持一致 |
| 禁用历史章节 | 内容逐字节等价核对通过 |
| 文献元数据 | 仅4个条目的 `note` 字段发生日期变化；其余作者、年份、题名、来源、URL/DOI等字段一致 |
| Git差异空白检查 | `git diff --check` 通过 |

编译不是完全无警告：原来的6条 `Overfull \hbox` 减为4条，表4相关警告已消除。保留的4条宽度分别为123.62721 pt、0.76843 pt、0.5575 pt和0.92711 pt，均在基线中已存在，涉及首页CAS标题/前置信息、表2、正文或文献行。页面复查未观察到相应裁切或重叠。另有8条基线已存在的 BibTeX “empty pages”警告；本轮没有为这些条目杜撰页码，也没有将其视为引用缺失。

修改版PDF的SHA-256：`247001310a23413e36e33a021d93f577ff27c0e5657ee21369ca288b4a7c354d`。

机器验证：[scope_validation.json](<D:/multi-agent review_joural/ESWA_Submission_caomodify/tmp/format_review/scope_validation.json>)。基线文件哈希：[baseline_manifest.json](<D:/multi-agent review_joural/ESWA_Submission_caomodify/tmp/format_review/baseline_manifest.json>)。最终构建日志：`D:/multi-agent review_joural/ESWA_Submission_caomodify/tmp/format_review/afterbuild/`。

## PDF逐页检查报告

先渲染全部22页，并逐页查看完整缩略页；随后对第3、4、12、13、14、15、16、22页进行页面尺度复查，重点核查表1、表4、图5及其相邻正文。**以下仅为排版检查，不重新审查科学内容或图像数据。**

| 页 | 主要对象 | 排版检查结果 |
|---|---|---|
| 1 | 标题、摘要、关键词、引言 | CAS前置结构正常；正文双栏，未见裁切或重叠 |
| 2 | 引言、证据映射、背景 | 双栏连续，段落及小标题衔接正常 |
| 3 | 图1、图2、表1首次引用 | 两幅图完整；下方为双栏正文，表1引用位于表前 |
| 4 | **表1**及相邻正文 | 表格跨栏且完整；表后立即恢复双栏，没有强制单栏段落 |
| 5 | 图3及架构正文 | 跨栏图完整，下方双栏连续 |
| 6 | 架构正文 | 双栏连续，页边界正常 |
| 7 | 表2及选择标准 | 跨栏表完整；下方正文双栏，没有异常空白 |
| 8 | 图4及选择标准 | 图完整，图注和正文衔接正常 |
| 9 | 表3及关键技术章节 | 表格完整，标题与正文衔接正常 |
| 10 | 通信、调度与公式 | 双栏及公式位置正常 |
| 11 | 知识、记忆与推理 | 双栏连续，公式未越过栏界 |
| 12 | 图5首次引用及资源章节 | 图5引用位于紧邻的前一页；正文双栏，未出现单独的章节标题空页 |
| 13 | **图5**及表4引用 | 图5宽约163.4 mm，高约96.8 mm，保持原比例；文字、节点和箭头可辨；图注完整，下方继续双栏正文，消除原图5专页的大面积留白 |
| 14 | **表4**及相邻正文 | 8个框架行和6列完整；框架名称与引用换行可读；表格没有越界，下方继续双栏正文，消除原表4专页的大面积留白 |
| 15 | 表5及**表6正文引用** | 表5完整；新增引用正确显示为Table 6，位于表6之前 |
| 16 | 表6及挑战章节 | 表6跨栏且完整；表后双栏正常 |
| 17 | 未来方向 | 双栏连续，小标题未出现单独空页 |
| 18 | 局限、结论、声明 | 双栏连续；未改变正文内容 |
| 19 | 声明及参考文献开始 | 文献开始位置正常，新增访问日期可见 |
| 20 | 参考文献 | 双栏正常，长作者名单与链接换行完整 |
| 21 | 参考文献 | 双栏正常，未见裁切或重叠 |
| 22 | 参考文献结束 | 最后3条文献完整；有正常的文献末页余白，不是图5或表4强制分页产生的空白 |

页面预览：`tmp/format_review/after_pages/page-01.png` 至 `page-22.png`。前后对照 PDF：`tmp/format_review/before.pdf`、`tmp/format_review/after.pdf`。

## 恢复与后续边界

本轮变化保留在工作区，恢复标签固定指向修改前提交。需要恢复正式源文件时，可使用 `git restore --source=codex/eswa-format-baseline-20261010 -- manuscript.tex references.bib`，随后重新编译以更新生成PDF；该恢复命令未在本轮执行。

APA严格合规仍为待完成事项，已按用户选择暂缓。后续如继续定制BibTeX或改用Biber，须重新通过独立样例；本报告没有将当前CAS输出标为近似合规或严格合规。
