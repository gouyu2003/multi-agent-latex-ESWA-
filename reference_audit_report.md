# 第二阶段参考文献与正文证据审计报告

核查日期：2026-10-10。唯一基线：ESWA_Submission_caomodify。

## 当前结论

第二阶段已完成：书目版本及必要字段修正、有效正文引用相关性、13项核心纳入标准、十案例统一分类及匹配修正均已落实；新稿已编译并通过保护与结构验收。
这里的完成不代表所有可选字段均得到证明：缺乏正式证据的DOI、页码、出版者等仍逐字段标为未核实；不据篇幅编造出版页码，不将作者分析改标为原文实证。

## 核查覆盖

| 项目 | 当前结果 |
|---|---|
| 书目池 | 85条；全部逐字段记录 |
| 有效引用 | 78篇；136处引用命令；180个逐来源判断 |
| 池内角色 | {"B": 46, "S": 17, "I": 13, "T": 9} |
| 有效引用角色 | {"B": 42, "S": 15, "I": 13, "T": 8} |
| 核心纳入重核 | 13项；五项标准均有方法/评估证据定位 |
| 本次实施 | 55项书目字段修改；38处正文差异块 |
| 引用判断 | {"direct": 105, "author_inference": 28, "mixed": 2, "proposal": 1} |
| 十案例 | 6例一致；4例不一致；来源流程编码为9层级、1扁平、0混合 |

未引用的7条记录保留在书目池，未为凑数补引。I是核心研究、S是支持研究、B是背景、T是技术资源；Triad按作者明确决定为S。

## 已落实的主要修改

- AutoGen使用用户提供的COLM 2024正式全文，核对14位作者、正式题名及GroupChatManager等机制位置；没有把46页篇幅填成正式出版页码。
- GPT-4、MemGPT、ChatLaw、AgentCoder固定实际使用的arXiv版本。AgentCoder按2023 v1的五位作者及顺序修正；该版本测试执行角色为脚本，正文不把它算作第三个LLM智能体。
- DSPy题名/作者以正式全文为依据；GAIA补回Craig Swift；Self-RAG使用官方Zeqiu拼写及正式全文Avirup全名；LegalBench以正式全文作者列为依据，保留网页差异历史。
- Natural Questions采用正式PDF和出版商登记一致的453–466；ACL网页452–466差异保留。LLM-MedQA的1–8获出版商登记支持；Memory survey按Article155写为155:1–155:47；EduPlanner题名按Multiagent规范。
- 仅据正式来源补入可确认的ICLR/NeurIPS连续页码与DOI。未获证明的字段维持未核实；可访问的摘要不替代未读的实验内容。
- CrewAI固定0.1.0、Dify固定0.6.0、RAGFlow固定v0.6.0；MCP采用2024-11-25公告、A2A采用2025-04-09公告；不以当前功能倒推早期版本。
- 十案例保留既有建议架构，按统一控制权标准重新编码来源流程。MedAgents、LLM-MedQA、LegalGraphRAG、EduPlanner改判为层级，得到六例一致、四例不一致；不作为选择策略预测准确率。
- CAMEL角色对、AutoGen可配置会话、GPTSwarm图结构、AgentVerse反馈、LangGraph状态图不再机械等同扁平或混合。区分控制权架构与可复用机制。
- Financial QA收窄为critic feedback and answer revision；其多轮反复辩论是未来工作。撤去必须全局知识图谱、实时同步及保证避免重复检索等缺少依据的强断言。

## 按有效章节定位

| 章节 | 本次相关修正 |
|---|---|
| 第1章 Introduction及文献筛选说明 | 历史检索描述收窄为工作记录，85/78与核心13口径同步；绝对性领域知识/增长断言收窄 |
| 第2章 Background | 跨reasoner答案比较与普遍优于自我修正分开；已核机制归因保持来源边界 |
| 第3章 Architectures | 控制权分类、交叉机制表、十案例编码/勾叉、人工审批及混合判断规则修正 |
| 第4章 Key technologies | 按选定版本核实MemGPT/Self-RAG/FLARE/ToT/GoT/CoVe；知识共享与自省效果不作无条件保证 |
| 第5章 Development and evaluation resources | 框架表按实际机制命名，固定软件/协议版本，不扩展为自动架构选择或部署验证 |
| 第6章 Challenges and Future Directions | Financial QA反馈修订机制收窄；建议和来源实测效果明确区分 |
| 第7章 Conclusion及末尾声明 | 六/四回顾性比较、无来源编码混合样本、非独立验证局限及版本选择同步 |

导师隐藏的旧应用章/旧完整选择章及独立历史章节文件继续保留，不参与此次有效正文核查。完整逐处before/after见[正文修改日志](audit_work/stage2_manuscript_correction_log.json)；逐字段见[书目修改日志](audit_work/stage2_reference_correction_log.json)。

## 核心证据与限制

[书目字段台账](audit_work/reference_field_audit.md)覆盖全部85条及附加字段；[正文证据台账](audit_work/citation_claim_audit.md)覆盖全部136处有效引用及180个逐来源语境。
[核心纳入重核](audit_work/core_eligibility_audit.md)记录13项五标准证据；[十案例复核](audit_work/case_classification_audit.md)记录来源流程、编码和匹配。
来源优先正式全文、出版社/会议官方页、出版商登记、选定arXiv版本及官方日期/发行记录；同一机构的HTML和PDF属于主来源的不同载体，不冒充独立双源。检索失败、页面访问限制和版本差异保留在快照/检索记录与字段台账中。
[余下未核实字段](audit_work/pending_reference_decisions.md)逐项列出，均保留限制而非标记通过。历史检索原始导出、独立编码/前瞻验证未取得，已在正文收窄或声明限制；它们不被伪造为已完成的实证。

## 验收与后续范围

当前输入绑定的新编译：True；[编译与渲染记录](audit_work/compile_verification.json)。pdfLaTeX → BibTeX → pdfLaTeX → pdfLaTeX，保持SyncTeX同步。
[结构验收](audit_work/static_reference_checks.json)检查引用、aux/bbl、证据覆盖及输入输出哈希；结构通过不代表所有字段全部核实。
[保护验收](audit_work/correction_verification.json)检查隐藏正文、19个原图、历史章节、历史排除记录和五篇用户PDF未变化。修正前文件保存在audit_work/before_stage2_completion_20261010.zip。
全面格式调整与图中文字缩小仍是后续阶段。原图仍保留旧84条快照，需要随后同步为pool85（I13/S17/B46/T9）、active78（I13/S15/B42/T8），并核对分类标签。此次未改原图。
长URL、原有版面警告及AI绘图采用来源说明留待相应阶段，不能据本次编译宣称整篇已达到最终投稿排版要求。

复核命令：

```powershell
python -B tools/build_reference_inventory.py
python -B tools/build_audit_ledgers.py
python -B tools/static_reference_checks.py
```

生成器仅整理已审阅证据，不能靠改哈希、题名相似或自动匹配证明来源。历史literature_audit.csv的旧匹配列保留；当前结论以两份台账为准。
