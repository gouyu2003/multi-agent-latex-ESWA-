# Table 2 导师原版最小纠错执行报告

日期：2026-10-14。批准方案 A；仅修改 manuscript.tex 的 Table 2 与指定导语。不提交、不推送、不合并。

## 实际修改与逐格验收

导师基线 f84c78b；执行前分支 codex/mentor-conservative-restore-stage2，HEAD 00f9b61。

38 项 KEEP 均与导师原格逐字相同（只忽略空白、换行及分类显示格式）；九项必要纠错全部符合获批建议；R1C6 采用 Cost and aggregation sensitivity。六列表头、八机制行、原行序均保留。

恢复 manager--executor 与 evidence-processing 两个独立行，取消两区分组及长篇 Hybrid 定义行。CAMEL / MDAgents 分类带特定工作流脚注；--- 不构成第四类。表注逐字包含 A hybrid architecture requires a demonstrated change in decision authority.。

表前导语仅删除 are shown separately and；其余内容不变。caption 保留方案 A 已批准的 and related mechanisms。

## 必要排版调整

第一轮恢复原列宽时，分类格 Hierarchical 加上脚注导致 1.22806 pt 超宽；窄列两端对齐也造成过大字间距。最终仅把 C1 从 1.4 cm 调至 1.5 cm，六列使用 raggedright / arraybackslash 左对齐。其余列宽、scriptsize、行距、table* 浮动环境与表中文字均未更改。Hierarchical 跨行数由导师原 3 修为 2。

## 逐格导师原文与最终值

| 单元格 | 批准判定 | 导师原文 | 最终内容 |
|---|---|---|---|
| R1C1 | KEEP：逐字保留 | `Flat` | `Flat` |
| R1C2 | KEEP：逐字保留 | `Multi-agent debate` | `Multi-agent debate` |
| R1C3 | KEEP：逐字保留 | `\citet{du2024multiagent_debate}` | `\citet{du2024multiagent_debate}` |
| R1C4 | KEEP：逐字保留 | `Peer critique and aggregation can add independent answer paths` | `Peer critique and aggregation can add independent answer paths` |
| R1C5 | KEEP：逐字保留 | `Tasks needing competing factual or reasoning views` | `Tasks needing competing factual or reasoning views` |
| R1C6 | R1C6：用户批准的最小修正 | `Cost, degeneration, and aggregation sensitivity` | `Cost and aggregation sensitivity` |
| R2C1 | STRUCTURAL FIX | `Flat` | `Hierarchical$^{a}$` |
| R2C2 | KEEP：逐字保留 | `Role-conditioned collaboration` | `Role-conditioned collaboration` |
| R2C3 | KEEP：逐字保留 | `CAMEL \citep{li2023camel}` | `CAMEL \citep{li2023camel}` |
| R2C4 | KEEP：逐字保留 | `Personas structure interaction but do not by themselves establish QA gains` | `Personas structure interaction but do not by themselves establish QA gains` |
| R2C5 | KEEP：逐字保留 | `Exploratory collaboration and prompt-role studies` | `Exploratory collaboration and prompt-role studies` |
| R2C6 | KEEP：逐字保留 | `Fixed roles or correlated perspectives` | `Fixed roles or correlated perspectives` |
| R3C1 | STRUCTURAL FIX | `Flat` | `---` |
| R3C2 | KEEP：逐字保留 | `Group-chat collaboration` | `Group-chat collaboration` |
| R3C3 | KEEP：逐字保留 | `AutoGen \citep{wu2024autogen}` | `AutoGen \citep{wu2024autogen}` |
| R3C4 | KEEP：逐字保留 | `Developer-defined speaker selection and dialogue patterns` | `Developer-defined speaker selection and dialogue patterns` |
| R3C5 | KEEP：逐字保留 | `Applications requiring configurable conversations` | `Applications requiring configurable conversations` |
| R3C6 | KEEP：逐字保留 | `Topology and QA performance depend on configuration` | `Topology and QA performance depend on configuration` |
| R4C1 | KEEP：逐字保留 | `Hierarchical` | `Hierarchical` |
| R4C2 | KEEP：逐字保留 | `Manager--executor pattern` | `Manager--executor pattern` |
| R4C3 | KEEP：逐字保留 | `MetaGPT \citep{hong2024metagpt}` | `MetaGPT \citep{hong2024metagpt}` |
| R4C4 | KEEP：逐字保留 | `Manager assigns staged work to specialised executors` | `Manager assigns staged work to specialised executors` |
| R4C5 | KEEP：逐字保留 | `Structured engineering workflows` | `Structured engineering workflows` |
| R4C6 | KEEP：逐字保留 | `Planner bottleneck and error propagation` | `Planner bottleneck and error propagation` |
| R5C1 | KEEP：逐字保留 | `Hierarchical` | `Hierarchical` |
| R5C2 | MINIMAL FIX | `Plan--retrieve--generate pipeline` | `Staged evidence-processing pipeline` |
| R5C3 | MINIMAL FIX | `LONGAGENT; Chain-of-Agents; CoCoA \citep{zhao2024longagent,zhang2024chain_agents,jiang2026cocoa}` | `LONGAGENT; Chain-of-Agents; CoCoA-zero \citep{zhao2024longagent,zhang2024chain_agents,jiang2026cocoa}` |
| R5C4 | KEEP：逐字保留 | `Explicit sequencing and final synthesis over distributed evidence` | `Explicit sequencing and final synthesis over distributed evidence` |
| R5C5 | KEEP：逐字保留 | `Long-document or knowledge-intensive QA` | `Long-document or knowledge-intensive QA` |
| R5C6 | KEEP：逐字保留 | `Information loss and coordination cost at synthesis` | `Information loss and coordination cost at synthesis` |
| R6C1 | STRUCTURAL FIX | `Hybrid` | `---` |
| R6C2 | KEEP：逐字保留 | `Graph-structured agent networks` | `Graph-structured agent networks` |
| R6C3 | KEEP：逐字保留 | `GPTSwarm; LangGraph \citep{zhuge2024gptswarm,langgraph2024}` | `GPTSwarm; LangGraph \citep{zhuge2024gptswarm,langgraph2024}` |
| R6C4 | MINIMAL FIX | `Graph transitions permit loops, branches, and routing policies` | `GPTSwarm DAG connection optimisation; LangGraph transitions permit loops, branches, and routing policies` |
| R6C5 | KEEP：逐字保留 | `Workflows with conditional state transitions` | `Workflows with conditional state transitions` |
| R6C6 | KEEP：逐字保留 | `Different evidence roles; difficult debugging and tracing` | `Different evidence roles; difficult debugging and tracing` |
| R7C1 | STRUCTURAL FIX | `Hybrid` | `Hierarchical$^{b}$` |
| R7C2 | KEEP：逐字保留 | `Adaptive collaboration-mode switching` | `Adaptive collaboration-mode switching` |
| R7C3 | KEEP：逐字保留 | `MDAgents \citep{kim2024mdagents}` | `MDAgents \citep{kim2024mdagents}` |
| R7C4 | KEEP：逐字保留 | `Changes collaboration in response to case characteristics` | `Changes collaboration in response to case characteristics` |
| R7C5 | KEEP：逐字保留 | `Tasks with heterogeneous requirements` | `Tasks with heterogeneous requirements` |
| R7C6 | KEEP：逐字保留 | `Routing policy must be evaluated, not assumed beneficial` | `Routing policy must be evaluated, not assumed beneficial` |
| R8C1 | STRUCTURAL FIX | `Hybrid` | `---` |
| R8C2 | KEEP：逐字保留 | `Human-in-the-loop design pattern` | `Human-in-the-loop design pattern` |
| R8C3 | MINIMAL FIX | `LangGraph breakpoints \citep{langgraph2024}` | `LangGraph breakpoints \citep{langgraph2024interrupt}` |
| R8C4 | KEEP：逐字保留 | `Human review at explicitly defined decision points` | `Human review at explicitly defined decision points` |
| R8C5 | KEEP：逐字保留 | `High-risk workflows requiring accountability` | `High-risk workflows requiring accountability` |
| R8C6 | KEEP：逐字保留 | `Direct comparative QA evidence remains limited` | `Direct comparative QA evidence remains limited` |

## 编译与一致性

现有 APA7/Biber 流程完整通过：pdfLaTeX → Biber → pdfLaTeX → pdfLaTeX。PDF 共 23 页；Table 2 在第 7 页。Biber 在沙箱内启动失败后，仅以沙箱外现有 Biber 重试成功，没有改配置或安装。

参考文献池85、实际引用78、核心13未变；BCF引用集合与有效源码一致，BBL含78条；10个唯一交叉引用目标均存在。恢复独立的两行引用后，引用命令由135变136，键出现仍为180，不增加文献。

Q5评分6/2/2与来源9H/1F/0Hybrid、Triad的S归属均保留。所有其他正文、其他表格、hidden history、书目与现有图稿/PPTX/图稿PDF均按内容指纹保护；初次全量验证7662文件仅正文改变。最终再验525个非临时现有文件，除正文外检测到根目录6个编译产物并发更新，保留未回退，见concurrent_generated_changes.json。Figure 4 authority_v2路径保持，并由编译fls证实读取。

Table 2无Overfull hbox、无过大浮动体；全文无未定义引用/交叉引用及待重运行提示。文档其他位置仍有两条已有超宽提示：标题123.62721 pt及未改正文0.5575 pt，未扩大范围处理。

本轮脚本没有向根目录发布/复制编译产物。但根目录manuscript.pdf及aux/bcf/blg/log/synctex.gz在16:37:18被并发编译过程更新，其日志声明Output written on manuscript.pdf，与本轮独立输出目录不同。未将并发变化误报为字节不变，也未覆盖/还原。Git HEAD/分支/索引未动；本轮新PDF为 output/pdf/table2_minimal_20261014.pdf；完整修改补丁 before_after.patch；逐格结构化记录 cell_verification.json；编译检查 compile_acceptance.json。

最终第7页与Table 2放大预览已实际检查：六列左对齐后无异常拉伸字间距，长机制名自然断行，未见文字裁切、重叠或溢出；原字号/行距保留，表注完整且可读，页面下部双栏正常。最终预览为preview/final_table2.png；修改前第7页为preview/before_table2_page.png。本轮只针对Table 2及关联页面视觉验收，未重新审计其他图表。
