# ESWA APA 第七版迁移与会议文献收尾当前验收

更新日期：2026-10-12。当前正式稿 `cas-dc + biblatex-apa + Biber`；完整中文逐篇报告见 [九篇最终核查](apa7_audit/conference9_final_review.md)。原2026-10-11迁移报告完整保存在 [历史报告](apa7_audit/history/conference9_baseline_20261012/APA7_MIGRATION_REPORT.md)，其旧哈希、9篇缺证和旧PDF说明均为历史状态。

**当前格式回归与范围保护已通过；全部78篇严格出版元数据验收仍未闭环：8篇会议文献的editor等字段继续PENDING。** 不因空字段推断不存在。

## 当前结果

- 原始85条references.bib、78篇正文来源、136处引用命令和全部引用键完整保留。
- APA 核心14/14、扩展15/15、78条实际输出78/78、85条独立预览85/85通过。
- Generative Agents补出版社明确标注的四位editor，使用eid=2打印Article 2，pagetotal=22仅保存篇幅；内部1–22不冒充连续论文集分页。
- AutoGen保留COLM2024的14人正式作者名单，Awadallah的Hassan修正为A. H.；Self-Consistency／Least-to-Most的Le、Chi及ReAct的Narasimhan中间名同期修正。
- 两篇ACM出版社采用Association for Computing Machinery；只四篇ICLR2023改正式The Eleventh会名。
- 四阶段正式构建成功，22页；前18页像素完全一致，图表/位置和CAS未变。三条既有Overfull一致，Underfull未增加，无最终Biber/biblatex警告。
- 冻结BBL本机重建22页全部文本/像素一致；ESWA服务器后端与包版本兼容仍待平台核实。

当前 PDF SHA-256：`4c57b1d85fd178fa9a5b7c72a1c565be21baf45590e6a657f9da9ea8b136847d`；原库SHA-256：`ef7c289c90c183c5f72f5484ee31b64d675a0f7a8dbfc325803d1bdc1d7b9a59`。所有当前配置哈希见 [final_checks.json](apa7_audit/final_checks.json)，逐篇before/after/证据/未决项见完整中文报告。

## 仍未确认的字段

|key|剩余未核实字段|
|---|---|
|fatemi2024financialqa|editor: primary publication registration has no editor field; absence of editorial credit is not established; supplementation stopped|
|hendrycks2021mmlu|editor: official record supplies no editor; no unsupported editor was added；pages: no confirmed pagination in consulted primary records; left empty|
|khot2023decomposed_prompting|editor: official record supplies no editor; no unsupported editor was added；pages: no confirmed pagination in consulted primary records; left empty|
|wang2023self_consistency|editor: official record supplies no editor; no unsupported editor was added；pages: no confirmed pagination in consulted primary records; left empty|
|wu2024autogen|editor/publisher/pages: COLM/OpenReview official accepted paper supplies no verified values; supplementation stopped；pages: no confirmed pagination in consulted primary records; left empty|
|tang2025llmmedqa|editor: primary publication registration has no editor field; absence of editorial credit is not established; supplementation stopped|
|yao2023react|editor: official record supplies no editor; no unsupported editor was added；pages: no confirmed pagination in consulted primary records; left empty|
|zhou2023least_to_most|editor: official record supplies no editor; no unsupported editor was added；pages: no confirmed pagination in consulted primary records; left empty|

ICLR/OpenReview空页码、AutoGen空publisher和以上空editor均不补造。未引用记录与既有可选限制保持，不改变正式版本、内容论证或引用关系。原迁移文档中的完整测试规则、投稿源文件包与历史差异可追溯，但其旧验证hash不得当作当前hash。

## 审阅状态

核查完成后，用户已授权将本轮改动提交并推送至GitHub的codex/eswa-apa7-migration分支；不合并main。审阅以该分支的核查提交为准。修改仅涉及项目引用适配、受影响审计/报告及为本机验收所需的工具修正。
