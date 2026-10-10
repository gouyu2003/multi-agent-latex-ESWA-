# 十案例控制权分类复核

日期：2026-10-10。保留此前建议标签，来源流程使用统一规则重编码。
稳定调度、审批或最终决策权归为层级；没有持续上级控制的对等更新归为扁平；混合需要实际控制权切换的证据。反馈、投票、图结构或多角色本身不足以认定混合。

六例一致、四例不一致；来源流程9层级、1扁平、0混合。这是本文回顾性解释，不是原作者自报类别、独立盲评或预测准确率；当前样本不能验证混合分支。

| 案例 | 角色 | 原建议 | 来源流程编码 | 匹配 | 原文位置与依据 |
|---|---|---|---|---|---|
| MedAgents | I | Flat | Hierarchical | 不一致 | [§§2.1–2.5, Algorithm1, printed601–603](https://aclanthology.org/2024.findings-acl.33.pdf)：Experts analyse and vote; fixed report revision and final decision roles retain asymmetric authority. |
| LLM-MedQA | I | Flat | Hierarchical | 不一致 | [Formal IJCNN2025 §§III-A–F, Fig2 and Algorithm1, physical pp3–6](D:/multi-agent review_joural/10.10ziliao/LLM-MedQA_Enhancing_Medical_Question_Answering_through_Case_Studies_in_Large_Language_Models (1).pdf)：Several experts vote on a report; a fixed revision and decision pipeline controls the final answer. |
| LegalGraphRAG | I | Hybrid | Hierarchical | 不一致 | [Formal ACL2026 §4.3, printed37459–37460; Fig3](https://aclanthology.org/2026.acl-long.1738.pdf)：Researcher, Auditor and Adjudicator perform ordered retrieval, audit and synthesis; graph structure does not switch authority. |
| Triad | S | Hierarchical | Hierarchical | 一致 | [Formal EMNLP2024 §3, printed1700–1702](https://aclanthology.org/2024.emnlp-main.101.pdf)：One multi-role agent follows staged Text-to-SPARQL processing; hierarchical describes its workflow, not a qualifying multi-agent study. |
| LONGAGENT | I | Hierarchical | Hierarchical | 一致 | [Formal EMNLP2024 §§2.1–2.4, Fig2, printed16311–16313](https://aclanthology.org/2024.emnlp-main.912.pdf)：The leader selects query or conflict-resolution actions and makes the final answer from member evidence. |
| ChatDev | S | Hierarchical | Hierarchical | 一致 | [Formal ACL2024 §3.1 and Fig2, printed15176–15177](https://aclanthology.org/2024.acl-long.810.pdf)：An ordered ChatChain assigns instructor–assistant interactions across design, coding and testing phases. |
| AgentCoder | S | Hierarchical | Hierarchical | 一致 | [arXiv2312.13010v1 §§3.1–3.4, Fig1, pp3–4](https://arxiv.org/pdf/2312.13010v1)：Programmer and test designer are LLM agents; a scripted executor controls testing acceptance and feedback. |
| Multiagent debate (Du) | I | Flat | Flat | 一致 | [Formal ICML2024 §§2.1–2.2, Fig2–3, physical pp2–4; peer updates and rule-based majority at end of debate](https://raw.githubusercontent.com/mlresearch/v235/main/assets/du24e/du24e.pdf)：Peer model instances exchange critiques using the same update procedure; repeated rounds retain peer control. |
| EduPlanner | S | Flat | Hierarchical | 不一致 | [Formal TLT2025 Fig3, §§III-C–E, Algorithms1–3, printed419–422](D:/multi-agent review_joural/10.10ziliao/EduPlanner_LLM-Based_Multiagent_Systems_for_Customized_and_Intelligent_Instructional_Design.pdf)：Evaluator scoring and the optimizer/analyst workflow impose stable selection and revision authority. |
| Financial Reflection QA | I | Hierarchical | Hierarchical | 一致 | [Formal ICAIF2024 §3.1, printed532; §6, printed534](D:/multi-agent review_joural/10.10ziliao/Enhancing Financial Question Answering with a Multi-Agent Reflection Framework.pdf)：Two critics give sequential feedback to an expert that revises the answer; repeated multi-turn debate is future work. |

Triad是单智能体多角色流程，作为S支持例子；ChatDev/AgentCoder代码任务、EduPlanner教学设计均不纳入核心QA研究。AgentCoder v1的executor是脚本，不能据三个命名角色认定三个LLM智能体。
