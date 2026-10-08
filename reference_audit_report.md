# 参考文献修正与验收报告

日期：2026-10-08。已应用有来源依据的书目字段修正和正文最小修正，保留导师修改后的章节结构及原有 citation keys；图片留待下一阶段。

## 当前统计

| 口径 | 数量 |
|---|---:|
| 书目池 | 85 |
| 有效正文不同文献 | 78 |
| 有效引用命令 | 136 |
| 展开多键后的出现次数 | 180 |
| 保留的未引用记录 | 7 |

原有84条全部保留。新增1条有日期的官方 LangGraph interrupt 技术文章，用于暂停、检查点和恢复机制；不是补足文献数量。
书目池角色：{"B": 46, "S": 16, "I": 14, "T": 9}；有效引用角色：{"B": 42, "S": 14, "I": 14, "T": 8}。
14项I沿用作者编码；Triad的一个LLM承担三角色已在方法和表格中披露为纳入边界，是否转为S仍待作者裁定。

## 已完成修改

- 修正 Natural Questions 页码、ReAct及NeurIPS会议条目类型、GLM集体署名、MemGPT姓名显示、SWE-agent错误URL、CrewAI首次PyPI发布日期；补充已核实的会议DOI。
- Guo综述使用IJCAI2024正式出处，GPTSwarm使用ICML/PMLR正式出处；Least-to-Most、Decomposed Prompting、Self-Consistency使用ICLR2023正式出处。仍存在来源冲突的作者字段没有自动覆盖。
- 收窄综述新颖性定位；修正MemGPT、Self-RAG/FLARE、ToT/GoT、CoVe、AgentVerse/MetaGPT及GPTSwarm等机制归因。区分CoCoA-zero多代理推理与CoCoA单模型蒸馏。
- 将架构适用性、成本收益准则、治理要求和部分评估建议标为作者综合或建议；修复两处失效交叉引用，保留AI使用披露。
- 正文与literature_audit.csv同步当前统计，历史排除记录保留；搜索历史与本次字段核查分别记录。
书目修改日志含100项字段/新增记录操作；正文有49个差异块。日志包含修正前后内容，不能把一个差异块视为一个独立科学结论。

完整记录：[书目before/after](audit_work/reference_correction_log.json)、[正文before/after](audit_work/manuscript_correction_log.json)、[修改前快照](audit_work/before_reference_corrections_20261008.zip)。

## 当前证据台账

- [85条书目字段台账](audit_work/reference_field_audit.md)：[CSV](audit_work/reference_field_audit.csv)、[JSON](audit_work/reference_field_audit.json)。逐字段标明已核实、冲突、未核实等，原差异与已修正项保留历史。
- [136处正文引用证据台账](audit_work/citation_claim_audit.md)：[CSV](audit_work/citation_claim_audit.csv)、[JSON](audit_work/citation_claim_audit.json)。当前原句、证据位置、支持程度、实施状态及修改前句分别记录，多键命令逐来源判断。

10项核心字段状态：

| 状态 | 字段数 |
|---|---:|
| 已核实 | 569 |
| 未核实 | 131 |
| 不适用 | 120 |
| 版本/来源冲突 | 17 |
| 建议规范化 | 10 |
| 字段不完整 | 3 |

引用命令状态：

| 支持程度 | 命令数 |
|---|---:|
| 直接支持 | 99 |
| 部分支持/表述需收窄 | 8 |
| 作者推论，须标明边界 | 21 |
| 多来源支持程度不同 | 7 |
| 前瞻建议，非原论文验证 | 1 |

作者推论或前瞻建议不自动视为错误，也不升级为原论文已验证结论。存在性核实不等于所有字段核实；未获取正式全文的字段保持限制说明。

## 编译及一致性验收

当前编译快照有效：True；编译和引用解析通过：True。
[编译记录](audit_work/compile_verification.json)保存命令、退出码、未定义引用检查、版面警告和输入/输出哈希。过长URL与原有版面警告留待格式阶段，不据此声称最终排版已验收。
[当前清单](audit_work/inventory_summary.json)对照实际主稿、.aux及.bbl；[静态检查](audit_work/static_reference_checks.json)检查覆盖、定位和哈希，warnings为待确认项，不等同于结构检查失败。
禁用条件块、未被主稿包含的历史章节和19个原图片文件保持不变；保护检查见[correction_verification.json](audit_work/correction_verification.json)。

复现台账检查：

```powershell
python -m unittest discover -s tools -p test_active_tex.py -v
python tools/build_reference_inventory.py
python tools/build_audit_ledgers.py
python tools/static_reference_checks.py
```

证据生成器不联网，也不自动证明来源；来源变化后需要重新审阅，禁止仅改哈希绕过。旧finalize工具入口已停用，防止过时缓存删掉未引记录。

## 待确认及图片阶段

[待确认清单](audit_work/pending_reference_decisions.md)汇总Triad、版本选择、官方网页/PDF冲突及未直接核实字段；[CSV](audit_work/pending_reference_decisions.csv)逐字段保留。
图片仍有84 active或旧角色分配等口径。正文已注明旧快照；下一阶段需同步为书目池85、有效引用78、作者编码I14（Triad待裁定），并缩小图中文字。本轮未改图。
以下7条保留，不为凑数补引：

- `li2024genmentor`
- `singhal2023medpalm`
- `guha2023legalbench`
- `brynjolfsson2023generative_ai_work`
- `yang2024swe_agent`
- `jimenez2024swe_bench`
- `xagent2023`

[旧报告归档](audit_work/reference_audit_report_legacy_20260802.md)保留历史75条结论。literature_audit.csv的引用标志和次数已同步，旧元数据匹配列仍属历史证据，当前字段结论以两份台账为准。
