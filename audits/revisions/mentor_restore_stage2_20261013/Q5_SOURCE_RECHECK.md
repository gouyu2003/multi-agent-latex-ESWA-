# Q5来源再核查与逐例评分

2026-10-13。MedAgents正式ACL全文及LLM-MedQA正式IJCNN2025全文重新核读；其余八例沿用已批准方法证据及冻结P/S。

## F1/F2/F3证据

| 案例 | F1 | F2 | F3 | 定位与边界 |
|---|---|---|---|---|
| tang2024medagents | 成立 | 成立 | 成立 | ACL 2024 §§2.1–2.5, Algorithm1, printed601–603；各领域专家给出分析；全专家用同一yes/no提示审同一报告；no产生修改意见并进入更新后重审。t上限；固定报告修订和最终决策仍H。 |
| tang2025llmmedqa | 成立 | 成立 | 成立 | 正式IJCNN2025 §§III-A–F, Algorithm1, physical3–6；v1作补充；question与option专家逐角色分析；共同报告交所有专家同规则Approve/Reject；Reject意见整合进修订并重投。Algorithm1有k上限；§III-F固定MakeDecision仍H。F1是角色贡献，不是统计独立；option分析可参照question分析。 |

MedAgents的全专家复核见Algorithm1 for i=1…n；LLM-MedQA的for each expert采用同一pvote。二者专家反对意见进入固定修订模型，后续轮次再审；达到上限时并不保证一致。LLM-MedQA算法的c_draft/current_draft/cc_draft名称不完全一致，§III-E及式(7)清楚说明修订与再次复核；本轮不执行原论文代码，也不据伪代码证明实现性能。

正式LLM-MedQA PDF SHA256：4c27d253f6df5b9834392cc4550db905b3e47eaf6e3732a414c76480398d226b。原本方案的不可重读限制在当前机器已解除。旧方案/旧台账保留原样，只在本轮记录及新表注更新。

[MedAgents ACL正式论文](https://aclanthology.org/2024.findings-acl.33.pdf)；[LLM-MedQA v1补充文本](https://arxiv.org/html/2501.05464v1)。正式IJCNN PDF位于用户本地10.10ziliao目录，保护副本及全文提取见q5_sources。

## 十案例

| 案例 | 角色 | P | S | 评分 | 依据 |
|---|---|---|---|---|---|
| MedAgents | I | Flat | Hierarchical | 部分一致 | 各领域专家给出分析；全专家用同一yes/no提示审同一报告；no产生修改意见并进入更新后重审。t上限；固定报告修订和最终决策仍H。 |
| LLM-MedQA | I | Flat | Hierarchical | 部分一致 | question与option专家逐角色分析；共同报告交所有专家同规则Approve/Reject；Reject意见整合进修订并重投。Algorithm1有k上限；§III-F固定MakeDecision仍H。F1是角色贡献，不是统计独立；option分析可参照question分析。 |
| LegalGraphRAG | I | Hybrid | Hierarchical | 不一致 | Researcher→Auditor→Adjudicator固定不对称链；没有来源定位的决策权配置切换。 |
| Triad | S | Hierarchical | Hierarchical | 广泛一致 | One multi-role agent follows staged Text-to-SPARQL processing; hierarchical describes its workflow, not a qualifying multi-agent study. |
| LONGAGENT | I | Hierarchical | Hierarchical | 广泛一致 | The leader selects query or conflict-resolution actions and makes the final answer from member evidence. |
| ChatDev | S | Hierarchical | Hierarchical | 广泛一致 | An ordered ChatChain assigns instructor–assistant interactions across design, coding and testing phases. |
| AgentCoder | S | Hierarchical | Hierarchical | 广泛一致 | Programmer and test designer are LLM agents; a scripted executor controls testing acceptance and feedback. |
| Multiagent debate (Du) | I | Flat | Flat | 广泛一致 | Peer model instances exchange critiques using the same update procedure; repeated rounds retain peer control. |
| EduPlanner | S | Flat | Hierarchical | 不一致 | evaluator具有固定评分权，optimizer/analyst给出反馈；不是各专家对同一共同报告具同等复核权限。 |
| Financial Reflection QA | I | Hierarchical | Hierarchical | 广泛一致 | Two critics give sequential feedback to an expert that revises the answer; repeated multi-turn debate is future work. |

复算：6广泛一致、2部分一致、2不一致；9H/1F/0Hybrid，分母10。作者回顾性组织相容分析，非预测准确率、独立验证、实测性能或安全提升。