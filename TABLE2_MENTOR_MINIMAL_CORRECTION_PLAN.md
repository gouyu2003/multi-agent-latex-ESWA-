# Table 2：导师原版最小必要纠错方案（阶段一）

日期：2026-10-13。状态：**只生成方案；没有修改论文源文件、书目、图稿或 Git。完整 LaTeX 草案仍待批准，含一个明确暂停的单元格。**

## 1. 结论、范围与比较基线

推荐 **方案 A：保留导师八个机制行、六列和原顺序，仅修正必要分类、机制名称、系统归因和引用**。原表并不需要重构成两个展示区才能消除已经发现的科学问题。当前方案 B 的好处是更直观地分离“架构类别”与“实现机制”，但没有发现它解决了方案 A 无法用分类标签及短表注解决的事实问题。

48 个数据单元格的分类：**38 KEEP、4 MINIMAL FIX、5 STRUCTURAL FIX、1 UNCERTAIN**。其中 9 格有足够依据作必要修改；UNCERTAIN 不计入必要纠错。八个 Suitable contexts 格逐字保留；七个机制名逐字保留，另一个只作必要流程名更正；Manager--executor 原名恢复；七个 Limitations 格逐字保留，debate 的 degeneration 单独待确认。38 格是逐字内容统计，忽略源码换行、空白和为修复跨行加入的格式命令，不把表注算入单元格。草案当前保留 38/48 原始内容；如果 UNCERTAIN 最终可恢复原文，可提高到 39/48，不能预先把它算成已核实 KEEP。

原来的三个无条件分块不能原样恢复：CAMEL 的具体基本工作流具有持续指令权；AutoGen、graph networks 和 HITL 没有一个不依赖配置的整体类别；MDAgents 的整体 moderator 控制也不因团队变化而变成 Hybrid。**保留的是三类控制权框架，不是保留错误的三组 multirow 归属。**方案 A 不新增第四类，也不增加长篇 Hybrid 定义行；没有可核实的 Hybrid 代表项时，不凑案例。八个机制行及行序不变。

本轮实际比较：

- 导师原始版本：`f84c78b2720bd5cad8fa32eeb7eaa3a510a8263d`，通过 `git show <该提交>:manuscript.tex` 读取；原 Table 2 从第 546 行开始。
- 当前分支：`codex/mentor-conservative-restore-stage2`；HEAD：`30b7758f0ed7da134b54909d698a791833811f9c`。当前有效 Table 2 从第 569 行开始。
- 比较的是**当前工作区文件**，未用 main 替代导师基线；当前 Table 2 与 HEAD 一致。
- 开始时有 `manuscript.tex` 的一处未暂存 Figure 4 路径替换，以及新版 Figure 4 authority_v2 PDF/PPTX 两个未跟踪文件。全部保留，不 stash、不 checkout、不覆盖、不提交。
- 保护核对以 506 个现有跟踪文件/当前 PDF/新版图稿的内容指纹为基础；Git 暂存区开始为空。正文 SHA256：`25c6c9242cb4e1b5bba1f97cb84810016369f7e83d8392144096a718959e480e`；书目 SHA256：`ef7c289c90c183c5f72f5484ee31b64d675a0f7a8dbfc325803d1bdc1d7b9a59`。
- 只写本报告。完整草案只在代码块中，未写 `manuscript.tex`，没有编译新表或生成其他预览文件。

本轮使用的历史定位材料为 MENTOR_BASELINE_RESTORE_PLAN.md、Q4_Q5_CONSERVATIVE_RESTORE_PROPOSAL.md、MENTOR_BASELINE_RESTORE_STAGE2_REPORT.md、audit_work/manuscript_correction_log.json、audit_work/stage2_manuscript_correction_log.json；均未改写。上轮批准两区方案的历史记录继续保留，本轮提出重新选择方案 A，不追溯篡改既有审批记录。

## 2. 来源核查、版本与判定边界

本轮重读原论文方法或现有原论文 PDF 提取文本，并打开出版方/作者官方来源；历史审计只是定位线索，不作为自动正确的结论。这里核查的是表中系统身份、技术归因和控制关系，**不是对 85 条文献全部元数据重新验收**。架构标签按本文控制权定义作作者综合判断，不能写成原作者自报标签。应用场景、潜在局限也属于综述作者分析，不应改造成原论文已测得的效果。

| 证据 ID / 现有引用键 | 本轮核读来源与具体定位 | 支持的范围及限制 |
|---|---|---|
| S1 / du2024multiagent_debate | [ICML 2024 / PMLR 正式记录](https://proceedings.mlr.press/v235/du24e.html)；本地正式 PDF 的 §2.1–2.2（物理页 3–4）、§5（物理页 9）。 | 同级回答更新；共识不保证，结束时有 majority fallback；主要直接局限为成本与长对话上下文处理。不能把 majority fallback 当持续上级控制，也不能把 degeneration 当已证明的专门结果。 |
| S2 / li2023camel | [NeurIPS 2023 正式 PDF](https://proceedings.neurips.cc/paper_files/paper/2023/file/a3621ee907def47c1b952ade25c67698-Paper-Conference.pdf)，§3.1、Fig. 1，物理页 4–5；另读 arXiv v2 方法作交叉检查。 | 基本 AI User 给指令、规划步骤、判断任务完成，AI Assistant 执行。此具体持续关系支持本文的 Hierarchical 推断；不能从“角色名称不同”直接推断。 |
| S3 / wu2024autogen | [作者原论文 arXiv v2](https://arxiv.org/html/2308.08155v2)，§2.2、§3 的 A5、Appendix A5 / Fig. 12；[COLM 2024 记录](https://openreview.net/forum?id=BAakY1hNKS)与现有官方快照定位。 | 会话控制可编程；A5 的 GroupChatManager 选择说话者并广播。架构依配置，不能固定为 Flat。本轮 OpenReview 页面出现验证页，正式身份沿用已有记录并与作者论文核对；没有声称本轮重新读取 COLM 全文。 |
| S4 / hong2024metagpt | [ICLR 2024 正式记录](https://proceedings.iclr.cc/paper_files/paper/2024/hash/6507b115562bb0a305f1958ccc87355a-Abstract-Conference.html)；[作者方法全文 v7](https://arxiv.org/html/2308.00352v7)，§3.1 “Workflow across Agents”、Appendix B.2 “Project Manager”。 | SOP 固定分工；Project Manager 分解代码文件任务交给 Engineers。支持原 manager--executor 短句作为机制概括，不把整框架缩减为仅一个 manager。正式 PDF 本轮未成功取回，不将 v7 说成已逐字核对过的正式全文。 |
| S5 / zhao2024longagent | [EMNLP 2024 正式来源](https://aclanthology.org/2024.emnlp-main.912/)；本地正式 PDF，§2.1–2.4、Fig. 2，印刷页 16311–16313。 | Leader 组织文档成员提取、冲突解决及最终回答；不是三个系统共用的字面 plan--retrieve--generate 流程。 |
| S6 / zhang2024chain_agents | [NeurIPS 2024 正式来源](https://proceedings.neurips.cc/paper_files/paper/2024/hash/ee71a4b14ec26710b39ee6be113d7750-Abstract-Conference.html)；本地正式 PDF，§3.1–3.2、Algorithm 1、Fig. 1（物理页 2、4）。 | Workers 按上下文块传递 CU，manager 综合最后 CU；不强加一个文献没有共同描述的检索规划阶段。 |
| S7 / jiang2026cocoa | [ACL 2026 正式来源](https://aclanthology.org/2026.acl-long.167/)；本地正式 PDF，§3.2.1–3.2.2、§3.3、Algorithm 1，印刷页 3665–3666。 | CoCoA-zero 的内部/外部知识归纳代理 + 决策代理；CoCoA 用其长轨迹训练单模型。两个名称不能在多代理推理代表项中混用。 |
| S8 / zhuge2024gptswarm | [ICML 2024 / PMLR 正式记录](https://proceedings.mlr.press/v235/zhuge24a.html)；[作者原论文 v1](https://arxiv.org/html/2402.16823v1)，§2.2–2.4、Algorithms 1–3。 | 已核读方法限定 agent/composite DAG，并优化节点提示和跨代理连接。正式 PDF 下载和 OpenReview 本轮分别取回失败/出现验证页；不声称完成正式 PDF 全文复读。DAG 描述限于已核读论文方法，不推断当前库全部配置。 |
| S9 / langgraph2024 | [官方 2024-01-23 技术文章](https://www.langchain.com/blog/langgraph-multi-agent-workflows)，开篇、Multi Agent Collaboration、Agent Supervisor、Hierarchical Agent Teams。 | 支持 cycles、图状态路由、supervisor 配置；这是机制能力，不能直接证明 Hybrid 或 QA 性能。 |
| S10 / kim2024mdagents | [NeurIPS 2024 正式 PDF](https://proceedings.neurips.cc/paper_files/paper/2024/file/90d1fc07f46e31387978b88e7e057a31-Paper-Conference.pdf)，§3.1–3.5（物理页 4–5）、Fig. 1、Fig. 10、Algorithm 1（物理页 30）。本地 43 页正式 PDF 方法亦核读。 | Moderator 选 solo/MDT/ICT 并监督；中等复杂度有固定反馈与最终决定，高复杂度有团队报告后最终决定。按本文规则属于整体层级组织，局部专家会话/团队变化不足以证明整体 Hybrid。算法定位以本轮读到的正式版本为准，不沿用正文方法中旧行号作为全部精确编号。 |
| S11 / langgraph2024interrupt | [官方 2024-12-14 技术文章](https://www.langchain.com/blog/making-it-easier-to-build-human-in-the-loop-agents-with-interrupt)，How we built...、interrupt、Common human-in-the-loop workflows。 | 已有 breakpoints 与 NodeInterrupt；checkpoint 支持 pause/edit/resume，列出 approve/reject。保留旧术语 breakpoints 有直接依据；该来源没有比较 QA 安全效果试验。 |

本轮核读的现有本地原始 PDF（均未写入）：

| 现有相对路径（均在 audit_work/stage2_sources/） | 页数 | SHA256 |
|---|---:|---|
| du2024multiagent_debate__formal_pmlr_pdf.pdf | 31 | 80ecf57b31f248e6ce234412618aa6001d19630a9de0cf18c24cb60ae3a8054d |
| kim2024mdagents__pdf.pdf | 43 | ee5165fd72486bef7039a6810b29d3f9e852c06bb27e9b1048533fa250f53887 |
| jiang2026cocoa__pdf.pdf | 18 | 7872127a86b92d43aa31e828d4606682653f08f72bf184363bc77109c435aff3 |
| zhao2024longagent__pdf.pdf | 15 | f7a3b0bf221c20de654c4bea81fb31f07e17be2fbe20a9154746ebcc26e6aa2c |
| zhang2024chain_agents__pdf.pdf | 30 | 8462522a91815f38062ae6f2ece4d5edfb04e612a5f08e359189c7eebeacf158 |

现有日志中将 Plan--retrieve--generate 改为 Staged evidence-processing、CoCoA 改为 CoCoA-zero 的修正，本轮按 S5–S7 重新核实后保留。历史方案的“两区”和合并 Hierarchical 行属于组织方式选择，不能由来源真实性要求自动推出。

## 3. 八行六列的精确单元格审查

列编号：C1 Architecture；C2 Sub-paradigm；C3 Representative systems；C4 Coordination and control；C5 Suitable contexts；C6 Limitations。

以下导师/当前英文按实际源码提取，只合并换行和连续空白，不改标点、术语、引用命令或引用键。原表 C1 的空白格按所属 multirow **展开其逻辑标签**，因此不是把空白误认为导师未分类。R4/R5 当前均对应同一个合并 Hierarchical 行，其六格全文分别列出；这是两对一映射，不能据此认为原来的两个独立机制不存在。分类以“从导师原版出发是否必须改”为标准，KEEP 也包括必须从当前版本恢复的原词句。

### R1：Multi-agent debate

| 格号 / 列 | 导师原文 | 当前版本 | 判定 | 推荐最小结果与理由 / 影响 |
|---|---|---|---|---|
| R1C1 / C1 | `Flat` | `Flat` | **KEEP** | 逐字保留导师内容。 S1：按本文无持续上级控制标准，Du 的 peer-update/majority fallback 可标 Flat。 仅保留/恢复本格，不连带润色其他格或正文。 |
| R1C2 / C2 | `Multi-agent debate` | `Multi-agent debate` | **KEEP** | 逐字保留导师内容。 S1：原机制名与研究相符。 仅保留/恢复本格，不连带润色其他格或正文。 |
| R1C3 / C3 | `\citet{du2024multiagent_debate}` | `\citet{du2024multiagent_debate}` | **KEEP** | 逐字保留导师内容。 S1：作者与正式 ICML 2024 文献身份匹配，引用键正确。 仅保留/恢复本格，不连带润色其他格或正文。 |
| R1C4 / C4 | `Peer critique and aggregation can add independent answer paths` | `Peer critique and aggregation; no persistent top-down controller` | **KEEP** | 逐字保留导师内容。 S1：初始各自回答后互评可增加答案路径；can 未承诺收益，independent 不解读为统计独立。 仅保留/恢复本格，不连带润色其他格或正文。 |
| R1C5 / C5 | `Tasks needing competing factual or reasoning views` | `Tasks needing competing factual or reasoning views` | **KEEP** | 逐字保留导师内容。 作者场景分析，不是原论文实测适用性或唯一场景结论。 仅保留/恢复本格，不连带润色其他格或正文。 |
| R1C6 / C6 | `Cost, degeneration, and aggregation sensitivity` | `Coordination cost and aggregation sensitivity` | **UNCERTAIN** | 拟用：`Coordination cost and aggregation sensitivity`。 S1：§5 直接报告多轮成本与长上下文处理困难；§2.2 报告共识不保证与 majority fallback。尚不能把它们直接等同于 degeneration，也不能仅凭未出现该词证明导师错。 实际正文暂不动；草案暂占当前文本，是否恢复/局部替换该词需明确确认。 |

### R2：Role-conditioned collaboration

| 格号 / 列 | 导师原文 | 当前版本 | 判定 | 推荐最小结果与理由 / 影响 |
|---|---|---|---|---|
| R2C1 / C1 | `Flat` | `---` | **STRUCTURAL FIX** | 拟用：`Hierarchical$^{a}$`。 S2：原论文基本 AI User--AI Assistant 工作流有持续规划、指令与终止控制。只改具体工作流分类；角色名称不作为判据。 移除原 Flat 三行跨行单元格；增加作用域表注 a。 |
| R2C2 / C2 | `Role-conditioned collaboration` | `Role-conditioned collaboration` | **KEEP** | 逐字保留导师内容。 S2：角色条件化是论文实际机制，不等于架构定义。 仅保留/恢复本格，不连带润色其他格或正文。 |
| R2C3 / C3 | `CAMEL \citep{li2023camel}` | `CAMEL \citep{li2023camel}` | **KEEP** | 逐字保留导师内容。 S2：CAMEL 系统与现有 NeurIPS 2023 引用对应。 仅保留/恢复本格，不连带润色其他格或正文。 |
| R2C4 / C4 | `Personas structure interaction but do not by themselves establish QA gains` | `Personas structure interaction; AI User and AI Assistant have asymmetric instructions` | **KEEP** | 逐字保留导师内容。 S2：原句已明确角色不直接证明 QA 增益，控制事实放在分类作用域注中即可。 仅保留/恢复本格，不连带润色其他格或正文。 |
| R2C5 / C5 | `Exploratory collaboration and prompt-role studies` | `Exploratory collaboration and prompt-role studies` | **KEEP** | 逐字保留导师内容。 作者场景分析；原文无排除 QA 或声称性能之意。 仅保留/恢复本格，不连带润色其他格或正文。 |
| R2C6 / C6 | `Fixed roles or correlated perspectives` | `Role playing alone does not establish flat control or QA gains` | **KEEP** | 逐字保留导师内容。 作者定性风险分析；固定角色/视角相关的可能性不等于论文已证明退化。 仅保留/恢复本格，不连带润色其他格或正文。 |

### R3：Group-chat collaboration

| 格号 / 列 | 导师原文 | 当前版本 | 判定 | 推荐最小结果与理由 / 影响 |
|---|---|---|---|---|
| R3C1 / C1 | `Flat` | `---` | **STRUCTURAL FIX** | 拟用：`---`。 S3：AutoGen 是可配置框架，GroupChatManager 示例有选人和广播控制；不能把框架及所有 group-chat 配置固定标 Flat。 使用表注解释未指定配置，保留原 Group-chat 行及其他五格。 |
| R3C2 / C2 | `Group-chat collaboration` | `Group-chat collaboration` | **KEEP** | 逐字保留导师内容。 S3：框架原生 group-chat 机制确实存在。 仅保留/恢复本格，不连带润色其他格或正文。 |
| R3C3 / C3 | `AutoGen \citep{wu2024autogen}` | `AutoGen \citep{wu2024autogen}` | **KEEP** | 逐字保留导师内容。 S3：AutoGen 名称、对应论文与引用键保留。 仅保留/恢复本格，不连带润色其他格或正文。 |
| R3C4 / C4 | `Developer-defined speaker selection and dialogue patterns` | `Developer-defined conversations and speaker selection` | **KEEP** | 逐字保留导师内容。 S3：developer-defined speaker selection 与 dialogue patterns 直接对应可编程会话。 仅保留/恢复本格，不连带润色其他格或正文。 |
| R3C5 / C5 | `Applications requiring configurable conversations` | `Applications requiring configurable conversations` | **KEEP** | 逐字保留导师内容。 作者场景分析，与可配置会话能力相符。 仅保留/恢复本格，不连带润色其他格或正文。 |
| R3C6 / C6 | `Topology and QA performance depend on configuration` | `Architecture depends on the specific configuration` | **KEEP** | 逐字保留导师内容。 S3：原句已明确 topology/QA 性能取决于配置；不必再改写成 Architecture depends...。 仅保留/恢复本格，不连带润色其他格或正文。 |

### R4：Manager--executor pattern

| 格号 / 列 | 导师原文 | 当前版本 | 判定 | 推荐最小结果与理由 / 影响 |
|---|---|---|---|---|
| R4C1 / C1 | `Hierarchical` | `Hierarchical` | **KEEP** | 逐字保留导师内容。 S4：固定 SOP/task allocation 控制足以符合现有 Hierarchical 定义。 仅保留/恢复本格，不连带润色其他格或正文。 |
| R4C2 / C2 | `Manager--executor pattern` | `Manager--executor; staged evidence-processing pipeline` | **KEEP** | 逐字保留导师内容。 S4：作为项目经理分配给工程师的机制概括成立，不主张只有一个全局 manager。 仅保留/恢复本格，不连带润色其他格或正文。 |
| R4C3 / C3 | `MetaGPT \citep{hong2024metagpt}` | `MetaGPT; LONGAGENT; Chain-of-Agents; CoCoA-zero \citep{hong2024metagpt,zhao2024longagent,zhang2024chain_agents,jiang2026cocoa}` | **KEEP** | 逐字保留导师内容。 S4：MetaGPT 与正式 ICLR 2024 记录对应。 仅保留/恢复本格，不连带润色其他格或正文。 |
| R4C4 / C4 | `Manager assigns staged work to specialised executors` | `Fixed planning, routing or synthesis authority; explicit sequencing over distributed evidence` | **KEEP** | 逐字保留导师内容。 S4：§3.1 task distribution 与 Appendix B 项目经理分配代码文件，支持原短句。 仅保留/恢复本格，不连带润色其他格或正文。 |
| R4C5 / C5 | `Structured engineering workflows` | `Structured engineering workflows; long-document or knowledge-intensive QA` | **KEEP** | 逐字保留导师内容。 S4：软件工程工作流场景正确；不改写为 QA 评测。 仅保留/恢复本格，不连带润色其他格或正文。 |
| R4C6 / C6 | `Planner bottleneck and error propagation` | `Planner bottleneck, error propagation and information loss at synthesis` | **KEEP** | 逐字保留导师内容。 作者定性风险分析；不声称 MetaGPT 实验测得具体瓶颈幅度。 仅保留/恢复本格，不连带润色其他格或正文。 |

### R5：Plan--retrieve--generate pipeline

| 格号 / 列 | 导师原文 | 当前版本 | 判定 | 推荐最小结果与理由 / 影响 |
|---|---|---|---|---|
| R5C1 / C1 | `Hierarchical` | `Hierarchical` | **KEEP** | 逐字保留导师内容。 S5/S6/S7：leader/manager/final decision 的非对等综合权符合现有分类。 仅保留/恢复本格，不连带润色其他格或正文。 |
| R5C2 / C2 | `Plan--retrieve--generate pipeline` | `Manager--executor; staged evidence-processing pipeline` | **MINIMAL FIX** | 拟用：`Staged evidence-processing pipeline`。 S5/S6/S7：三个系统并不共同执行字面上的 plan--retrieve--generate；用原有共有的证据处理与最终综合机制代替错误统一流程名。 只改机制名称；原 C4 已足够，不展开三套算法。 |
| R5C3 / C3 | `LONGAGENT; Chain-of-Agents; CoCoA \citep{zhao2024longagent,zhang2024chain_agents,jiang2026cocoa}` | `MetaGPT; LONGAGENT; Chain-of-Agents; CoCoA-zero \citep{hong2024metagpt,zhao2024longagent,zhang2024chain_agents,jiang2026cocoa}` | **MINIMAL FIX** | 拟用：`LONGAGENT; Chain-of-Agents; CoCoA-zero \citep{zhao2024longagent,zhang2024chain_agents,jiang2026cocoa}`。 S7：此处多智能体推理机制是 CoCoA-zero；CoCoA 是利用其轨迹训练的单模型，不可混作同一实际执行系统。 仅加 -zero；引用键不变。 |
| R5C4 / C4 | `Explicit sequencing and final synthesis over distributed evidence` | `Fixed planning, routing or synthesis authority; explicit sequencing over distributed evidence` | **KEEP** | 逐字保留导师内容。 S5/S6/S7：存在有序处理和最终综合；不解读为所有证据代理串行执行，CoCoA-zero Stage I 可并行。 仅保留/恢复本格，不连带润色其他格或正文。 |
| R5C5 / C5 | `Long-document or knowledge-intensive QA` | `Structured engineering workflows; long-document or knowledge-intensive QA` | **KEEP** | 逐字保留导师内容。 S5/S6/S7：涵盖长文档与知识密集 QA，保留 or。 仅保留/恢复本格，不连带润色其他格或正文。 |
| R5C6 / C6 | `Information loss and coordination cost at synthesis` | `Planner bottleneck, error propagation and information loss at synthesis` | **KEEP** | 逐字保留导师内容。 作者定性风险分析；合并当前两行不是保留此风险所必需。 仅保留/恢复本格，不连带润色其他格或正文。 |

### R6：Graph-structured agent networks

| 格号 / 列 | 导师原文 | 当前版本 | 判定 | 推荐最小结果与理由 / 影响 |
|---|---|---|---|---|
| R6C1 / C1 | `Hybrid` | `---` | **STRUCTURAL FIX** | 拟用：`---`。 S8/S9：图、DAG 优化、循环和条件路由本身不证明控制权配置切换，故取消无条件 Hybrid。 移除原 Hybrid 三行跨行单元格；不添加长篇 Hybrid 定义行。 |
| R6C2 / C2 | `Graph-structured agent networks` | `Graph-structured agent networks` | **KEEP** | 逐字保留导师内容。 S8/S9：graph-structured 是实际机制名称，取消错误 Hybrid 归属即可。 仅保留/恢复本格，不连带润色其他格或正文。 |
| R6C3 / C3 | `GPTSwarm; LangGraph \citep{zhuge2024gptswarm,langgraph2024}` | `GPTSwarm; LangGraph \citep{zhuge2024gptswarm,langgraph2024}` | **KEEP** | 逐字保留导师内容。 S8/S9：两个来源身份正确；保留研究与技术资源并列，证据角色不混为 QA 效果。 仅保留/恢复本格，不连带润色其他格或正文。 |
| R6C4 / C4 | `Graph transitions permit loops, branches, and routing policies` | `GPTSwarm DAG connection optimisation; LangGraph loops and conditional routing` | **MINIMAL FIX** | 拟用：`GPTSwarm DAG connection optimisation; LangGraph transitions permit loops, branches, and routing policies`。 S8/S9：原句把两个系统共同描述为支持 loops；已核读 GPTSwarm 方法限定 DAG，循环/条件路由来自 LangGraph。 只在本格区分系统，保留原 transitions permit loops, branches, and routing policies 主体。 |
| R6C5 / C5 | `Workflows with conditional state transitions` | `Workflows with conditional state transitions` | **KEEP** | 逐字保留导师内容。 S9：工作流条件状态转换场景保留；不强称 GPTSwarm 核心 DAG 实验实现状态机循环。 仅保留/恢复本格，不连带润色其他格或正文。 |
| R6C6 / C6 | `Different evidence roles; difficult debugging and tracing` | `Graph structure or edge optimisation alone does not establish hybrid authority` | **KEEP** | 逐字保留导师内容。 作者定性比较；Different evidence roles 符合 GPTSwarm=S 与 LangGraph=T，调试/追踪困难是设计风险而非实测比较。 仅保留/恢复本格，不连带润色其他格或正文。 |

### R7：Adaptive collaboration-mode switching

| 格号 / 列 | 导师原文 | 当前版本 | 判定 | 推荐最小结果与理由 / 影响 |
|---|---|---|---|---|
| R7C1 / C1 | `Hybrid` | `---` | **STRUCTURAL FIX** | 拟用：`Hierarchical$^{b}$`。 S10：moderator 选 solo/MDT/ICT 路径并监督，正式 Algorithm 1 有固定反馈与最终决策权；团队模式变化不足以成立 Hybrid。 表注 b 保留 moderator 与 solo/MDT/ICT 事实；C4、场景和局限不必重写。 |
| R7C2 / C2 | `Adaptive collaboration-mode switching` | `Adaptive collaboration-mode switching` | **KEEP** | 逐字保留导师内容。 S10：切换协作模式是论文事实；不把 collaboration-mode 偷换成 decision-authority。 仅保留/恢复本格，不连带润色其他格或正文。 |
| R7C3 / C3 | `MDAgents \citep{kim2024mdagents}` | `MDAgents \citep{kim2024mdagents}` | **KEEP** | 逐字保留导师内容。 S10：MDAgents 的正式 NeurIPS 2024 文献身份正确。 仅保留/恢复本格，不连带润色其他格或正文。 |
| R7C4 / C4 | `Changes collaboration in response to case characteristics` | `Moderator routes solo, multidisciplinary-team or integrated-care-team consultation by complexity` | **KEEP** | 逐字保留导师内容。 S10：原句准确而且没有自动宣称控制权切换；moderator/solo/MDT/ICT 在作用域注 b 保留，避免整格重写。 仅保留/恢复本格，不连带润色其他格或正文。 |
| R7C5 / C5 | `Tasks with heterogeneous requirements` | `Tasks with heterogeneous requirements` | **KEEP** | 逐字保留导师内容。 作者场景分析；异质任务需求不作为 Hybrid 充分条件。 仅保留/恢复本格，不连带润色其他格或正文。 |
| R7C6 / C6 | `Routing policy must be evaluated, not assumed beneficial` | `Changing team composition alone does not establish a change in decision authority` | **KEEP** | 逐字保留导师内容。 原句已经要求评估 routing policy，不是假定收益；源论文有评估不使一般要求变错。 仅保留/恢复本格，不连带润色其他格或正文。 |

### R8：Human-in-the-loop design pattern

| 格号 / 列 | 导师原文 | 当前版本 | 判定 | 推荐最小结果与理由 / 影响 |
|---|---|---|---|---|
| R8C1 / C1 | `Hybrid` | `---` | **STRUCTURAL FIX** | 拟用：`---`。 S11：HITL 是干预机制；固定人工审批构成层级控制边界，只有实际权力配置切换才可能符合 Hybrid。 表注限定固定审批，保留原人工审核单元格。 |
| R8C2 / C2 | `Human-in-the-loop design pattern` | `Human-in-the-loop design pattern` | **KEEP** | 逐字保留导师内容。 S11：HITL 是正确的机制名，错误只在其无条件 Hybrid 归属。 仅保留/恢复本格，不连带润色其他格或正文。 |
| R8C3 / C3 | `LangGraph breakpoints \citep{langgraph2024}` | `LangGraph breakpoints \citep{langgraph2024interrupt}` | **MINIMAL FIX** | 拟用：`LangGraph breakpoints \citep{langgraph2024interrupt}`。 S11：2024-12-14 官方来源直接讨论 breakpoints、interrupt、checkpoint、恢复与审批，引用应指向该现有键。 只替换引用键；保留 breakpoints，references.bib 不变。 |
| R8C4 / C4 | `Human review at explicitly defined decision points` | `Human review at defined decision points` | **KEEP** | 逐字保留导师内容。 S11：defined decision points 与官方 pause/review 对应；explicitly 不必删掉。 仅保留/恢复本格，不连带润色其他格或正文。 |
| R8C5 / C5 | `High-risk workflows requiring accountability` | `High-risk workflows requiring accountability` | **KEEP** | 逐字保留导师内容。 作者设计场景；高风险需要审核不意味着 Hybrid，也不声称已验证安全提升。 仅保留/恢复本格，不连带润色其他格或正文。 |
| R8C6 / C6 | `Direct comparative QA evidence remains limited` | `A fixed approver remains hierarchical; comparative QA safety evidence is limited` | **KEEP** | 逐字保留导师内容。 S11 是技术文档，不能充当比较 QA 效果证据；原 limited 比当前增写 safety 范围更贴合原讨论。 仅保留/恢复本格，不连带润色其他格或正文。 |

## 4. 九个必要修改项：证据、最小英文与联动边界

此处只收录确有必要改变导师内容的 9 格；表头、caption、跨行代码和一处关联导语在第 6 节另计，不混入 48 格统计。每项均给出完整原/当前值，避免以“整行更严谨”为理由连带修改。

### R2C1 — STRUCTURAL FIX

1. **导师原文**：`Flat`。
2. **当前内容**：`---`。
3. **具体问题**：S2：原论文基本 AI User--AI Assistant 工作流有持续规划、指令与终止控制。只改具体工作流分类；角色名称不作为判据。
4. **来源定位**：[S2：CAMEL 正式 §3.1 / Fig. 1，物理页 4–5](https://proceedings.neurips.cc/paper_files/paper/2023/file/a3621ee907def47c1b952ade25c67698-Paper-Conference.pdf)；本地/在线实际读取及版本限制见第 2 节。
5. **必须修改的原因**：持续规划、指令和终止权与本文 Flat 的“无持续上级控制”直接冲突，属于分类错误。只是指出 persona 不对称尚不足作 H 证据；本轮使用的是实际控制流程。基本 pair 可标 H，不把所有 CAMEL 扩展配置固定为 H。
6. **最小英文建议**：`Hierarchical$^{a}$`。
7. **影响范围**：移除原 Flat 三行跨行单元格；增加作用域表注 a。 不修改正文其他论证或 Q5 评分。

### R3C1 — STRUCTURAL FIX

1. **导师原文**：`Flat`。
2. **当前内容**：`---`。
3. **具体问题**：S3：AutoGen 是可配置框架，GroupChatManager 示例有选人和广播控制；不能把框架及所有 group-chat 配置固定标 Flat。
4. **来源定位**：[S3：AutoGen §2.2、A5 / Fig. 12](https://arxiv.org/html/2308.08155v2)；本地/在线实际读取及版本限制见第 2 节。
5. **必须修改的原因**：原 Architecture 列的 Flat 是对未指定配置的框架作固定归属；原 Limitations 格已承认配置依赖，说明只改分类就足够。若直接改为无条件 H，同样过度概括；若特指 A5 的 manager 配置可以判 H，但这会不必要地缩窄导师整行。
6. **最小英文建议**：`---`。
7. **影响范围**：使用表注解释未指定配置，保留原 Group-chat 行及其他五格。 不修改正文其他论证或 Q5 评分。

### R5C2 — MINIMAL FIX

1. **导师原文**：`Plan--retrieve--generate pipeline`。
2. **当前内容**：`Manager--executor; staged evidence-processing pipeline`。
3. **具体问题**：S5/S6/S7：三个系统并不共同执行字面上的 plan--retrieve--generate；用原有共有的证据处理与最终综合机制代替错误统一流程名。
4. **来源定位**：[S5：LONGAGENT §2.1–2.4 / Fig. 2](https://aclanthology.org/2024.emnlp-main.912/)、[S6：Chain-of-Agents §3 / Algorithm 1](https://proceedings.neurips.cc/paper_files/paper/2024/hash/ee71a4b14ec26710b39ee6be113d7750-Abstract-Conference.html)、[S7：CoCoA §3.2–3.3 / Algorithm 1](https://aclanthology.org/2026.acl-long.167/)；本地/在线实际读取及版本限制见第 2 节。
5. **必须修改的原因**：原名称声称三项系统共用一个包含规划与检索的具体流水线。LONGAGENT 的 leader 多轮动作、CoA 的块传递和 CoCoA-zero 的两路归纳并不等同于该流程；保留误名会错误归因。修正共有机制名即可，不需要合并两行。
6. **最小英文建议**：`Staged evidence-processing pipeline`。
7. **影响范围**：只改机制名称；原 C4 已足够，不展开三套算法。 不修改正文其他论证或 Q5 评分。

### R5C3 — MINIMAL FIX

1. **导师原文**：`LONGAGENT; Chain-of-Agents; CoCoA \citep{zhao2024longagent,zhang2024chain_agents,jiang2026cocoa}`。
2. **当前内容**：`MetaGPT; LONGAGENT; Chain-of-Agents; CoCoA-zero \citep{hong2024metagpt,zhao2024longagent,zhang2024chain_agents,jiang2026cocoa}`。
3. **具体问题**：S7：此处多智能体推理机制是 CoCoA-zero；CoCoA 是利用其轨迹训练的单模型，不可混作同一实际执行系统。
4. **来源定位**：[S7：正式论文 §3.2–3.3 / Algorithm 1，印刷页 3665–3666](https://aclanthology.org/2026.acl-long.167/)；本地/在线实际读取及版本限制见第 2 节。
5. **必须修改的原因**：一个系统名称错误即可造成多智能体推理架构归因错误，新增 -zero 是最低限度；没有必要更换引用、添加文献或重写同行。
6. **最小英文建议**：`LONGAGENT; Chain-of-Agents; CoCoA-zero \citep{zhao2024longagent,zhang2024chain_agents,jiang2026cocoa}`。
7. **影响范围**：仅加 -zero；引用键不变。 不修改正文其他论证或 Q5 评分。

### R6C1 — STRUCTURAL FIX

1. **导师原文**：`Hybrid`。
2. **当前内容**：`---`。
3. **具体问题**：S8/S9：图、DAG 优化、循环和条件路由本身不证明控制权配置切换，故取消无条件 Hybrid。
4. **来源定位**：[S8：GPTSwarm 方法 §2.2–2.4](https://arxiv.org/html/2402.16823v1)、[S9：LangGraph 官方图/路由/supervisor 示例](https://www.langchain.com/blog/langgraph-multi-agent-workflows)；本地/在线实际读取及版本限制见第 2 节。
5. **必须修改的原因**：条件边、输出节点、图连通性优化都不等价于谁拥有决策权的改变。没有指定且证实的权力配置切换，原 Hybrid 分类缺乏支持；取消默认归属比虚构一个 Hybrid 系统必要且更小。
6. **最小英文建议**：`---`。
7. **影响范围**：移除原 Hybrid 三行跨行单元格；不添加长篇 Hybrid 定义行。 不修改正文其他论证或 Q5 评分。

### R6C4 — MINIMAL FIX

1. **导师原文**：`Graph transitions permit loops, branches, and routing policies`。
2. **当前内容**：`GPTSwarm DAG connection optimisation; LangGraph loops and conditional routing`。
3. **具体问题**：S8/S9：原句把两个系统共同描述为支持 loops；已核读 GPTSwarm 方法限定 DAG，循环/条件路由来自 LangGraph。
4. **来源定位**：[S8：GPTSwarm §2.2 / Algorithm 1，composite graph 的 DAG 限定](https://arxiv.org/html/2402.16823v1)、[S9：LangGraph 开篇 cycles 与 routing 示例](https://www.langchain.com/blog/langgraph-multi-agent-workflows)；本地/在线实际读取及版本限制见第 2 节。
5. **必须修改的原因**：原句未区分两框架，容易将 LangGraph 的循环能力同时归给论文中的 GPTSwarm DAG 执行。必须按系统分别归因；不需要借此改动场景、局限或机制名，也不把 DAG 优化写成决定权切换。
6. **最小英文建议**：`GPTSwarm DAG connection optimisation; LangGraph transitions permit loops, branches, and routing policies`。
7. **影响范围**：只在本格区分系统，保留原 transitions permit loops, branches, and routing policies 主体。 不修改正文其他论证或 Q5 评分。

### R7C1 — STRUCTURAL FIX

1. **导师原文**：`Hybrid`。
2. **当前内容**：`---`。
3. **具体问题**：S10：moderator 选 solo/MDT/ICT 路径并监督，正式 Algorithm 1 有固定反馈与最终决策权；团队模式变化不足以成立 Hybrid。
4. **来源定位**：[S10：MDAgents 正式 §3.1–3.5 / Algorithm 1，物理页 4–5、30](https://proceedings.neurips.cc/paper_files/paper/2024/file/90d1fc07f46e31387978b88e7e057a31-Paper-Conference.pdf)；本地/在线实际读取及版本限制见第 2 节。
5. **必须修改的原因**：原 Hybrid 将组队模式改变等同于架构权力改变。正式算法第 15 行由 Moderator 反馈，第 22 行明确固定 moderator 最终决定，中高复杂度又有固定最终综合。按当前定义标整体 H 是作者推断；不否认局部讨论或团队变化。原 C4 完全正确，不能为补充解释而整格改写。
6. **最小英文建议**：`Hierarchical$^{b}$`。
7. **影响范围**：表注 b 保留 moderator 与 solo/MDT/ICT 事实；C4、场景和局限不必重写。 不修改正文其他论证或 Q5 评分。

### R8C1 — STRUCTURAL FIX

1. **导师原文**：`Hybrid`。
2. **当前内容**：`---`。
3. **具体问题**：S11：HITL 是干预机制；固定人工审批构成层级控制边界，只有实际权力配置切换才可能符合 Hybrid。
4. **来源定位**：[S11：LangGraph 官方 Common human-in-the-loop workflows / Approve or Reject](https://www.langchain.com/blog/making-it-easier-to-build-human-in-the-loop-agents-with-interrupt)；本地/在线实际读取及版本限制见第 2 节。
5. **必须修改的原因**：仅仅有人工暂停审核不能推出整体 Hybrid；固定审批符合当前层级控制判据。未指定具体权力变化的通用 HITL 行不宜一概标 H 或 Hybrid，采用 --- 并以表注解释固定审批，避免把审查能力误作新架构。
6. **最小英文建议**：`---`。
7. **影响范围**：表注限定固定审批，保留原人工审核单元格。 不修改正文其他论证或 Q5 评分。

### R8C3 — MINIMAL FIX

1. **导师原文**：`LangGraph breakpoints \citep{langgraph2024}`。
2. **当前内容**：`LangGraph breakpoints \citep{langgraph2024interrupt}`。
3. **具体问题**：S11：2024-12-14 官方来源直接讨论 breakpoints、interrupt、checkpoint、恢复与审批，引用应指向该现有键。
4. **来源定位**：[S11：2024-12-14 官方文章的 breakpoints / NodeInterrupt / interrupt 段落](https://www.langchain.com/blog/making-it-easier-to-build-human-in-the-loop-agents-with-interrupt)；本地/在线实际读取及版本限制见第 2 节。
5. **必须修改的原因**：技术论断应指向直接支撑人工中断与审核的现有官方来源。现有 langgraph2024interrupt 已在文献池及有效正文中，替换该键不扩充文献或数量；breakpoints 被官方明确提及，无须改成一个全新机制名。
6. **最小英文建议**：`LangGraph breakpoints \citep{langgraph2024interrupt}`。
7. **影响范围**：只替换引用键；保留 breakpoints，references.bib 不变。 不修改正文其他论证或 Q5 评分。

## 5. UNCERTAIN：R1C6 的 degeneration，不默认恢复或删除

- **导师原文**：`Cost, degeneration, and aggregation sensitivity`。
- **当前内容**：`Coordination cost and aggregation sensitivity`。
- **问题**：degeneration 未明确指“答案退化”“对话内容退化”还是“多轮上下文处理能力下降”。[Du 正式论文](https://proceedings.mlr.press/v235/du24e.html) §5 支持成本和长对话处理困难；§2.2 支持共识不保证、提示敏感及最终 majority fallback。它们不能不加说明地等同于某种已实测的 degeneration。
- **为什么不是 MINIMAL FIX**：本轮未在正式全文提取文本中找到 degener- 字根，但“没有这个词”不是“导师分析一定错误”的证明。更不能把此前其他论文的错误归因直接移植到 Du 这行。
- **建议处理**：暂不决定这格的实质修改。完整草案用当前格作**明确标注的占位**；这不是认定当前措辞优于导师措辞，也不是把删除 degeneration 纳入获批必要纠错。
- **需要确认**：是否接受在此次 Table 2 恢复中继续保留当前格，或先确认 degeneration 的具体含义/现有来源后再恢复导师原词。若要将该词最小替换为 `long-context processing limits`，可用 `Cost, long-context processing limits, and aggregation sensitivity`，直接依据 §5；这也是需明确确认的局部替换选项，不在草案中自动执行，不新增文献。
- **其他格与正文影响**：无；不影响 Flat 编码、debate 方法描述、Q5 6/2/2 或 9H/1F/0Hybrid。

## 6. 单元格之外的最小结构、代码与联动修正

| 项目 | 导师原版 / 当前版本 | 方案 A 的处理与必要理由 |
|---|---|---|
| 六列表头 | 原 `Architecture / Sub-paradigm / Representative systems / Coordination and control / Suitable contexts / Limitations`；当前 C2 增加 `/ mechanism`，C3 增加 `/ evidence` | 恢复原六个表头，逐字保留；短注已说明机制/资源的架构标签作用域，不需要扩张列标题。 |
| 行数、顺序 | 原八机制行；当前也是八数据行，但合并原 R4/R5、插入 Hybrid 定义行、移动两项原 Flat 机制到附区 | 恢复导师八个机制行原序；不新增 Hybrid 长行，不重分机制段落，不增删代表系统名单。 |
| Caption | 原 `Comparison of multi-agent collaborative QA architecture classes.`；当前增加 `and related mechanisms` | 保留当前这段最小增词。有 --- 框架/通用机制项，caption 应承认相关机制；不改 Table 2 编号或标签。 |
| Flat 跨行 | 原 `multirow{3}` 覆盖 debate/CAMEL/AutoGen | 必须取消跨三行。后两项不能无条件继承 Flat，仅第一行保留 Flat；这是分类纠错的代码后果。 |
| Hierarchical 跨行 | 原 `multirow{3}` 实际只有两机制行；当前两行合一 | 恢复两行，把原 `3` 改为 `2`，避免跨过分隔线。只改跨行数，不恢复错误排版。 |
| Hybrid 跨行 | 原三机制共同继承 Hybrid；当前另写定义行 | 取消这个错误共用标签；图/HITL 用 ---、MDAgents 用限定 H。三类定义仍由正文承担，不能为保留一个标签虚构实例。 |
| --- | 当前附区使用 --- | 方案 A 保留必要的“未赋配置无关标签”记号，但放回原行序。它不是第四架构，不等于“系统无架构”；三类之一仍须由具体配置判断。 |
| 作用域表注 a / b | 导师无；当前是总注 | 最小增加 CAMEL 基本 AI User 控制、MDAgents moderator-led solo/MDT/ICT 范围；保留原两行 C4，而不是把准确短句扩成新段落。 |
| 总表注 | 导师无；当前强调 specific implementation / actual authority change | 保留这一必要边界并添加 --- 与固定人工审批说明；不宣称全领域不存在 Hybrid，不作 QA 性能验证结论。 |
| 宽度、字号、浮动环境 | 导师 `table*`、`scriptsize`、六个 p 列；当前宽度相同 | 草案保留。原 Hierarchical 跨行数修为 2；暂不增加横向缩放或包。批准后的实际双栏 PDF 若出现问题，只调必要列宽/跨行布局，不能现在宣称排版通过。 |

**关联正文必须另外批准，仅建议改表前导语的一处展示方式短语。**

当前第二句为：

```latex
Architecture labels, suitable contexts, and
limitations are the authors' synthesis; related mechanisms are shown separately
and do not define additional architecture classes.
```

方案 A 没有单独附区，“are shown separately” 会与实际展示冲突；建议只删这一短语，得到：

```latex
Architecture labels, suitable contexts, and
limitations are the authors' synthesis; related mechanisms
do not define additional architecture classes.
```

前一句仍可作为对三类定义及其机制的总体比较导语阅读，**无需扩写**；没有增加完整 Hybrid 代表行也不删除正文 Hybrid 定义。如用户要求必须逐一展示三类的实证代表，应另选 B 的条件设计条目或寻找实际来源，这超出当前不新增文献/结论的范围。本轮既不修改这段导语，也不视批准 Table 2 自动等于批准关联正文。其余段落、控制权定义、Q5、其他表及 Conclusion 无改动需要。

## 7. 方案 A 与方案 B 的比较

| 比较维度 | 方案 A：导师原表最小纠错 | 方案 B：当前两区表 |
|---|---|---|
| 六列 | 原六列标题、顺序、宽度 | 同样六列，但两个标题增加机制/证据字样 |
| 八行意图 | 原八机制逐行保留 | 三类别主区 + 五机制附区；原两个 H 机制合并，另添 Hybrid 条件定义行 |
| 机制顺序 | debate → role-conditioned → group-chat → manager--executor → staged evidence-processing → graph → adaptive → HITL | 两项原 Flat 机制移到附区；H 两行合并 |
| 无条件 Flat 错误 | CAMEL 基本工作流限定 H，AutoGen 用 --- + 配置注 | CAMEL/AutoGen 放附区，统一 --- |
| 图结构与 Hybrid 混淆 | graph 行 ---，本格区分 GPTSwarm 与 LangGraph，表注限定实际权力配置 | graph 放附区，局限格改写为分类警告 |
| MDAgents | 基本机制句原样；H 作用域注保留 moderator/solo/MDT/ICT | 放附区并重写控制/局限两格 |
| HITL | 原审核、场景、局限保留；只改分类及已有引用键，表注说明固定审批 | 放附区并重写局限、删去 explicitly |
| CoCoA-zero | 独立原 R5 中只改名称和流程术语 | 与 MetaGPT 一起塞入合并 H 行 |
| Hybrid 的存在范围 | 保留正文条件定义；不添加未经核实实例，不从十案例推断全领域 | 另设定义行，明确十案例中无 Hybrid |
| 原应用场景 | 八格全部逐字保留 | 合并 H 场景并加入新 Hybrid 场景 |
| 原局限分析 | 七格逐字保留，一格待确认；分类警告置于表注 | 多格用新的分类警告替换原局限 |
| 科学问题能否解决 | 能；通过具体分类/---、系统名、机制归因、引用与短注 | 也能，但并非必须通过两区才能解决 |
| 原文字一致度 | 确定 38/48 格，另 1 格待决定 | 按第 3 节对齐并展开合并格后，20/48 与导师原内容一致；仅是文本距离指标，不是科学评分 |
| 额外代价 | 必须放弃原来错误的三组默认 multirow；分类列在原行序中不连续 | 离导师设计更远；把原机制比较变成类别定义 + 工具/机制附表 |
| 选择依据 | 来源、事实和控制权规则均能满足，且更接近导师原表 | 展示组织更直观，但这种好处不能作为覆盖原文的必要纠错理由 |

**结论：推荐 A。**B 的“类别/机制分区”是可选组织方式，不是科学准确性强制要求。A 中的 --- 和具体工作流限定已避免把框架整体固定归类；表注保留三类判据，原机制标题不自动定义架构。原八行无需重排或合并，表内也不应新增一个长 Hybrid 定义行。

三个原类别标签不能在原三个分块中完全照搬，原因是其中两组存在经核实的分类冲突。这是方案 A 仍需 5 个 STRUCTURAL FIX 的确切边界；它并非声称“导师所有原结构都正确”。如果同时强制“原行序 + 原三组无条件共同标签”，任何方案都会产生来源与控制权定义的冲突。

## 8. 完整 Table 2 LaTeX 草案（仅供批准预览）

这是以 `git show` 取得的导师原表直接作局部替换的草案，保留原八行、六列、顺序、场景和多数局限。R1C6 已在代码注释中标为 UNCERTAIN，暂放当前内容；这格尚未获准作最后取舍。没有新增宏包、表格、文献或长篇 Hybrid 定义行。

```latex
\begin{table*}[pos=t]
  \centering
  \caption{Comparison of multi-agent collaborative QA architecture classes and related mechanisms.}
  \label{tab:9categories}
  \scriptsize
  \begin{tabular}{p{1.4cm} p{2.0cm} p{2.4cm}  p{3.2cm} p{2.3cm} p{2.2cm}}
    \toprule
    \textbf{Architecture} & \textbf{Sub-paradigm} &
    \textbf{Representative systems} &
    \textbf{Coordination and control} &
    \textbf{Suitable contexts} & \textbf{Limitations} \\
    \midrule
    \textbf{Flat} &
    Multi-agent debate & \citet{du2024multiagent_debate} &
    Peer critique and aggregation can add independent answer paths &
    Tasks needing competing factual or reasoning views &
    % UNCERTAIN R1C6: keep the current cell pending a separate decision.
    Coordination cost and aggregation sensitivity \\
    \textbf{Hierarchical}$^{a}$ & Role-conditioned collaboration & CAMEL \citep{li2023camel} &
    Personas structure interaction but do not by themselves establish QA gains &
    Exploratory collaboration and prompt-role studies &
    Fixed roles or correlated perspectives \\
    --- & Group-chat collaboration & AutoGen \citep{wu2024autogen}  &
    Developer-defined speaker selection and dialogue patterns &
    Applications requiring configurable conversations &
    Topology and QA performance depend on configuration \\
    \midrule
    \multirow{2}{*}{\textbf{Hierarchical}} &
    Manager--executor pattern & MetaGPT \citep{hong2024metagpt}  &
    Manager assigns staged work to specialised executors &
    Structured engineering workflows &
    Planner bottleneck and error propagation \\
    & Staged evidence-processing pipeline & LONGAGENT; Chain-of-Agents; CoCoA-zero
    \citep{zhao2024longagent,zhang2024chain_agents,jiang2026cocoa}  &
    Explicit sequencing and final synthesis over distributed evidence &
    Long-document or knowledge-intensive QA &
    Information loss and coordination cost at synthesis \\

    \midrule
    --- &
    Graph-structured agent networks & GPTSwarm; LangGraph
    \citep{zhuge2024gptswarm,langgraph2024}  &
    GPTSwarm DAG connection optimisation; LangGraph transitions permit loops, branches, and routing policies &
    Workflows with conditional state transitions &
    Different evidence roles; difficult debugging and tracing \\
    \textbf{Hierarchical}$^{b}$ & Adaptive collaboration-mode switching & MDAgents \citep{kim2024mdagents}  &
    Changes collaboration in response to case characteristics &
    Tasks with heterogeneous requirements &
    Routing policy must be evaluated, not assumed beneficial \\
    --- & Human-in-the-loop design pattern & LangGraph breakpoints \citep{langgraph2024interrupt} &
    Human review at explicitly defined decision points &
    High-risk workflows requiring accountability &
    Direct comparative QA evidence remains limited \\
    \bottomrule
  \end{tabular}
  \par\smallskip\footnotesize
  \textit{Note}: Architecture labels concern decision authority in a specified
  implementation. $^{a}$CAMEL: persistent AI User instruction and termination
  control in the reported AI User--AI Assistant workflow.
  $^{b}$MDAgents: moderator-led routing among solo, multidisciplinary-team
  (MDT), and integrated-care-team (ICT) pathways.
  --- denotes a mechanism or framework without a configuration-independent
  architecture label, not a fourth class. Flat, Hierarchical, and Hybrid retain
  the definitions in the text; graph structure, team switching, and human review
  alone do not establish Hybrid. A fixed human approver is hierarchical.
\end{table*}
```

## 9. 保留/修改汇总、统计与验收边界

- **逐字保留**：第 3 节标为 KEEP 的 38 格，其中 18 格当前已经改写，应恢复导师原词句；八个场景格、七个局限格、七个机制名和七个未涉及修正的 control 描述等按单元格表逐项执行，不以此概括替代 48 格台账。六个原表头也全部保留。
- **证据支持的单元格修改**：R2C1、R3C1、R6C1、R7C1、R8C1（5 个分类结构）；R5C2、R5C3、R6C4、R8C3（4 个名称/机制/引用最小修改）。不要求把当前各行已扩写的 control/limitations 全保留。
- **暂停项**：R1C6。完整草案中的当前文本只是占位；不能由审批其他九格推定 degeneration 已被证实错误或获准删除。
- **关联说明待单独批准**：仅第 6 节导语中 `are shown separately and` 的展示方式修正。正文其他范围无需改动。
- **三类边界**：CAMEL 基本 pair 与 MDAgents 报告工作流的 H 标签是本综述的具体实施编码，不是作者自报、框架全部配置定性或新增 Q5 案例。--- 不构成第四类。没有核实的 Hybrid 代表项，不强行归类，也不宣称领域没有 Hybrid。

本轮按有效 TeX（排除 `iffalse` 历史区及注释/宏定义）重新静态统计：

| 项目 | 当前值 / 本轮影响 |
|---|---|
| 文献池 / 实际引用 / 核心研究 | **85 / 78 / 13**；不增删 |
| 池内角色 I/S/B/T | **13 / 17 / 46 / 9**；统计仅针对 references.bib 的 85 个键 |
| 实际引用角色 I/S/B/T | **13 / 15 / 42 / 8** |
| Table 2 草案唯一引用键 | 11，全部已存在于 references.bib 和当前有效引用集合 |
| Q5 当前有效正文与符号 | **6 广泛一致 / 2 部分一致 / 2 不一致** |
| Q5 整体来源编码 | **9H / 1F / 0Hybrid**，仅十案例；保持现有作者编码与局限 |
| Triad | 仍为 S，未进入 13 核心；Table 2 不新增该系统 |
| 合并 H 引用命令的恢复 | 恢复两个原独立机制行会把一条引用命令拆回两条；唯一引用 78 不变，不把命令数变化当文献数变化 |

原文件中存在 `iffalse` 保存的旧 Q5 5/3/2 和旧分类，属于不编译的历史正文；本轮没有修改或删除它们，也没有拿这些旧值覆盖有效正文。literature_audit.csv 还保留 X 类历史记录，不能将全部 CSV 行数当作 85 条文献池。本轮角色计数以当前 bib 键集合筛选。

阶段一完成的检查：

1. 精确导师 Git 提取、当前有效 Table 2 比较及 48 格覆盖；原八行完整保留，没有把当前新 Hybrid 定义行冒充导师原机制。
2. LaTeX 草案静态检查：六列、八数据行、原 label、原行序、现有引用键；不把这些静态检查说成编译或 PDF 验收。
3. 写报告前后核对既有 506 个保护文件的内容指纹、HEAD、暂存区；本轮新增项只有本报告，原有未提交图稿与 Figure 4 路径改动仍保留。
4. 无 git add/commit/push/merge/reset/checkout；无论文、书目、图稿或脚本修改。

**尚未执行的验收**：方案 A 没有写入实际源文件，因此未运行 pdfLaTeX → Biber → pdfLaTeX → pdfLaTeX，未在 ESWA 双栏 PDF 中检查新表的完整性、字号、列宽、断行及溢出。待明确批准阶段二和 UNCERTAIN/关联导语处置后，只实施获批边界并完成这些检查。现在的稿件 PDF 不能用来证明尚未落地的草案排版合格。

**既有图稿问题继续独立处理**：本轮未改任何 Figure、PPTX、PDF 或图片脚本；此前 fig_flow.jpg 的箭头/分类语义同步不在 Table 2 范围。用户新版 Figure 4 authority_v2 及现有引入路径完整保留。本轮没有复核所有图内语义，不声称最终图文一致性已验收。

本报告批准所需的具体范围：方案 A 的九个必要单元格修改、38 个 KEEP 的保留/恢复、必要表注/跨行代码；R1C6 和表前导语需明确分别决定。此前全文阶段二权限不自动视为本轮 Table 2 实施权限。
