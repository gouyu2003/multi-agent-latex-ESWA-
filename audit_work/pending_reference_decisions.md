# 参考文献与证据边界待确认清单

日期：2026-10-08。确定错误已修正；以下不确定项保留，不自动替作者选择版本或调整纳入范围。

| 项目 | 当前处理 | 后续具体步骤 |
|---|---|---|
| Triad纳入标准 | 保留I编码及十案例比较，正文披露一个LLM三角色 | 由作者裁定独立多代理标准。若严格要求≥2独立代理，改为S并重算I/S和图中数量；是否保留十案例诊断另行说明。 |
| 书籍/预印本版本 | 保留当前Minsky版次、GPT-4/MemGPT/ChatLaw等版本冲突 | 固定实际使用的版次或arXiv vN；核对该版本作者、年份及链接后一致更新。citation key无需改名。 |
| 网页与PDF作者冲突 | GAIA、DSPy、Self-RAG、LegalBench等不盲改姓名 | 取得正式PDF首页，与官方HTML/版本历史逐项核对，记录冲突与采用理由。 |
| 未直接核实的出版字段 | LLM-MedQA、Financial Reflection QA、SWE-agent等部分页码或DOI保留未核实状态 | 以本条出版商元数据或论文PDF核实；另一论文的参考文献仅作间接线索。 |
| 软件与协议版本 | Dify/RAGFlow/CrewAI、MCP/A2A等保留历史版本限制 | 若论述特定年份能力，固定release/tag/commit或当时文档；当前文档只支持当前能力。 |
| 历史检索过程 | 108候选、四异常等写为历史日志记录 | 若需方法复现，补原始检索导出和筛选记录；本次核查不替代当年的实际检索凭证。 |
| 图片同步 | 原图未修改，图注已标历史快照 | 统一pool85、active78及I14边界说明；核对所有图内84 active、旧角色数量和CoCoA等标签，再缩小字体导出。 |
| AI绘图来源 | 保留AI使用披露，去掉不存在的图引用 | 图片阶段确认Nano Banana所对应的实际采用图及编辑来源，若未采用则准确说明。 |

逐字段未决记录共183项（含非必填附加字段，不等于183篇文献有错误）；完整值、状态与证据见[CSV](pending_reference_decisions.csv)。

## 版本/来源冲突的具体字段

| key | 字段 | 当前值 | 来源值/冲突 |
|---|---|---|---|
| minsky1988society | year | 1986 | 1988 for the linked ISBN edition; 1986 only if a different first-edition source is selected |
| khattab2024dspy | author | Khattab, Omar and Singhvi, Arnav and Maheshwari, Paridhi and Zhang, Zhiyuan and Santhanam, Keshav and A, Sri Vardhamanan and Haq, Saiful and Sharma, Ashutosh and Joshi, Thomas and Moazam, Hanna and Miller, Heather and Zaharia, Matei and Potts, Christopher | {"pdf": "Sri Vardhamanan; Thomas T. Joshi", "landing_page": "Sri Vardhamanan A; Thomas Joshi"} |
| khattab2024dspy | title | {DSPy}: Compiling Declarative Language Model Calls into State-of-the-Art Pipelines | {"preferred_pdf": "DSPy: Compiling Declarative Language Model Calls into Self-Improving Pipelines", "landing_page": "{DSPy}: Compiling Declarative Language Model Calls into State-of-the-Art Pipelines"} |
| packer2023memgpt | url | https://arxiv.org/abs/2310.08560 | https://arxiv.org/abs/2310.08560v1 |
| asai2024selfrag | author | Asai, Akari and Wu, Zeqiu and Wang, Yizhong and Sil, Avi and Hajishirzi, Hannaneh | {"landing_page": "Zeqiu Wu; Avi Sil", "pdf": "Zeqi Wu; Avirup Sil"} |
| cui2023chatlaw | url | https://arxiv.org/abs/2306.16092 | https://arxiv.org/abs/2306.16092v1 |
| guha2023legalbench | author | Guha, Neel and Nyarko, Julian and Ho, Daniel and R{\'e}, Christopher and Chilton, Adam and K, Aditya and Chohlas-Wood, Alex and Peters, Austin and Waldon, Brandon and Rockmore, Daniel and Zambrano, Diego and Talisman, Dmitry and Hoque, Enam and Surani, Faiz and Fagan, Frank and Sarfaty, Galit and Dickinson, Gregory and Porat, Haggai and Hegland, Jason and Wu, Jessica and Nudell, Joe and Niklaus, Joel and Nay, John and Choi, Jonathan and Tobia, Kevin and Hagan, Margaret and Ma, Megan and Livermore, Michael and Rasumov-Rahe, Nikon and Holzenberger, Nils and Kolt, Noam and Henderson, Peter and Rehaag, Sean and Goel, Sharad and Gao, Shang and Williams, Spencer and Gandhi, Sunny and Zur, Tom and Iyer, Varun and Li, Zehua | {"preferred_pdf_sixth_author": "Narayana, Aditya", "landing_page_sixth_author": "K, Aditya", "other_full_names": "Daniel E. Ho; Daniel N. Rockmore; Gregory M. Dickinson; Jonathan H. Choi"} |
| anthropic2024mcp | author | {Anthropic} | — |
| anthropic2024mcp | title | Model Context Protocol ({MCP}): Technical Specification | — |
| google2025a2a | author | {Google} | — |
| dify2024 | author | {Dify.AI} | — |
| dify2024 | title | {Dify: Open-source LLM App Development Platform} | — |
| dify2024 | year | 2024 | — |
| ragflow2024 | author | {InfiniFlow} | — |
| ragflow2024 | title | {RAGFlow}: An Open-Source {RAG} Engine Based on Deep Document Understanding | — |
| ragflow2024 | year | 2024 | — |
| mialon2024gaia | author | Mialon, Gr{\'e}goire and Fourrier, Cl{\'e}mentine and Wolf, Thomas and LeCun, Yann and Scialom, Thomas | Mialon, Grégoire and Fourrier, Clémentine and Swift, Craig and Wolf, Thomas and LeCun, Yann and Scialom, Thomas |

## 未核实字段按记录列出

| key | 未决字段及状态 |
|---|---|
| brown2020gpt3 | number:未核实, pages:未核实, doi:未核实 |
| openai2023gpt4 | doi:未核实, type:未核实 |
| minsky1988society | year:版本/来源冲突, volume:未核实, number:未核实, pages:未核实, doi:未核实 |
| wooldridge1995intelligent | publisher:未核实 |
| wu2024autogen | title:未核实, year:未核实, venue:未核实, volume:未核实, number:未核实, pages:未核实, doi:未核实, url:未核实, type:未核实 |
| hong2024metagpt | doi:未核实 |
| du2024multiagent_debate | doi:未核实, series:未核实, publisher:未核实 |
| tran2025multiagent_survey | doi:未核实, type:未核实 |
| wang2024survey_autonomous_agents | number:未核实, publisher:未核实 |
| kwiatkowski2019natural_questions | publisher:未核实 |
| reddy2019coqa | publisher:未核实 |
| lewis2020rag | number:未核实, pages:未核实, doi:未核实 |
| yao2023react | doi:未核实 |
| vaswani2017attention | number:未核实, pages:未核实, doi:未核实 |
| devlin2019bert | volume:未核实 |
| touvron2023llama | doi:未核实, type:未核实 |
| glm2024chatglm | doi:未核实, type:未核实 |
| ouyang2022instructgpt | author:建议规范化, number:未核实 |
| qian2024scaling_multiagent | doi:未核实 |
| park2023generative_agents | author:建议规范化, volume:未核实, number:未核实, pages:未核实 |
| li2023camel | author:建议规范化, number:未核实 |
| qian2023chatdev | volume:未核实 |
| gao2024rag_survey | doi:字段不完整 |
| shen2024hugginggpt | number:未核实, pages:未核实 |
| zhao2024longagent | author:建议规范化 |
| khattab2024dspy | author:版本/来源冲突, title:版本/来源冲突, pages:未核实, doi:未核实 |
| duan2024langgraph_crewai | doi:未核实 |
| zhuge2024gptswarm | doi:未核实 |
| chen2024agentverse | pages:未核实, doi:未核实 |
| kim2024mdagents | number:未核实, pages:未核实 |
| zhou2023least_to_most | volume:未核实, number:未核实, pages:未核实, doi:未核实 |
| khot2023decomposed_prompting | volume:未核实, number:未核实, pages:未核实, doi:未核实 |
| packer2023memgpt | doi:未核实, url:版本/来源冲突, publisher:未核实 |
| zhang2024memory_survey | publisher:未核实 |
| asai2024selfrag | author:版本/来源冲突, pages:未核实, doi:未核实 |
| wei2022chain_of_thought | number:未核实, pages:未核实 |
| wang2023self_consistency | volume:未核实, number:未核实, pages:未核实, doi:未核实 |
| yao2023tree_of_thoughts | author:建议规范化, number:未核实, pages:未核实 |
| shinn2023reflexion | number:未核实, pages:未核实 |
| madaan2023self_refine | number:未核实, pages:未核实 |
| cui2023chatlaw | doi:未核实, url:版本/来源冲突 |
| li2024genmentor | pages:未核实 |
| singhal2023medpalm | number:未核实, publisher:未核实 |
| guha2023legalbench | author:版本/来源冲突, number:未核实, pages:未核实 |
| brynjolfsson2023generative_ai_work | publisher:未核实 |
| yang2024swe_agent | number:未核实, pages:未核实 |
| jimenez2024swe_bench | pages:未核实, doi:未核实 |
| han2024mast | number:未核实, pages:未核实 |
| anthropic2024mcp | author:版本/来源冲突, title:版本/来源冲突, venue:未核实, doi:未核实, url:未核实 |
| google2025a2a | author:版本/来源冲突, title:未核实, venue:未核实, doi:未核实, url:未核实 |
| langgraph2024 | venue:未核实, doi:未核实, note:未核实 |
| crewai2023 | venue:未核实, doi:未核实 |
| dify2024 | author:版本/来源冲突, title:版本/来源冲突, year:版本/来源冲突, venue:未核实, doi:未核实, note:未核实 |
| tang2025llmmedqa | pages:未核实, url:未核实, organization:未核实 |
| legalgraphrag2026 | publisher:未核实 |
| huang2023agentcoder | volume:未核实, number:未核实, pages:未核实, doi:字段不完整, url:未核实 |
| zhang2024eduplanner | title:建议规范化, number:未核实, url:未核实, publisher:未核实 |
| fatemi2024financialqa | venue:未核实, pages:未核实, url:未核实 |
| peffers2007dsrm | url:未核实, publisher:未核实 |
| xagent2023 | venue:未核实, doi:未核实 |
| chen2024reconcile | publisher:未核实 |
| zhang2024chain_agents | author:建议规范化, pages:未核实 |
| jiang2026cocoa | publisher:未核实 |
| shao2024storm | author:建议规范化, publisher:未核实 |
| shao2024costorm | author:建议规范化, publisher:未核实 |
| ragflow2024 | author:版本/来源冲突, title:版本/来源冲突, year:版本/来源冲突, venue:未核实, doi:未核实, note:未核实 |
| hendrycks2021mmlu | pages:未核实, doi:未核实, url:未核实 |
| trivedi2022musique | title:建议规范化, number:未核实, publisher:未核实 |
| liu2024agentbench | pages:未核实, doi:未核实 |
| mialon2024gaia | author:版本/来源冲突, pages:未核实, doi:未核实, url:未核实 |
| zhou2024webarena | pages:未核实, doi:未核实 |
| autorag2024 | volume:未核实, number:未核实, pages:未核实, doi:字段不完整 |
| langgraph2024interrupt | doi:未核实 |

## 正文证据边界

当前台账对作者综合、前瞻建议和来源获取限制继续单独标记。对于未修正且证据仍不足的具体断言，须取得原文证据或进一步收窄；不得因结构检查通过而标成已验证。

| 引用ID | 当前支持程度 | 后续/保留理由 |
|---|---|---|
| C009 | 部分支持/表述需收窄 | Current wording re-read against retained source evidence. Source confirms identity, not the manuscript's historical update-search action; link internal dated search evidence. |
| C010 | 部分支持/表述需收窄 | Current wording re-read against retained source evidence. Keep identity; independently document when it was added and what metadata fields were verified. |
| C011 | 部分支持/表述需收窄 | Current wording re-read against retained source evidence. Keep eligible July 2026 record; distinguish paper identity from proof that a targeted search added it. |
| C026 | 作者推论，须标明边界 | Retain the 'Inspired by' framing. The edition/year conflict remains a bibliography question; this conceptual analogy is not a validated LLM result. |
| C031 | 多来源支持程度不同 | Retain 'may' and the comparison's task-conditional scope.<br>Current wording re-read against retained source evidence. Keep the qualified may-correct-errors claim; avoid universal superiority to self-refinement based on abstract evidence.<br>Retain the grouped conditional claim because Du supplies the reflection comparison; avoid attributing a universal self-refinement superiority result to Xiong. |
| C049 | 作者推论，须标明边界 | Retain the mechanism row and explicit author-synthesis statement; the risk/suitability cells are not claimed as source-validated selection results. |
| C050 | 作者推论，须标明边界 | Retain the row and synthesis qualification; no comparative QA superiority is asserted. |
| C052 | 作者推论，须标明边界 | Retain the supported role mechanism and table-level synthesis qualification. |
| C053 | 多来源支持程度不同 | 保留；任务适配及聚合限制为本文分析。<br>Staged evidence-processing row and CoCoA-zero name corrected. Keep hierarchical placement as review coding, not the source authors' original label. |
| C054 | 多来源支持程度不同 | 保留已区分的机制；本项仅核GPTSwarm部分。<br>Current wording re-read against retained source evidence. Keep technical capabilities; hybrid placement is author classification, not a reported original label. |
| C056 | 作者推论，须标明边界 | HITL source mismatch resolved by the independent December 2024 official article. Checkpointed interruption/review/resume is supported; high-risk usefulness or architecture placement is a design interpretation, not an evaluated safety guarantee. |
| C057 | 作者推论，须标明边界 | Cost-benefit threshold is now explicitly the review's design criterion. Retain the sourced failure-mode motivation without attributing the entire overhead list or threshold to MAST. |
| C058 | 作者推论，须标明边界 | Current wording re-read against retained source evidence. Retain attribution; distinguish borrowing DSRM from empirical validation of this review's proposed artifact. |
| C059 | 作者推论，须标明边界 | 保留作者编码；不作为来源自报架构标签或已量化风险结果。 |
| C060 | 作者推论，须标明边界 | Current wording re-read against retained source evidence. Retain MCQ/voting workflow; attach coding rationale for flat/hybrid labels and match marker. |
| C061 | 作者推论，须标明边界 | Current wording re-read against retained source evidence. Retain verdict/audit mechanism; high-risk profile and hybrid label are author judgments, not validated safety guarantees. |
| C062 | 作者推论，须标明边界 | Enterprise claim corrected. Retain the KBQA/SPARQL description and disclosed single-agent multi-role boundary; author decision on role-I eligibility remains pending. |
| C063 | 作者推论，须标明边界 | 保留明确的作者编码，不声称来源自报匹配结论。 |
| C064 | 作者推论，须标明边界 | Retain the illustrated coding/checkmark and explicit evidence boundary. |
| C065 | 作者推论，须标明边界 | Current wording re-read against retained source evidence. Retain dependencies/feedback loop; record taxonomy coding and pin the consulted arXiv version. |
| C066 | 作者推论，须标明边界 | Retain the diagnostic row and author-coding note; do not interpret the score as independently validated selection accuracy. |
| C067 | 作者推论，须标明边界 | Current wording re-read against retained source evidence. Retain educational workflow; justify hierarchical classification rather than attributing that label directly to the source. |
| C068 | 作者推论，须标明边界 | Self-critique wording corrected to critic feedback. Mechanism supported; hybrid classification and match marker remain review coding. |
| C073 | 多来源支持程度不同 | Present the criteria as design guidance inferred from the cited mechanisms, with task-level validation still needed.<br>Retain as mechanism evidence and mark the selection criterion as review synthesis.<br>Current wording re-read against retained source evidence. Keep interface-layer distinction; present traceability/state/cost selection criteria as review synthesis.<br>Current wording re-read against retained source evidence. Keep interoperability distinction; avoid claiming one topology or empirical QA reliability from protocol existence. |
| C083 | 部分支持/表述需收窄 | 保留当前宽泛限定；待正式TOIS全文核对定位，不能称正式全文已确认。 |
| C098 | 多来源支持程度不同 | 保留当前方法描述；正式元数据已同步，未读OpenReview全文的范围限制保留。<br>Retain the debate-specific portion; other methods in the sentence are assessed under their own citations.<br>Current wording re-read against retained source evidence. Retain mechanism distinction; communication loss and stopping-cost generalizations are review synthesis.<br>保留当前限定表述；来源支持上列具体机制，作者条件分析不作为该文实测结果。 |
| C109 | 作者推论，须标明边界 | Graph state transitions and developer-defined nodes supported; hybrid label and suitability for long-running QA remain author interpretation. Checkpoint recovery is supported by the separately cited interrupt source.<br>Persistent checkpoints and resumption supported. Hybrid label and long-running QA suitability are review coding; do not claim an evaluated QA recovery benefit. |
| C112 | 部分支持/表述需收窄 | Current wording re-read against retained source evidence. Retain interface/control distinction; do not treat specification existence as proof of effective collaboration. |
| C115 | 部分支持/表述需收窄 | Current wording re-read against retained source evidence. Keep engineering description with a fixed release/commit and honest access-date provenance. |
| C124 | 部分支持/表述需收窄 | Current wording re-read against retained source evidence. Retain mixed-objective example; topology-selection implications are review synthesis. |
| C125 | 部分支持/表述需收窄 | Current wording re-read against retained source evidence. Retain numerical QA/critic iteration; multi-label architecture interpretation is author synthesis. |
| C127 | 作者推论，须标明边界 | Prior exhaustive process-analysis implication removed. The claim now distinguishes outcome scores from evidence about individual collaboration mechanisms; this is explicit review inference.<br>Retain the corrected acknowledgment of supporting-fact metrics and the outcome-versus-process qualification. |
| C128 | 作者推论，须标明边界 | Unverified prevalence assertion removed. Named MAST categories are supported; complementary contribution/error-correction measures are now proposed as review synthesis. |
| C129 | 作者推论，须标明边界 | 保留医学背景引用和明确的作者规范性建议。<br>保留背景引用；书目版本链接差异仍pending。 |
| C131 | 多来源支持程度不同 | Retain the claim; the requirement for validation before deployment is the review's recommendation, not an empirical AutoGen deployment guarantee.<br>Reusable graph/nested workflow components supported. Current paragraph explicitly treats automatic declarative assembly as a proposal requiring validation.<br>The pinned 0.1.0 description supports basic roles, assigned tasks and reusable Crew/Process components. Broader historical capabilities and automatic architecture assembly are not established by this source.<br>Current wording re-read against retained source evidence. Pin release/commit supporting the claim; do not present a mutable current README as dated 2024 evidence. |
| C135 | 多来源支持程度不同 | 保留组件级未来建议；来源/时间戳/置信度要求为本文建议，正式全文定位pending。<br>保留当前限定表述；来源支持上列具体机制，作者条件分析不作为该文实测结果。 |
| C136 | 前瞻建议，非原论文验证 | Keep 'could' and identify learned team coordination as a research proposal inspired by memory mechanisms; do not imply Park validated those team policies.<br>保留could与future directions边界；不把未来team-policy学习标为该文已验证结果。 |
