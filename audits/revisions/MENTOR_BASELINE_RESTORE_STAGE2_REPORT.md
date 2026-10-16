# 导师基线保守正文恢复：阶段二验收报告

日期：2026-10-13。**已完成获批正文恢复及当前 APA7/Biber 编译验收；图片语义同步尚未完成，不宣称最终图文一致或投稿验收全部通过。**

## 版本与 Git 保护

- 导师原版：`f84c78b2720bd5cad8fa32eeb7eaa3a510a8263d`。
- 开始分支：`codex/eswa-apa7-migration`；HEAD：`6191a1b7d6e562c4cd65d2c409840dadccae58ba`。开始时暂存区与工作区均干净。并发历史提交 `43495d239b8e1fdb2ac06a43a499080800592349` 已在该 HEAD 历史中。
- 已核对报告基线 `f67f294` 到开始 HEAD 的正文差异：仅图1引图句、图注及 AI 声明更新。这些片段全部原样保留。开始正文 SHA256 与已批准方案相同：`3acc39b05e660d1517dada3b59c316b2a1b84a38beffea1b132a9a81bfb02115`。
- 修改前为 **1,484 个现有文件**建立逐文件哈希和完整保护副本。备份遇到 Windows 长路径限制时改用长路径文件接口继续完成，没有删改源文件。
- 按批准方案建立独立分支：`codex/mentor-conservative-restore-stage2`。创建分支所需 `.git` 写权限经沙箱执行权限审查后获得；未强制切换、reset、stash、丢弃或覆盖用户改动。
- 执行结束 HEAD 仍为 `6191a1b`。本轮未运行 `git add`、commit、push 或 merge，暂存区仍为空。
- 正文补丁：190 行新增、159 行删除；行数包含必要的 Q4 表格联动及 Q5 操作判据，不能作为独立科学改动数量。

执行期间，图2、图4、图5的可编辑 `*_edited.pptx` 出现并发外部保存，伴随 Office 锁文件。本轮没有工具写入这些源路径，也没有自动将 PPTX 替换为编译图源。保留开始副本及后续检查点副本，详见 `concurrent_changes.json` 和 `concurrent_protection/`。锁文件未清理。因此不能将工作区所有图片相关文件描述为“与开始哈希相同”；准确结论是**本轮没有编辑图稿，外部并发编辑已保留**。

最后一次Git检查还发现图2、图4、图5目录各新增一份外部导出的未跟踪PDF。原文件均保留，另存检查点副本与哈希，见 `concurrent_new_files.json`。这些导出没有自动成为当前论文的编译图源。

## A/B/C 实际执行

| 类别 | 批准项数 | 实际结果 |
|---|---:|---|
| A | 64 | 必要事实、来源、统计、技术机制与格式纠正成果保留；共享段落仅按获批 B/C 边界恢复，不要求保留所有原扩写 |
| B | 25 | 全部执行：6项完整恢复、19项局部恢复 |
| C | 30 | Q1–Q5全部按本次批准处理；已经符合批准规则的片段保留，避免额外重写 |

完整恢复：D004、D011、D019、D025、D057、D078。其余局部恢复：D003b、D005b、D010c、D013c、D018b、D024a、D026c、D027b、D039b、D040b、D049b、D050b、D052b、D053b、D055b、D060b、D075c、D080b、D084a。

119 项逐项记录均包含批准决策、导师原片段、执行前片段、执行后片段或同段联动片段、操作编号。实际顺序记录有42个操作；同一操作可覆盖多个批准项，不能将操作数与119项混用。

- [逐项执行记录](audit_work/mentor_restore_stage2_20261013/EXECUTION_LEDGER.md)
- [结构化逐项台账](audit_work/mentor_restore_stage2_20261013/execution_ledger.json)
- [执行前到恢复后的完整补丁](audit_work/mentor_restore_stage2_20261013/before_after.patch)
- [导师原版到恢复后的完整补丁](audit_work/mentor_restore_stage2_20261013/mentor_to_restored.patch)
- [按顺序的精确替换记录](audit_work/mentor_restore_stage2_20261013/operations.json)

## Q1–Q3

- Q1：恢复导师 Although 开头、QA专属整合缺口及贡献导语；只承认既有综述也覆盖通信、编排与部分 QA，不新增首创性主张。五项贡献条目不重写。
- Q2：恢复 `primary evaluated task`，增加获批的 co-primary 澄清；不允许偶然 QA 展示。核心名单仍为13项，Triad仍为S。
- Q3：保留历史日志/working records层级，不恢复未独立重建的检索动作或全面元数据核验承诺。D010c只缩短已有核查段，核查日期、85/78及未决字段边界保留；旧审计文件不修改。

## Q4：定义、表格和选择规则

- Table 2 / `tab:9categories` 保持一个 `table*`、原表号与六列意图；主区为 Flat、Hierarchical、Hybrid，附区为原五个机制主题，八个数据行。没有新增第四种架构。
- Hybrid代表项明确为条件性设计模式，并限定本十案例没有源编码的Hybrid实例；不虚构已验证系统。
- CAMEL角色不对称、AutoGen配置依赖、GPTSwarm的DAG优化与LangGraph循环/分支区分、MDAgents的moderator与solo/MDT/ICT路径均保留。
- 固定人工审批仍属于层级控制；只有实际决策权配置改变才能采用Hybrid。图、投票、成员变化或相关工具本身不足证明Flat/Hybrid。总架构定义、四标准及Phase 2现有正确边界原样保留；应用段仅恢复批准的场景与论证顺序并保留必要限定。
- Table 4 / `tab:framework_compare` 仅同步 `Control / organisation` 列名及对应导语；八行不变。D075c恢复三个原技术单元，GPTSwarm的组织描述及真实MMLU/graph optimisation用途保留。

## Q5：写入前再核查及十案例一致性

MedAgents重新核读正式ACL全文§§2.1–2.5与Algorithm1（印刷601–603页），并在线核对[官方全文](https://aclanthology.org/2024.findings-acl.33.pdf)。本机另发现此前方案环境不能重读的LLM-MedQA正式IJCNN2025 PDF现在可访问，因此重新核读§III-A–F与Algorithm1（物理3–6页），v1仅作补充。正式PDF SHA256为 `4c27d253f6df5b9834392cc4550db905b3e47eaf6e3732a414c76480398d226b`。旧方案/旧日志的访问限制保留为历史记录；本轮新表注记录实际核读的正式版。

两个案例均支持F1/F2/F3同时成立：专家角色贡献各自分析，所有专家按相同规则复核同一报告，反对意见进入修订并触发后续轮次复核。二者算法都有轮次上限；固定修订与最终决策角色仍使整体源编码为H。F1指角色贡献，不声称模型输出统计独立或所有阶段互不依赖。LLM-MedQA伪代码的draft变量命名存在不一致，§III-E及式(7)明确说明修订与再次复核；本轮没有执行论文代码，不用伪代码声称实现或性能验证。

| 案例 | 冻结建议P | 整体源编码S | 三档结果 |
|---|---|---|---|
| MedAgents | F | H | 部分一致 |
| LLM-MedQA | F | H | 部分一致 |
| LegalGraphRAG | Hybrid | H | 不一致 |
| Triad（S） | H | H | 广泛一致 |
| LONGAGENT | H | H | 广泛一致 |
| ChatDev（S） | H | H | 广泛一致 |
| AgentCoder（S） | H | H | 广泛一致 |
| Du debate | F | F | 广泛一致 |
| EduPlanner（S） | F | H | 不一致 |
| Financial Reflection QA | H | H | 广泛一致 |

按先整体、后局部机制的互斥规则复算，**6广泛一致、2部分一致、2不一致，分母10；整体9H/1F/0Hybrid**。十行符号、正文统计、表注及全稿局限一致。LegalGraphRAG没有来源定位的控制权配置切换；EduPlanner具有固定evaluator评分权，不符合F2，不能靠多个角色凑部分一致。

保留导师关于边界案例、竞争需求和多标签描述的论证，同时明确整体架构与局部机制分开描述。这是作者回顾性组织相容分析，未实施独立编码、盲评或预注册，不是预测准确率、独立验证、实测性能或安全提升。其余八例沿用批准方案与既有来源定位，不声称本轮重新核读全部原论文。

详细条件与逐例来源见 [Q5再核查记录](audit_work/mentor_restore_stage2_20261013/Q5_SOURCE_RECHECK.md)及 `q5_case_scores.json`；原文保护副本、提取文本及算法页面检查材料在 `q5_sources/`、`pdf_review/`。

## 有效正文、统计与未批准区域

| 项目 | 结果 |
|---|---|
| 书目池 / 实际引用 / 核心 | 85 / 78 / 13，唯一键集合与开始一致 |
| 池内I/S/B/T | 13 / 17 / 46 / 9 |
| 实际引用I/S/B/T | 13 / 15 / 42 / 8 |
| 未引用记录 | 7 |
| 引用命令 / 键出现次数 | 136→135 / 180不变；Q4合并层级两行引用为一条命令，78个唯一引用不变 |
| references.bib、APA配置、sourcemap、生成脚本 | 哈希不变 |
| 章节标题及顺序、总架构定义 | 逐字一致 |
| 全部六个有效图环境、图注、图1说明、AI声明 | 逐字一致 |
| iffalse禁用旧章、archive、旧审计和保护文件 | 不修改 |
| Conclusion | 逐字一致 |
| 非批准正文改动 | 顺序重放42条精确操作与最终全文一致，无未记录额外正文改动 |

去除注释、禁用历史块、图/表/展示公式和引用/交叉引用命令，再按相同英文词元方法比较导师原版：差异词数从 **2,065降到1,531**，相似度代理指标从0.89815到0.92552。完整方法与结果见 `mentor_prose_comparison.json`。它用于辅助检查非必要改写是否减少，不是导师文风的定量证明。新增的Q5操作判据是批准方案必要内容，不能要求其与导师原文逐字相同。

静态检查曾因Python导入刷新一份既有`__pycache__`缓存；已按开始保护副本恢复，其最终哈希一致，后续扫描禁用字节码写入。最终既有文件变化仅为批准正文、匹配构建产物及单独记录的三个外部PPTX。详见 `static_acceptance.json` 和 `protected_manifest.json`。

## APA7/Biber与PDF验收

当前恢复稿完成 `pdfLaTeX → Biber 2.22 → pdfLaTeX → pdfLaTeX`，隔离目录为 `tmp/mentor_restore_stage2_20261013_build/`。初次沙箱内启动Biber出现Windows DLL重定位错误；仅对Biber命令取得执行权限后正常完成，没有安装、升级、更改系统或APA配置。正式来源表注更新后重新完成最终链；未拿第一轮旧PDF代替最终稿。

- 最终PDF：23页，已同步根目录 `manuscript.pdf`及匹配aux/bbl/bcf/log/blg等生成物，并保存独立交付副本 `audit_work/mentor_restore_stage2_20261013/restored_manuscript.pdf`。
- PDF SHA256：`2efa90d4bd1d6cf626de760ba40542c3aac7ed53855f06ff89a4ef288d2fe0df`。
- 编译实际输入为隔离目录的新BBL；全局参考文献列表78项，无重复项。
- 未定义引用0、未定义交叉引用0，无需重跑提示，无Float too large。
- 按现有APA逐条渲染检查器检查78项：**78通过，0格式失败**。没有重写原APA审计输出；本轮结果为 `apa_render_acceptance.json/.csv`。格式通过不代表历史元数据未决字段全部解决。
- 浏览最终23页联系表，重点检查第1、7、10、14、19页大图：正文双栏、Table 2/3/4完整，未见新增裁切或重叠；引用、表注、局限及Conclusion可读。QA截图位于本轮新目录，原图片没有被编辑。
- 原有两处日志提示保留：`\maketitle`处123.62721pt hbox，以及未修改的长期团队学习段0.5575pt hbox。二者在执行前日志已存在；重点页面未见对应新增可见遮挡。本轮不扩大到全稿排版修复。旧Table 2的0.76843pt提示已不出现。
- `git diff --check`通过。

编译、渲染与格式证据见 `compile_acceptance.json`、构建日志、`compiled_text.txt`及 `pdf_review/`。

## 明确遗留事项

1. **`fig_flow.jpg`三处图内语义冲突仍待单独修改**：高安全Medical/Legal直接导向Hybrid+HITL；难度波动/跨域直接导向Hybrid switching/mesh而没有authority-change条件；默认Role play/Group chat导向Flat而没有排除持续controller。本轮未改图片，也未改图注掩盖冲突。
2. 其他现有图稿/可编辑稿的完整语义同步尚未闭环。图2/图4/图5并发编辑已保护，但不自动计为本轮图稿验收或当前PDF图源更新。
3. 两处原有排版日志提示、既有元数据可获性与可选字段限制继续保留；不将78项APA格式通过扩展为85条书目全面元数据复核完成。
4. Q5仍是混合I/S样本的作者分析；没有整体Hybrid源案例、独立编码或性能验证。这些局限已留在正文。

**本轮正文恢复及上述限定范围内验收完成；提交、推送、合并和图稿修改均未执行。**
