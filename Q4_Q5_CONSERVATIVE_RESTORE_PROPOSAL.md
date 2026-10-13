# Q4架构比较表与Q5三档评分：待确认具体方案

日期：2026-10-13。**仅为方案与重评分建议；尚未实施阶段二。**

## 建议结论

- Q4采用**一个比较表、两个展示区**：主区比较Flat、Hierarchical、Hybrid三类；附区容纳导师原有机制与框架例子，不把它们列成新增架构类。正文小节顺序及论证主线保持导师版。
- Q5采用下文“整体控制类别＋局部机制相容性”的统一三档规则。逐例计算建议为 **6广泛一致、2部分一致、2不一致**；整体源流程编码仍为 **9 Hierarchical、1 Flat、0 Hybrid**。
- 6/2/2是本次待批准的作者分析建议。它不是原论文报告的统计、独立验证结果或选择策略准确率。
- A64项保护成果维持，B25项按已同意的最小恢复原则处理；Q1恢复导师缺口导语，Q2恢复primary evaluated task并最小澄清，Q3保留日志级叙述。现在不改正文、图像、书目、配置或旧审计记录。

## 本轮输入与授权边界

基线f84c78b2720bd5cad8fa32eeb7eaa3a510a8263d；当前分支codex/eswa-apa7-migration，HEAD f67f29499dd54822305576d2230ce5154f8dedb3。工作区未提交项与阶段一相同：manuscript.tex、图1 PDF/PNG/SVG和生成脚本；figure1_audit/、figure1_source_data.csv、output/、tools/verify_figure1_revision.py仍保留。[MENTOR_BASELINE_RESTORE_PLAN.md](<C:/Users/ShenTianyu(CN-TV-T1)/schoolwork/ESWA-multiagent/MENTOR_BASELINE_RESTORE_PLAN.md>)也不改写。

当前manuscript.tex字节SHA-256仍为3acc39b05e660d1517dada3b59c316b2a1b84a38beffea1b132a9a81bfb02115。本轮保护集合包含471个现有文件，覆盖所有原跟踪文件、阶段一报告及现有图1审计/可编辑图输出；集合摘要4e3be0d9d103cfb5d7b6d1ed4dcb6163c6131fc019a3d6d5aefbe2c45e685110。

这次只新增本方案文件；不建立分支、不切换或重置工作区、不执行编译、不重写旧台账、不提交/推送/合并。正式实施还需你最终确认Q4结构、Q5判据及其6/2/2建议。

## 已接收的Q1–Q3决定

| 决定 | 后续局部操作 | 保护限制 |
|---|---|---|
| Q1选项1 | 恢复导师Although…与QA特定整合缺口导语的句序，保留原remains limited定位 | 已有综述覆盖通信/协作/编排/QA的范围必须承认；不新增first/novel首创性声明；五项贡献条目保留 |
| Q2倾向选项2 | 恢复as the primary evaluated task | 主要任务允许并列QA主评估方向；不能只有偶然演示；13核心与Triad为S不改、不重筛 |
| Q3选项2 | 保留historical log/working records语义 | 不恢复未独立重建的检索动作或全面metadata verification承诺；历史108等不作为当前池筛选流程 |

Q2最小澄清草案：原第4条恢复primary evaluated task，其后只保留一句：**“QA may be a co-primary evaluated task, but incidental QA demonstrations are insufficient.”** 这只是澄清已批准的纳入解释，不改变13项核心名单。

## Q4：架构比较表结构草案

### 1. 保留与必要调整

导师章节中Flat→Hierarchical→Hybrid的顺序、总定义、原八个机制主题和“控制—适用任务—局限”的比较意图均保留。没有新增第四种架构类。实际导师表为八个机制行，尽管历史标签叫tab:9categories；不为凑九行新增观点，也不改这个引用标签。

建议仍使用原六列和同一table*浮动体：

1. Architecture
2. Sub-paradigm / mechanism
3. Representative systems / evidence
4. Coordination and control
5. Suitable contexts
6. Limitations

表内增加两个区标题，不新增独立表号：
- **Architecture classes**：三类总比较。
- **Related mechanisms and implementation resources**：具体机制；Architecture列为“—”，不填Role-paired、Configurable或Cross-cutting作为类别。

将原Hierarchical的manager--executor与staged evidence两行合并呈现，恢复一条明确的Hybrid类别行，再把五条机制行放入附区。合计仍为八个数据行。这个表内位置调整用于避免错误归类；正文原有段落位置与论证顺序不动。

### 2. 主区三类比较（内容草案）

| Architecture | Sub-paradigm / mechanism | Representative systems / evidence | Coordination and control | Suitable contexts | Limitations |
|---|---|---|---|---|---|
| Flat | Multi-agent debate | Du et al.; du2024multiagent_debate | Peer critique and aggregation; no persistent top-down controller | Tasks needing competing factual or reasoning views | Coordination cost and aggregation sensitivity |
| Hierarchical | Manager--executor; staged evidence-processing pipeline | MetaGPT; LONGAGENT; Chain-of-Agents; CoCoA-zero | Fixed planning, routing or synthesis authority; explicit sequencing over distributed evidence | Structured engineering workflows; long-document or knowledge-intensive QA | Planner bottleneck, error propagation and information loss at synthesis |
| Hybrid | Changes in decision authority across stages or decision states | Conditional design pattern; no hybrid case under the present ten-case source coding | A documented change between peer control and asymmetric decision authority | Heterogeneous requirements that call for changing control configurations | Routing, state-transition and cross-mode coordination costs require evaluation |

Hybrid一行概括的是导师已有定义及现有局限，不是假称补入一篇已实测Hybrid论文。“no hybrid case”仅限本十案例、现有宏观源编码，不称整个文献池无Hybrid。

### 3. 附区机制例子（内容草案）

本区Architecture列全部为“—”；下表为便于阅读省略该空列。

| Sub-paradigm / mechanism | Representative systems / evidence | Coordination and control | Suitable contexts | Limitations |
|---|---|---|---|---|
| Role-conditioned collaboration | CAMEL; li2023camel | Personas structure interaction; AI User and AI Assistant have asymmetric instructions | Exploratory collaboration and prompt-role studies | Role playing alone does not establish flat control or QA gains |
| Group-chat collaboration | AutoGen; wu2024autogen | Developer-defined conversations and speaker selection | Applications requiring configurable conversations | Architecture depends on the specific configuration |
| Graph-structured agent networks | GPTSwarm; LangGraph; zhuge2024gptswarm, langgraph2024 | GPTSwarm DAG connection optimisation; LangGraph loops and conditional routing | Workflows with conditional state transitions | Graph structure or edge optimisation alone does not establish hybrid authority |
| Adaptive collaboration-mode switching | MDAgents; kim2024mdagents | Moderator routes solo, multidisciplinary-team or integrated-care-team consultation by complexity | Tasks with heterogeneous requirements | Changing team composition alone does not establish a change in decision authority |
| Human-in-the-loop design pattern | LangGraph breakpoints; langgraph2024interrupt | Human review at defined decision points | High-risk workflows requiring accountability | A fixed approver remains hierarchical; comparative QA safety evidence is limited |

拟题名在导师原caption上最小增补：
**“Comparison of multi-agent collaborative QA architecture classes and related mechanisms.”**

拟表注只写必要边界：
**“Architecture classes refer to decision authority in a specified implementation. The related mechanisms do not by themselves establish a flat or hybrid architecture. A hybrid label requires a change in decision authority.”**

上述英文是表结构草案，并未替换正文；最终单元应优先复用导师及已核实当前短语，不再自由润色。

### 4. 与导师表相比哪些恢复、哪些保护

| 对象 | 恢复部分 | 必须保留的纠正 |
|---|---|---|
| 三类比较 | 明确Flat/Hierarchical/Hybrid主区、原比较目的与章节顺序 | 类别只用于指定实现的控制权；工具/机制不被当类别 |
| CAMEL/AutoGen | 原role-conditioned/group-chat主题、对应引用键与应用语境 | 不恢复整个CAMEL=Flat或AutoGen所有配置=Flat |
| LONGAGENT/CoA/CoCoA | 层级时序/综合的原论述 | 表内staged evidence-processing名称与CoCoA-zero对象；不把三者统一当实际plan–retrieve–generate实现 |
| 图结构 | 原graph主题与现有例子 | GPTSwarm DAG优化与LangGraph循环/分支分开；图不是Hybrid证据 |
| MDAgents | 原adaptive主题与原state/performance尾句 | moderator、solo/MDT/ICT真实路径；团队变化不等于权力变化 |
| HITL | 原defined breakpoints表达 | 现langgraph2024interrupt补证键；固定人工审批不自动Hybrid |
| 表格TeX | 原六列意图、同一标签/双栏浮动环境 | 不恢复越界multirow、onecolumn、旧BibTeX命令 |

角色对话、group chat、图网络等段落仍处于导师原小节位置，但邻近一句限定其为相关机制，避免章内位置被读成对整个框架的类别认定。既有条件分析和来源归因修复优先使用短句，不搬动整段。

### 5. 框架技术表的同步处理

[manuscript.tex](<C:/Users/ShenTianyu(CN-TV-T1)/schoolwork/ESWA-multiagent/manuscript.tex:1653>)的tab:framework_compare保留八行。CAMEL的Role-paired workflow、AutoGen的Configurable、AgentVerse的Adaptive role pipeline、LangGraph的Configurable state graph、GPTSwarm的Optimizable agent graph继续描述实现组织或能力，不恢复全框架固定Flat/Hybrid。

仅将当前Architecture列表头/对应导语最小明确为**“Control / organisation”**，不把这几个描述词宣称为新分类体系。B项D075c恢复GPTSwarm原计算图、连接搜索、节点内部状态三个单元；A项保留真实MMLU/graph optimisation用途，不能恢复Parallel inference optimization应用归因。ChatDev、MetaGPT的已核记忆/消息机制保持。

## Q5：三档评分规则 v1（待作者批准）

### 1. 比较对象固定

- 对象是原十案例，原建议类别P与criterion profile冻结；不借重评分修改建议标签或重新运行选择方法。
- 整体类别S按导师现有决策权定义，针对论文所报具体工作流编码。保留当前9H/1F/0Hybrid宏观判断；不因部分一致把MedAgents、LLM-MedQA改成Flat或Hybrid。
- 比较维度限定为**建议控制组织与来源所报组织的解释性相容程度**。不是任务准确率、风险水平验证、临床部署安全或四个选择标准全部被实测证明。
- 每例分别记录P、S、局部机制与控制冲突、来源版本及定位。类别与评分均是本文作者分析，不是原论文自报标签。

### 2. 三档互斥、按顺序判定

| 档次 | 明确判据 | 不能作为该档理由 |
|---|---|---|
| 广泛一致（✓） | 资料充分；P=S，来源流程不违背该类别核心控制特征 | 不要求每种交互/反馈完全相同；不把“广泛”解释为所有性能/治理指标均一致 |
| 部分一致（△） | 资料充分；P≠S，但存在**有来源定位的实质性局部组织机制**，满足下列L_P，并明确指出整体控制冲突 | 有多个角色、迭代、投票、图或HITL的表面相似均不足；不能用来源信息不够来凑部分一致 |
| 不一致（×） | 资料充分；P≠S，且没有得到L_P必要证据，或仅有上述表面机制相似 | 不是证明该系统性能差、设计无效或任何其他实现都不可能相容 |

证据不足另记**待核/暂不评分**，不是第四个匹配档；不得强行记△或×，必须报告计数分母。当前十例对这次限定维度有足够方法描述，因此本建议分母为10；正式版不可重读的版本边界仍单独标明。

### 3. 局部相容机制L_P的操作判据

**P=Flat时，F1/F2/F3必须同时满足：**

- **F1：多视角独立贡献。** 至少两个参与角色形成各自分析/意见，不只是同一结果的多次投票或同一模型采样路径。
- **F2：共同对象、同等复核权限。** 这些参与者独立检查同一报告或候选产物，使用同一接受/反对规则；没有某个独占复核裁定权的专家。不同专长不等于不同复核权限。
- **F3：复核驱动实质修订。** 反对意见或批评进入共同产物的修订输入并触发重新复核，而非仅最终统计票数。轮次上限允许存在，但须记录；不能称每次必达一致。

这是**局部平等参与/共同复核相容性**，不称该模块或整个系统已被证明Flat。若整体仍有固定报告修订、调度或最终决定角色，S仍为H，评分至多△。不据该局部特征证明Hybrid权力切换。只有投票，没有独立分析及反馈修订闭环，F条件不成立。

**P=Hierarchical时：** 需在一段实质性子流程中明确报告固定角色对其他贡献的任务委派、路由、审批或综合决定权；机械末轮计票、单纯时序或角色名不同不够。若整体类别已是H，先按P=S记✓，不重复降档。

**P=Hybrid时：** 需在已报告的实质性子流程内看到**实际控制权配置切换**，例如由对等共同决定切到固定审批/综合权，且有清楚阶段/状态与控制条件。换代理名字、检索图层、反馈轮次、成员数量或加入同一固定审批者不够。只有一个固定H流程，不因为它是潜在Hybrid的一种组件就给△。

这些L_P必须按相同分析粒度应用；主控制角色的更换与权力关系的更换不能混为一谈。本规则是为导师原三档解释方法制定的操作化建议，不新增架构类或新的实证研究。

### 4. 决策顺序与可复算输入

1. 检查方法证据是否足够；不足时待核。
2. 从固定authority事实编码S，不看预期匹配数。
3. 若P=S，记✓。
4. 若P≠S，逐一检查相应L_P；满足记△，否则×。
5. 逐例定档后再计数。不得按5/3/2、6/4或其他目标反向调整条件。

代码只负责对已经人工、来源定位的特征和类别套用规则并计数，不能自动证明论文机制。实质判断仍可由另一位编码者审阅；尚未实施独立编码、盲评或一致性系数测量。

## 十案例逐项建议与证据

### 1. MedAgents（I）

- 冻结建议P：Flat；来源整体控制S：Hierarchical；**建议评分：部分一致 △**。
- 来源工作流：专家分别分析，同一报告接受各专家同规则复核；反对意见进入报告修订，循环至一致或轮次上限；之后固定LLM决策角色给答案。
- 按同一规则的判断：整体固定综合/最终决策仍为H；局部共同复核同时满足F1/F2/F3，支持Flat建议的多视角参与意图，但不满足整体Flat的无持续上级条件。
- 原文证据：[正式§2.1–2.5、Algorithm1，印刷601–603页](https://aclanthology.org/2024.findings-acl.33.pdf)。本次读取正式文本快照并在线复核方法。
- 引用键保护：tang2024medagents不更名、不删除。

### 2. LLM-MedQA（I）

- 冻结建议P：Flat；来源整体控制S：Hierarchical；**建议评分：部分一致 △**。
- 来源工作流：专家独立分析，所有专家对共同报告按同一赞成/反对规则复核；反对意见进入修订，修订报告再次复核；固定最终决策角色选答案。
- 按同一规则的判断：整体H；Algorithm1/§III-E的局部报告复核满足F1/F2/F3，§III-F仍保留固定最终决定，故为部分而不是广泛一致。
- 原文证据：[v1 §III-A–F、Algorithm1](https://arxiv.org/html/2501.05464v1)。本次核读v1；历史正式IJCNN2025物理3–6页定位保留，但正式用户PDF本轮不可重读。
- 引用键保护：tang2025llmmedqa不更名、不删除。

### 3. LegalGraphRAG（I）

- 冻结建议P：Hybrid；来源整体控制S：Hierarchical；**建议评分：不一致 ×**。
- 来源工作流：Researcher检索→Auditor验证/过滤→Adjudicator综合判决；改变检索图或证据内容不等于改变审批、综合决策权。
- 按同一规则的判断：整体H；未找到局部实际决策权配置切换L_Y的证据。不同角色交接和图结构不能满足Hybrid必要特征，故不一致。
- 原文证据：[正式§4.3、Fig3，印刷37459–37460页](https://aclanthology.org/2026.acl-long.1738.pdf)。本次读取正式全文文本快照§4.3。
- 引用键保护：legalgraphrag2026不更名、不删除。

### 4. Triad（S）

- 冻结建议P：Hierarchical；来源整体控制S：Hierarchical；**建议评分：广泛一致 ✓**。
- 来源工作流：一个LLM-based agent以三角色执行Text-to-SPARQL与候选选择/问答；阶段有序，选择与重试由固定角色/策略控制。
- 按同一规则的判断：建议H、整体工作流H，广泛一致。H指其工作流组织；该案例仍为S，不能因符号✓把它计为多代理核心研究。
- 原文证据：[正式§3、Fig2，印刷1700–1702页](https://aclanthology.org/2024.emnlp-main.101.pdf)。本次读取正文和图2文本快照。
- 引用键保护：hu2024triad不更名、不删除。

### 5. LONGAGENT（I）

- 冻结建议P：Hierarchical；来源整体控制S：Hierarchical；**建议评分：广泛一致 ✓**。
- 来源工作流：leader组织文档member、决定查询/冲突处理动作并控制最终综合；member之间的信息交换在leader组织的流程内。
- 按同一规则的判断：建议H、整体H；内部交换和多轮不改变持续leader权，广泛一致。
- 原文证据：[正式§2.1–2.4、Fig2，印刷16311–16313页](https://aclanthology.org/2024.emnlp-main.912.pdf)。本次读取方法全文文本快照。
- 引用键保护：zhao2024longagent不更名、不删除。

### 6. ChatDev（S）

- 冻结建议P：Hierarchical；来源整体控制S：Hierarchical；**建议评分：广泛一致 ✓**。
- 来源工作流：design→coding→testing的有序ChatChain；子任务中instructor发指令、assistant响应，阶段沿固定工作流执行。
- 按同一规则的判断：建议H、整体H；成对对话不是因此就Flat，广泛一致。
- 原文证据：[正式§3.1、Fig2，印刷15176–15177页](https://aclanthology.org/2024.acl-long.810.pdf)。本次读取正式ChatChain文本快照。
- 引用键保护：qian2023chatdev不更名、不删除。

### 7. AgentCoder（S）

- 冻结建议P：Hierarchical；来源整体控制S：Hierarchical；**建议评分：广泛一致 ✓**。
- 来源工作流：programmer和test designer为LLM角色，Python脚本executor执行测试并按通过/错误反馈控制接受或修订。
- 按同一规则的判断：建议H、整体H；固定执行验收/反馈门槛明确，广泛一致。仍为S，不恢复三个LLM代理说法。
- 原文证据：[选定v1 §3.1–3.4、Fig1，物理3–4页](https://arxiv.org/pdf/2312.13010v1)。本次读取选定版本全文文本快照。
- 引用键保护：huang2023agentcoder不更名、不删除。

### 8. Multiagent debate (Du)（I）

- 冻结建议P：Flat；来源整体控制S：Flat；**建议评分：广泛一致 ✓**。
- 来源工作流：各模型实例使用同类规则交换观点并更新自己的答案；末轮不一致采用规则式多数，没有持续top-down控制者。
- 按同一规则的判断：建议F、整体F；重复辩论或最终规则聚合在导师Flat定义中被允许，故广泛一致，不因迭代降为部分。
- 原文证据：[正式ICML2024 §2.1–2.2、Fig2–3，物理2–4页](https://raw.githubusercontent.com/mlresearch/v235/main/assets/du24e/du24e.pdf)。本次读取正式PMLR全文文本快照。
- 引用键保护：du2024multiagent_debate不更名、不删除。

### 9. EduPlanner（S）

- 冻结建议P：Flat；来源整体控制S：Hierarchical；**建议评分：不一致 ×**。
- 来源工作流：固定Evaluator产生评分/反馈；Optimizer依评分与反馈改方案，Analyst提供错误分析；候选按评分组织。
- 按同一规则的判断：整体H；有反馈修订，但未报告多个对等复核者对同一产物具有相同接受/拒绝权限，F1/F2不成立。异质角色和迭代不能单独算Flat相容闭环，故不一致。
- 原文证据：[v1 §III-C–E、Algorithms1–3](https://arxiv.org/html/2504.05370v1)。本次核读v1；正式TLT2025印刷419–422页旧定位保留，正式用户PDF本轮不可重读。
- 引用键保护：zhang2024eduplanner不更名、不删除。

### 10. Financial Reflection QA（I）

- 冻结建议P：Hierarchical；来源整体控制S：Hierarchical；**建议评分：广泛一致 ✓**。
- 来源工作流：专家先答，固定critic角色评数据/计算，专家使用反馈修订；反复multi-turn辩论在未来工作中提出。
- 按同一规则的判断：建议H、整体H；critic反馈不自动构成控制权切换，广泛一致。保留critic feedback/answer revision纠正，不恢复已实现多轮辩论说法。
- 原文证据：[v1 §3.1、§6](https://arxiv.org/html/2410.21741v1)。本次核读v1；旧正式ICAIF2024印刷532、534页定位保留，正式用户PDF本轮不可重读。
- 引用键保护：fatemi2024financialqa不更名、不删除。

## 重算汇总与边界

| 案例 | 角色 | P | S | 局部相容性／冲突 | 建议 |
|---|---|---|---|---|---|
| MedAgents | I | Flat | Hierarchical | F1=是/F2=是/F3=是；整体固定决策仍H | 部分一致 △ |
| LLM-MedQA | I | Flat | Hierarchical | F1=是/F2=是/F3=是；整体固定决策仍H | 部分一致 △ |
| LegalGraphRAG | I | Hybrid | Hierarchical | 未证实际权力切换；图与阶段交接不足 | 不一致 × |
| Triad | S | Hierarchical | Hierarchical | 整体控制类别一致 | 广泛一致 ✓ |
| LONGAGENT | I | Hierarchical | Hierarchical | 整体控制类别一致 | 广泛一致 ✓ |
| ChatDev | S | Hierarchical | Hierarchical | 整体控制类别一致 | 广泛一致 ✓ |
| AgentCoder | S | Hierarchical | Hierarchical | 整体控制类别一致 | 广泛一致 ✓ |
| Multiagent debate (Du) | I | Flat | Flat | 整体控制类别一致 | 广泛一致 ✓ |
| EduPlanner | S | Flat | Hierarchical | 固定Evaluator；F1/F2不成立，反馈修订不足 | 不一致 × |
| Financial Reflection QA | I | Hierarchical | Hierarchical | 整体控制类别一致 | 广泛一致 ✓ |

| 分组 | 广泛一致 | 部分一致 | 不一致 | 合计 |
|---|---:|---:|---:|---:|
| 全部十案例 | 6 | 2 | 2 | 10 |
| 其中核心I案例 | 3 | 2 | 1 | 6 |
| 其中支持S案例 | 3 | 0 | 1 | 4 |

**来源整体类别不变：9H+1F+0Hybrid=10。** 局部协作层的相容性不进入整体类别统计，因此不会把2个△误写成2个Hybrid。

6个✓：Triad、LONGAGENT、ChatDev、AgentCoder、Du、Financial QA。
2个△：MedAgents、LLM-MedQA。
2个×：LegalGraphRAG、EduPlanner。

与当前二档相比，MedAgents和LLM-MedQA由×细分为△；另两个×不变。与导师旧三档相比，Du和Financial改为✓，LegalGraphRAG改为×；其余机制纠错保留。不是直接恢复旧5/3/2，也不是为了保持2个部分而推定它们相容；F条件必须能从方法/算法找到。

### 可复算代码（仅存在本方案中，不写入原审计脚本）

```python
from collections import Counter

# P/S来自冻结建议与所报工作流的作者编码。
# F1/F2/F3来自方法定位，不能靠脚本从题名自动推断。
rows = [
    ("MedAgents", "F", "H", (True, True, True)),
    ("LLM-MedQA", "F", "H", (True, True, True)),
    ("LegalGraphRAG", "Y", "H", None),
    ("Triad", "H", "H", None),
    ("LONGAGENT", "H", "H", None),
    ("ChatDev", "H", "H", None),
    ("AgentCoder", "H", "H", None),
    ("Du", "F", "F", None),
    ("EduPlanner", "F", "H", (False, False, True)),
    ("Financial QA", "H", "H", None),
]
# LegalGraphRAG的局部Hybrid切换没有得到证据；L_Y=False。
# 本数据中没有整体不一致的P=H案例；遇到此类必须按L_H审阅。
counts = Counter()
for name, proposed, source, flat_features in rows:
    if proposed == source:
        grade = "broadly_aligned"
    elif proposed == "F" and flat_features is not None and all(flat_features):
        grade = "partially_aligned"
    else:
        grade = "divergent"
    counts[grade] += 1
print(dict(counts))
# broadly_aligned=6, partially_aligned=2, divergent=2
```

代码展示当前十例的具体输入，不是一个会把未知L_H/L_Y默认×的通用评分器。未知特征必须停止评分；本表LegalGraphRAG是已审阅后的“没有所需切换证据”，不是未读论文。EduPlanner具备反馈修订，但不能以F3独自满足Flat局部相容性。

## 正文、表格、图注与局限的同步清单

以下仅是最终确认后的限定修改范围，不是本轮已经实施的修改。

| 位置（当前工作区行号） | 同步要求 | 原文恢复与保护 |
|---|---|---|
| §3.1总定义，[manuscript.tex](<C:/Users/ShenTianyu(CN-TV-T1)/schoolwork/ESWA-multiagent/manuscript.tex:413>) | 总定义不改；明确具体实现与宏观控制层 | 三类、章节顺序、正交属性原样保护 |
| §3.1相关机制，[manuscript.tex](<C:/Users/ShenTianyu(CN-TV-T1)/schoolwork/ESWA-multiagent/manuscript.tex:453>)–563 | CAMEL/AutoGen/图/MDA/HITL只留必要边界 | B恢复原句骨架和尾句；不恢复全框架类别错误 |
| 比较表导语/题名，[manuscript.tex](<C:/Users/ShenTianyu(CN-TV-T1)/schoolwork/ESWA-multiagent/manuscript.tex:568>)与tab:9categories | 按Q4双展示区，主区恢复三类比较 | 保留标签、键、table*，不恢复旧multirow溢出；正文段落不搬家 |
| 第2项process/dynamism，[manuscript.tex](<C:/Users/ShenTianyu(CN-TV-T1)/schoolwork/ESWA-multiagent/manuscript.tex:663>) | 模式变化必须对应decision authority变化 | 只给hybrid routing加必要条件；不整体改写标准 |
| Phase2，[manuscript.tex](<C:/Users/ShenTianyu(CN-TV-T1)/schoolwork/ESWA-multiagent/manuscript.tex:709>) | peer观点候选F；固定controller/approver为H；有实际控制配置变化才候选Hybrid | 保留两阶段、四标准、single-agent baseline与task-level比较 |
| 应用建议，[manuscript.tex](<C:/Users/ShenTianyu(CN-TV-T1)/schoolwork/ESWA-multiagent/manuscript.tex:782>) | 并行专家+固定最终复核可仍为H；不是自动Hybrid | 恢复high-risk/educational/legal场景和导师尾句；保留局部控制边界 |
| 十案例方法/结果/表，[manuscript.tex](<C:/Users/ShenTianyu(CN-TV-T1)/schoolwork/ESWA-multiagent/manuscript.tex:730>)与tab:validation | 用同一三档规则、逐例✓△×和6/2/2；表头为作者源编码 | 保留十例、原建议类别；不称来源自报标签、不称预测准确率 |
| 十案例表注，[manuscript.tex](<C:/Users/ShenTianyu(CN-TV-T1)/schoolwork/ESWA-multiagent/manuscript.tex:773>) | 解释三档、整体vs局部、来源版本、Triad及另3项S边界 | 替换exact类别二档说明，保留单代理/支持例等A保护 |
| §3.2末尾limitations，[manuscript.tex](<C:/Users/ShenTianyu(CN-TV-T1)/schoolwork/ESWA-multiagent/manuscript.tex:796>) | 继续强调多要求/边界、qualitative、需外部测试 | 导师原意已吻合，无须新改写整段 |
| 框架技术表及导语，[manuscript.tex](<C:/Users/ShenTianyu(CN-TV-T1)/schoolwork/ESWA-multiagent/manuscript.tex:1644>)–1711 | 最小澄清Control/organisation含工具能力与组织描述 | 保留当前非全框架标签及已核机制；D075c仅恢复3单元 |
| architecture challenges，[manuscript.tex](<C:/Users/ShenTianyu(CN-TV-T1)/schoolwork/ESWA-multiagent/manuscript.tex:1939>) | 多标签说明区分整体架构与局部协作机制 | Financial critic事实不回退；现段多数原句可保持 |
| 全稿局限，[manuscript.tex](<C:/Users/ShenTianyu(CN-TV-T1)/schoolwork/ESWA-multiagent/manuscript.tex:2165>) | 保留导师verification exercise而非independent general validity原句；说明无整体Hybrid例 | B词组恢复；三档相容性不是拓扑切换验证、非独立编码/预测精度 |
| Conclusion，[manuscript.tex](<C:/Users/ShenTianyu(CN-TV-T1)/schoolwork/ESWA-multiagent/manuscript.tex:2186>) | 核查与表/结果一致 | 三段原结论已经不声称普适拓扑或性能因果，预计无需改写 |
| 图1图注/AI声明、85/78/13统计 | 不变 | 当前图1与声明、引用角色、APA7/Biber、参考台账保护 |
| 隐藏旧章/独立archive | 不参与同步 | iffalse块及archive不动，不修其中历史5/3/2等数字 |

### 图注与实际图文件：已核实的冲突

- fig:topology图注（[manuscript.tex](<C:/Users/ShenTianyu(CN-TV-T1)/schoolwork/ESWA-multiagent/manuscript.tex:432>)）保持“illustrative”及修复后的tab:9categories引用。不改图，不恢复无效tab:core_taxonomy_mapping。
- fig:decision_flow图注目前没有案例数字，不需为6/2/2改图号。**但当前编译实际包含的是fig_flow.jpg，其图内分支仍有实质冲突**。本次直接查看[fig_flow.jpg](<C:/Users/ShenTianyu(CN-TV-T1)/schoolwork/ESWA-multiagent/fig_flow.jpg>)，不是根据旧日志猜测：
  1. 高安全/合规要求的Medical/Legal直接导向“Hybrid + HITL”；这把固定审批等同Hybrid。
  2. 难度波动、复杂跨域推理导向“Hybrid Adaptive switching / Mesh network”；这未检查决策权配置是否变化。
  3. 最后默认分支把Role play / Group chat放在Flat终点；这未确认没有持续controller。
- 后续图稿需要把高风险作为治理/复核约束、把Hybrid条件明确为authority-change、把Flat条件明确为无持续top-down；这些是既有正文定义的图形同步，不是新研究观点。本轮及正文恢复都不擅自覆盖图片。
- 可以在最终批准后用最小图注说明当前图为概念筛选示意，但**只增加图注不能让上述实质箭头与正文完全一致**。若图片继续冻结，阶段二可以交付正文恢复及编译结果，但须明确图内语义同步尚未闭环，不能声称全文图文最终一致。
- output/中的可编辑版本不自动成为当前编译图源；不得因那里存在新稿就忽略fig_flow.jpg。这些输出和图1、图2均受保护。

### 十案例正文的最小英文片段草案

恢复导师原结果句骨架，仅替换复算数字：
**“Six cases are broadly aligned, two are partially aligned, and two are divergent under the coding used here.”**

随后保留导师边界与多标签论证，必要短限定为：
**“MedAgents and LLM-MedQA retain hierarchical overall control while supporting equal-participation expert review locally. These local mechanisms explain partial alignment with a flat recommendation; they do not establish a flat or hybrid overall architecture.”**

这个新增方法澄清是Q5可重复评分必需的一部分，不是自由润色。其余原多要求与多标签结论尽量复用导师原句；不把所有边界例都叫Hybrid。所有三档指示、数字及局限必须同时更新。

## B25项恢复的预计范围及A保护交叉核对

“25项”是阶段一批准项的语义范围，不是承诺25个Git hunk。Q4/Q5表格重排、同段A/B/C交叠，实际差异块/行数须正式补丁后复算；此阶段不预填新增/删除行数。

| 章节 | B项ID | 项数 | 恢复重点 |
|---|---|---:|---|
| 摘要 | D003b | 1 | based on/including与core empirical原句骨架；85/78/13不变 |
| 第1章 | D004、D005b、D010c、D011、D013c | 5 | 修辞、删重复扩写、引导句、核心证据句；Q3历史边界不回退 |
| 第2章 | D018b、D019 | 2 | 任务分工过渡与can/may可靠性原段；Park来源范围仍限定 |
| 第3章 | D024a、D025、D026c、D027b、D039b、D040b、D049b | 7 | 恢复句式/尾句、breakpoints与原成本收益门槛、场景与论证顺序 |
| 第4章 | D050b、D052b、D053b、D055b、D057、D060b | 6 | 原协议过渡、角色分配目标、去非必要共享库扩写、RAG顺序、CoT与反思句骨架 |
| 第5章 | D075c、D078 | 2 | GPTSwarm三个原单元；删除新增表格指路句，不删表 |
| 第6章 | D080b、D084a | 2 | 原quadratic表达与有限verification exercise局限 |
| 合计 | — | 25 | 6项完整恢复、19项局部恢复 |

完整恢复仅D004、D011、D019、D025、D057、D078。局部恢复全部以可读原句片段重建，不整段git checkout或粘贴导师版本覆盖；Q4/Q5对同段的必要限定优先。

| A保护面 | 本方案承诺 |
|---|---|
| 统计/纳入 | pool85、cited78、core13、Triad为S；角色13/17/46/9及13/15/42/8不变 |
| 参考与编译 | 既有引用键、必要补证、references.bib、APA7/Biber配置/sourcemap均保留；不回旧BibTeX |
| 已核机制 | CoCoA-zero、MemGPT函数/FIFO、Self-RAG/FLARE单模型机制、ToT/GoT状态、SC主体、CoVe事实边界保留 |
| 技术表 | 真实message pool、ChatDev阶段记忆、AgentVerse来源范围、RAGFlow版本、Financial critic反馈保持 |
| 因果/绝对保证 | 不恢复must全局KG、实时保证、最大吞吐、所有领域不可能覆盖、普遍安全或普遍性能保证 |
| 分类底线 | 工具/图/投票/HITL不自动对应Flat或Hybrid；固定审批/最终决策权仍被记录 |
| 文件与排版 | 图1/图2/其他原图、现有可编辑输出、双栏、必要表格环境/引用修复、隐藏历史章节全部保护 |

“保留A”保护的是必要事实或来源边界，不要求保留新版全部扩写。B25并不撤销A64。Q5将MedAgents/LLM-MedQA从×改△只改变已待确认的比较评分，没有改写源流程A事实；Q4Hybrid比较行是恢复已有分类主线，不虚构Hybrid实测样本。

## 必须等待的最终确认与后续验收

需要最终确认的具体方案：
1. Q4一个表两区、三类主区＋五项相关机制附区，并允许框架表列名最小明确为Control / organisation。
2. Q5上述三档顺序、L_P判据及来源版本边界；接受建议6/2/2与宏观9H/1F/0Hybrid。
3. 按同步清单和已批准B25/Q1–Q3最小恢复正文。当前图片仍保护；fig_flow图内语义同步作为明确待处理项，不由本轮覆盖。

批准后再建立独立分支，仅实施获准manuscript.tex恢复；不携带用户图表改动去做未经授权的提交。复查全部引用/交叉引用、统计与表/结论，使用当前APA7/Biber完整编译与双栏PDF验收，输出逐ID before/after，检查未批准区域逐字不变。不提交、推送或合并。

**当前到此停止，仅提供方案与建议重评分，等待最终确认。**
