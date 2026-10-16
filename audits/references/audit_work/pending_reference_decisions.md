# 第二阶段已处理事项与剩余证据限制

截至：2026-10-10。第二阶段完成状态：True。
书目、版本、案例和必要正文修正已落实；下面未核实的字段仍不标记通过。作者分析/未来建议有明确边界，不因结构通过升级为原论文实证。

## 已关闭事项

| 项目 | 当前处理 |
|---|---|
| Triad | 作者已确认I→S；正文/CSV/Highlights同步，支持性例子保留 |
| 版本选择 | GPT-4、MemGPT、ChatLaw、AgentCoder固定v1；Minsky采用所链接1988版；软件/协议采用记录的版本或日期 |
| 正式PDF差异 | AutoGen14作者、AgentCoder v1五作者、GAIA六作者、DSPy题名/作者、Self-RAG与LegalBench作者表示已核；差异历史保留 |
| 出版字段 | Natural Questions453–466；LLM-MedQA1–8；Memory survey Article155/155:1–155:47；EduPlanner Multiagent；其他可确认正式页码补齐 |
| 重要正文归因 | Financial QA反馈及答案修订；跨reasoner比较、框架类别、知识共享/自省效果边界已修正 |
| 核心纳入 | 13项按五标准重核；QA需是实质主要评估轨道，可同时包含代码/写作等任务 |
| 十案例 | 固定原建议标签，来源流程统一编码；六例一致、四例不一致，不是预测准确率或混合架构验证 |

## 剩余限制与后续范围

逐字段未核实记录45项，当前阻塞项0项。条目数量不是错误文献数量，包含空白可选字段和访问限制。完整当前值、证据、原因与blocking标志见[CSV](pending_reference_decisions.csv)。
部分会议论文的DOI/页码缺少正式证明；URL挑战页/访问失败不代表作品不存在。无正式页码依据的字段保持空白；既有而未证实的可选值标为未核实。Attention等未获正式页码证明的限制保留；SWE-agent已取得正式页面和官方BibTeX，旧页码限制已关闭。
原始检索导出不可获得：正文只将候选和筛选数量称为历史日志，未重建或冒充当年的实际检索。十案例没有独立盲评、前瞻验证或来源编码的混合案例，已在正文声明。
后续格式阶段处理长URL和版面；图片阶段缩小图中文字、同步旧84快照和相关分类标签，核实AI绘图采用来源。此次原图、隐藏章节和用户PDF保持不变。

## 未核实字段按记录列出

| key | 字段及状态 |
|---|---|
| brown2020gpt3 | doi:未核实 |
| minsky1988society | doi:未核实 |
| wooldridge1995intelligent | publisher:未核实 |
| wu2024autogen | pages:未核实, doi:未核实, url:未核实 |
| hong2024metagpt | doi:未核实 |
| du2024multiagent_debate | doi:未核实 |
| lewis2020rag | doi:未核实 |
| yao2023react | doi:未核实 |
| vaswani2017attention | pages:未核实, doi:未核实 |
| qian2024scaling_multiagent | doi:未核实 |
| khattab2024dspy | doi:未核实 |
| zhuge2024gptswarm | doi:未核实 |
| chen2024agentverse | doi:未核实 |
| zhou2023least_to_most | pages:未核实, doi:未核实 |
| khot2023decomposed_prompting | pages:未核实, doi:未核实 |
| packer2023memgpt | publisher:未核实 |
| asai2024selfrag | doi:未核实 |
| wang2023self_consistency | pages:未核实, doi:未核实 |
| jimenez2024swe_bench | pages:未核实, doi:未核实 |
| anthropic2024mcp | doi:未核实 |
| google2025a2a | doi:未核实 |
| langgraph2024 | doi:未核实, note:未核实 |
| crewai2023 | doi:未核实 |
| dify2024 | doi:未核实 |
| zhang2024eduplanner | number:未核实 |
| peffers2007dsrm | publisher:未核实 |
| xagent2023 | doi:未核实 |
| ragflow2024 | doi:未核实 |
| hendrycks2021mmlu | pages:未核实, doi:未核实, url:未核实 |
| trivedi2022musique | number:未核实 |
| liu2024agentbench | doi:未核实 |
| mialon2024gaia | pages:未核实, doi:未核实 |
| zhou2024webarena | doi:未核实 |
| langgraph2024interrupt | doi:未核实 |

## 正文证据边界

下列均按具体语境标记为作者综合、方案建议或混合支持；没有未经处理的partial/unsupported/contradicted/not_verified事实归因。逐来源支持范围见citation_claim_audit.md。

| 引用ID | 判断 | 保留理由 |
|---|---|---|
| C026 | 作者推论，须标明边界 | Retain the 'Inspired by' framing. The edition/year conflict remains a bibliography question; this conceptual analogy is not a validated LLM result. |
| C049 | 作者推论，须标明边界 | Retain the mechanism row and explicit author-synthesis statement; the risk/suitability cells are not claimed as source-validated selection results. |
| C050 | 作者推论，须标明边界 | 具体机制/资源能力获来源支持；控制权类别、适用情境及局限属于明确标注的作者分析。无条件flat/hybrid标签已移除。 |
| C052 | 作者推论，须标明边界 | Retain the supported role mechanism and table-level synthesis qualification. |
| C053 | 多来源支持程度不同 | 保留；任务适配及聚合限制为本文分析。<br>Staged evidence-processing row and CoCoA-zero name corrected. Keep hierarchical placement as review coding, not the source authors' original label. |
| C054 | 作者推论，须标明边界 | 具体机制/资源能力获来源支持；控制权类别、适用情境及局限属于明确标注的作者分析。无条件flat/hybrid标签已移除。 |
| C055 | 作者推论，须标明边界 | 具体机制/资源能力获来源支持；控制权类别、适用情境及局限属于明确标注的作者分析。无条件flat/hybrid标签已移除。 |
| C056 | 作者推论，须标明边界 | 具体机制/资源能力获来源支持；控制权类别、适用情境及局限属于明确标注的作者分析。无条件flat/hybrid标签已移除。 |
| C057 | 作者推论，须标明边界 | Cost-benefit threshold is now explicitly the review's design criterion. Retain the sourced failure-mode motivation without attributing the entire overhead list or threshold to MAST. |
| C058 | 作者推论，须标明边界 | Current wording re-read against retained source evidence. Retain attribution; distinguish borrowing DSRM from empirical validation of this review's proposed artifact. |
| C059 | 作者推论，须标明边界 | 统一控制权编码已实施；源流程获支持，架构标签和匹配为本文回顾性判断。见case_classification_audit.json；不是来源自报标签或性能/安全保证。 |
| C060 | 作者推论，须标明边界 | 统一控制权编码已实施；源流程获支持，架构标签和匹配为本文回顾性判断。见case_classification_audit.json；不是来源自报标签或性能/安全保证。 |
| C061 | 作者推论，须标明边界 | 统一控制权编码已实施；源流程获支持，架构标签和匹配为本文回顾性判断。见case_classification_audit.json；不是来源自报标签或性能/安全保证。 |
| C062 | 作者推论，须标明边界 | 统一控制权编码已实施；源流程获支持，架构标签和匹配为本文回顾性判断。见case_classification_audit.json；不是来源自报标签或性能/安全保证。 |
| C063 | 作者推论，须标明边界 | 统一控制权编码已实施；源流程获支持，架构标签和匹配为本文回顾性判断。见case_classification_audit.json；不是来源自报标签或性能/安全保证。 |
| C064 | 作者推论，须标明边界 | 统一控制权编码已实施；源流程获支持，架构标签和匹配为本文回顾性判断。见case_classification_audit.json；不是来源自报标签或性能/安全保证。 |
| C065 | 作者推论，须标明边界 | 统一控制权编码已实施；源流程获支持，架构标签和匹配为本文回顾性判断。见case_classification_audit.json；不是来源自报标签或性能/安全保证。 |
| C066 | 作者推论，须标明边界 | 统一控制权编码已实施；源流程获支持，架构标签和匹配为本文回顾性判断。见case_classification_audit.json；不是来源自报标签或性能/安全保证。 |
| C067 | 作者推论，须标明边界 | 统一控制权编码已实施；源流程获支持，架构标签和匹配为本文回顾性判断。见case_classification_audit.json；不是来源自报标签或性能/安全保证。 |
| C068 | 作者推论，须标明边界 | 统一控制权编码已实施；源流程获支持，架构标签和匹配为本文回顾性判断。见case_classification_audit.json；不是来源自报标签或性能/安全保证。 |
| C073 | 作者推论，须标明边界 | 按COLM2024正式§§2.1–2.2及§3A5复核；通用选择/部署建议保持作者分析，不归为该文实测效果。<br>具体机制/资源能力获来源支持；控制权类别、适用情境及局限属于明确标注的作者分析。无条件flat/hybrid标签已移除。 |
| C104 | 作者推论，须标明边界 | 具体机制/资源能力获来源支持；控制权类别、适用情境及局限属于明确标注的作者分析。无条件flat/hybrid标签已移除。 |
| C108 | 作者推论，须标明边界 | 具体机制/资源能力获来源支持；控制权类别、适用情境及局限属于明确标注的作者分析。无条件flat/hybrid标签已移除。 |
| C109 | 作者推论，须标明边界 | 具体机制/资源能力获来源支持；控制权类别、适用情境及局限属于明确标注的作者分析。无条件flat/hybrid标签已移除。 |
| C110 | 作者推论，须标明边界 | 具体机制/资源能力获来源支持；控制权类别、适用情境及局限属于明确标注的作者分析。无条件flat/hybrid标签已移除。 |
| C127 | 作者推论，须标明边界 | Prior exhaustive process-analysis implication removed. The claim now distinguishes outcome scores from evidence about individual collaboration mechanisms; this is explicit review inference.<br>Retain the corrected acknowledgment of supporting-fact metrics and the outcome-versus-process qualification. |
| C128 | 作者推论，须标明边界 | Unverified prevalence assertion removed. Named MAST categories are supported; complementary contribution/error-correction measures are now proposed as review synthesis. |
| C129 | 作者推论，须标明边界 | 保留医学背景引用和明确的作者规范性建议。<br>保留背景引用；书目版本链接差异仍pending。 |
| C131 | 作者推论，须标明边界 | 所选版本支持基本可复用组件；自动组装和部署前验证仍是本文提出的方案，不是原资源验证的选择策略。 |
| C135 | 多来源支持程度不同 | Formal version supports memory components. Future QA updates and metadata/validation requirements remain manuscript proposals; formal-locator restriction resolved.<br>保留当前限定表述；来源支持上列具体机制，作者条件分析不作为该文实测结果。 |
| C136 | 前瞻建议，非原论文验证 | Keep 'could' and identify learned team coordination as a research proposal inspired by memory mechanisms; do not imply Park validated those team policies.<br>保留could与future directions边界；不把未来team-policy学习标为该文已验证结果。 |
