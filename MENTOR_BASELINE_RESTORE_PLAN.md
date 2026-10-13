# 导师原版正文保护与保守恢复审查计划

**日期：2026-10-13。阶段一，等待作者确认；未实施任何正文恢复。**

## 审查结论与计数口径

对导师提交与当前工作区的实际正文差异逐项核查后，建议恢复 **25 项 B 类内容**，保留 **64 项 A 类必要事实/来源/格式边界**，另有 **30 项 C 类实质变更等待确认**。

25 项恢复建议中，**6 项可完整恢复差异块，19 项为局部恢复、删除非必要扩写或恢复原句骨架**。A 类“必须保留”指必须保留纠错成果；不意味着新版整个段落、所有新增解释或每个新词都必须照抄。C 类不因新版已被旧审计标为完成而自动获得本次批准。

数字来自实际差异清单，未设恢复比例：Git 的 unified=1 差异显示73个上下文片段；去掉上下文、按连续变化编号为87块（D001–D087）。对混合了事实纠错、语言改写或方法变化的块再拆分，得到119个互不重复的决策项目：64+25+30=119。相邻代码行的技术配对也逐项列出，便于确认不会遗漏；它们不是119个独立科学结论。按行对齐算法划分的空行不同，不能用Git的新增/删除行数当作“修改处数”。

**总体保护结论：**

- 七个有效章节的顺序和章标题没有改变；没有理由重排章节。
- 导师原版已经以决策权与控制定义 Flat、Hierarchical、Hybrid，并明确图结构、角色分工、HITL、运行时路由是正交属性。总定义本身保持原样，无需重写。
- 四个架构选择标准、两阶段流程、单智能体基线、DSRM方法框架和结论正文基本保持；实质变化集中在局部推荐规则、比较表和十案例解释。
- 五项贡献条目只有 corpus 核实措辞改动；缺口导语的改写另列C类。Conclusion的三段正文没有发生英文内容改写；局限小节与末尾声明有差异，不能混为结论重写。
- 14→13不是任意压缩文献数量：仅 hu2024triad 从I移到S。保持原版“至少两个智能体”的条件时，不能把三角色单智能体重新计入核心。
- 原十案例5/3/2与现6/4各自符合所在版本表格符号；两者差别不只是算术，而是来源流程重编码和匹配评分规则改变。必须由作者确认比较方法。

## 版本、工作区及保护范围

| 项目 | 实际审查状态 |
|---|---|
| 仓库remote | [GitHub仓库](https://github.com/gouyu2003/multi-agent-latex-ESWA-) |
| 导师基线 | f84c78b2720bd5cad8fa32eeb7eaa3a510a8263d |
| 当前分支 | codex/eswa-apa7-migration |
| 本地HEAD | f67f29499dd54822305576d2230ce5154f8dedb3 |
| 本次“当前正文” | 工作区 manuscript.tex，包含未提交图1引图句、图注、AI声明 |
| 当前正文原始文件SHA-256 | 3acc39b05e660d1517dada3b59c316b2a1b84a38beffea1b132a9a81bfb02115 |
| 导师正文 git show UTF-8/LF内容SHA-256 | 9e4211f310203d36ce9ffd2cb7e3713be42809e2e6231057c4bf11565a341aac |
| 文件行数 | 导师2201行；工作区2241行 |
| Git正文差异 | 276行新增、236行删除；包含排版、配置、空行及文字替换 |
| 当前未提交跟踪文件 | manuscript.tex；fig_reference_corpus.pdf/.png/.svg；tools/generate_reference_figures.py |
| 当前未跟踪内容 | figure1_audit/；figure1_source_data.csv；output/；tools/verify_figure1_revision.py |

本次只新增本报告。不改分支、索引、正文、书目、配置、图像、历史章节或核查台账；未执行reset、checkout还原、生成图、完整编译、提交、推送或合并。未读取/修改GitHub远程状态，不将本地HEAD表述为已重新验证的远程最新状态。

有效正文根为 [manuscript.tex](<C:/Users/ShenTianyu(CN-TV-T1)/schoolwork/ESWA-multiagent/manuscript.tex>)。唯一有效input是APA配置，不包含独立历史章节。导师1095–1544行与当前1129–1578行的整个 iffalse/fi 禁用块（旧应用章、旧完整架构选择章）内容逐行一致。archive/ch3_en.tex–ch9_en.tex分别与导师提交根目录同名文件按换行规范化后相同；仅归档路径迁移，不恢复或修改它们。

图1及其最新未提交图注、图2和其他图片是保护对象。本报告里的“联动核查图片”仅要求阶段二检查语义/引用一致性，不授权回退图片。图1现阶段记录仍为PENDING_USER_VSCODE，不把独立图形验收当作全文PDF已验收。

## 方法与现有日志的使用边界

实际读取并对照：

- [audit_work/manuscript_correction_log.json](<C:/Users/ShenTianyu(CN-TV-T1)/schoolwork/ESWA-multiagent/audit_work/manuscript_correction_log.json>)（49条历史记录）
- [audit_work/stage2_manuscript_correction_log.json](<C:/Users/ShenTianyu(CN-TV-T1)/schoolwork/ESWA-multiagent/audit_work/stage2_manuscript_correction_log.json>)（38条第二阶段记录）
- [reference_audit_report.md](<C:/Users/ShenTianyu(CN-TV-T1)/schoolwork/ESWA-multiagent/reference_audit_report.md>)
- [audit_work/citation_claim_audit.md](<C:/Users/ShenTianyu(CN-TV-T1)/schoolwork/ESWA-multiagent/audit_work/citation_claim_audit.md>)及其JSON完整语境
- [audit_work/case_classification_audit.md](<C:/Users/ShenTianyu(CN-TV-T1)/schoolwork/ESWA-multiagent/audit_work/case_classification_audit.md>)及JSON逐案例证据
- [audit_work/core_eligibility_audit.md](<C:/Users/ShenTianyu(CN-TV-T1)/schoolwork/ESWA-multiagent/audit_work/core_eligibility_audit.md>)、原论文全文文本快照、search_log.csv、literature_audit.csv与相关版本记录

日志用于定位，**不作为原句有错的唯一证据**。本次另外执行git show、基线→HEAD diff、HEAD→工作区 diff和各阶段提交diff；核对完整邻近段落、表格整行、当前有效引用与必要主来源。首次发生阶段按实际提交追溯；日志中的“baseline_lines”“applied_line”是当时快照行号，不能直接当本次工作区行号。

采用nature-polishing的事实与原意保护、nature-ref-verifier的来源边界；任务轴是英文综述、全稿差异审查、ESWA（非Nature目标）。用户的“最大限度保留导师表达”优先于技能的默认学术润色建议。本次不开展全池85篇元数据重新验证。

历史正式PDF的D:/multi-agent review_joural/10.10ziliao路径在本次环境下没有可重读文件。LLM-MedQA、Financial QA、EduPlanner和AutoGen通过对应公开预印本方法再次核读；原正式版页码/哈希定位保留在历史记录，但**不声称本次重读了这些用户PDF或再次证明正式/预印本全部相同**。不能获取的细节不据题名或摘要强行确认。

复核使用只读模块导入，不执行会重写台账的生成器。当前数值由文件重算，而非引用旧验收哈希。APA7渲染样式、双栏视觉质量及全文编译留在阶段二验收。

## B类优先恢复清单

下列25项是本次可恢复范围；“局部”项不得整段使用导师版本覆盖。原文/现文及提交定位见后面的同号详细条目。涉及同段C类的恢复应只处理本项明确的非实质片段。

| ID | 恢复对象 | 建议范围 |
|---|---|---|
| [D003b](#d003) | using…with…coded as core evidence 替代 based on…including…core empirical studies | 建议 based on 78 cited sources from an 85-record bibliography pool, including 13 core empirical studies；不改变统计。 |
| [D004](#d004) | extraordinary / ushering…new era → strong…relevant to QA | 恢复导师原句；引用键不变。若作者希望全稿弱化修辞，另行统一决定。 |
| [D005b](#d005) | combining perspectives…benefit requires task-level evaluation 的新增尾句 | 删除这一新增尾句；不删除后文原有任务评估限制。 |
| [D010c](#d010) | 新核查段的逐流程展开 | 保留核查日期、统计及有待核字段的最短交代，将其余既有过程说明留在现有记录；不删除记录。 |
| [D011](#d011) | Core included studies…had to satisfy → core eligibility screen…used | 只恢复引导句，不连带恢复Q2所涉及的第4条。 |
| [D013c](#d013) | 原句 The 14 role-I studies provide the empirical basis…及原段顺序被删除 | 恢复 The 13 role-I studies provide the empirical basis for the architecture taxonomy and subsequent evidence synthesis; other claims…；保留必要新统计、Triad边界及当前图1说明。 |
| [D018b](#d018) | 原版 capability extension→task decomposition 的论证被全句替换 | 恢复原句的分解/职责分工论述为本文分析；把已有Park社交模拟说明留作该引用的适用限定，不新增观点或键。 |
| [D019](#d019) | can improve…may expose…coordination quality 等段落 | 保留原can/may、来源组及原失败限制；若限定on evaluated tasks，只在该短语处处理，不全段润色。 |
| [D024a](#d024) | provides another example through an empirical study…→provides an empirical example… | 保留现有引用键；不改变书目池或78篇唯一引用统计。 |
| [D025](#d025) | adjust…control patterns as tasks evolve→can adjust…interaction patterns | 不回退D026的moderator真实机制。 |
| [D026c](#d026) | 原 State management/performance要求尾句的替换 | 恢复原 yet introduce extra requirements for state management and performance evaluation 的尾句；机制主体按A修正。 |
| [D027b](#d027) | defined breakpoints→checkpointed state…interrupt扩写 | 恢复导师For example…defined breakpoints for human review…句式，使用现有langgraph2024interrupt键。 |
| [D039b](#d039) | LangGraph breakpoints→LangGraph interrupts | 可恢复LangGraph breakpoints并保留langgraph2024interrupt引用键；不回退书目。 |
| [D040b](#d040) | 新增失败动机与重述成本标准的两句扩写 | 恢复A collaborative design is justified only when…offset those costs；标明as a criterion of this review，引用仍支持失败动机，避免再绑定门槛。 |
| [D049b](#d049) | 删除high-risk、educational/legal、auditability/human accountability及原尾句 | 恢复原场景、论证顺序和These examples illustrate…尾句；hybrid/hierarchical短语等待Q4。 |
| [D050b](#d050) | 原互操作障碍→标准化努力的过渡被缩成Industry initiatives | 恢复原With the rapid development…与To address…，保留A2A机制修正与证据边界。 |
| [D052b](#d052) | most suitable→suitable 的段首替换 | 恢复After decomposition…most suitable agents一句，保留之后的已核机制。 |
| [D053b](#d053) | 新增graph/vector/document枚举及provenance/access checks | 用原图-向量库论证结构做最小弱化；删除新实现枚举和访问检查扩写。 |
| [D055b](#d055) | A representative access mechanism is…等原句骨架被重排 | 尽量复用原Long-term memory…A representative access mechanism…A retrieval agent…，将typically改can、agent加illustrative限定；不恢复A类错误。 |
| [D057](#d057) | greatly unlocked reasoning potential→任务列表效果 | 恢复导师定性句，不添加普遍正确性或新定量结论。 |
| [D060b](#d060) | correctness/evidence免责声明的额外尾句 | 保留原一短句结构并用A的最小弱化替换。 |
| [D075c](#d075) | Computational graph connections / Automatic graph-structure search / Intra-node state→更细的三单元表述 | 可恢复原三单元文字；不得恢复Hybrid全框架标签或Parallel inference optimization应用定位。保留zhuge2024gptswarm键。 |
| [D078](#d078) | 新增 Table summarizes…primary evaluation roles 两行 | tab:benchmark_resources定义和表内容保留。 |
| [D080b](#d080) | 新增N(N−1)推导句及扩写 | 恢复原potential…quadratically；只在成本效果处保留条件限制。不改原论文实验结果。 |
| [D084a](#d084) | verification exercise rather than independent confirmation→retrospective diagnostic comparison… | 保持原limited…rather than independent confirmation of general validity；不删原局限。 |

**完整恢复的6块：** D004、D011、D019、D025、D057、D078。其余19项是同块中的局部恢复。D078的“恢复”指删掉新增指路句；不删除表格。D004、D057按用户的保守恢复标准属于定性修辞，不能把“更克制”自动等同“事实必须纠正”。它们不允许扩展为普遍准确、安全或定量收益结论。

## C类待作者确认的五组决定

### Q1：研究缺口与贡献定位（D007）

事实底线：已有综述确实讨论协作结构、通信、编排甚至QA；不能写成这些主题完全无人综述。导师原句是QA专属多维整合“remains limited”，比“完全不存在”弱，不能被本次来源自动否定。

- **选项1：尽量恢复导师定位。** 恢复Although…与QA整合缺口的叙述顺序，仅修必要的前作范围限定；保留五项原贡献条目，不引入新的首创性声明。
- **选项2：保留当前builds on叙述。** 接受删去显式缺口定位，把贡献解释为基于既有综述的QA任务治理与选择权衡综合。

### Q2：核心纳入第4条是“主要任务”还是“可并列的主要评估轨道”（D012、D013b）

**14→13的Triad纠错已归A，不是这里待选的数字。** 在导师原版的至少两个智能体条件下，Triad必须仍为S。当前13项名单和统计不得因恢复措辞而自动变更。

- **选项1：承认现有13项的QA轨道可以与其他主要任务并列。** 将现句视为对导师primary task的明确解释，保留13与现有核心名单；QA不能只是偶然演示。
- **选项2：恢复primary evaluated task原词。** 作者明确它同样容许并列主任务，保持现13；或明确要收窄为QA占主导时另行重筛。后一种是额外方法决定，需逐项重新判定，不能预设新数量。

Qian的MMLU、Liang的反直觉算术、Chain-of-Agents的QA与其他长文本任务，是这个解释边界的具体例子。CoCoA只纳入CoCoA-zero多代理证据，不能拿蒸馏单模型充多代理收益。

### Q3：历史检索动作是否作为作者方法陈述保留（D009b、D010a）

search_log.csv确实记录108条候选、2026-08-02及查询组合，但没有完整原始导出可重建每次检索结果。**“无法重建”不等于“作者没有做”；“日志有记录”也不等于全字段核实完成。**

- **选项1：作者确认历史步骤确实实施。** 尽量恢复导师方法叙述和查询组合/数据库顺序，标明是作者记录的检索；删去全面metadata verification承诺，保留当前核查限制。
- **选项2：仅保留可追溯日志层级。** 保留current historical working records/log records措辞，不宣称本次独立复现原检索。

108候选、四条未确认记录只是历史记录口径；不把它们当当前85池或78引用的筛选数学流程。图1继续保护当前数据图，不重新加入历史PRISMA支路。

### Q4：三类架构、交叉机制表与选择规则的呈现（16项）

总定义保持原样：Flat无持续top-down；Hierarchical有固定规划/路由/审批/综合或有序不对称控制；Hybrid改变决策权配置。不能仅以graph、投票、多个角色或HITL宣称hybrid。来源具体机制保留；宏观编码与表格呈现由作者裁定。

- **选项1：以导师叙述结构为主。** 保留Flat/Hierarchical/Hybrid小节和原论证顺序；对CAMEL、AutoGen、图工具、MDAgents只作最小实例范围限定，区分机制和具体控制模式。原三类比较的呈现可以保留，但不能恢复“整个框架固定flat/hybrid”的错误暗示；未有证据的hybrid实现不能自动补造。
- **选项2：接受当前机制与控制模式并列表。** 保留Role-paired、Configurable、Cross-cutting等行，明确它们不是新架构类别；保留当前实际authority-change判据与条件审批规则。当前表头仍写Architecture，确认此方案后需最小澄清该列含机制名称，避免误读为新的五类分类体系。

选择时应一并决定D028、D041、D049a的推荐规则，不能表里按固定controller编码、正文却把同一固定审批自动说成hybrid。图表文件不回退，图中既有控制模式文字仅待语义核查。

### Q5：十案例比较继续三档还是采用精确二档（9项）

| 案例 | 导师建议→来源标签 / 匹配 | 当前建议→作者源编码 / 匹配 | 来源机制事实与本次证据边界 |
|---|---|---|---|
| MedAgents | F→Hybrid / 部分 | F→H / 不一致 | 专家分析、报告、投票修订、最后决策；正式原文已核读 |
| LLM-MedQA | F→Hybrid / 部分 | F→H / 不一致 | 六阶段与最终决策；当前重新核读的是v1预印本 |
| LegalGraphRAG | Hybrid→Hybrid / 广泛一致 | Hybrid→H / 不一致 | Researcher→Auditor→Adjudicator；正式原文已核读 |
| Triad | H→H / 广泛一致 | H→H / 一致 | 单代理多角色、KBQA；只作为S工作流支持例 |
| LONGAGENT | H→H / 广泛一致 | H→H / 一致 | leader选择动作并最终综合；原文快照已核读 |
| ChatDev | H→H / 广泛一致 | H→H / 一致 | 有序ChatChain instructor/assistant；原文快照已核读 |
| AgentCoder | H→H / 广泛一致 | H→H / 一致 | 两个LLM角色+脚本executor；v1快照已核读 |
| Du debate | F→F / 部分 | F→F / 一致 | 对等更新、末轮多数；正式ICML原文已核读 |
| EduPlanner | F→H / 不一致 | F→H / 不一致 | evaluator评分、optimizer/analyst反馈；本次核读v1预印本 |
| Financial QA | H→Hybrid / 不一致 | H→H / 一致 | experts与critics反馈、专家修订；多轮辩论为未来工作，v1已核读 |

原三档符号计算为5广泛一致、3部分、2不同；当前二档为6精确一致、4不同。现源编码9H/1F/0Hybrid是当前统一控制权规则的作者分析结果，**不是这十篇原作者都自报这些标签**。风险/复杂度档案也仍是本文判断，不是临床或部署安全实测。

- **选项1：保留现二档。** 保留6/4与9H/1F/0Hybrid，明确retrospective、作者编码、混合核心与支持例、非独立验证；不能声称6/10预测准确率或hybrid已得到验证。
- **选项2：保留导师三档解释方法。** 保留广泛/部分/不同及边界、多标签的原论证意图；接受已核真实流程纠错后，由作者明确“部分”的判据并重新逐例匹配，再复算统计。**不预设重得5/3/2，不恢复已经纠正的源机制或错误数字。**
- **选项3：保留定性案例诊断，取消匹配总数的结果性主张。** 仍可保留十案例与来源描述，但应明确这是作者设计分析。此选项改变比较呈现，须明确批准，不能由本次审查擅自执行。

D042、D043、D045a/b/c、D046b、D047b、D048a、D084b必须随同一方案同步。原版已经排除性能评估、因果利益和外部有效性，相关保护句可尽量原样保留。当前新加的“未盲评/未预注册”是历史方法记录的限制，不能伪造独立验证。

## 统计、核心研究与术语保护

| 对象 | 导师文件实数 | 当前工作区实数 | 结论 |
|---|---:|---:|---|
| references.bib记录 | 84 | 85 | 唯一新增langgraph2024interrupt，旧84键没有删除 |
| 有效唯一引用 | 77 | 78 | 导师“84 verified sources”混淆池与正文引用，不能恢复 |
| 有效引用命令 | 136 | 136 | 当前只读有效扫描；不按archive或禁用块计数 |
| 引用键出现次数 | 179 | 180 | 新官方来源进入多键框架表等；唯一数与出现数不同 |
| 核心I标签（池内） | 14 | 13 | 唯一移出hu2024triad；没有另一项替代移入 |
| 当前池内I/S/B/T | — | 13/17/46/9 | 合计85 |
| 当前有效引用I/S/B/T | — | 13/15/42/8 | 合计78 |
| 当前池内未引用 | — | 7 | 保留池，不为凑数补引 |

导师引用数量通过去除注释与禁用块的只读提取交叉计算；当前数量通过仓库active_tex有效包含扫描复算。literature_audit.csv另有历史X条目，**不能把整CSV的112行角色计数当85池计数**；必须以实际bib键集合过滤。

当前七个未引用键：brynjolfsson2023generative_ai_work、guha2023legalbench、jimenez2024swe_bench、li2024genmentor、singhal2023medpalm、xagent2023、yang2024swe_agent。无缺失有效引用键。恢复计划不删除这些池条目，也不把未引用等同虚假文献。

| 术语/口径 | 本次保护决定 |
|---|---|
| Flat / Hierarchical / Hybrid | 保留导师总定义；实现归类与比较表具体编码等Q4/Q5 |
| CoCoA / CoCoA-zero | 多智能体证据对象明确CoCoA-zero；原键jiang2026cocoa不重命名 |
| Triad（三角色） | 一代理三角色，S；键hu2024triad虽与现作者姓不同也保留 |
| MAD / Du debate | Du与Liang区分；不把Liang的judge方法移给Du |
| breakpoint / interrupt | 两种LangGraph暂停机制均存在；保留当前补证键，允许恢复原breakpoint表达 |
| bibliography pool / cited sources / core studies | 分别85 / 78 / 13；不得混用 |
| source-based coding / reported architecture | 归类为本文作者编码，不能写成全由原作者报告 |
| 思维节点 / agents | ToT/GoT的thought状态不能自动等同多个独立agent |

## 按章节逐处核查：完整原文、现文与决策

每块保留真实连续差异的全部文字；未变化的上下文不重复引用。块内a/b/c表示可分别决定的局部，分类、动作与影响均单列。纯删除以当前插入边界定位，纯增加以导师插入边界定位。阶段记录是整个块的轨迹；不同子项的先后变化在理由或后面的来源中进一步说明。

### 摘要与文献工作流

<a id="d001"></a>

#### D001 Biber 编辑器指令

导师位置：f84c78b:manuscript.tex 2行。当前位置：[manuscript.tex](<C:/Users/ShenTianyu(CN-TV-T1)/schoolwork/ESWA-multiagent/manuscript.tex:2>) 2行。

追溯：6679e5a（2026-10-11，APA7/Biber 迁移）。f67f294本身没有新增manuscript.tex文字差异。

**导师原版：**

```tex
% !BIB program = bibtex
```

**当前版本：**

```tex
% !BIB program = biber
```

**D001 · A类 · 推荐：保留**

- 决策对象：编译指令。
- 理由：当前工作流使用 Biber；回退会与 biblatex 不一致。
- 引用、表格、图注、统计或章节结论影响：保留 APA7/Biber 编译入口。
- 依据：[E01](#e01)。

<a id="d002"></a>

#### D002 APA7 导言区

导师位置：f84c78b:manuscript.tex 9–11行。当前位置：[manuscript.tex](<C:/Users/ShenTianyu(CN-TV-T1)/schoolwork/ESWA-multiagent/manuscript.tex:9>) 9–11行。

追溯：6679e5a（2026-10-11，APA7/Biber 迁移）。f67f294本身没有新增manuscript.tex文字差异。

**导师原版：**

```tex
% ESWA author-year citations use the abbreviated author list in running text
% (e.g., Ouyang et al., 2022), including the first occurrence.
\usepackage[authoryear]{natbib}
```

**当前版本：**

```tex
% ESWA APA seventh edition; preserve existing natbib citation commands.
\input{eswa-apa-config.tex}
\addbibresource{references.bib}
```

**D002 · A类 · 推荐：保留**

- 决策对象：natbib→APA7 配置入口。
- 理由：必要格式迁移；现有 citep/citet 由兼容配置承载。
- 引用、表格、图注、统计或章节结论影响：不恢复 natbib 包或旧 BibTeX 配置。
- 依据：[E01](#e01)。

<a id="d003"></a>

#### D003 摘要语料统计与核心研究措辞

导师位置：f84c78b:manuscript.tex 64–65行。当前位置：[manuscript.tex](<C:/Users/ShenTianyu(CN-TV-T1)/schoolwork/ESWA-multiagent/manuscript.tex:64>) 64–66行。

追溯：首次 4ff0569；98732a2 继续修改（含 Triad 边界/角色决定、来源重编码或表格机制标签）。f67f294本身没有新增manuscript.tex文字差异。

**导师原版：**

```tex
review of multi-agent collaborative QA based on 84 verified sources,
including 14 core empirical studies published through July 2026. We first
```

**当前版本：**

```tex
review of multi-agent collaborative QA using 78 cited sources from an
85-record bibliography pool, with 13 studies coded as core
evidence published through July 2026. We first
```

**D003a · A类 · 推荐：保留**

- 决策对象：84/14→85池、78引用、13核心。
- 理由：当前文件复算和 Triad 原文支持这些数字；不能为了原版一致而回退。
- 引用、表格、图注、统计或章节结论影响：摘要与图1、纳入标准同步；Q2未裁定前保持13。
- 依据：[E01](#e01)、[E02](#e02)、[E03](#e03)。

**D003b · B类 · 推荐：恢复（局部）**

- 决策对象：using…with…coded as core evidence 替代 based on…including…core empirical studies。
- 理由：新增编码表达不纠正独立事实；保留新数字即可恢复原句骨架。
- 引用、表格、图注、统计或章节结论影响：建议 based on 78 cited sources from an 85-record bibliography pool, including 13 core empirical studies；不改变统计。
- 依据：[E01](#e01)、[E03](#e03)。

### 第1章 Introduction与文献筛选说明

<a id="d004"></a>

#### D004 LLM 能力的引言修辞

导师位置：f84c78b:manuscript.tex 134–135行。当前位置：[manuscript.tex](<C:/Users/ShenTianyu(CN-TV-T1)/schoolwork/ESWA-multiagent/manuscript.tex:135>) 135–136行。

追溯：4ff0569（2026-10-08，第一阶段参考文献/归因核查）。f67f294本身没有新增manuscript.tex文字差异。

**导师原版：**

```tex
extraordinary natural-language understanding and generation capabilities,
ushering QA systems into a new, agent-centric era.
```

**当前版本：**

```tex
strong natural-language understanding and generation capabilities relevant
to QA.
```

**D004 · B类 · 推荐：恢复**

- 决策对象：extraordinary / ushering…new era → strong…relevant to QA。
- 理由：原句是定性引言修辞，未报告定量效果或无条件安全结论；GPT-3/GPT-4 所引能力未被本次证据否定。新句更克制并不足以构成必须保留理由。
- 引用、表格、图注、统计或章节结论影响：恢复导师原句；引用键不变。若作者希望全稿弱化修辞，另行统一决定。
- 依据：[E04](#e04)。

<a id="d005"></a>

#### D005 单模型领域覆盖断言

导师位置：f84c78b:manuscript.tex 142–144行。当前位置：[manuscript.tex](<C:/Users/ShenTianyu(CN-TV-T1)/schoolwork/ESWA-multiagent/manuscript.tex:143>) 143–145行。

追溯：98732a2（2026-10-10，第二阶段证据与控制流重编码）。f67f294本身没有新增manuscript.tex文字差异。

**导师原版：**

```tex
\emph{Third}, a monolithic model cannot simultaneously possess expert-level
knowledge across all domains, often failing on queries that require
cross-disciplinary collaboration.
```

**当前版本：**

```tex
\emph{Third}, a single model may lack sufficient domain coverage for a query
that requires several areas of expertise; combining perspectives is one
possible response whose benefit requires task-level evaluation.
```

**D005a · A类 · 推荐：最小修正**

- 决策对象：cannot…all domains。
- 理由：绝对不可能性和经常失败没有对应实测证明，应改为可能不足。
- 引用、表格、图注、统计或章节结论影响：保留 Third 与跨领域逻辑；仅将绝对句收窄，不恢复 cannot。
- 依据：[E04](#e04)。

**D005b · B类 · 推荐：恢复（删除扩写）**

- 决策对象：combining perspectives…benefit requires task-level evaluation 的新增尾句。
- 理由：这一原则已在原版后文和选择方法中充分存在；此处扩写不是修正绝对句所必需。
- 引用、表格、图注、统计或章节结论影响：删除这一新增尾句；不删除后文原有任务评估限制。
- 依据：[E04](#e04)。

<a id="d006"></a>

#### D006 爆发式增长句的删除

导师位置：f84c78b:manuscript.tex 150行。当前位置：[manuscript.tex](<C:/Users/ShenTianyu(CN-TV-T1)/schoolwork/ESWA-multiagent/manuscript.tex:151>) 151行。

追溯：98732a2（2026-10-10，第二阶段证据与控制流重编码）。f67f294本身没有新增manuscript.tex文字差异。

**导师原版：**

```tex
Between 2023 and 2026 this field has witnessed explosive growth. For example,
```

**当前版本：**

```tex
For example,
```

**D006 · A类 · 推荐：保留删除**

- 决策对象：explosive growth 的未经量化增长断言。
- 理由：没有按2023–2026同口径计算的增长数据；论文数量或下载量不能自动证明该具体断言。
- 引用、表格、图注、统计或章节结论影响：不把历史图1筛选/增长数字重新带回引言。
- 依据：[E01](#e01)、[E04](#e04)。

<a id="d007"></a>

#### D007 研究缺口与贡献定位

导师位置：f84c78b:manuscript.tex 158–164行。当前位置：[manuscript.tex](<C:/Users/ShenTianyu(CN-TV-T1)/schoolwork/ESWA-multiagent/manuscript.tex:159>) 159–164行。

追溯：4ff0569（2026-10-08，第一阶段参考文献/归因核查）。f67f294本身没有新增manuscript.tex文字差异。

**导师原版：**

```tex
Although several surveys on LLM-based agents exist
\citep{guo2024llm_multiagent_survey,tran2025multiagent_survey,wang2024survey_autonomous_agents},
they focus primarily on general agent architectures or foundational
capabilities. A systematic account of collaboration topologies, enabling
mechanisms, task and governance requirements, and architecture-selection
trade-offs for QA remains limited. This survey addresses that gap through five
related contributions:
```

**当前版本：**

```tex
Existing surveys cover general LLM-agent construction, communication,
and orchestration
\citep{guo2024llm_multiagent_survey,tran2025multiagent_survey,wang2024survey_autonomous_agents}.
This survey builds on that coverage by connecting collaboration topologies and enabling mechanisms
to QA-specific task and governance requirements and architecture-selection
trade-offs through five related contributions:
```

**D007 · C类 · 推荐：等待确认 Q1**

- 决策对象：QA系统性综述缺口段落被改为 builds on…。
- 理由：Tran 已覆盖通信、组织结构、编排及 QA，但这并不等于已经覆盖原句所称 QA任务治理与选择权衡的整合；整个删除缺口陈述改变论文定位，不能据台账直接裁定原句错误。
- 引用、表格、图注、统计或章节结论影响：五项贡献条目本身基本原样；需确认缺口定位，不增加新的创新主张。
- 依据：[E05](#e05)。

<a id="d008"></a>

#### D008 verified corpus→source-checked corpus

导师位置：f84c78b:manuscript.tex 168行。当前位置：[manuscript.tex](<C:/Users/ShenTianyu(CN-TV-T1)/schoolwork/ESWA-multiagent/manuscript.tex:168>) 168行。

追溯：4ff0569（2026-10-08，第一阶段参考文献/归因核查）。f67f294本身没有新增manuscript.tex文字差异。

**导师原版：**

```tex
        QA, based on a verified corpus with explicit roles for core empirical
```

**当前版本：**

```tex
        QA, based on a source-checked corpus with explicit roles for core empirical
```

**D008 · A类 · 推荐：保留**

- 决策对象：全池已核实的暗示。
- 理由：仍有不可核字段/来源冲突；source-checked 区分已检查与全部已证明。
- 引用、表格、图注、统计或章节结论影响：保留现有引用键；不改变书目池或78篇唯一引用统计。
- 依据：[E01](#e01)。

<a id="d009"></a>

#### D009 历史语料核查叙述

导师位置：f84c78b:manuscript.tex 209行。当前位置：[manuscript.tex](<C:/Users/ShenTianyu(CN-TV-T1)/schoolwork/ESWA-multiagent/manuscript.tex:209>) 209–215行。

追溯：4ff0569（2026-10-08，第一阶段参考文献/归因核查）。f67f294本身没有新增manuscript.tex文字差异。

**导师原版：**

```tex
The initial candidate set contained 108 unique entries from the authors' working bibliography. On 2 August 2026, each entry was verified by title, first author, publication year, venue, and persistent identifier against Crossref, OpenAlex, arXiv, and, where available, official publisher proceedings or project documentation. This process uncovered four records with corrupted or mismatched metadata for which an authoritative source could not be confirmed. The process also identified duplicate, uncited, and out-of-scope records; these were preserved in the audit trail but excluded from the active bibliography.
```

**当前版本：**

```tex
The historical audit log records an initial candidate set of 108 unique
entries from the authors' working bibliography and checks dated 2 August
2026 using Crossref, OpenAlex, arXiv, and official sources. It records four
corrupted or mismatched records for which an authoritative source was not
confirmed, together with duplicate, uncited, and out-of-scope records. These
historical records are retained in the audit trail; the log alone is not
independent evidence that every publication field was verified.
```

**D009a · A类 · 推荐：最小修正**

- 决策对象：each entry was verified 的全字段核实断言。
- 理由：日志与当前字段台账不能证明每条作者/年份/出版字段/标识均已核实；不恢复全面验证承诺。
- 引用、表格、图注、统计或章节结论影响：保留108/四条作为历史记录数，与85/78分开。
- 依据：[E01](#e01)。

**D009b · C类 · 推荐：等待确认 Q3**

- 决策对象：由作者执行过程改为 historical audit log records。
- 理由：仓库 search_log.csv 确实记录日期与动作；缺少原始检索导出不证明作者没有实施这些步骤。是否保留作者方法陈述需作者确认。
- 引用、表格、图注、统计或章节结论影响：影响方法可追溯性；只确认历史动作，不重新确认未核字段。
- 依据：[E01](#e01)。

<a id="d010"></a>

#### D010 定向检索与10月核查段落

导师位置：f84c78b:manuscript.tex 211–217行。当前位置：[manuscript.tex](<C:/Users/ShenTianyu(CN-TV-T1)/schoolwork/ESWA-multiagent/manuscript.tex:217>) 217–230行。

追溯：首次 4ff0569；98732a2 继续修改（含 Triad 边界/角色决定、来源重编码或表格机制标签）。f67f294本身没有新增manuscript.tex文字差异。

**导师原版：**

```tex
A targeted update search was then conducted using combinations of \textit{multi-agent},
\textit{LLM}, \textit{question answering}, \textit{reasoning},
\textit{long-context}, and \textit{retrieval-augmented generation} across the ACL
Anthology, OpenReview, arXiv, and publisher proceedings. Three directly
relevant studies absent from the initial collection were added after full
metadata verification: ReConcile \citep{chen2024reconcile}, Chain-of-Agents
\citep{zhang2024chain_agents}, and CoCoA \citep{jiang2026cocoa}. 
```

**当前版本：**

```tex
The historical working records list ReConcile
\citep{chen2024reconcile}, Chain-of-Agents \citep{zhang2024chain_agents}, and
CoCoA \citep{jiang2026cocoa} as additions. The source audit confirms their
identities and publication dates; it does not reconstruct the original update
queries, retrieval results, or search dates.

Source-level checks on 8 and 10 October 2026 compared the bibliography with
publisher records, official proceedings, versioned arXiv papers, and dated or
versioned project documentation. The current pool contains 85 records, of
which 78 are cited in the active manuscript. The audit separates source
existence, field accuracy, version selection, and claim support. Confirmed
corrections were applied; unavailable optional fields and source discrepancies
are recorded without blanket verification claims. One dated official LangGraph
article supports the interrupt and checkpoint mechanisms discussed below.
```

**D010a · C类 · 推荐：等待确认 Q3**

- 决策对象：删除查询组合、数据库与实际检索动作陈述。
- 理由：实际原版和日志给出了查询词与来源；新增检查不能重建历史动作，但也不能据此认定其虚假。
- 引用、表格、图注、统计或章节结论影响：保留 ReConcile/CoA/CoCoA 的三个引用键和添加身份；不借此补新文献。
- 依据：[E01](#e01)、[E03](#e03)。

**D010b · A类 · 推荐：最小修正**

- 决策对象：after full metadata verification 与当前85/78、LangGraph补证。
- 理由：全元数据验证承诺过强；新补证来源及统计真实。
- 引用、表格、图注、统计或章节结论影响：保留现有引用键；不改变书目池或78篇唯一引用统计。
- 依据：[E01](#e01)、[E12](#e12)。

**D010c · B类 · 推荐：恢复（缩短新增段）**

- 决策对象：新核查段的逐流程展开。
- 理由：existence/field/version/claim 的完整说明及每个不可获字段的叙述已有审计文件；不是正文事实纠错必需的全部篇幅。
- 引用、表格、图注、统计或章节结论影响：保留核查日期、统计及有待核字段的最短交代，将其余既有过程说明留在现有记录；不删除记录。
- 依据：[E01](#e01)。

<a id="d011"></a>

#### D011 纳入标准引导句

导师位置：f84c78b:manuscript.tex 225行。当前位置：[manuscript.tex](<C:/Users/ShenTianyu(CN-TV-T1)/schoolwork/ESWA-multiagent/manuscript.tex:238>) 238行。

追溯：4ff0569（2026-10-08，第一阶段参考文献/归因核查）。f67f294本身没有新增manuscript.tex文字差异。

**导师原版：**

```tex
Core included studies (role \textbf{I}) had to satisfy five criteria:
```

**当前版本：**

```tex
The core eligibility screen (role \textbf{I}) used five criteria:
```

**D011 · B类 · 推荐：恢复**

- 决策对象：Core included studies…had to satisfy → core eligibility screen…used。
- 理由：同样列出五项条件，纯表达替换。
- 引用、表格、图注、统计或章节结论影响：只恢复引导句，不连带恢复Q2所涉及的第4条。
- 依据：[E03](#e03)。

<a id="d012"></a>

#### D012 QA主要任务→主要评估轨道

导师位置：f84c78b:manuscript.tex 229行。当前位置：[manuscript.tex](<C:/Users/ShenTianyu(CN-TV-T1)/schoolwork/ESWA-multiagent/manuscript.tex:242>) 242行。

追溯：98732a2（2026-10-10，第二阶段证据与控制流重编码）。f67f294本身没有新增manuscript.tex文字差异。

**导师原版：**

```tex
(4) QA, retrieval-augmented answering, conversational QA, or question-driven domain decision support as the primary evaluated task; and
```

**当前版本：**

```tex
(4) QA, retrieval-augmented answering, conversational QA, or question-driven domain decision support as a substantive primary evaluation track; and
```

**D012 · C类 · 推荐：等待确认 Q2**

- 决策对象：第4条纳入标准的解释范围。
- 理由：Qian、Liang、CoA 有实质 QA 评估及其他主要任务；是否原标准允许并列主任务是作者的方法解释，不由来源替作者决定。
- 引用、表格、图注、统计或章节结论影响：当前13保持；若改成更窄规则，必须另行重筛全部13项，不能直接填新数量。
- 依据：[E03](#e03)。

<a id="d013"></a>

#### D013 角色统计与核心证据说明

导师位置：f84c78b:manuscript.tex 233–235行。当前位置：[manuscript.tex](<C:/Users/ShenTianyu(CN-TV-T1)/schoolwork/ESWA-multiagent/manuscript.tex:246>) 246–259行。

追溯：首次 4ff0569；98732a2 继续修改（含 Triad 边界/角色决定、来源重编码或表格机制标签）；末尾引图句另含 2026-10-13 未提交更新。f67f294本身没有新增manuscript.tex文字差异。

**导师原版：**

```tex
Foundational models, datasets, single-agent methods, and review articles were coded as background (role \textbf{B}); official protocols and software documentation were coded as technical sources (role \textbf{T}). Sources excluded from the active bibliography remain coded as \textbf{X} in the audit file. The resulting active bibliography contains 84 verified sources:
14~I, 16~S, 46~B, and 8~T. Fig.~\ref{fig:reference_corpus} summarizes the verification and evidence-role allocation. The 14 role-I studies provide the empirical basis for the architecture taxonomy and subsequent evidence synthesis;
other claims are supported by sources appropriate to their scope.
```

**当前版本：**

```tex
Foundational models, datasets, single-agent methods, and review articles were coded as background (role \textbf{B}); official protocols and software documentation were coded as technical sources (role \textbf{T}).
Historically excluded sources remain coded as \textbf{X} in the audit file.
The current bibliography pool contains 85 records: 13~I, 17~S, 46~B, and
9~T. The effective manuscript cites 78 of these records: 13~I, 15~S, 42~B,
and 8~T; seven uncited records remain in the pool. The 13 role-I studies
were reassessed against these five criteria and retain their labels.
QA need not be their sole task, but incidental QA demonstrations are
insufficient for inclusion. Triad uses a single LLM-based agent
in three roles and is coded as a supporting study (role~S), because it does
not meet the core criterion of at least two agents. It remains a related
boundary example in Table~\ref{tab:validation}, outside the 13 core studies.
Other claims use sources appropriate to their scope.
Fig.~\ref{fig:reference_corpus} shows the current bibliography pool,
its cited and uncited records, and the evidence-role composition of cited sources.
```

**D013a · A类 · 推荐：保留**

- 决策对象：85/78、I13/S17/B46/T9与Triad边界。
- 理由：直接从现有文件复算，Triad 为一个LLM-based agent的三角色系统，不满足原版至少两个智能体的条件。
- 引用、表格、图注、统计或章节结论影响：保留 pool/cited 两种角色统计及Triad为S；不删Triad引用。
- 依据：[E01](#e01)、[E02](#e02)。

**D013b · C类 · 推荐：等待确认 Q2**

- 决策对象：QA need not be their sole task 的纳入解释。
- 理由：与第4条的范围调整相同，应与Q2联动，不能独立裁定。
- 引用、表格、图注、统计或章节结论影响：不自动改动13项现有核心标签。
- 依据：[E03](#e03)。

**D013c · B类 · 推荐：恢复（局部）**

- 决策对象：原句 The 14 role-I studies provide the empirical basis…及原段顺序被删除。
- 理由：将14改为13后，核心论文作为分类与证据综合的经验来源仍合理；该句没有宣称分类已独立验证。
- 引用、表格、图注、统计或章节结论影响：恢复 The 13 role-I studies provide the empirical basis for the architecture taxonomy and subsequent evidence synthesis; other claims…；保留必要新统计、Triad边界及当前图1说明。
- 依据：[E02](#e02)、[E03](#e03)。

<a id="d014"></a>

#### D014 图1当前数据图注

导师位置：f84c78b:manuscript.tex 240行。当前位置：[manuscript.tex](<C:/Users/ShenTianyu(CN-TV-T1)/schoolwork/ESWA-multiagent/manuscript.tex:264>) 264行。

追溯：首次 4ff0569 改为历史图注；2026-10-13 未提交图1更新改为当前池/引用图注。f67f294本身没有新增manuscript.tex文字差异。

**导师原版：**

```tex
  \caption{Reference-corpus verification and evidence-role allocation. The counts describe the reconstructed working bibliography and targeted update, rather than an exhaustive PRISMA screening flow across the entire database.}
```

**当前版本：**

```tex
  \caption{Current bibliography pool and evidence-role composition of cited sources. The pool contains 85 records: 78 cited sources and seven uncited records. Under the authors' evidence-role classification, cited sources comprise 13 core studies (I), 15 supporting studies (S), 42 background sources (B), and eight technical resources (T); segment widths in the horizontal bar are proportional to these counts. AI tools assisted with plotting code and layout; counts are computed from the bibliography, active citations, and evidence-role table.}
```

**D014 · A类 · 推荐：保留（保护未提交改动）**

- 决策对象：历史语料流程图注→当前文献池图注。
- 理由：当前未提交图1已移除历史筛选流程，只显示当前池与引用角色；回退旧图注会与现图不符。
- 引用、表格、图注、统计或章节结论影响：85=78+7、78=13+15+42+8；保护当前图1三种格式；本次不评价全文嵌图分页。
- 依据：[E01](#e01)、[E22](#e22)。

### 第2章 Background

<a id="d015"></a>

#### D015 Transformer/BERT历史机制

导师位置：f84c78b:manuscript.tex 290–291行。当前位置：[manuscript.tex](<C:/Users/ShenTianyu(CN-TV-T1)/schoolwork/ESWA-multiagent/manuscript.tex:314>) 314–316行。

追溯：4ff0569（2026-10-08，第一阶段参考文献/归因核查）。f67f294本身没有新增manuscript.tex文字差异。

**导师原版：**

```tex
which introduced self-attention; BERT \citep{devlin2019bert}, which established
the pre-train--fine-tune paradigm; and GPT-3 \citep{brown2020gpt3} and GPT-4
```

**当前版本：**

```tex
which introduced an attention-only sequence-transduction architecture; BERT
\citep{devlin2019bert}, which advanced bidirectional pretraining and
task-specific fine-tuning; and GPT-3 \citep{brown2020gpt3} and GPT-4
```

**D015 · A类 · 推荐：保留必要纠正**

- 决策对象：introduced self-attention / established pre-train--fine-tune。
- 理由：Transformer 提出 attention-only 序列架构，不是整个self-attention概念的最早发明；BERT不是整个预训练微调范式的起点。
- 引用、表格、图注、统计或章节结论影响：保留现有引用键；不改变书目池或78篇唯一引用统计。
- 依据：[E06](#e06)。

<a id="d016"></a>

#### D016 LLaMA/ChatGLM开放性与效果措辞

导师位置：f84c78b:manuscript.tex 293–294行。当前位置：[manuscript.tex](<C:/Users/ShenTianyu(CN-TV-T1)/schoolwork/ESWA-multiagent/manuscript.tex:318>) 318–320行。

追溯：4ff0569（2026-10-08，第一阶段参考文献/归因核查）。f67f294本身没有新增manuscript.tex文字差异。

**导师原版：**

```tex
capabilities. Open-source models such as LLaMA \citep{touvron2023llama} and
ChatGLM \citep{glm2024chatglm} further democratized agent development, while
```

**当前版本：**

```tex
capabilities. Open-weight releases such as LLaMA \citep{touvron2023llama} and
ChatGLM \citep{glm2024chatglm} provide additional options for local
experimentation, while
```

**D016 · A类 · 推荐：最小修正**

- 决策对象：open-source 全称与 democratized 效果。
- 理由：LLaMA初代是研究用途权重开放；ChatGLM报告含开放与闭源系列，不能笼统覆盖。社会效果 democratized 未被所引实验直接测量。
- 引用、表格、图注、统计或章节结论影响：恢复原句句序与模型顺序，必要处用 open-weight，保留局部使用支持的含义；不恢复全系列开源或已测社会效果。
- 依据：[E06](#e06)。

<a id="d017"></a>

#### D017 移除背景表之前强制单栏

导师位置：f84c78b:manuscript.tex 299–301行。当前位置：[manuscript.tex](<C:/Users/ShenTianyu(CN-TV-T1)/schoolwork/ESWA-multiagent/manuscript.tex:325>) 插入/删除边界325行。

追溯：1233a8b（2026-10-10，CAS 双栏格式阶段）。f67f294本身没有新增manuscript.tex文字差异。

**导师原版：**

```tex

\clearpage
\onecolumn
```

**当前版本：**

```tex
[原文已删除：此处无当前文字]
```

**D017 · A类 · 推荐：保留删除**

- 决策对象：clearpage/onecolumn。
- 理由：双栏排版修复；原命令会使后续有效章节继续单栏。
- 引用、表格、图注、统计或章节结论影响：保留 table*；不改变模型能力表数据。
- 依据：[E01](#e01)。

<a id="d018"></a>

#### D018 Park社交模拟与任务分工归因

导师位置：f84c78b:manuscript.tex 346–348行。当前位置：[manuscript.tex](<C:/Users/ShenTianyu(CN-TV-T1)/schoolwork/ESWA-multiagent/manuscript.tex:369>) 369–371行。

追溯：4ff0569（2026-10-08，第一阶段参考文献/归因核查）。f67f294本身没有新增manuscript.tex文字差异。

**导师原版：**

```tex
\citep{minsky1988society}, a multi-agent architecture decomposes a complex
task and assigns subtasks to agents with distinct responsibilities
\citep{park2023generative_agents}. A single ``generalist'' workflow may combine
```

**当前版本：**

```tex
\citep{minsky1988society}, multi-agent architectures can combine agents with
individual memory, reflection, and planning, as illustrated in social
simulations \citep{park2023generative_agents}. A single ``generalist'' workflow may combine
```

**D018a · A类 · 推荐：保留来源边界**

- 决策对象：把任务分解分配直接归于Generative Agents。
- 理由：Park 实测社交代理记忆、反思、规划，不能作为专业QA任务调度的直接证据。
- 引用、表格、图注、统计或章节结论影响：保留Park键，避免错误紧邻归因。
- 依据：[E07](#e07)。

**D018b · B类 · 推荐：恢复（原论证骨架）**

- 决策对象：原版 capability extension→task decomposition 的论证被全句替换。
- 理由：任务分解和职责分工本身是原稿观点，后文MetaGPT等已有支持；不必因一个引用范围问题撤去原来的过渡逻辑。
- 引用、表格、图注、统计或章节结论影响：恢复原句的分解/职责分工论述为本文分析；把已有Park社交模拟说明留作该引用的适用限定，不新增观点或键。
- 依据：[E07](#e07)、[E15](#e15)。

<a id="d019"></a>

#### D019 多智能体可靠性整段收窄

导师位置：f84c78b:manuscript.tex 370–377行。当前位置：[manuscript.tex](<C:/Users/ShenTianyu(CN-TV-T1)/schoolwork/ESWA-multiagent/manuscript.tex:393>) 393–400行。

追溯：98732a2（2026-10-10，第二阶段证据与控制流重编码）。f67f294本身没有新增manuscript.tex文字差异。

**导师原版：**

```tex
Multi-agent collaboration can also improve reasoning reliability by creating
separate candidate, review, and verification paths. Debate, cross-checking,
and reconciliation may expose errors that self-refinement within one workflow
overlooks \citep{du2024multiagent_debate,chen2024reconcile,
xiong2023inter_consistency}. However, additional agents do not guarantee
correctness: weak aggregation, poor interaction design, or correlated errors
can preserve or amplify an incorrect answer. Coordination quality is thus a
central design variable, not an incidental implementation detail.
```

**当前版本：**

```tex
Multi-agent collaboration provides mechanisms for comparing candidate answers
and review paths. Debate and reconciliation compare answers from different
reasoners \citep{du2024multiagent_debate,chen2024reconcile,
xiong2023inter_consistency}; their benefits depend on the task and the agents
involved. Additional agents do not guarantee correctness or establish universal
superiority over self-refinement: weak aggregation, poor interaction design,
or correlated errors can preserve an incorrect answer. Coordination quality
therefore requires evaluation.
```

**D019 · B类 · 推荐：恢复**

- 决策对象：can improve…may expose…coordination quality 等段落。
- 理由：原版已经用can/may，且紧接does not guarantee correctness及失败条件。Du正式论文Table1–2实际对照single-agent reflection并报告任务内改进；原句不是普遍优越性断言。台账把它当作普遍对照不足以支持整段改写。
- 引用、表格、图注、统计或章节结论影响：保留原can/may、来源组及原失败限制；若限定on evaluated tasks，只在该短语处处理，不全段润色。
- 依据：[E08](#e08)。

### 第3章 Architectures与架构选择方法

<a id="d020"></a>

#### D020 图拓扑图注交叉引用

导师位置：f84c78b:manuscript.tex 411行。当前位置：[manuscript.tex](<C:/Users/ShenTianyu(CN-TV-T1)/schoolwork/ESWA-multiagent/manuscript.tex:434>) 434行。

追溯：4ff0569（2026-10-08，第一阶段参考文献/归因核查）。f67f294本身没有新增manuscript.tex文字差异。

**导师原版：**

```tex
		control, as specified in the text and Table~\ref{tab:core_taxonomy_mapping}.}
```

**当前版本：**

```tex
		control, as specified in the text and Table~\ref{tab:9categories}.}
```

**D020 · A类 · 推荐：保留**

- 决策对象：tab:core_taxonomy_mapping→tab:9categories。
- 理由：旧标签在有效正文未定义；当前标签存在。
- 引用、表格、图注、统计或章节结论影响：修复图注引用；图片文件不变。
- 依据：[E01](#e01)。

<a id="d021"></a>

#### D021 Xiong来源机制术语

导师位置：f84c78b:manuscript.tex 426行。当前位置：[manuscript.tex](<C:/Users/ShenTianyu(CN-TV-T1)/schoolwork/ESWA-multiagent/manuscript.tex:449>) 449行。

追溯：4ff0569（2026-10-08，第一阶段参考文献/归因核查）。f67f294本身没有新增manuscript.tex文字差异。

**导师原版：**

```tex
In the multi-agent debate paradigm, several LLM agents generate candidate answers and critique one another across one or more rounds. Representative studies illustrate both the potential and the limits of this design. For example, \citet{du2024multiagent_debate} report improved factuality and reasoning performance on the tasks they evaluate, whereas divergent prompting can mitigate convergence toward similar reasoning paths \citep{liang2024divergent_debate}. ReConcile provides another example by integrating heterogeneous models with confidence-weighted consensus \citep{chen2024reconcile}; answer consistency and degeneration nevertheless remain notable failure modes \citep{xiong2023inter_consistency}. Accordingly, adding more agents or debate rounds does not reliably boost QA performance; instead, the interaction rules, diversity of evidence, and aggregation procedure determine whether disagreement yields correction, inconsistency, or unnecessary computational cost.
```

**当前版本：**

```tex
In the multi-agent debate paradigm, several LLM agents generate candidate answers and critique one another across one or more rounds. Representative studies illustrate both the potential and the limits of this design. For example, \citet{du2024multiagent_debate} report improved factuality and reasoning performance on the tasks they evaluate, whereas divergent prompting can mitigate convergence toward similar reasoning paths \citep{liang2024divergent_debate}. ReConcile provides another example by integrating heterogeneous models with confidence-weighted consensus \citep{chen2024reconcile}; inter-model inconsistency and capability imbalance nevertheless remain important considerations \citep{xiong2023inter_consistency}. Accordingly, adding more agents or debate rounds does not reliably boost QA performance; instead, the interaction rules, diversity of evidence, and aggregation procedure determine whether disagreement yields correction, inconsistency, or unnecessary computational cost.
```

**D021 · A类 · 推荐：保留最小词组修正**

- 决策对象：answer consistency and degeneration→inter-model inconsistency and capability imbalance。
- 理由：已读正文研究inter-inconsistency、能力不匹配和弱模型支配等；旧短语错误概括来源重点。
- 引用、表格、图注、统计或章节结论影响：保留现有引用键；不改变书目池或78篇唯一引用统计。
- 依据：[E09](#e09)。

<a id="d022"></a>

#### D022 CAMEL角色不对称与flat判断

导师位置：f84c78b:manuscript.tex 431行。当前位置：[manuscript.tex](<C:/Users/ShenTianyu(CN-TV-T1)/schoolwork/ESWA-multiagent/manuscript.tex:454>) 454行。

追溯：98732a2（2026-10-10，第二阶段证据与控制流重编码）。f67f294本身没有新增manuscript.tex文字差异。

**导师原版：**

```tex
Role-conditioned collaboration assigns different prompts or task views to participating agents. For example, CAMEL \citep{li2023camel} employs an "AI User" and an "AI Assistant" paired with inception prompting to maintain role-conditioned interaction. This constitutes an adjacent multi-agent framework and does not serve as direct evidence that role playing improves QA accuracy. 
```

**当前版本：**

```tex
Role-conditioned collaboration assigns different prompts or task views to participating agents. For example, CAMEL \citep{li2023camel} employs an "AI User" and an "AI Assistant" paired with inception prompting to maintain role-conditioned interaction. This role pair has asymmetric instructions; role play alone does not establish a flat decision-authority structure. This constitutes an adjacent multi-agent framework and does not serve as direct evidence that role playing improves QA accuracy. 
```

**D022 · C类 · 推荐：等待确认 Q4**

- 决策对象：新增 role pair has asymmetric instructions…not establish flat。
- 理由：AI User发指令、Assistant求解是原论文事实；但如何将其映射到本文flat或独立机制栏仍属本文编码。保留真实角色描述，表呈现方式待确认。
- 引用、表格、图注、统计或章节结论影响：与D031/D032/D068统一；不因章标题而声称框架所有配置flat。
- 依据：[E15](#e15)。

<a id="d023"></a>

#### D023 CoCoA-zero与蒸馏单模型

导师位置：f84c78b:manuscript.tex 464–465行。当前位置：[manuscript.tex](<C:/Users/ShenTianyu(CN-TV-T1)/schoolwork/ESWA-multiagent/manuscript.tex:487>) 487–489行。

追溯：4ff0569（2026-10-08，第一阶段参考文献/归因核查）。f67f294本身没有新增manuscript.tex文字差异。

**导师原版：**

```tex
CoCoA \citep{jiang2026cocoa}, which coordinates parametric and retrieved
knowledge for QA. These role-I systems differ in their communication
```

**当前版本：**

```tex
CoCoA-zero \citep{jiang2026cocoa}, which coordinates parametric and retrieved
knowledge using three agents at inference time. CoCoA subsequently distils
that collaboration into a single model. These role-I systems differ in their communication
```

**D023 · A类 · 推荐：保留**

- 决策对象：CoCoA→CoCoA-zero。
- 理由：原论文§3.2为三代理推理管线；§3.3为蒸馏到单模型的CoCoA。必须区分被纳入的多智能体证据对象。
- 引用、表格、图注、统计或章节结论影响：保留jiang2026cocoa键，表中代表系统名同步CoCoA-zero。
- 依据：[E10](#e10)。

<a id="d024"></a>

#### D024 图网络优化与hybrid判据

导师位置：f84c78b:manuscript.tex 483行。当前位置：[manuscript.tex](<C:/Users/ShenTianyu(CN-TV-T1)/schoolwork/ESWA-multiagent/manuscript.tex:507>) 507行。

追溯：98732a2（2026-10-10，第二阶段证据与控制流重编码）。f67f294本身没有新增manuscript.tex文字差异。

**导师原版：**

```tex
Graph-structured networks represent agents and transitions as an executable graph. For example, LangGraph \citep{langgraph2024} serves as an official technical framework for defining state transitions, loops, and conditional branches; it provides technical evidence (role T), rather than constituting a QA evaluation. GPTSwarm \citep{zhuge2024gptswarm} provides another example through an empirical study of agent methodologies that optimises prompts and inter-agent graph connections. 
```

**当前版本：**

```tex
Graph-structured networks represent agents and transitions as an executable graph. For example, LangGraph \citep{langgraph2024} serves as an official technical framework for defining state transitions, loops, and conditional branches; it provides technical evidence (role T), rather than constituting a QA evaluation. GPTSwarm \citep{zhuge2024gptswarm} provides an empirical example of optimising prompts and inter-agent graph connections. A graph representation, edge optimisation, or conditional routing alone does not establish hybrid decision authority; the implementation must actually change who controls decisions.
```

**D024a · B类 · 推荐：恢复（首句局部）**

- 决策对象：provides another example through an empirical study…→provides an empirical example…。
- 理由：这部分只压缩同一机制描述，无事实变化。
- 引用、表格、图注、统计或章节结论影响：保留现有引用键；不改变书目池或78篇唯一引用统计。
- 依据：[E11](#e11)。

**D024b · C类 · 推荐：等待确认 Q4**

- 决策对象：新增 graph/edge/routing 不足证明hybrid的整句。
- 理由：总定义原版已要求控制权变化；新增句落实到图工具时需明确实现级别。是否保留正文重复说明和表分类方案一起裁定。
- 引用、表格、图注、统计或章节结论影响：联动表 tab:9categories、框架表、十案例表及选择流程；图片仅列一致性核查，不覆盖。
- 依据：[E11](#e11)、[E12](#e12)。

<a id="d025"></a>

#### D025 Adaptive systems引导句

导师位置：f84c78b:manuscript.tex 488行。当前位置：[manuscript.tex](<C:/Users/ShenTianyu(CN-TV-T1)/schoolwork/ESWA-multiagent/manuscript.tex:512>) 512行。

追溯：98732a2（2026-10-10，第二阶段证据与控制流重编码）。f67f294本身没有新增manuscript.tex文字差异。

**导师原版：**

```tex
Adaptive systems adjust team composition or control patterns as tasks evolve.
```

**当前版本：**

```tex
Adaptive systems can adjust team composition or interaction patterns.
```

**D025 · B类 · 推荐：恢复**

- 决策对象：adjust…control patterns as tasks evolve→can adjust…interaction patterns。
- 理由：泛指自适应系统可调整成员/控制模式，与AgentVerse/MDAgents机制没有实质矛盾；是措辞与范围替换。
- 引用、表格、图注、统计或章节结论影响：不回退D026的moderator真实机制。
- 依据：[E13](#e13)、[E15](#e15)。

<a id="d026"></a>

#### D026 MDAgents真实路由和判定

导师位置：f84c78b:manuscript.tex 492–495行。当前位置：[manuscript.tex](<C:/Users/ShenTianyu(CN-TV-T1)/schoolwork/ESWA-multiagent/manuscript.tex:516>) 516–520行。

追溯：98732a2（2026-10-10，第二阶段证据与控制流重编码）。f67f294本身没有新增manuscript.tex文字差异。

**导师原版：**

```tex
hierarchical" rule. MDAgents \citep{kim2024mdagents} provides direct
in-case evidence for adaptive medical collaboration. Such adaptive mechanisms
enhance routing flexibility, yet introduce extra requirements for state management
and performance evaluation.
```

**当前版本：**

```tex
hierarchical" rule. MDAgents \citep{kim2024mdagents} routes medical queries to
solo, multidisciplinary-team, or integrated-care-team pathways according to
complexity under a moderator. This supports adaptive collaboration, but a
persistent moderator means that mode switching alone is insufficient to prove
hybrid authority. State management and performance still require evaluation.
```

**D026a · A类 · 推荐：保留机制事实**

- 决策对象：新增solo/MDT/ICT与moderator。
- 理由：原论文§3.1–3.4明确复杂度评估、招募及监督路径，事实可核。
- 引用、表格、图注、统计或章节结论影响：保留现有引用键；不改变书目池或78篇唯一引用统计。
- 依据：[E13](#e13)。

**D026b · C类 · 推荐：等待确认 Q4**

- 决策对象：persistent moderator…insufficient to prove hybrid authority。
- 理由：监督存在获来源支持，但架构整体如何编码还要按本文粒度判断；不能把方法标签说成来源自报事实。
- 引用、表格、图注、统计或章节结论影响：联动表 tab:9categories、框架表、十案例表及选择流程；图片仅列一致性核查，不覆盖。
- 依据：[E13](#e13)。

**D026c · B类 · 推荐：恢复（局部）**

- 决策对象：原 State management/performance要求尾句的替换。
- 理由：原版已限定额外状态管理与评估需要，无无条件性能收益；新尾句仅为润色。
- 引用、表格、图注、统计或章节结论影响：恢复原 yet introduce extra requirements for state management and performance evaluation 的尾句；机制主体按A修正。
- 依据：[E13](#e13)。

<a id="d027"></a>

#### D027 LangGraph暂停机制句与来源

导师位置：f84c78b:manuscript.tex 500–502行。当前位置：[manuscript.tex](<C:/Users/ShenTianyu(CN-TV-T1)/schoolwork/ESWA-multiagent/manuscript.tex:525>) 525–527行。

追溯：4ff0569（2026-10-08，第一阶段参考文献/归因核查）。f67f294本身没有新增manuscript.tex文字差异。

**导师原版：**

```tex
For example, LangGraph supports pausing a workflow at defined breakpoints for
human review \citep{langgraph2024}, which may be useful for high-risk
decisions.
```

**当前版本：**

```tex
For example, LangGraph supports checkpointed state and pausing a workflow
with an interrupt for human review \citep{langgraph2024interrupt}, which may
be useful for high-risk decisions.
```

**D027a · A类 · 推荐：保留引用修复**

- 决策对象：langgraph2024→langgraph2024interrupt。
- 理由：具体暂停/恢复功能应保留已经加入的日期明确的官方来源。
- 引用、表格、图注、统计或章节结论影响：保留现有引用键；不改变书目池或78篇唯一引用统计。
- 依据：[E12](#e12)。

**D027b · B类 · 推荐：恢复（局部）**

- 决策对象：defined breakpoints→checkpointed state…interrupt扩写。
- 理由：官方文章明确此前已有breakpoints/NodeInterrupt；旧词不是错误，增加完整checkpoint句非必要。
- 引用、表格、图注、统计或章节结论影响：恢复导师For example…defined breakpoints for human review…句式，使用现有langgraph2024interrupt键。
- 依据：[E12](#e12)。

<a id="d028"></a>

#### D028 Hybrid适用条件

导师位置：f84c78b:manuscript.tex 538行。当前位置：[manuscript.tex](<C:/Users/ShenTianyu(CN-TV-T1)/schoolwork/ESWA-multiagent/manuscript.tex:563>) 563行。

追溯：98732a2（2026-10-10，第二阶段证据与控制流重编码）。f67f294本身没有新增manuscript.tex文字差异。

**导师原版：**

```tex
Hybrid architectures are useful when task requirements are heterogeneous or when the workflow must combine deliberation, controlled execution, and conditional review. Their trade-off lies in engineering complexity: dynamic routing, state transitions, and cross-mode information transfer are more difficult to configure, debug, evaluate, and reproduce. A hybrid design is justified when this additional adaptability addresses documented uncertainty or risk, rather than serving as a default replacement for fixed control patterns.
```

**当前版本：**

```tex
Hybrid architectures may be appropriate when heterogeneous task requirements call for transitions between peer deliberation and central decision authority. Their trade-off lies in engineering complexity: dynamic routing, state transitions, and cross-mode information transfer are more difficult to configure, debug, evaluate, and reproduce. A hybrid design is justified when this additional adaptability addresses documented uncertainty or risk, rather than serving as a default replacement for fixed control patterns.
```

**D028 · C类 · 推荐：等待确认 Q4**

- 决策对象：heterogeneous/combine deliberation/review→peer与central authority转换。
- 理由：涉及选择建议的边界，原版定义已经要求adaptive authority；需作者确认以实现控制权还是阶段组合为判定粒度。
- 引用、表格、图注、统计或章节结论影响：联动表 tab:9categories、框架表、十案例表及选择流程；图片仅列一致性核查，不覆盖。
- 依据：[E11](#e11)、[E12](#e12)、[E13](#e13)。

<a id="d029"></a>

#### D029 架构比较表导语重构

导师位置：f84c78b:manuscript.tex 543–544行。当前位置：[manuscript.tex](<C:/Users/ShenTianyu(CN-TV-T1)/schoolwork/ESWA-multiagent/manuscript.tex:568>) 568–572行。

追溯：首次 4ff0569；98732a2 继续修改（含 Triad 边界/角色决定、来源重编码或表格机制标签）。f67f294本身没有新增manuscript.tex文字差异。

**导师原版：**

```tex
Table~\ref{tab:9categories} compares the three architecture classes and their
sub-paradigms in terms of control, task suitability, and limitations.
```

**当前版本：**

```tex
Table~\ref{tab:9categories} compares representative control patterns and
related mechanisms. Architecture labels, suitable contexts, and limitations
are the authors' synthesis. Role-paired, configurable, and cross-cutting
entries describe mechanisms or tool capabilities, not additional architecture
classes or evidence that every configuration is hybrid.
```

**D029 · C类 · 推荐：等待确认 Q4**

- 决策对象：三类与子范式→控制模式与机制混列表。
- 理由：改变表格承担的分类贡献与展示结构，不能只按语言处理。必要底线是区分作者归类与来源机制，避免全框架标签。
- 引用、表格、图注、统计或章节结论影响：仍保留三类总定义与章节；不把Role-paired/Configurable/Cross-cutting升级新架构类别。
- 依据：[E11](#e11)、[E12](#e12)、[E15](#e15)。

<a id="d030"></a>

#### D030 架构比较表题名

导师位置：f84c78b:manuscript.tex 548行。当前位置：[manuscript.tex](<C:/Users/ShenTianyu(CN-TV-T1)/schoolwork/ESWA-multiagent/manuscript.tex:576>) 576行。

追溯：98732a2（2026-10-10，第二阶段证据与控制流重编码）。f67f294本身没有新增manuscript.tex文字差异。

**导师原版：**

```tex
  \caption{Comparison of multi-agent collaborative QA architecture classes.}
```

**当前版本：**

```tex
  \caption{Representative control patterns and related mechanisms for multi-agent collaborative QA.}
```

**D030 · C类 · 推荐：等待确认 Q4**

- 决策对象：architecture classes→control patterns and related mechanisms。
- 理由：与表格重构一体，不宜单独恢复或保留。
- 引用、表格、图注、统计或章节结论影响：联动表 tab:9categories、框架表、十案例表及选择流程；图片仅列一致性核查，不覆盖。
- 依据：[E11](#e11)、[E12](#e12)、[E15](#e15)。

<a id="d031"></a>

#### D031 Flat三行合并标签

导师位置：f84c78b:manuscript.tex 558行。当前位置：[manuscript.tex](<C:/Users/ShenTianyu(CN-TV-T1)/schoolwork/ESWA-multiagent/manuscript.tex:586>) 586行。

追溯：98732a2（2026-10-10，第二阶段证据与控制流重编码）。f67f294本身没有新增manuscript.tex文字差异。

**导师原版：**

```tex
    \multirow{3}{*}{\textbf{Flat}} &
```

**当前版本：**

```tex
    \textbf{Flat} &
```

**D031 · C类 · 推荐：等待确认 Q4**

- 决策对象：Flat分组三行→仅Du一行。
- 理由：CAMEL/AutoGen是否在架构列单独作为机制需要作者选择展示方案；不是multirow排版修复。
- 引用、表格、图注、统计或章节结论影响：联动表 tab:9categories、框架表、十案例表及选择流程；图片仅列一致性核查，不覆盖。
- 依据：[E15](#e15)。

<a id="d032"></a>

#### D032 Debate限制与CAMEL行

导师位置：f84c78b:manuscript.tex 562–563行。当前位置：[manuscript.tex](<C:/Users/ShenTianyu(CN-TV-T1)/schoolwork/ESWA-multiagent/manuscript.tex:590>) 590–591行。

追溯：首次 4ff0569；98732a2 继续修改（含 Triad 边界/角色决定、来源重编码或表格机制标签）。f67f294本身没有新增manuscript.tex文字差异。

**导师原版：**

```tex
    Cost, degeneration, and aggregation sensitivity \\
    & Role-conditioned collaboration & CAMEL \citep{li2023camel} & 
```

**当前版本：**

```tex
    Coordination cost and aggregation sensitivity \\
    \textbf{Role-paired} & Role-conditioned collaboration & CAMEL \citep{li2023camel} & 
```

**D032a · A类 · 推荐：保留最小修正**

- 决策对象：移除degeneration限制词。
- 理由：此行对应Du来源；不能把其他研究的退化机制不加区分地归入该例。
- 引用、表格、图注、统计或章节结论影响：限制保持coordination cost、aggregation sensitivity。
- 依据：[E08](#e08)、[E09](#e09)。

**D032b · C类 · 推荐：等待确认 Q4**

- 决策对象：CAMEL行标签Role-paired。
- 理由：将原子范式移出flat类是分类呈现变更。
- 引用、表格、图注、统计或章节结论影响：联动表 tab:9categories、框架表、十案例表及选择流程；图片仅列一致性核查，不覆盖。
- 依据：[E15](#e15)。

<a id="d033"></a>

#### D033 AutoGen行标签

导师位置：f84c78b:manuscript.tex 567行。当前位置：[manuscript.tex](<C:/Users/ShenTianyu(CN-TV-T1)/schoolwork/ESWA-multiagent/manuscript.tex:595>) 595行。

追溯：98732a2（2026-10-10，第二阶段证据与控制流重编码）。f67f294本身没有新增manuscript.tex文字差异。

**导师原版：**

```tex
    & Group-chat collaboration & AutoGen \citep{wu2024autogen}  &
```

**当前版本：**

```tex
    \textbf{Configurable} & Group-chat collaboration & AutoGen \citep{wu2024autogen}  &
```

**D033 · C类 · 推荐：等待确认 Q4**

- 决策对象：Flat分组→Configurable。
- 理由：原版正文已说配置决定拓扑；框架不是所有配置都flat。事实限制必须保留，是否单独机制栏由作者定。
- 引用、表格、图注、统计或章节结论影响：联动表 tab:9categories、框架表、十案例表及选择流程；图片仅列一致性核查，不覆盖。
- 依据：[E15](#e15)。

<a id="d034"></a>

#### D034 Hierarchical多行跨度

导师位置：f84c78b:manuscript.tex 572行。当前位置：[manuscript.tex](<C:/Users/ShenTianyu(CN-TV-T1)/schoolwork/ESWA-multiagent/manuscript.tex:600>) 600行。

追溯：98732a2（2026-10-10，第二阶段证据与控制流重编码）。f67f294本身没有新增manuscript.tex文字差异。

**导师原版：**

```tex
    \multirow{3}{*}{\textbf{Hierarchical}} &
```

**当前版本：**

```tex
    \multirow{2}{*}{\textbf{Hierarchical}} &
```

**D034 · A类 · 推荐：保留**

- 决策对象：multirow{3}→multirow{2}。
- 理由：该分组只有两行；原跨度越过分组线，属于排版错误。
- 引用、表格、图注、统计或章节结论影响：不恢复越界multirow；与内容分类无关。
- 依据：[E01](#e01)。

<a id="d035"></a>

#### D035 管线范式与CoCoA-zero

导师位置：f84c78b:manuscript.tex 577行。当前位置：[manuscript.tex](<C:/Users/ShenTianyu(CN-TV-T1)/schoolwork/ESWA-multiagent/manuscript.tex:605>) 605行。

追溯：4ff0569（2026-10-08，第一阶段参考文献/归因核查）。f67f294本身没有新增manuscript.tex文字差异。

**导师原版：**

```tex
    & Plan--retrieve--generate pipeline & LONGAGENT; Chain-of-Agents; CoCoA
```

**当前版本：**

```tex
    & Staged evidence-processing pipeline & LONGAGENT; Chain-of-Agents; CoCoA-zero
```

**D035 · A类 · 推荐：保留最小名称修正**

- 决策对象：Plan--retrieve--generate→Staged evidence-processing；CoCoA-zero。
- 理由：CoA实际为顺序worker处理上下文再manager综合，不必先规划检索；统一旧名称误概括代表方法。
- 引用、表格、图注、统计或章节结论影响：保留三篇引用键、显式时序和综合描述。
- 依据：[E03](#e03)、[E10](#e10)。

<a id="d036"></a>

#### D036 Hybrid三行→Cross-cutting

导师位置：f84c78b:manuscript.tex 584行。当前位置：[manuscript.tex](<C:/Users/ShenTianyu(CN-TV-T1)/schoolwork/ESWA-multiagent/manuscript.tex:612>) 612行。

追溯：98732a2（2026-10-10，第二阶段证据与控制流重编码）。f67f294本身没有新增manuscript.tex文字差异。

**导师原版：**

```tex
    \multirow{3}{*}{\textbf{Hybrid}} &
```

**当前版本：**

```tex
    \multirow{3}{*}{\shortstack{\textbf{Cross-}\\\textbf{cutting}}} &
```

**D036 · C类 · 推荐：等待确认 Q4**

- 决策对象：图/自适应/HITL从Hybrid分组撤出。
- 理由：来源只证明机制，是否为本文hybrid实例要按实现判据；该改动删除比较表显式hybrid分组，影响核心展示。
- 引用、表格、图注、统计或章节结论影响：联动表 tab:9categories、框架表、十案例表及选择流程；图片仅列一致性核查，不覆盖。
- 依据：[E11](#e11)、[E12](#e12)、[E13](#e13)。

<a id="d037"></a>

#### D037 GPTSwarm与LangGraph图机制

导师位置：f84c78b:manuscript.tex 587行。当前位置：[manuscript.tex](<C:/Users/ShenTianyu(CN-TV-T1)/schoolwork/ESWA-multiagent/manuscript.tex:615>) 615行。

追溯：4ff0569（2026-10-08，第一阶段参考文献/归因核查）。f67f294本身没有新增manuscript.tex文字差异。

**导师原版：**

```tex
    Graph transitions permit loops, branches, and routing policies &
```

**当前版本：**

```tex
    DAG connection optimization in GPTSwarm; loops and conditional routing in LangGraph &
```

**D037 · A类 · 推荐：保留**

- 决策对象：统一loops/branches→分别说明DAG优化与状态图路由。
- 理由：GPTSwarm图优化与LangGraph循环/条件分支不能合并当作两者共有的实测机制。
- 引用、表格、图注、统计或章节结论影响：保留现有引用键；不改变书目池或78篇唯一引用统计。
- 依据：[E11](#e11)、[E12](#e12)。

<a id="d038"></a>

#### D038 MDAgents表格机制

导师位置：f84c78b:manuscript.tex 591行。当前位置：[manuscript.tex](<C:/Users/ShenTianyu(CN-TV-T1)/schoolwork/ESWA-multiagent/manuscript.tex:619>) 619行。

追溯：98732a2（2026-10-10，第二阶段证据与控制流重编码）。f67f294本身没有新增manuscript.tex文字差异。

**导师原版：**

```tex
    Changes collaboration in response to case characteristics &
```

**当前版本：**

```tex
    Moderator routes solo or team consultation according to complexity &
```

**D038 · A类 · 推荐：保留**

- 决策对象：changes collaboration→moderator routes solo/team。
- 理由：具体机制可由正式方法部分核实；不恢复掩去固定moderator的描述。
- 引用、表格、图注、统计或章节结论影响：与D026保留同一事实，标签仍按Q4。
- 依据：[E13](#e13)。

<a id="d039"></a>

#### D039 HITL表格术语和来源

导师位置：f84c78b:manuscript.tex 594行。当前位置：[manuscript.tex](<C:/Users/ShenTianyu(CN-TV-T1)/schoolwork/ESWA-multiagent/manuscript.tex:622>) 622行。

追溯：4ff0569（2026-10-08，第一阶段参考文献/归因核查）。f67f294本身没有新增manuscript.tex文字差异。

**导师原版：**

```tex
    & Human-in-the-loop design pattern & LangGraph breakpoints \citep{langgraph2024} &
```

**当前版本：**

```tex
    & Human-in-the-loop design pattern & LangGraph interrupts \citep{langgraph2024interrupt} &
```

**D039a · A类 · 推荐：保留引用修复**

- 决策对象：新增langgraph2024interrupt键。
- 理由：保留具体功能正式补证。
- 引用、表格、图注、统计或章节结论影响：保留现有引用键；不改变书目池或78篇唯一引用统计。
- 依据：[E12](#e12)。

**D039b · B类 · 推荐：恢复（局部）**

- 决策对象：LangGraph breakpoints→LangGraph interrupts。
- 理由：该官方文章同时承认旧breakpoints；原术语并非事实错误。
- 引用、表格、图注、统计或章节结论影响：可恢复LangGraph breakpoints并保留langgraph2024interrupt引用键；不回退书目。
- 依据：[E12](#e12)。

<a id="d040"></a>

#### D040 成本收益标准与MAST归因

导师位置：f84c78b:manuscript.tex 643–647行。当前位置：[manuscript.tex](<C:/Users/ShenTianyu(CN-TV-T1)/schoolwork/ESWA-multiagent/manuscript.tex:671>) 671–676行。

追溯：4ff0569（2026-10-08，第一阶段参考文献/归因核查）。f67f294本身没有新增manuscript.tex文字差异。

**导师原版：**

```tex
communication, aggregation, state-management, and inference costs. A
collaborative design is justified only when expected gains in coverage,
reliability, or adaptability offset those costs
\citep{han2024mast}. Assessment should include latency, token use, tool calls,
monitoring, and recovery overhead.
```

**当前版本：**

```tex
communication, aggregation, state-management, and inference costs. Reported
multi-agent failure modes \citep{han2024mast} motivate checking whether
additional coordination provides useful benefits. As a design criterion,
this review requires expected gains in coverage, reliability, or adaptability
to justify the resource burden. Assessment should include latency, token use,
tool calls, monitoring, and recovery overhead.
```

**D040a · A类 · 推荐：最小修正**

- 决策对象：成本收益门槛被绑定MAST来源。
- 理由：MAST研究失败模式，不直接实测本文的通用收益抵消成本门槛。
- 引用、表格、图注、统计或章节结论影响：把MAST作为失败模式依据，把阈值明确为本文设计判断。
- 依据：[E20](#e20)。

**D040b · B类 · 推荐：恢复（原句骨架）**

- 决策对象：新增失败动机与重述成本标准的两句扩写。
- 理由：原门槛本就是本文四标准之一，不必把它替换成两句新表达；只需消除错误来源归因。
- 引用、表格、图注、统计或章节结论影响：恢复A collaborative design is justified only when…offset those costs；标明as a criterion of this review，引用仍支持失败动机，避免再绑定门槛。
- 依据：[E20](#e20)。

<a id="d041"></a>

#### D041 第二阶段拓扑选择规则

导师位置：f84c78b:manuscript.tex 683–686行。当前位置：[manuscript.tex](<C:/Users/ShenTianyu(CN-TV-T1)/schoolwork/ESWA-multiagent/manuscript.tex:712>) 712–716行。

追溯：98732a2（2026-10-10，第二阶段证据与控制流重编码）。f67f294本身没有新增manuscript.tex文字差异。

**导师原版：**

```tex
when independent perspectives are valuable; changing requirements or
conditional review support hybrid control. Compare the selected design with a
single-agent baseline using task quality, latency, cost, provenance, and
failure-recovery measures.
```

**当前版本：**

```tex
when independent perspectives are valuable; hybrid control is a candidate
when changing requirements necessitate a change in decision authority.
Conditional review under a fixed approver remains hierarchical. Compare the
selected design with a single-agent baseline using task quality, latency,
cost, provenance, and failure-recovery measures.
```

**D041 · C类 · 推荐：等待确认 Q4**

- 决策对象：changing requirements/conditional review→actual authority change。
- 理由：影响架构推荐输出；固定审批不能仅因出现就称hybrid的事实限制合理，但方法边界与表分类需共同裁定。
- 引用、表格、图注、统计或章节结论影响：原两阶段、四标准、单智能体基线及性能比较要求均保持。
- 依据：[E12](#e12)、[E13](#e13)。

<a id="d042"></a>

#### D042 十案例比较方法重写

导师位置：f84c78b:manuscript.tex 700–705行。当前位置：[manuscript.tex](<C:/Users/ShenTianyu(CN-TV-T1)/schoolwork/ESWA-multiagent/manuscript.tex:730>) 730–738行。

追溯：98732a2（2026-10-10，第二阶段证据与控制流重编码）。f67f294本身没有新增manuscript.tex文字差异。

**导师原版：**

```tex
The approach is verified for interpretive consistency by comparing its
inferred architectures with ten published systems. This purposive sample was
selected because the systems report agent roles and control flow with enough
detail for coding and cover different domains, process structures, and risk
levels. The comparison does not evaluate system performance, establish causal
benefit, or claim external validity.
```

**当前版本：**

```tex
The approach is examined for interpretive consistency using ten published
systems. This purposive sample contains both core QA studies and supporting
workflow examples; it does not evaluate performance, establish causal benefit,
or provide independent validation. The existing proposed labels are retained
for comparison, while reported workflows are re-coded using one rule:
flat control has no persistent top-down controller; hierarchical control has
stable routing, approval, or final-decision authority; hybrid control requires
a demonstrated change in that authority. Iteration, voting, multiple roles,
and graph structure alone are insufficient.
```

**D042 · C类 · 推荐：等待确认 Q5**

- 决策对象：verified purposive comparison→冻结建议标签并按一规则重编码。
- 理由：原版已经不声称性能、因果、外部有效性；新增重编码、冻结建议标签的评价方法不能作为纯事实纠错自动保留。
- 引用、表格、图注、统计或章节结论影响：与表中匹配符号、六/四、no-hybrid限制联动；不改十个案例身份。
- 依据：[E14](#e14)。

<a id="d043"></a>

#### D043 十案例5/3/2→6/4及结论

导师位置：f84c78b:manuscript.tex 707–714行。当前位置：[manuscript.tex](<C:/Users/ShenTianyu(CN-TV-T1)/schoolwork/ESWA-multiagent/manuscript.tex:740>) 740–748行。

追溯：98732a2（2026-10-10，第二阶段证据与控制流重编码）。f67f294本身没有新增manuscript.tex文字差异。

**导师原版：**

```tex
Five cases are broadly aligned, three are partially aligned, and two are
divergent under the coding used here. MedAgents and LLM-MedQA combine
parallel expert perspectives with staged synthesis; MAD is flat at the macro
level but uses iterative convergence; EduPlanner and Financial Reflection QA
combine convergent objectives with evaluator or critic feedback. These boundary
cases show that competing requirements can make a single categorical label
insufficient and that a multi-label description of control flow may sometimes
be preferable.
```

**当前版本：**

```tex
Exact category agreement occurs in six cases, with four disagreements.
MedAgents, LLM-MedQA, LegalGraphRAG, and EduPlanner have fixed asymmetric
stages or final-decision roles, while their retained proposed labels differ.
Du et al.'s peer debate remains flat despite repeated rounds, and Financial
Reflection QA remains hierarchical despite critic feedback. Nine reported
workflows are coded hierarchical and one flat; this sample therefore does not
validate the hybrid category. The comparison is retrospective and was not
blind or preregistered. The six agreements are descriptive, not prediction
accuracy or evidence of an effective architecture-selection policy.
```

**D043 · C类 · 推荐：等待确认 Q5**

- 决策对象：匹配数、粒度、多标签建议结论。
- 理由：原数字按原三档符号算术成立；新6/4按新二档符号也成立。变化来自重新编码及评分规则，不是只修算术。新否定hybrid验证结论依赖当前源标签。
- 引用、表格、图注、统计或章节结论影响：不混用旧5/3/2与新二档规则；不把6/10说成预测准确率。
- 依据：[E14](#e14)。

<a id="d044"></a>

#### D044 十案例表头来源性质

导师位置：f84c78b:manuscript.tex 724行。当前位置：[manuscript.tex](<C:/Users/ShenTianyu(CN-TV-T1)/schoolwork/ESWA-multiagent/manuscript.tex:758>) 758行。

追溯：4ff0569（2026-10-08，第一阶段参考文献/归因核查）。f67f294本身没有新增manuscript.tex文字差异。

**导师原版：**

```tex
    \textbf{Inferred versus reported architecture} & \textbf{Match} \\
```

**当前版本：**

```tex
    \textbf{Inferred versus source-based architecture coding} & \textbf{Match} \\
```

**D044 · A类 · 推荐：保留最小表头修正**

- 决策对象：reported architecture→source-based architecture coding。
- 理由：这些标签是本文作者回顾性判断，未证明由每篇原作者自报；必须去掉来源自报的误导。
- 引用、表格、图注、统计或章节结论影响：不预先决定Q5的评分档数。
- 依据：[E14](#e14)。

<a id="d045"></a>

#### D045 MedAgents、LLM-MedQA、LegalGraphRAG和Triad表行

导师位置：f84c78b:manuscript.tex 726–729行。当前位置：[manuscript.tex](<C:/Users/ShenTianyu(CN-TV-T1)/schoolwork/ESWA-multiagent/manuscript.tex:760>) 760–763行。

追溯：首次 4ff0569；98732a2 继续修改（含 Triad 边界/角色决定、来源重编码或表格机制标签）。f67f294本身没有新增manuscript.tex文字差异。

**导师原版：**

```tex
    MedAgents \citep{tang2024medagents} & Multi-specialty medical QA; high complexity and moderate risk & Flat versus hybrid staged synthesis & $\triangle$ \\
    LLM-MedQA \citep{tang2025llmmedqa} & Standardised medical MCQ; convergent objective with diverse views & Flat versus hybrid voting pipeline & $\triangle$ \\
    LegalGraphRAG \citep{legalgraphrag2026} & Legal verdict prediction; high risk and structured retrieval & Hybrid versus hybrid graph audit chain & $\checkmark$ \\
    Triad \citep{hu2024triad} & Enterprise KBQA; standardised Text-to-SPARQL workflow & Hierarchical versus hierarchical pipeline & $\checkmark$ \\
```

**当前版本：**

```tex
    MedAgents \citep{tang2024medagents} & Multi-specialty medical QA; high complexity and moderate risk & Flat versus hierarchical staged synthesis & $\times$ \\
    LLM-MedQA \citep{tang2025llmmedqa} & Standardised medical MCQ; convergent objective with diverse views & Flat versus hierarchical voting pipeline & $\times$ \\
    LegalGraphRAG \citep{legalgraphrag2026} & Legal verdict prediction; high risk and structured retrieval & Hybrid versus hierarchical graph audit chain & $\times$ \\
    Triad \citep{hu2024triad} & Knowledge-base QA; standardised Text-to-SPARQL workflow & Hierarchical versus hierarchical pipeline & $\checkmark$ \\
```

**D045a · C类 · 推荐：等待确认 Q5**

- 决策对象：MedAgents source Hybrid→Hierarchical、△→×。
- 理由：五阶段与固定最终决策确证；全局标签和匹配仍是本文判断。
- 引用、表格、图注、统计或章节结论影响：原建议Flat保持；不同评分方案需重算。
- 依据：[E14](#e14)。

**D045b · C类 · 推荐：等待确认 Q5**

- 决策对象：LLM-MedQA source Hybrid→Hierarchical、△→×。
- 理由：六阶段、专家投票、报告修订与最终选择获预印本支持；正式用户PDF当前不可重读，不能把版本一致性默认为已重新证明。
- 引用、表格、图注、统计或章节结论影响：原建议Flat保持；记录正式证据定位与当前版本限制。
- 依据：[E14](#e14)。

**D045c · C类 · 推荐：等待确认 Q5**

- 决策对象：LegalGraphRAG source Hybrid→Hierarchical、✓→×。
- 理由：Researcher→Auditor→Adjudicator时序确证；图结构不自动证明决策权切换，类别由本文规则解释。
- 引用、表格、图注、统计或章节结论影响：原建议Hybrid保持，不伪造原作者标签。
- 依据：[E14](#e14)。

**D045d · A类 · 推荐：保留最小领域名称纠正**

- 决策对象：Triad Enterprise KBQA→Knowledge-base QA。
- 理由：实测为公开KBQA基准，不是企业部署证据。
- 引用、表格、图注、统计或章节结论影响：仍为十案例支持例、S角色，不计入13核心。
- 依据：[E02](#e02)。

<a id="d046"></a>

#### D046 Du案例身份、描述与匹配

导师位置：f84c78b:manuscript.tex 733行。当前位置：[manuscript.tex](<C:/Users/ShenTianyu(CN-TV-T1)/schoolwork/ESWA-multiagent/manuscript.tex:767>) 767行。

追溯：98732a2（2026-10-10，第二阶段证据与控制流重编码）。f67f294本身没有新增manuscript.tex文字差异。

**导师原版：**

```tex
    MAD \citep{du2024multiagent_debate} & Open-domain reasoning; open process and low risk & Flat versus flat iterative convergence & $\triangle$ \\
```

**当前版本：**

```tex
    Multiagent debate (Du) \citep{du2024multiagent_debate} & Factual QA and reasoning; peer exchange & Flat versus flat iterative debate & $\checkmark$ \\
```

**D046a · A类 · 推荐：保留必要身份与事实修正**

- 决策对象：MAD/low risk→Multiagent debate (Du)/peer exchange。
- 理由：避免与Liang的MAD及judge流程混淆；原文没有现实风险量化，不能保留low risk为研究实测。
- 引用、表格、图注、统计或章节结论影响：保留du2024multiagent_debate键；不改案例数量。
- 依据：[E08](#e08)。

**D046b · C类 · 推荐：等待确认 Q5**

- 决策对象：Flat/Flat 的△→✓。
- 理由：旧△并非算错，它反映旧“部分一致”的过程评价；新✓来自精确类别一致新规则。
- 引用、表格、图注、统计或章节结论影响：不能独立改一个符号却保留5/3/2总数。
- 依据：[E14](#e14)。

<a id="d047"></a>

#### D047 Financial QA critic事实与架构匹配

导师位置：f84c78b:manuscript.tex 735行。当前位置：[manuscript.tex](<C:/Users/ShenTianyu(CN-TV-T1)/schoolwork/ESWA-multiagent/manuscript.tex:769>) 769行。

追溯：首次 4ff0569；98732a2 继续修改（含 Triad 边界/角色决定、来源重编码或表格机制标签）。f67f294本身没有新增manuscript.tex文字差异。

**导师原版：**

```tex
    Financial Reflection QA \citep{fatemi2024financialqa} & Numerical QA; convergence with self-critique & Hierarchical versus hybrid reflection loop & $\times$ \\
```

**当前版本：**

```tex
    Financial Reflection QA \citep{fatemi2024financialqa} & Numerical QA; convergence with critic feedback & Hierarchical versus hierarchical critic feedback & $\checkmark$ \\
```

**D047a · A类 · 推荐：保留事实纠正**

- 决策对象：self-critique→critic feedback。
- 理由：实现为专家与外部critic反馈；来源§6把反复多轮辩论列作未来工作。
- 引用、表格、图注、统计或章节结论影响：保留现有引用键；不改变书目池或78篇唯一引用统计。
- 依据：[E14](#e14)。

**D047b · C类 · 推荐：等待确认 Q5**

- 决策对象：Hierarchical/Hybrid ×→Hierarchical/Hierarchical ✓。
- 理由：稳定critics→expert修订支持当前编码，但宏观类别及评分是作者判断，需与其他案例统一。
- 引用、表格、图注、统计或章节结论影响：禁止恢复未实现的多轮机制。
- 依据：[E14](#e14)。

<a id="d048"></a>

#### D048 十案例表注

导师位置：f84c78b:manuscript.tex 739–741行。当前位置：[manuscript.tex](<C:/Users/ShenTianyu(CN-TV-T1)/schoolwork/ESWA-multiagent/manuscript.tex:773>) 773–779行。

追溯：首次 4ff0569；98732a2 继续修改（含 Triad 边界/角色决定、来源重编码或表格机制标签）。f67f294本身没有新增manuscript.tex文字差异。

**导师原版：**

```tex
  \textit{Note}: $\checkmark$ = broadly aligned; $\triangle$ = partially aligned;
  $\times$ = divergent. The labels are author coding and do not constitute
  independent validation.
```

**当前版本：**

```tex
  \textit{Note}: $\checkmark$ = exact category agreement; $\times$ = different
  categories. Proposed labels are retained from the preceding draft;
  source-based labels are the authors' retrospective control-flow coding.
  Neither label nor agreement establishes selection accuracy or safety.
  Triad is a single-agent, three-role supporting study (S), outside the
  13 core studies. ChatDev, AgentCoder, and EduPlanner are also supporting
  workflow examples. Criterion profiles are illustrative author judgments.
```

**D048a · C类 · 推荐：等待确认 Q5**

- 决策对象：三档→二档；冻结建议标签等方法说明。
- 理由：必须与Q5整体决定；原注已经说作者编码且非独立验证，新长注并非全部必需。
- 引用、表格、图注、统计或章节结论影响：评分、方法、正文统计同步。
- 依据：[E14](#e14)。

**D048b · A类 · 推荐：保留必要边界**

- 决策对象：Triad S/单代理；ChatDev/AgentCoder/EduPlanner支持工作流边界。
- 理由：这些支持例不能充当13项核心QA研究；并不意味着删除十案例的支持例。
- 引用、表格、图注、统计或章节结论影响：保留十个案例、核心13和相关键；不把混合样本称十项核心QA研究。
- 依据：[E02](#e02)、[E03](#e03)、[E15](#e15)。

<a id="d049"></a>

#### D049 架构应用建议整段

导师位置：f84c78b:manuscript.tex 745–752行。当前位置：[manuscript.tex](<C:/Users/ShenTianyu(CN-TV-T1)/schoolwork/ESWA-multiagent/manuscript.tex:783>) 783–790行。

追溯：98732a2（2026-10-10，第二阶段证据与控制流重编码）。f67f294本身没有新增manuscript.tex文字差异。

**导师原版：**

```tex
high-risk, cross-domain consultation, parallel specialist analysis may improve
coverage, but final decisions require an explicit review boundary, making a
hybrid workflow with human approval a plausible candidate. Standardised,
evidence-grounded QA generally supports a hierarchical RAG baseline with
source and citation checks. Open-ended educational or legal tasks may benefit
from bounded peer critique, but legal use additionally requires auditability
and human accountability. These examples illustrate how task and governance
requirements constrain the design space; they do not imply one universally
```

**当前版本：**

```tex
cross-domain consultation, parallel specialist analysis may improve coverage,
while a fixed review and final-decision boundary produces a hierarchical
workflow. A hybrid candidate requires an actual conditional change in decision
authority, rather than the mere addition of human approval. Standardised,
evidence-grounded QA can use a hierarchical retrieval-and-synthesis baseline
with source and citation checks. Open-ended tasks may use bounded peer
critique, while consequential decisions call for explicit accountability.
These are design hypotheses, not evaluated prescriptions for a universally
```

**D049a · C类 · 推荐：等待确认 Q4**

- 决策对象：parallel specialist + approval Hybrid→Hierarchical／actual authoritychange。
- 理由：改变场景对应架构的建议，是方法应用的重要部分，需按总定义明确。
- 引用、表格、图注、统计或章节结论影响：与选择流程图和Q5案例解释联动；不自行改图。
- 依据：[E12](#e12)、[E13](#e13)。

**D049b · B类 · 推荐：恢复（不涉及架构标签的部分）**

- 决策对象：删除high-risk、educational/legal、auditability/human accountability及原尾句。
- 理由：这些是导师原有应用场景与治理要求，原句已经使用may/plausible及not universally correct，不因修一个hybrid判定就应概括掉。
- 引用、表格、图注、统计或章节结论影响：恢复原场景、论证顺序和These examples illustrate…尾句；hybrid/hierarchical短语等待Q4。
- 依据：[E04](#e04)。

### 第4章 Key technologies

<a id="d050"></a>

#### D050 MCP/A2A协议段

导师位置：f84c78b:manuscript.tex 815–824行。当前位置：[manuscript.tex](<C:/Users/ShenTianyu(CN-TV-T1)/schoolwork/ESWA-multiagent/manuscript.tex:853>) 853–858行。

追溯：4ff0569（2026-10-08，第一阶段参考文献/归因核查）。f67f294本身没有新增manuscript.tex文字差异。

**导师原版：**

```tex
With the rapid development of multi-agent ecosystems, interoperability barriers have arisen between agents developed by different vendors.
To address this issue, the industry has initiated efforts to standardize communication protocols. For example, Anthropic introduced the Model Context Protocol (MCP)
\citep{anthropic2024mcp}—dubbed the "USB-C of AI"—to standardise
the way agents connect to external tools and data sources.
Another example is Google's proposed Agent-to-Agent (A2A) protocol
\citep{google2025a2a}, which regulates horizontal peer-to-peer collaboration
among agents.
These standards are being gradually adopted by the open-source
community and the Linux Foundation, laying a foundation for heterogeneous
multi-agent QA systems.
```

**当前版本：**

```tex
Industry initiatives address different parts of the interface problem.
Anthropic introduced the Model Context Protocol (MCP)
\citep{anthropic2024mcp} to standardise connections to external tools and data
sources. Google's Agent2Agent (A2A) protocol \citep{google2025a2a} supports
communication and task coordination between agents across frameworks and
vendors. These interfaces can support heterogeneous multi-agent QA systems.
```

**D050a · A类 · 推荐：最小修正**

- 决策对象：A2A仅horizontal peer-to-peer；未给日期的Linux Foundation共同采用。
- 理由：A2A为跨框架/厂商任务协调接口，并不规定QA决策权平等；现有两篇公告不能证明全段后续基金会采用历史。USB-C外号亦不能当Anthropic公告原词。
- 引用、表格、图注、统计或章节结论影响：保留MCP工具数据接口、A2A官方名称及跨厂商机制，不恢复不明日期采用结论。
- 依据：[E16](#e16)。

**D050b · B类 · 推荐：恢复（开头过渡）**

- 决策对象：原互操作障碍→标准化努力的过渡被缩成Industry initiatives。
- 理由：官方公告本就针对接口碎片化和互操作；原开头两句的叙述逻辑没有实质错误。
- 引用、表格、图注、统计或章节结论影响：恢复原With the rapid development…与To address…，保留A2A机制修正与证据边界。
- 依据：[E16](#e16)。

<a id="d051"></a>

#### D051 Plan-and-Solve效果范围

导师位置：f84c78b:manuscript.tex 866–868行。当前位置：[manuscript.tex](<C:/Users/ShenTianyu(CN-TV-T1)/schoolwork/ESWA-multiagent/manuscript.tex:900>) 900–901行。

追溯：4ff0569（2026-10-08，第一阶段参考文献/归因核查）。f67f294本身没有新增manuscript.tex文字差异。

**导师原版：**

```tex
by explicitly separating
the planning and solving phases, substantially improving decomposition
reliability.
```

**当前版本：**

```tex
by explicitly separating planning from solving and reducing missing-step
errors on the evaluated reasoning tasks.
```

**D051 · A类 · 推荐：最小修正**

- 决策对象：substantially improving decomposition reliability→missing-step errors on evaluated tasks。
- 理由：原文Table6测missing-step错误，不证明所有任务的总体分解可靠性。
- 引用、表格、图注、统计或章节结论影响：保留现有引用键；不改变书目池或78篇唯一引用统计。
- 依据：[E17](#e17)。

<a id="d052"></a>

#### D052 职责分配与吞吐保证

导师位置：f84c78b:manuscript.tex 886–893行。当前位置：[manuscript.tex](<C:/Users/ShenTianyu(CN-TV-T1)/schoolwork/ESWA-multiagent/manuscript.tex:919>) 919–925行。

追溯：4ff0569（2026-10-08，第一阶段参考文献/归因核查）。f67f294本身没有新增manuscript.tex文字差异。

**导师原版：**

```tex
After decomposition, the system must assign sub-tasks to the most suitable
agents. For example, MetaGPT \citep{hong2024metagpt} and AgentVerse
\citep{chen2024agentverse}
construct fine-grained agent profiles (Agent Profiling) that tag each agent
with specific role labels.
During runtime, a scheduler uses skill-based routing to dispatch sub-tasks
such as code writing, literature retrieval, or logical verification to the
corresponding expert agent, maximising throughput.
```

**当前版本：**

```tex
After decomposition, the system must assign sub-tasks to suitable agents.
For example, MetaGPT \citep{hong2024metagpt} organises agents through
predefined software-engineering roles, while AgentVerse
\citep{chen2024agentverse} recruits experts by generating task-specific
expertise descriptions and adjusts team composition using evaluation
feedback. These mechanisms guide which agents contribute to a task;
their scheduling efficiency requires separate evaluation.
```

**D052a · A类 · 推荐：保留机制纠正**

- 决策对象：统一profiling/skill-based routing/maximum throughput。
- 理由：MetaGPT预定义角色、AgentVerse按目标招募及反馈调整的机制不同；没有通用skill-routing或最大吞吐保证。
- 引用、表格、图注、统计或章节结论影响：保留现有引用键；不改变书目池或78篇唯一引用统计。
- 依据：[E15](#e15)。

**D052b · B类 · 推荐：恢复（段首）**

- 决策对象：most suitable→suitable 的段首替换。
- 理由：原段首是设计目的，应给子任务选择最合适角色，并非已证实全局最优调度算法；后文错误不要求删这个普通目标。
- 引用、表格、图注、统计或章节结论影响：恢复After decomposition…most suitable agents一句，保留之后的已核机制。
- 依据：[E15](#e15)。

<a id="d053"></a>

#### D053 共享知识的必要性与效果

导师位置：f84c78b:manuscript.tex 932–938行。当前位置：[manuscript.tex](<C:/Users/ShenTianyu(CN-TV-T1)/schoolwork/ESWA-multiagent/manuscript.tex:964>) 964–970行。

追溯：98732a2（2026-10-10，第二阶段证据与控制流重编码）。f67f294本身没有新增manuscript.tex文字差异。

**导师原版：**

```tex
In complex collaboration, knowledge must not be siloed within individual
agents.
The system needs a global knowledge graph shared across agents so that all
collaborative nodes can synchronise critical facts in real time.
By constructing a shared graph-vector database, newly spawned sub-agents
can rapidly inherit the team's cumulative knowledge, avoiding redundant
retrieval and cognitive divergence.
```

**当前版本：**

```tex
In complex collaboration, designers may provide a shared evidence repository
when agents need access to the same verified information. A graph, vector
store, document store, or their combination is an implementation choice,
rather than a requirement that every system use a global knowledge graph.
New agents may reuse relevant context subject to provenance and access
checks. Whether this reduces repeated retrieval or inconsistent answers
requires measurement; synchronisation is not automatically real time.
```

**D053a · A类 · 推荐：最小修正**

- 决策对象：must/global KG/real time/avoiding retrieval保证。
- 理由：所有复杂系统都必须全局图且实时同步、一定避开冗余，没有本段证据支持。
- 引用、表格、图注、统计或章节结论影响：把必须改可选；去掉实时与效果保证；不撤掉原共享知识论点。
- 依据：[E18](#e18)。

**D053b · B类 · 推荐：恢复（删除非必要新增内容）**

- 决策对象：新增graph/vector/document枚举及provenance/access checks。
- 理由：合理工程建议也不是纠正原绝对句所必需；用户明确不新增内容。
- 引用、表格、图注、统计或章节结论影响：用原图-向量库论证结构做最小弱化；删除新实现枚举和访问检查扩写。
- 依据：[E18](#e18)。

<a id="d054"></a>

#### D054 MemGPT机制

导师位置：f84c78b:manuscript.tex 965–969行。当前位置：[manuscript.tex](<C:/Users/ShenTianyu(CN-TV-T1)/schoolwork/ESWA-multiagent/manuscript.tex:997>) 997–1001行。

追溯：4ff0569（2026-10-08，第一阶段参考文献/归因核查）。f67f294本身没有新增manuscript.tex文字差异。

**导师原版：**

```tex
current QA session. For example, MemGPT \citep{packer2023memgpt} draws on the
paged-memory mechanism of modern operating systems to design a hierarchical
working-memory system. The system retains critical context in memory based on
attention weights and evicts redundant information, providing seamless
long-conversation support within a limited context window.
```

**当前版本：**

```tex
current QA session. For example, MemGPT \citep{packer2023memgpt} draws on
operating-system memory hierarchies to manage a limited main context and
external memory. Function calls control information transfer between them,
while a FIFO message queue and recursive summaries manage dialogue context
under the context-window limit.
```

**D054 · A类 · 推荐：保留**

- 决策对象：attention-weight eviction→function calls/FIFO/recursive summaries。
- 理由：已读v1§2.1–2.2原文直接支持函数控制和FIFO；注意力权重淘汰错误。
- 引用、表格、图注、统计或章节结论影响：保留现有引用键；不改变书目池或78篇唯一引用统计。
- 依据：[E19](#e19)。

<a id="d055"></a>

#### D055 长期记忆与RAG主体

导师位置：f84c78b:manuscript.tex 974–979行。当前位置：[manuscript.tex](<C:/Users/ShenTianyu(CN-TV-T1)/schoolwork/ESWA-multiagent/manuscript.tex:1006>) 1006–1011行。

追溯：4ff0569（2026-10-08，第一阶段参考文献/归因核查）。f67f294本身没有新增manuscript.tex文字差异。

**导师原版：**

```tex
Long-term memory typically relies on vector databases to store vast
historical experiences and external domain knowledge
\citep{zhang2024memory_survey}. A representative access mechanism is
Retrieval-Augmented Generation (RAG) \citep{lewis2020rag,gao2024rag_survey},
through which multi-agent QA systems access long-term memory. A retrieval
agent selects the Top-$k$ relevant documents from knowledge base $\mathcal{D}$
```

**当前版本：**

```tex
Long-term memory can retain historical experiences and domain knowledge in
external stores \citep{zhang2024memory_survey}. Vector retrieval is one way
to access such information: Retrieval-Augmented Generation (RAG)
\citep{lewis2020rag,gao2024rag_survey} augments generation with retrieved
documents. As one illustrative multi-agent implementation, a retrieval agent
can select the Top-$k$ relevant documents from knowledge base $\mathcal{D}$
```

**D055a · A类 · 推荐：最小修正**

- 决策对象：长期记忆普遍vector/RAG必然多智能体。
- 理由：存储与访问方式应分开；原RAG不是多代理系统实证。当前示例性multi-agent限定必要。
- 引用、表格、图注、统计或章节结论影响：保留向量余弦检索公式与Top-k定义，不把单模型来源说成多代理。
- 依据：[E18](#e18)。

**D055b · B类 · 推荐：恢复（原句顺序）**

- 决策对象：A representative access mechanism is…等原句骨架被重排。
- 理由：说明RAG是代表访问机制本身正确；无需为限定主体而改写整段。
- 引用、表格、图注、统计或章节结论影响：尽量复用原Long-term memory…A representative access mechanism…A retrieval agent…，将typically改can、agent加illustrative限定；不恢复A类错误。
- 依据：[E18](#e18)。

<a id="d056"></a>

#### D056 Self-RAG/FLARE机制

导师位置：f84c78b:manuscript.tex 991–995行。当前位置：[manuscript.tex](<C:/Users/ShenTianyu(CN-TV-T1)/schoolwork/ESWA-multiagent/manuscript.tex:1023>) 1023–1028行。

追溯：4ff0569（2026-10-08，第一阶段参考文献/归因核查）。f67f294本身没有新增manuscript.tex文字差异。

**导师原版：**

```tex
evolved from early passive Naive RAG to active variants. For example, Self-RAG
\citep{asai2024selfrag} and proactive retrieval (FLARE)
\citep{jiang2023active_rag} allow specialised retrieval agents to autonomously
determine when to retrieve, evaluate retrieval quality, and pass refined
knowledge to the generation agent.
```

**当前版本：**

```tex
evolved from passive retrieval to active variants. Self-RAG
\citep{asai2024selfrag} uses reflection tokens to decide when to retrieve and
to critique generated passages, while FLARE \citep{jiang2023active_rag}
triggers retrieval when predicted upcoming text contains low-confidence
tokens and then regenerates that text. These controls can inform retrieval
components in a multi-agent workflow.
```

**D056 · A类 · 推荐：保留**

- 决策对象：specialised retrieval agents→reflection tokens与low-confidence触发。
- 理由：分别是受反思token控制的单LM推理，以及预测低置信句后检索再生成；不能直接当成原生专门多代理。
- 引用、表格、图注、统计或章节结论影响：保留现有引用键；不改变书目池或78篇唯一引用统计。
- 依据：[E18](#e18)。

<a id="d057"></a>

#### D057 CoT效果的修辞

导师位置：f84c78b:manuscript.tex 1023–1024行。当前位置：[manuscript.tex](<C:/Users/ShenTianyu(CN-TV-T1)/schoolwork/ESWA-multiagent/manuscript.tex:1056>) 1056–1058行。

追溯：4ff0569（2026-10-08，第一阶段参考文献/归因核查）。f67f294本身没有新增manuscript.tex文字差异。

**导师原版：**

```tex
Chain-of-Thought (CoT) prompting \citep{wei2022chain_of_thought} has
greatly unlocked the reasoning potential of LLMs.
```

**当前版本：**

```tex
Chain-of-Thought (CoT) prompting \citep{wei2022chain_of_thought}
can improve performance on evaluated arithmetic, commonsense, and symbolic
reasoning tasks.
```

**D057 · B类 · 推荐：恢复**

- 决策对象：greatly unlocked reasoning potential→任务列表效果。
- 理由：CoT来源确有推理任务改进；原句没有说适用于全部任务，也无准确率或安全承诺。此处主要是修辞变得更克制，不能以更学术为由强留。
- 引用、表格、图注、统计或章节结论影响：恢复导师定性句，不添加普遍正确性或新定量结论。
- 依据：[E21](#e21)。

<a id="d058"></a>

#### D058 Self-Consistency公式主体

导师位置：f84c78b:manuscript.tex 1032–1034行。当前位置：[manuscript.tex](<C:/Users/ShenTianyu(CN-TV-T1)/schoolwork/ESWA-multiagent/manuscript.tex:1066>) 1066–1068行。

追溯：4ff0569（2026-10-08，第一阶段参考文献/归因核查）。f67f294本身没有新增manuscript.tex文字差异。

**导师原版：**

```tex
Each agent independently samples $K$ reasoning paths
$\{(r_k, a_k)\}_{k=1}^{K}$ for the same question, and majority voting
selects the final answer:
```

**当前版本：**

```tex
In the single-model baseline, $K$ reasoning paths
$\{(r_k, a_k)\}_{k=1}^{K}$ are sampled for the same question, and majority
voting selects the final answer:
```

**D058 · A类 · 推荐：保留最小主体修正**

- 决策对象：Each agent→single-model baseline。
- 理由：前文明确介绍单模型SC，再讲多代理推广；原Each agent紧邻公式混淆主体且未说明多代理二层聚合。
- 引用、表格、图注、统计或章节结论影响：原公式、K、argmax保持；不是研究方法或公式结果更改。
- 依据：[E21](#e21)。

<a id="d059"></a>

#### D059 ToT/GoT thought与agent

导师位置：f84c78b:manuscript.tex 1051–1055行。当前位置：[manuscript.tex](<C:/Users/ShenTianyu(CN-TV-T1)/schoolwork/ESWA-multiagent/manuscript.tex:1085>) 1085–1089行。

追溯：4ff0569（2026-10-08，第一阶段参考文献/归因核查）。f67f294本身没有新增manuscript.tex文字差异。

**导师原版：**

```tex
Representative search topologies include Chain-of-Agents
\citep{zhang2024chain_agents}, Tree of Thoughts
\citep{yao2023tree_of_thoughts}, and Graph of Thoughts
\citep{besta2024graph_of_thoughts}; these distribute reasoning across multiple
serially or graph-connected agents.
```

**当前版本：**

```tex
Chain-of-Agents \citep{zhang2024chain_agents} distributes evidence processing
across worker agents, while Tree of Thoughts
\citep{yao2023tree_of_thoughts} and Graph of Thoughts
\citep{besta2024graph_of_thoughts} organise intermediate reasoning states as
search structures.
```

**D059 · A类 · 推荐：保留**

- 决策对象：these distribute…across multiple agents→search states。
- 理由：原方法的thought/state不是必须独立智能体，不能与CoA统一说成多agent。
- 引用、表格、图注、统计或章节结论影响：保留CoA多worker证据及三个键。
- 依据：[E21](#e21)。

<a id="d060"></a>

#### D060 自省必要条件与新免责声明

导师位置：f84c78b:manuscript.tex 1066–1067行。当前位置：[manuscript.tex](<C:/Users/ShenTianyu(CN-TV-T1)/schoolwork/ESWA-multiagent/manuscript.tex:1100>) 1100–1101行。

追溯：98732a2（2026-10-10，第二阶段证据与控制流重编码）。f67f294本身没有新增manuscript.tex文字差异。

**导师原版：**

```tex
To suppress hallucination, agents must be capable of iterative
self-examination.
```

**当前版本：**

```tex
Reflection and critique are possible approaches to factual-error reduction;
they do not guarantee correctness or replace checking the underlying evidence.
```

**D060a · A类 · 推荐：最小修正**

- 决策对象：To suppress hallucination…must。
- 理由：自省不是事实错误降低的必要或充分条件，原must应最小弱化。
- 引用、表格、图注、统计或章节结论影响：可沿原句改To help reduce hallucination, agents can perform iterative self-examination. 不恢复must。
- 依据：[E21](#e21)。

**D060b · B类 · 推荐：恢复（删重复扩写）**

- 决策对象：correctness/evidence免责声明的额外尾句。
- 理由：原段末本已有critic盲点、成本与必须按failure modes评估的限制；更长新句非修must所必需。
- 引用、表格、图注、统计或章节结论影响：保留原一短句结构并用A的最小弱化替换。
- 依据：[E21](#e21)。

<a id="d061"></a>

#### D061 CoVe四步骤与Critic扩展

导师位置：f84c78b:manuscript.tex 1072–1075行。当前位置：[manuscript.tex](<C:/Users/ShenTianyu(CN-TV-T1)/schoolwork/ESWA-multiagent/manuscript.tex:1106>) 1106–1109行。

追溯：4ff0569（2026-10-08，第一阶段参考文献/归因核查）。f67f294本身没有新增manuscript.tex文字差异。

**导师原版：**

```tex
In addition, combined with Chain-of-Verification
\citep{dhuliawala2023chain_of_verification}, the system can configure
dedicated \emph{Critic} agents that rigorously audit generated results for
safety, factuality, and logical coherence through mutual-critique mechanisms.
```

**当前版本：**

```tex
Chain-of-Verification \citep{dhuliawala2023chain_of_verification} drafts an
answer, plans verification questions, answers them independently, and then
revises the original answer. This procedure targets factual errors; dedicated
critic agents are a possible multi-agent extension that requires evaluation.
```

**D061 · A类 · 推荐：保留来源限定**

- 决策对象：安全/逻辑审计被挂在CoVe下。
- 理由：原论文§3仅LLM执行四步事实核查，不验证多critic安全审核。
- 引用、表格、图注、统计或章节结论影响：保留四步骤事实；若复用原system can configure结构，必须明确这是本文可能扩展且不恢复安全保证。
- 依据：[E21](#e21)。

### 第5章 Development and evaluation resources

<a id="d062"></a>

#### D062 资源图跨栏环境开始

导师位置：f84c78b:manuscript.tex 1563行。当前位置：[manuscript.tex](<C:/Users/ShenTianyu(CN-TV-T1)/schoolwork/ESWA-multiagent/manuscript.tex:1597>) 1597行。

追溯：1233a8b（2026-10-10，CAS 双栏格式阶段）。f67f294本身没有新增manuscript.tex文字差异。

**导师原版：**

```tex
\begin{figure}[t]
```

**当前版本：**

```tex
\begin{figure*}[pos=t,width=\textwidth]
```

**D062 · A类 · 推荐：保留**

- 决策对象：figure→figure*。
- 理由：格式调整，用当前跨栏排版承载资源图。
- 引用、表格、图注、统计或章节结论影响：仅TeX环境，不还原或覆盖classify.jpg。
- 依据：[E01](#e01)。

<a id="d063"></a>

#### D063 资源图嵌入宽度

导师位置：f84c78b:manuscript.tex 1565行。当前位置：[manuscript.tex](<C:/Users/ShenTianyu(CN-TV-T1)/schoolwork/ESWA-multiagent/manuscript.tex:1599>) 1599行。

追溯：1233a8b（2026-10-10，CAS 双栏格式阶段）。f67f294本身没有新增manuscript.tex文字差异。

**导师原版：**

```tex
\includegraphics[width=\columnwidth]{classify.jpg}
```

**当前版本：**

```tex
\includegraphics[width=0.94\textwidth]{classify.jpg}
```

**D063 · A类 · 推荐：保留**

- 决策对象：columnwidth→0.94textwidth。
- 理由：与跨栏环境配套，属于已经实施的格式；不是正文润色。
- 引用、表格、图注、统计或章节结论影响：图片内容和编辑中图源保护；本轮不重新渲染。
- 依据：[E01](#e01)。

<a id="d064"></a>

#### D064 资源图跨栏环境结束

导师位置：f84c78b:manuscript.tex 1568行。当前位置：[manuscript.tex](<C:/Users/ShenTianyu(CN-TV-T1)/schoolwork/ESWA-multiagent/manuscript.tex:1602>) 1602行。

追溯：1233a8b（2026-10-10，CAS 双栏格式阶段）。f67f294本身没有新增manuscript.tex文字差异。

**导师原版：**

```tex
\end{figure}
```

**当前版本：**

```tex
\end{figure*}
```

**D064 · A类 · 推荐：保留**

- 决策对象：end figure→end figure*。
- 理由：环境配对必要。
- 引用、表格、图注、统计或章节结论影响：与D062成组。
- 依据：[E01](#e01)。

<a id="d065"></a>

#### D065 框架表跨栏入口

导师位置：f84c78b:manuscript.tex 1616–1618行。当前位置：[manuscript.tex](<C:/Users/ShenTianyu(CN-TV-T1)/schoolwork/ESWA-multiagent/manuscript.tex:1650>) 1650行。

追溯：1233a8b（2026-10-10，CAS 双栏格式阶段）。f67f294本身没有新增manuscript.tex文字差异。

**导师原版：**

```tex
\clearpage
\onecolumn
\begin{table}[t]
```

**当前版本：**

```tex
\begin{table*}[pos=t,width=\textwidth]
```

**D065 · A类 · 推荐：保留**

- 决策对象：clearpage/onecolumn/table→table*。
- 理由：消除强制单栏与额外断页，符合现有双栏工作流。
- 引用、表格、图注、统计或章节结论影响：不改变表格内容。
- 依据：[E01](#e01)。

<a id="d066"></a>

#### D066 框架表字号

导师位置：f84c78b:manuscript.tex 1623行。当前位置：[manuscript.tex](<C:/Users/ShenTianyu(CN-TV-T1)/schoolwork/ESWA-multiagent/manuscript.tex:1655>) 1655行。

追溯：1233a8b（2026-10-10，CAS 双栏格式阶段）。f67f294本身没有新增manuscript.tex文字差异。

**导师原版：**

```tex
  \normalsize
```

**当前版本：**

```tex
  \small
```

**D066 · A类 · 推荐：保留**

- 决策对象：normalsize→small。
- 理由：现有表宽排版修复的一部分；用户不恢复旧格式。
- 引用、表格、图注、统计或章节结论影响：字号作为格式保护，不与正文语言混算。
- 依据：[E01](#e01)。

<a id="d067"></a>

#### D067 框架表列宽

导师位置：f84c78b:manuscript.tex 1626–1631行。当前位置：[manuscript.tex](<C:/Users/ShenTianyu(CN-TV-T1)/schoolwork/ESWA-multiagent/manuscript.tex:1658>) 1658–1663行。

追溯：1233a8b（2026-10-10，CAS 双栏格式阶段）。f67f294本身没有新增manuscript.tex文字差异。

**导师原版：**

```tex
  \begin{tabular}{>{\raggedright\arraybackslash}p{1.8cm}
                  >{\raggedright\arraybackslash}p{1.9cm}
                  >{\raggedright\arraybackslash}p{2.8cm}
                  >{\raggedright\arraybackslash}p{2.8cm}
                  >{\raggedright\arraybackslash}p{2.8cm}
                  >{\raggedright\arraybackslash}p{3.2cm}}
```

**当前版本：**

```tex
  \begin{tabularx}{\textwidth}{>{\raggedright\arraybackslash}p{2.6cm}
                  >{\raggedright\arraybackslash}p{2.0cm}
                  >{\raggedright\arraybackslash}X
                  >{\raggedright\arraybackslash}X
                  >{\raggedright\arraybackslash}X
                  >{\raggedright\arraybackslash}X}
```

**D067 · A类 · 推荐：保留**

- 决策对象：固定宽tabular→textwidth的tabularx。
- 理由：当前可伸缩列适配跨栏，避免原表宽/溢出问题。
- 引用、表格、图注、统计或章节结论影响：保持X列与width，不改机制内容。
- 依据：[E01](#e01)。

<a id="d068"></a>

#### D068 框架表CAMEL类别

导师位置：f84c78b:manuscript.tex 1637行。当前位置：[manuscript.tex](<C:/Users/ShenTianyu(CN-TV-T1)/schoolwork/ESWA-multiagent/manuscript.tex:1669>) 1669行。

追溯：98732a2（2026-10-10，第二阶段证据与控制流重编码）。f67f294本身没有新增manuscript.tex文字差异。

**导师原版：**

```tex
    CAMEL \citep{li2023camel} & Flat &
```

**当前版本：**

```tex
    CAMEL \citep{li2023camel} & Role-paired workflow &
```

**D068 · C类 · 推荐：等待确认 Q4**

- 决策对象：Flat→Role-paired workflow。
- 理由：实际instruction-solution角色对可核；从架构列改到机制名称属表呈现方案。
- 引用、表格、图注、统计或章节结论影响：联动表 tab:9categories、框架表、十案例表及选择流程；图片仅列一致性核查，不覆盖。
- 依据：[E15](#e15)。

<a id="d069"></a>

#### D069 CAMEL上下文树

导师位置：f84c78b:manuscript.tex 1640行。当前位置：[manuscript.tex](<C:/Users/ShenTianyu(CN-TV-T1)/schoolwork/ESWA-multiagent/manuscript.tex:1672>) 1672行。

追溯：4ff0569（2026-10-08，第一阶段参考文献/归因核查）。f67f294本身没有新增manuscript.tex文字差异。

**导师原版：**

```tex
      Dialogue context tree &
```

**当前版本：**

```tex
      Role-conditioned dialogue context &
```

**D069 · A类 · 推荐：保留**

- 决策对象：Dialogue context tree→Role-conditioned dialogue context。
- 理由：已读角色对话实现是顺序instruction-solution交流，未证明采用上下文树结构；不能按树写成已报机制。
- 引用、表格、图注、统计或章节结论影响：只替换该单元，不改引用或表结构。
- 依据：[E15](#e15)。

<a id="d070"></a>

#### D070 ChatDev记忆栏

导师位置：f84c78b:manuscript.tex 1645行。当前位置：[manuscript.tex](<C:/Users/ShenTianyu(CN-TV-T1)/schoolwork/ESWA-multiagent/manuscript.tex:1677>) 1677行。

追溯：4ff0569（2026-10-08，第一阶段参考文献/归因核查）。f67f294本身没有新增manuscript.tex文字差异。

**导师原版：**

```tex
      Local code and document files &
```

**当前版本：**

```tex
      Within-phase dialogue; cross-phase solutions &
```

**D070 · A类 · 推荐：保留最小机制修正**

- 决策对象：Local code/doc files→within-phase dialogue/cross-phase solutions。
- 理由：正式论文§3.1确证短期对话及跨阶段解决方案记忆；本列是memory/state，不应以产物文件替代已描述机制。
- 引用、表格、图注、统计或章节结论影响：保留现有引用键；不改变书目池或78篇唯一引用统计。
- 依据：[E15](#e15)。

<a id="d071"></a>

#### D071 MetaGPT消息机制

导师位置：f84c78b:manuscript.tex 1650行。当前位置：[manuscript.tex](<C:/Users/ShenTianyu(CN-TV-T1)/schoolwork/ESWA-multiagent/manuscript.tex:1682>) 1682行。

追溯：4ff0569（2026-10-08，第一阶段参考文献/归因核查）。f67f294本身没有新增manuscript.tex文字差异。

**导师原版：**

```tex
      Message queue and project documents &
```

**当前版本：**

```tex
      Shared message pool and project documents &
```

**D071 · A类 · 推荐：保留**

- 决策对象：Message queue→Shared message pool。
- 理由：原文§3.2/Fig2描述全局共享消息池及订阅，不能无依据改为队列式机制。
- 引用、表格、图注、统计或章节结论影响：保留现有引用键；不改变书目池或78篇唯一引用统计。
- 依据：[E15](#e15)。

<a id="d072"></a>

#### D072 框架表AgentVerse类别

导师位置：f84c78b:manuscript.tex 1657行。当前位置：[manuscript.tex](<C:/Users/ShenTianyu(CN-TV-T1)/schoolwork/ESWA-multiagent/manuscript.tex:1689>) 1689行。

追溯：98732a2（2026-10-10，第二阶段证据与控制流重编码）。f67f294本身没有新增manuscript.tex文字差异。

**导师原版：**

```tex
    AgentVerse \citep{chen2024agentverse} & Hybrid &
```

**当前版本：**

```tex
    AgentVerse \citep{chen2024agentverse} & Adaptive role pipeline &
```

**D072 · C类 · 推荐：等待确认 Q4**

- 决策对象：Hybrid→Adaptive role pipeline。
- 理由：招募/评价反馈实证不等于必然控制权切换；表归属方案需作者判断。
- 引用、表格、图注、统计或章节结论影响：联动表 tab:9categories、框架表、十案例表及选择流程；图片仅列一致性核查，不覆盖。
- 依据：[E15](#e15)。

<a id="d073"></a>

#### D073 AgentVerse黑板

导师位置：f84c78b:manuscript.tex 1660行。当前位置：[manuscript.tex](<C:/Users/ShenTianyu(CN-TV-T1)/schoolwork/ESWA-multiagent/manuscript.tex:1692>) 1692行。

追溯：4ff0569（2026-10-08，第一阶段参考文献/归因核查）。f67f294本身没有新增manuscript.tex文字差异。

**导师原版：**

```tex
      Shared blackboard &
```

**当前版本：**

```tex
      Conversation and evaluation context &
```

**D073 · A类 · 推荐：保留最小来源边界**

- 决策对象：Shared blackboard→conversation/evaluation context。
- 理由：本次可读方法描述招募、对话、执行、反馈，未据此确认特定blackboard存储架构；保留一般上下文描述避免过具体归因。
- 引用、表格、图注、统计或章节结论影响：未能证明原blackboard错误实现不存在，只是不把未获来源支持的专门机制作为事实。
- 依据：[E15](#e15)。

<a id="d074"></a>

#### D074 框架表LangGraph来源及类别

导师位置：f84c78b:manuscript.tex 1662行。当前位置：[manuscript.tex](<C:/Users/ShenTianyu(CN-TV-T1)/schoolwork/ESWA-multiagent/manuscript.tex:1694>) 1694行。

追溯：首次 4ff0569；98732a2 继续修改（含 Triad 边界/角色决定、来源重编码或表格机制标签）。f67f294本身没有新增manuscript.tex文字差异。

**导师原版：**

```tex
    LangGraph \citep{duan2024langgraph_crewai} & Hybrid &
```

**当前版本：**

```tex
    LangGraph \citep{langgraph2024,langgraph2024interrupt} & Configurable state graph &
```

**D074a · A类 · 推荐：保留引用修复**

- 决策对象：duan2024langgraph_crewai→官方两键。
- 理由：官方文档/有日期文章支持状态图及暂停机制，修复必要。
- 引用、表格、图注、统计或章节结论影响：保留现有引用键；不改变书目池或78篇唯一引用统计。
- 依据：[E12](#e12)。

**D074b · C类 · 推荐：等待确认 Q4**

- 决策对象：Hybrid→Configurable state graph。
- 理由：框架能力与实现架构区分是必要底线，具体架构列还是机制列的展示方式待定。
- 引用、表格、图注、统计或章节结论影响：联动表 tab:9categories、框架表、十案例表及选择流程；图片仅列一致性核查，不覆盖。
- 依据：[E12](#e12)。

<a id="d075"></a>

#### D075 GPTSwarm类别与技术单元

导师位置：f84c78b:manuscript.tex 1667–1671行。当前位置：[manuscript.tex](<C:/Users/ShenTianyu(CN-TV-T1)/schoolwork/ESWA-multiagent/manuscript.tex:1699>) 1699–1703行。

追溯：首次 4ff0569；98732a2 继续修改（含 Triad 边界/角色决定、来源重编码或表格机制标签）。f67f294本身没有新增manuscript.tex文字差异。

**导师原版：**

```tex
    GPTSwarm \citep{zhuge2024gptswarm} & Hybrid &
      Computational graph connections &
      Automatic graph-structure search &
      Intra-node state &
      Parallel inference optimization \\
```

**当前版本：**

```tex
    GPTSwarm \citep{zhuge2024gptswarm} & Optimizable agent graph &
      DAG information flow &
      Prompt and edge optimization &
      Node input--output histories &
      MMLU QA; graph optimization \\
```

**D075a · C类 · 推荐：等待确认 Q4**

- 决策对象：Hybrid→Optimizable agent graph。
- 理由：图优化不自动证明运行时决策权变化，但此处如何给类别仍是作者编码选择。
- 引用、表格、图注、统计或章节结论影响：联动表 tab:9categories、框架表、十案例表及选择流程；图片仅列一致性核查，不覆盖。
- 依据：[E11](#e11)。

**D075b · A类 · 推荐：最小修正（仅应用栏）**

- 决策对象：Parallel inference optimization→MMLU QA; graph optimization 的应用定位。
- 理由：所读§3评估MMLU、crosswords、HumanEval、GAIA等及图优化，并未把任务定位为并行推理性能优化；旧应用栏不准确。
- 引用、表格、图注、统计或章节结论影响：保留真实QA/graph优化用途；不以此要求整行所有新技术词必须保留。
- 依据：[E11](#e11)。

**D075c · B类 · 推荐：恢复（局部三个单元）**

- 决策对象：Computational graph connections / Automatic graph-structure search / Intra-node state→更细的三单元表述。
- 理由：本次补读公开v1§2.2–2.4：计算图连接、连边选择优化以及每节点历史集直接支持原表较粗的机制概括；更具体的DAG、prompt/edge、IO history并不证明原词错误。
- 引用、表格、图注、统计或章节结论影响：可恢复原三单元文字；不得恢复Hybrid全框架标签或Parallel inference optimization应用定位。保留zhuge2024gptswarm键。
- 依据：[E11](#e11)。

<a id="d076"></a>

#### D076 框架表跨栏收尾

导师位置：f84c78b:manuscript.tex 1678–1681行。当前位置：[manuscript.tex](<C:/Users/ShenTianyu(CN-TV-T1)/schoolwork/ESWA-multiagent/manuscript.tex:1710>) 1710–1711行。

追溯：1233a8b（2026-10-10，CAS 双栏格式阶段）。f67f294本身没有新增manuscript.tex文字差异。

**导师原版：**

```tex
  \end{tabular}
\end{table}
\clearpage
\twocolumn
```

**当前版本：**

```tex
  \end{tabularx}
\end{table*}
```

**D076 · A类 · 推荐：保留**

- 决策对象：end tabular/table与单双栏切换→tabularx/table*。
- 理由：与D065/067配套的格式修复。
- 引用、表格、图注、统计或章节结论影响：不要只恢复环境收尾造成错配。
- 依据：[E01](#e01)。

<a id="d077"></a>

#### D077 RAGFlow选定版本能力

导师位置：f84c78b:manuscript.tex 1785行。当前位置：[manuscript.tex](<C:/Users/ShenTianyu(CN-TV-T1)/schoolwork/ESWA-multiagent/manuscript.tex:1815>) 1815行。

追溯：98732a2（2026-10-10，第二阶段证据与控制流重编码）。f67f294本身没有新增manuscript.tex文字差异。

**导师原版：**

```tex
    Document ingestion, retrieval, and configurable workflow components \\
```

**当前版本：**

```tex
    Document ingestion, retrieval, and configurable RAG components \\
```

**D077 · A类 · 推荐：保留**

- 决策对象：workflow→RAG components。
- 理由：选定v0.6.0是RAG组件；不可用后续版本多代理工作流能力倒推。
- 引用、表格、图注、统计或章节结论影响：保留软件键与版本选择；不改平台数据。
- 依据：[E18](#e18)。

<a id="d078"></a>

#### D078 基准资源表新增指路句

导师位置：f84c78b:manuscript.tex 插入/删除边界1840行。当前位置：[manuscript.tex](<C:/Users/ShenTianyu(CN-TV-T1)/schoolwork/ESWA-multiagent/manuscript.tex:1870>) 1870–1871行。

追溯：1233a8b（2026-10-10，CAS 双栏格式阶段）。f67f294本身没有新增manuscript.tex文字差异。

**导师原版：**

```tex
[此处无原文：当前新增]
```

**当前版本：**

```tex
Table~\ref{tab:benchmark_resources} summarizes these resources and their
primary evaluation roles.
```

**D078 · B类 · 推荐：恢复（删除新增句）**

- 决策对象：新增 Table summarizes…primary evaluation roles 两行。
- 理由：纯新增导航，无实质纠错；删除不删表、不造成引用键变化或未定义引用。
- 引用、表格、图注、统计或章节结论影响：tab:benchmark_resources定义和表内容保留。
- 依据：[E01](#e01)。

### 第6章 Challenges and Future Directions

<a id="d079"></a>

#### D079 Financial QA多轮反思

导师位置：f84c78b:manuscript.tex 1917行。当前位置：[manuscript.tex](<C:/Users/ShenTianyu(CN-TV-T1)/schoolwork/ESWA-multiagent/manuscript.tex:1949>) 1949行。

追溯：98732a2（2026-10-10，第二阶段证据与控制流重编码）。f67f294本身没有新增manuscript.tex文字差异。

**导师原版：**

```tex
iterative multi-critic reflection. These cases illustrate why a single
```

**当前版本：**

```tex
critic feedback and answer revision. These cases illustrate why a single
```

**D079 · A类 · 推荐：保留**

- 决策对象：iterative multi-critic reflection→critic feedback/revision。
- 理由：来源把反复multi-turn作为未来工作，不能描述成已实现机制。
- 引用、表格、图注、统计或章节结论影响：挑战章与十案例事实同步；类别仍等Q5。
- 依据：[E14](#e14)。

<a id="d080"></a>

#### D080 通信数量与成本断言

导师位置：f84c78b:manuscript.tex 1929–1931行。当前位置：[manuscript.tex](<C:/Users/ShenTianyu(CN-TV-T1)/schoolwork/ESWA-multiagent/manuscript.tex:1961>) 1961–1965行。

追溯：4ff0569（2026-10-08，第一阶段参考文献/归因核查）。f67f294本身没有新增manuscript.tex文字差异。

**导师原版：**

```tex
resolving dependencies or disagreement. In a fully connected broadcast
topology, potential pairwise messages per round grow quadratically with team
size, increasing token and latency costs without guaranteeing information gain
```

**当前版本：**

```tex
resolving dependencies or disagreement. If each of $N$ agents sends one
message to every other agent, there are $N(N-1)$ directed message deliveries
per round. Actual token and latency costs also depend on message length,
scheduling, and context handling. Scaling experiments illustrate
task-dependent benefits and topology-dependent context costs
```

**D080a · A类 · 推荐：最小修正**

- 决策对象：quadratic→必然latency/cost 的推断。
- 理由：链路数二次增长不保证端到端延迟同率，实际调度/消息长度影响成本。
- 引用、表格、图注、统计或章节结论影响：保留现有引用键；不改变书目池或78篇唯一引用统计。
- 依据：[E03](#e03)。

**D080b · B类 · 推荐：恢复（前半句骨架）**

- 决策对象：新增N(N−1)推导句及扩写。
- 理由：原potential pairwise messages grow quadratically本身正确，新增精确计数不是纠正后半句所必需。
- 引用、表格、图注、统计或章节结论影响：恢复原potential…quadratically；只在成本效果处保留条件限制。不改原论文实验结果。
- 依据：[E03](#e03)。

<a id="d081"></a>

#### D081 评估指标与过程推断

导师位置：f84c78b:manuscript.tex 1957–1962行。当前位置：[manuscript.tex](<C:/Users/ShenTianyu(CN-TV-T1)/schoolwork/ESWA-multiagent/manuscript.tex:1991>) 1991–1996行。

追溯：4ff0569（2026-10-08，第一阶段参考文献/归因核查）。f67f294本身没有新增manuscript.tex文字差异。

**导师原版：**

```tex
modes, yet they are often compared only by final-answer accuracy. Conventional
benchmarks and agent environments measure answer correctness or task
completion \citep{hendrycks2021mmlu,yang2018hotpotqa,
liu2024agentbench,mialon2024gaia}; they do not reveal whether debate added
independent evidence, whether a long-context chain lost a decisive fact, or
whether a critic detected and corrected an error. Additional reasoning rounds
```

**当前版本：**

```tex
modes. Conventional benchmarks and agent environments measure answer
correctness, supporting-fact accuracy, or task completion
\citep{hendrycks2021mmlu,yang2018hotpotqa,liu2024agentbench,mialon2024gaia};
these outcome measures alone do not establish whether debate added independent
evidence, whether a long-context chain lost a decisive fact, or whether a
critic detected and corrected an error. Additional reasoning rounds
```

**D081 · A类 · 推荐：保留最小事实纠正**

- 决策对象：只final accuracy／不揭示过程的笼统表述。
- 理由：HotpotQA含supporting-fact指标；结果指标与完整过程因果贡献应区别。不能恢复只测最终答案的共同归因。
- 引用、表格、图注、统计或章节结论影响：保留原关于独立证据、信息损失、critic纠错的三个问题及原键。
- 依据：[E20](#e20)。

<a id="d082"></a>

#### D082 process metrics not standard断言

导师位置：f84c78b:manuscript.tex 1965–1966行。当前位置：[manuscript.tex](<C:/Users/ShenTianyu(CN-TV-T1)/schoolwork/ESWA-multiagent/manuscript.tex:1999>) 1999–2000行。

追溯：4ff0569（2026-10-08，第一阶段参考文献/归因核查）。f67f294本身没有新增manuscript.tex文字差异。

**导师原版：**

```tex
\citep{han2024mast}, but process-level measures of contribution,
complementarity, and error correction are not standard in QA evaluation.
```

**当前版本：**

```tex
\citep{han2024mast}, suggesting that process-level measures of contribution,
complementarity, and error correction could complement outcome measures.
```

**D082 · A类 · 推荐：最小修正**

- 决策对象：行业普遍缺失→作者建议complement outcomes。
- 理由：MAST证据证明失败类型，不证明全QA领域过程指标都不标准化；当前建议是合理边界。
- 引用、表格、图注、统计或章节结论影响：保留现有引用键；不改变书目池或78篇唯一引用统计。
- 依据：[E20](#e20)。

<a id="d083"></a>

#### D083 人工监督与来源能力

导师位置：f84c78b:manuscript.tex 1981–1985行。当前位置：[manuscript.tex](<C:/Users/ShenTianyu(CN-TV-T1)/schoolwork/ESWA-multiagent/manuscript.tex:2015>) 2015–2021行。

追溯：4ff0569（2026-10-08，第一阶段参考文献/归因核查）。f67f294本身没有新增manuscript.tex文字差异。

**导师原版：**

```tex
appropriate to the decision. Medical and legal QA illustrate these demands
\citep{tang2024medagents,cui2023chatlaw}. Yet many workflows provide only a
textual correction or final approval \citep{duan2024langgraph_crewai,
langgraph2024}, without specifying when intervention is useful, what can be
revised, or how the intervention affects subsequent reasoning. Oversight that
```

**当前版本：**

```tex
appropriate to the decision. Medical and legal QA provide application
contexts for these proposed oversight requirements
\citep{tang2024medagents,cui2023chatlaw}. Frameworks support configurable
interaction and workflow control \citep{duan2024langgraph_crewai,
langgraph2024interrupt}. Their use still requires designers to specify when
intervention is useful, what can be revised, and how the intervention affects
subsequent reasoning. Oversight that
```

**D083 · A类 · 推荐：最小修正**

- 决策对象：医学/法律实测监督权；many workflows only finalapproval。
- 理由：医学/法律来源提供应用背景而非整套规范验证；LangGraph支持状态编辑/流程重定向，only的共同归因不成立。
- 引用、表格、图注、统计或章节结论影响：保留导师监督论证顺序及责任需求；只修共同归因、only及引用键。
- 依据：[E12](#e12)、[E14](#e14)。

<a id="d084"></a>

#### D084 综述局限措辞与无hybrid样本

导师位置：f84c78b:manuscript.tex 2136行。当前位置：[manuscript.tex](<C:/Users/ShenTianyu(CN-TV-T1)/schoolwork/ESWA-multiagent/manuscript.tex:2172>) 2172–2173行。

追溯：98732a2（2026-10-10，第二阶段证据与控制流重编码）。f67f294本身没有新增manuscript.tex文字差异。

**导师原版：**

```tex
verification exercise rather than independent confirmation of general validity; broader
```

**当前版本：**

```tex
retrospective diagnostic comparison rather than independent validation; it contains
no source-coded hybrid example. Broader
```

**D084a · B类 · 推荐：恢复（词组）**

- 决策对象：verification exercise rather than independent confirmation→retrospective diagnostic comparison…。
- 理由：导师原句已经明确不是独立一般有效性确认；是换词，不必以更稳健语言为由替换。
- 引用、表格、图注、统计或章节结论影响：保持原limited…rather than independent confirmation of general validity；不删原局限。
- 依据：[E14](#e14)。

**D084b · C类 · 推荐：等待确认 Q5**

- 决策对象：新增no source-coded hybrid example。
- 理由：按现编码确为9H/1F；该结论依赖Q5的全局编码粒度，须同步该决定。
- 引用、表格、图注、统计或章节结论影响：若保留现源标签则保留无hybrid限制；不自动新增hybrid案例。
- 依据：[E14](#e14)。

### 第7章 Conclusion之后的声明与参考文献输出

<a id="d085"></a>

#### D085 数据可用性增加当前审计文件

导师位置：f84c78b:manuscript.tex 2184行。当前位置：[manuscript.tex](<C:/Users/ShenTianyu(CN-TV-T1)/schoolwork/ESWA-multiagent/manuscript.tex:2221>) 2221–2224行。

追溯：首次 4ff0569；98732a2 继续修改（含 Triad 边界/角色决定、来源重编码或表格机制标签）。f67f294本身没有新增manuscript.tex文字差异。

**导师原版：**

```tex
\texttt{search\_log.csv}.
```

**当前版本：**

```tex
\texttt{search\_log.csv}. The current field-level and claim-level audit tables
are \texttt{reference\_field\_audit.csv} and
\texttt{citation\_claim\_audit.csv}; they record unresolved
optional publication fields, documented version selections, and evidence boundaries.
```

**D085 · A类 · 推荐：保留**

- 决策对象：新增field/claim CSV及未决边界。
- 理由：保护可追溯核查记录，避免只提交旧历史audit和search log造成已全部验证误读。
- 引用、表格、图注、统计或章节结论影响：不覆盖原台账；reference_audit_report.md中的旧BibTeX编译命令不作为当前工作流。
- 依据：[E01](#e01)。

<a id="d086"></a>

#### D086 AI声明与错误图号

导师位置：f84c78b:manuscript.tex 2190–2191行。当前位置：[manuscript.tex](<C:/Users/ShenTianyu(CN-TV-T1)/schoolwork/ESWA-multiagent/manuscript.tex:2230>) 2230–2232行。

追溯：4ff0569 删除无效图号；2026-10-13 未提交更新增加图1绘图代码/布局说明。f67f294本身没有新增manuscript.tex文字差异。

**导师原版：**

```tex
reference formatting, and used Nano Banana to generate the initial draft of
the explanatory architecture schematic in Fig.~\ref{fig:arch_tradeoffs}.
```

**当前版本：**

```tex
reference formatting, and with plotting code and layout for the data-derived
reference-corpus diagram (Fig.~\ref{fig:reference_corpus}), and used Nano Banana to generate the initial draft of
an explanatory architecture schematic during drafting.
```

**D086 · A类 · 推荐：保留（保护工作区声明）**

- 决策对象：删除不存在的fig:arch_tradeoffs引用；新增图1代码/布局帮助。
- 理由：原图标签不在有效正文，不能复活未定义引用；当前图1生成记录对应代码/布局帮助，必须保持声明与实际素材来源一致。
- 引用、表格、图注、统计或章节结论影响：不恢复旧不存在图号；保护图1和图2文件；不据此认可其他图片生成政策或完成投稿审查。
- 依据：[E01](#e01)、[E22](#e22)。

<a id="d087"></a>

#### D087 参考文献输出

导师位置：f84c78b:manuscript.tex 2198–2199行。当前位置：[manuscript.tex](<C:/Users/ShenTianyu(CN-TV-T1)/schoolwork/ESWA-multiagent/manuscript.tex:2239>) 2239行。

追溯：6679e5a（2026-10-11，APA7/Biber 迁移）。f67f294本身没有新增manuscript.tex文字差异。

**导师原版：**

```tex
\bibliographystyle{cas-model2-names}
\bibliography{references}
```

**当前版本：**

```tex
\printbibliography
```

**D087 · A类 · 推荐：保留**

- 决策对象：bibliographystyle/bibliography→printbibliography。
- 理由：APA7/Biber必要输出配置。
- 引用、表格、图注、统计或章节结论影响：不恢复cas-model2-names/BibTeX输出。
- 依据：[E01](#e01)。

## 来源证据索引与可追溯限制

下述主来源链接定位事实；官方网页与同机构PDF不是独立双源。已读原文快照、当前在线核读和仅沿用历史正式证据分开标明。不以来源可访问或字段真实替代正文论断支持。

<a id="e01"></a>

### E01 实际Git、有效正文与统计

本次git show f84c78b:manuscript.tex、git diff f84c78b HEAD、git diff HEAD及4ff0569/98732a2/1233a8b/6679e5a逐提交差异；只读active_tex.scan_manuscript、balanced_entries与实际bib键过滤CSV。统计不是旧台账哈希代替计算。格式类根据真实TeX环境和用户明确保留当前工作流的指令分类，未以本次视觉编译声称排版全面合格。参考：[eswa-apa-config.tex](<C:/Users/ShenTianyu(CN-TV-T1)/schoolwork/ESWA-multiagent/eswa-apa-config.tex>)、[eswa-apa-sourcemap.tex](<C:/Users/ShenTianyu(CN-TV-T1)/schoolwork/ESWA-multiagent/eswa-apa-sourcemap.tex>)、[search_log.csv](<C:/Users/ShenTianyu(CN-TV-T1)/schoolwork/ESWA-multiagent/search_log.csv>)、[literature_audit.csv](<C:/Users/ShenTianyu(CN-TV-T1)/schoolwork/ESWA-multiagent/literature_audit.csv>)。旧reference_audit_report.md中的BibTeX命令是迁移前记录，不应拿来指导阶段二。

<a id="e02"></a>

### E02 Triad核心14→13的充分证据

[Triad正式全文](https://aclanthology.org/2024.emnlp-main.101.pdf)与[官方条目](https://aclanthology.org/2024.emnlp-main.101/)，§1及§3，印刷1699–1702页；本次读仓库全文文本快照第2–3页并在线核对官方摘要。作者将系统定义为一个LLM-based agent承担generalist/decision-maker/advisor三角色，任务为KBQA。对照导师原第3条至少两个智能体，移出I有直接依据；不是因名称Triad推断三个独立代理。原14与现13池内键集合比较仅相差hu2024triad。

<a id="e03"></a>

### E03 13项核心与多任务边界

本次读取[audit_work/core_eligibility_audit.md](<C:/Users/ShenTianyu(CN-TV-T1)/schoolwork/ESWA-multiagent/audit_work/core_eligibility_audit.md>)及JSON，并核读本地正式原文文本快照：Du、Qian、Liang、Xiong、LONGAGENT、MDAgents、MedAgents、LegalGraphRAG、ReConcile、Chain-of-Agents、CoCoA；LLM-MedQA和Financial以公开v1方法补核。核心名单为du2024multiagent_debate、qian2024scaling_multiagent、liang2024divergent_debate、xiong2023inter_consistency、zhao2024longagent、kim2024mdagents、tang2024medagents、tang2025llmmedqa、legalgraphrag2026、fatemi2024financialqa、chen2024reconcile、zhang2024chain_agents、jiang2026cocoa。Qian正式§3/Table1有MMLU与其他三轨道；Liang§2–3同时算术与翻译；CoA§3/Algorithm1和§4/Table1为worker→manager且评估QA及其他任务。来源证明这些任务存在，不替作者决定纳入标准的解释。[Qian正式论文](https://proceedings.iclr.cc/paper_files/paper/2025/file/66a026c0d17040889b50f0dfa650e5e0-Paper-Conference.pdf)、[Liang正式论文](https://aclanthology.org/2024.emnlp-main.992.pdf)、[CoA正式论文](https://proceedings.neurips.cc/paper_files/paper/2024/file/ee71a4b14ec26710b39ee6be113d7750-Paper-Conference.pdf)。

<a id="e04"></a>

### E04 能力、修辞与新增评估限制

本次核读[GPT-3官方摘要](https://proceedings.neurips.cc/paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html)和[GPT-4选定v6记录](https://arxiv.org/abs/2303.08774v6)。二者支持广泛语言/QA能力及局限，但不证明不能覆盖所有领域。D004/D057的修辞恢复是本次保守编辑判断，不是假称来源客观量化了extraordinary或新时代。原文已存在不少may/can与任务评估限制，应区分修辞、设计目标和新定量研究断言。

<a id="e05"></a>

### E05 综述前作范围与缺口不能由台账代裁

[Tran全文](https://arxiv.org/html/2501.06322v1)，本次核读§4.3–4.5与§5.2：通信、集中/分散/层级组织、静态/动态编排及QA/NLG均有涉及。Guo官方IJCAI摘要和现有登记也涵盖profiling/communication/skill与benchmark；这能约束前作范围概括，不能直接证明导师所称QA治理和架构选择多维整合缺口已经不存在。[Guo官方论文](https://www.ijcai.org/proceedings/2024/0890.pdf)。

<a id="e06"></a>

### E06 模型里程碑与开放范围

[Transformer官方记录](https://papers.nips.cc/paper/7181-attention-is-all-you-need)、[BERT官方摘要](https://aclanthology.org/N19-1423/)、[LLaMA初代记录](https://arxiv.org/abs/2302.13971)、[ChatGLM报告](https://arxiv.org/abs/2406.12793)。本次核对BERT双向预训练/微调、LLaMA向研究社区释放权重以及ChatGLM家族范围；Transformer既有self-attention不是本文最早发明的概念，attention-only序列架构才是这里的关键创新。需要保持修正范围最小，不将开放权重与全部无限制开源混同。

<a id="e07"></a>

### E07 Park的真正证据对象

本次核读[Generative Agents官方摘要](https://arxiv.org/abs/2304.03442)：25个社交模拟代理及记忆、反思、规划。该来源直接支持社会行为模拟，不直接验证QA专业任务调度；原版任务分解思想可作为本文分析或邻近已有MetaGPT来源所证，不必改掉整段论证。

<a id="e08"></a>

### E08 Du提供任务内self-reflection对照

本次核读[audit_work/stage2_sources/du2024multiagent_debate__formal_pmlr_pdf_text.json](<C:/Users/ShenTianyu(CN-TV-T1)/schoolwork/ESWA-multiagent/audit_work/stage2_sources/du2024multiagent_debate__formal_pmlr_pdf_text.json>)第4–6物理页，Table1–2含Single Agent (Reflection)与Multiagent (Debate)任务内结果；§2.1–2.2为对等模型交换、相同更新过程，末轮不一致采用多数票。[正式ICML条目](https://proceedings.mlr.press/v235/du24e.html)、[正式PDF](https://raw.githubusercontent.com/mlresearch/v235/main/assets/du24e/du24e.pdf)。这支持导师can/may的可能性表述；不支持把所有模型任务都说成普遍优于自我修正。Du的架构标签仍是本文作者编码。

<a id="e09"></a>

### E09 Xiong一致性与能力不平衡

本次读[audit_work/stage2_sources/xiong2023inter_consistency__pdf_text.json](<C:/Users/ShenTianyu(CN-TV-T1)/schoolwork/ESWA-multiagent/audit_work/stage2_sources/xiong2023inter_consistency__pdf_text.json>)第2–3页；[正式全文](https://aclanthology.org/2023.findings-emnlp.508.pdf)§2.1、§3/FORD和主要发现描述能力匹配与失衡、强弱模型让步/主导、judge流程。应修具体来源概括，避免把其他debate机制混用。

<a id="e10"></a>

### E10 CoCoA-zero与单模型蒸馏

本次读[audit_work/stage2_sources/jiang2026cocoa__pdf_text.json](<C:/Users/ShenTianyu(CN-TV-T1)/schoolwork/ESWA-multiagent/audit_work/stage2_sources/jiang2026cocoa__pdf_text.json>)第3–4页；[正式全文](https://aclanthology.org/2026.acl-long.167.pdf)§3.2/Algorithm1与§3.3。两类knowledge-induction agents加decision agent组成CoCoA-zero；后续监督/蒸馏使CoCoA成为单模型。13项核心中的多代理证据须指向前者。

<a id="e11"></a>

### E11 GPTSwarm图优化不等于全自动架构选择

[GPTSwarm官方摘要](https://proceedings.mlr.press/v235/zhuge24a.html)与本次补读的[公开v1方法全文](https://arxiv.org/html/2402.16823v1)，§2.2–2.4/Algorithms1–3：DAG执行、连边选择优化、节点prompt优化与每节点input/output历史集；§3评估包含MMLU。原表Computational graph connections、Automatic graph-structure search与Intra-node state是较粗但可成立的概括，因此D075c列B，建议局部恢复。Hybrid标签仍由Q4裁定；Parallel inference optimization不是这里的已报应用定位，D075b仅保留该用途纠正。正式PDF直接读取本次失败，未声称v1与正式版每个细节已重新核对；现证据足以反对把所有旧技术词机械认定为错误。

<a id="e12"></a>

### E12 LangGraph旧breakpoints与新interrupt均真实

本次核读[2024-12-14官方文章](https://www.langchain.com/blog/making-it-easier-to-build-human-in-the-loop-agents-with-interrupt)，How we built…和interrupt段：checkpoint、暂停/编辑/恢复，明确此前已有breakpoints和NodeInterrupt；Common workflows还支持状态编辑与tool-call review。因此D027/D039引用修复保留，但原breakpoint词并非错误。HITL功能本身不实测QA安全收益，也不必然是hybrid架构。

<a id="e13"></a>

### E13 MDAgentsmoderator与团队路线

本次读[audit_work/stage2_sources/kim2024mdagents__pdf_text.json](<C:/Users/ShenTianyu(CN-TV-T1)/schoolwork/ESWA-multiagent/audit_work/stage2_sources/kim2024mdagents__pdf_text.json>)物理4–5页，§3.1–3.4/Algorithm1：moderator评估复杂度并监督决策、recruiter招募、solo/MDT/ICT路径。正式来源：[audit_work/core_eligibility_audit.md](<C:/Users/ShenTianyu(CN-TV-T1)/schoolwork/ESWA-multiagent/audit_work/core_eligibility_audit.md>)中NeurIPS2024官方PDF定位；[官方论文页](https://proceedings.neurips.cc/paper_files/paper/2024/hash/90d1fc07f46e31387978b88e7e057a31-Abstract-Conference.html)。固定moderator事实获支持，是否整体hybrid需明确分类粒度。

<a id="e14"></a>

### E14 十案例事实、评分与版本边界

本次对照[audit_work/case_classification_audit.json](<C:/Users/ShenTianyu(CN-TV-T1)/schoolwork/ESWA-multiagent/audit_work/case_classification_audit.json>)、两版表格实际行/符号，按旧三档和新二档分别复算；两版建议标签均未改。MedAgents本次读[正式§2/Algorithm1](https://aclanthology.org/2024.findings-acl.33.pdf)，LegalGraphRAG读仓库正式文本§4.3；LLM-MedQA核读[v1 §III-E/F](https://arxiv.org/html/2501.05464v1)，EduPlanner核读[v1 §III-C–E/Algorithms1–3](https://arxiv.org/html/2504.05370v1)，Financial核读[v1 §3.1及§6](https://arxiv.org/html/2410.21741v1)。各自固定阶段、投票/反馈与最终决定是事实；F/H/Hybrid及匹配是本文解释。Financial§6明确把反复multi-turn作为未来工作。LLM-MedQA、EduPlanner、Financial正式用户PDF本轮不可访问；保留旧正式页码定位，不能冒充本次再次核读。LONGAGENT leader、ChatDev有序ChatChain与AgentCoder脚本executor的本地全文快照亦核读。

<a id="e15"></a>

### E15 框架角色、记忆与控制来源

本次核读[CAMEL v2 §3](https://arxiv.org/html/2303.17760v2)的instruction-solution角色对，[MetaGPT v7 §3.1–3.2/Fig2](https://arxiv.org/html/2308.00352v7)共享message pool与订阅，[AgentVerse正式§2.1/§2.4](https://proceedings.iclr.cc/paper_files/paper/2024/file/578e65cdee35d00c708d4c64bce32971-Paper-Conference.pdf)按目标招募和反馈，[AutoGen v2 §2.2/§3 A5](https://arxiv.org/html/2308.08155v2)可编程会话及GroupChatManager选speaker/广播。ChatDev正式§3.1物理4页的本地快照说明阶段内对话与跨阶段solutions；[AgentCoder v1 §3.3–3.4](https://arxiv.org/pdf/2312.13010v1)本地快照说明executor为脚本。框架一般能力不等于每个应用固定架构；CAMEL context tree与AgentVerse blackboard在本次所读方法中没有得到对应具体结构的支持，负证据不等于证明任何实现绝不可能使用它们。

<a id="e16"></a>

### E16 MCP与A2A公告范围

本次读[Anthropic 2024-11-25公告](https://www.anthropic.com/news/model-context-protocol)的工具/数据接口说明及[Google 2025-04-09 A2A公告](https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/)的跨框架、发现、任务委托、消息/状态沟通。它们不把所有参与agent规定为平等最终决策者。Linux Foundation后续采用历史和USB-C外号不由这两个所选公告直接证明，不能为恢复原段而补造新证据。原互操作障碍叙述可恢复。

<a id="e17"></a>

### E17 Plan-and-Solve的实测对象

本次核读[正式全文](https://aclanthology.org/2023.acl-long.147.pdf)§4.5/Table6，印刷2615页，错误分类包括calculation/missing/semantic；评估中的missing-step错误改善有直接依据，通用分解可靠性结论更强。最小修效果范围，无需扩充算法观点。

<a id="e18"></a>

### E18 记忆、RAG检索与版本边界

本次读MemGPT与Self-RAG本地正式全文文本，FLARE[正式摘要及§3.2](https://aclanthology.org/2023.emnlp-main.495.pdf)：预测将生成句，低置信触发检索再生成。[Self-RAG正式全文](https://proceedings.iclr.cc/paper_files/paper/2024/file/25f7be9694d7b32d5cc670927b8091e1-Paper-Conference.pdf)§3/Algorithm1为reflection-token控制；不是默认几个专门agent。记忆综述正式PDF本轮不可读，仅旧定位及登记摘要，不用于重新声称读过§5.2.1；通用外存而非唯一向量库可由MemGPT不同搜索存储实现补强。RAGFlow选定版本的仓库readme与发布快照在[audit_work/stage2_sources/ragflow_readme.txt](<C:/Users/ShenTianyu(CN-TV-T1)/schoolwork/ESWA-multiagent/audit_work/stage2_sources/ragflow_readme.txt>)、[audit_work/stage2_sources/ragflow_release_html.txt](<C:/Users/ShenTianyu(CN-TV-T1)/schoolwork/ESWA-multiagent/audit_work/stage2_sources/ragflow_release_html.txt>)；不以后期能力解释v0.6.0。共享知识图谱/实时同步的必要性与效果保证在原段没有直接引用支持，未发现可据以恢复的实验数据。

<a id="e19"></a>

### E19 MemGPT函数管理与FIFO

本次直接核读[audit_work/stage2_sources/packer2023memgpt__pdf_text.json](<C:/Users/ShenTianyu(CN-TV-T1)/schoolwork/ESWA-multiagent/audit_work/stage2_sources/packer2023memgpt__pdf_text.json>)物理3–4页；[选定v1](https://arxiv.org/pdf/2310.08560v1)§2.1–2.2明确main/external context、function calls、FIFO与递归总结，并非按attention-weight淘汰。保留此确定机制纠错。

<a id="e20"></a>

### E20 MAST、HotpotQA与评价边界

本次核读[MAST正式摘要](https://proceedings.neurips.cc/paper_files/paper/2025/hash/b1041e52d3be19f0a9bc491657488e4a-Abstract-Datasets_and_Benchmarks_Track.html)与[HotpotQA官方条目](https://aclanthology.org/D18-1259/)。MAST给出系统设计、代理对齐、任务验证失败类别，不实测本文通用收益抵消成本门槛；HotpotQA含supporting-fact监督与评估，不只最终答对。前者不证明全行业process指标均未标准化，后者也不等于完整协作贡献因果追踪。

<a id="e21"></a>

### E21 CoT、Self-Consistency、ToT/GoT、CoVe

Self-Consistency本次核读[官方ICLR摘要](https://iclr.cc/virtual/2023/poster/11718)为单模型多路径解码；ToT核读[正式§3](https://proceedings.neurips.cc/paper_files/paper/2023/file/271db9922b8d1f4dd7aaef84ed5ac703-Paper-Conference.pdf)thought states/BFS/DFS；CoVe核读[正式§3](https://aclanthology.org/2024.findings-acl.212.pdf)四步、独立回答验证问题，原实现各步使用LLM，并不验证多critic安全审核。GoT thought图结构以及CoT arithmetic/commonsense/symbolic效果已有主来源台账定位，保留其机制与数值，不把thought当agent。D057恢复的是导师定性效果表达，D060只把必要条件must收窄，不扩充新保证。

<a id="e22"></a>

### E22 图1当前未提交素材与AI声明

本次读[figure1_audit/README.md](<C:/Users/ShenTianyu(CN-TV-T1)/schoolwork/ESWA-multiagent/figure1_audit/README.md>)、[figure1_audit/acceptance.json](<C:/Users/ShenTianyu(CN-TV-T1)/schoolwork/ESWA-multiagent/figure1_audit/acceptance.json>)及当前图1生成脚本的Git改动范围。当前图只表示85/78/7及13/15/42/8引用来源角色，历史筛选支路已删除；声明图1代码/布局帮助对应当前工作记录。图2可编辑输出及其他图片只保护，不用这些记录声称本次新做全文PDF视觉验收。

## 完整C类项目索引

| 项目 | 待定内容 | 对应决定 |
|---|---|---|
| [D007](#d007) | QA系统性综述缺口段落被改为 builds on… | 等待确认 Q1 |
| [D009b](#d009) | 由作者执行过程改为 historical audit log records | 等待确认 Q3 |
| [D010a](#d010) | 删除查询组合、数据库与实际检索动作陈述 | 等待确认 Q3 |
| [D012](#d012) | 第4条纳入标准的解释范围 | 等待确认 Q2 |
| [D013b](#d013) | QA need not be their sole task 的纳入解释 | 等待确认 Q2 |
| [D022](#d022) | 新增 role pair has asymmetric instructions…not establish flat | 等待确认 Q4 |
| [D024b](#d024) | 新增 graph/edge/routing 不足证明hybrid的整句 | 等待确认 Q4 |
| [D026b](#d026) | persistent moderator…insufficient to prove hybrid authority | 等待确认 Q4 |
| [D028](#d028) | heterogeneous/combine deliberation/review→peer与central authority转换 | 等待确认 Q4 |
| [D029](#d029) | 三类与子范式→控制模式与机制混列表 | 等待确认 Q4 |
| [D030](#d030) | architecture classes→control patterns and related mechanisms | 等待确认 Q4 |
| [D031](#d031) | Flat分组三行→仅Du一行 | 等待确认 Q4 |
| [D032b](#d032) | CAMEL行标签Role-paired | 等待确认 Q4 |
| [D033](#d033) | Flat分组→Configurable | 等待确认 Q4 |
| [D036](#d036) | 图/自适应/HITL从Hybrid分组撤出 | 等待确认 Q4 |
| [D041](#d041) | changing requirements/conditional review→actual authority change | 等待确认 Q4 |
| [D042](#d042) | verified purposive comparison→冻结建议标签并按一规则重编码 | 等待确认 Q5 |
| [D043](#d043) | 匹配数、粒度、多标签建议结论 | 等待确认 Q5 |
| [D045a](#d045) | MedAgents source Hybrid→Hierarchical、△→× | 等待确认 Q5 |
| [D045b](#d045) | LLM-MedQA source Hybrid→Hierarchical、△→× | 等待确认 Q5 |
| [D045c](#d045) | LegalGraphRAG source Hybrid→Hierarchical、✓→× | 等待确认 Q5 |
| [D046b](#d046) | Flat/Flat 的△→✓ | 等待确认 Q5 |
| [D047b](#d047) | Hierarchical/Hybrid ×→Hierarchical/Hierarchical ✓ | 等待确认 Q5 |
| [D048a](#d048) | 三档→二档；冻结建议标签等方法说明 | 等待确认 Q5 |
| [D049a](#d049) | parallel specialist + approval Hybrid→Hierarchical／actual authoritychange | 等待确认 Q4 |
| [D068](#d068) | Flat→Role-paired workflow | 等待确认 Q4 |
| [D072](#d072) | Hybrid→Adaptive role pipeline | 等待确认 Q4 |
| [D074b](#d074) | Hybrid→Configurable state graph | 等待确认 Q4 |
| [D075a](#d075) | Hybrid→Optimizable agent graph | 等待确认 Q4 |
| [D084b](#d084) | 新增no source-coded hybrid example | 等待确认 Q5 |

## 经确认后阶段二的限定执行与验收门槛

本报告不是修改授权，也不是已执行before/after记录。作者可以按B项ID批准/排除，并分别给出Q1–Q5方案。未获明确确认前不建立恢复分支，不触碰正文。

确认后仅在独立工作分支对批准项最小化编辑manuscript.tex；保持用户现有未提交图表/脚本修改。不把当前整个工作区提交到该分支，不对图片或归档章节执行覆盖。若批准方案需要补读来源或重新判定方法，先完成对应证据再形成局部补丁，不预填新统计。

验收应覆盖：

1. 逐项before/after对应本报告ID；未批准段落逐字保护，禁止附带润色。
2. 全部有效引用键、交叉引用及隐藏块保护。唯一引用78、池85、核心13、池角色13/17/46/9和引用角色13/15/42/8不得被意外改动；引用命令/出现次数允许的任何变化须逐项解释，不静默继承136/180验收。
3. 十案例标签、匹配符号、总数、表注、局限和相关选择建议按Q4/Q5所选方案一致；不把源编码当作者自报类别。
4. 保留APA7配置、sourcemap及Biber，完整pdfLaTeX→Biber→pdfLaTeX→pdfLaTeX；不采用旧reference_audit_report.md里的BibTeX流程。
5. 当前输入绑定的PDF与日志，再检查双栏、图表宽度/分页、引图图注、引用、参考文献样式。图1最新独立图验收不能代替全文验收；图1/图2文件不覆盖。
6. 不自动提交、推送、合并；结果交作者确认。

## 阶段一最终范围声明

本次完成后的只读验收：323个原有跟踪文件的逐文件SHA-256集合与审查保护快照一致；集合摘要为6edcb581d656e9b54712bc85df4f7d3b69eb607443d7f3a86ecd7483da5a4d6c。manuscript.tex原始字节哈希仍为3acc39b05e660d1517dada3b59c316b2a1b84a38beffea1b132a9a81bfb02115。

报告87块的174段原文/现文摘录与真实源文件逐字匹配；决策标记及两个优先索引复算为A64/B25/C30，合计119项。当前有效源码扫描未发现缺失引用键或未定义的ref/eqref/autoref标签；85/78、136命令、180次键出现保持。上述是源码与保护检查，不是新编译PDF验收。

审查实际覆盖所有D001–D087有效源差异及混合块的119个决策项；B25/A64/C30，C归并五组选择。没有恢复旧英文，没有变更任何研究结果、角色、引用、编译配置、图像或归档章节。

已核实事实和必要引用纠正得到保护；新增作者解释、架构宏观类别、历史方法是否实施和匹配评价规则分别标明。**阶段一到此停止，等待明确确认。**
