# 阶段二逐项实际执行记录

2026-10-13。导师基线 f84c78b；执行前 HEAD 6191a1b。119项：A64/B25/C30。

before/after 为实际片段或同段必要联动片段。表内移动的条目附完整共同操作，不能将同一表的联动重复当作新授权。完整顺序补丁见 operations.json 和 before_after.patch。

## D001 — A — 必要纠错成果保留；共享片段仅按批准B/C边界恢复

操作编号：[]。

**before**
```tex
% !BIB program = biber

```

**after**
```tex
% !BIB program = biber
```

## D002 — A — 必要纠错成果保留；共享片段仅按批准B/C边界恢复

操作编号：[]。

**before**
```tex
% ESWA APA seventh edition; preserve existing natbib citation commands.
\input{eswa-apa-config.tex}
\addbibresource{references.bib}

```

**after**
```tex
% ESWA APA seventh edition; preserve existing natbib citation commands.
\input{eswa-apa-config.tex}
\addbibresource{references.bib}
```

## D003a — A — 必要纠错成果保留；共享片段仅按批准B/C边界恢复

操作编号：[1]。

**before**
```tex
review of multi-agent collaborative QA using 78 cited sources from an
85-record bibliography pool, with 13 studies coded as core
evidence published through July 2026. We first

```

**after**
```tex
review of multi-agent collaborative QA based on 78 cited sources from an
85-record bibliography pool, including 13 core empirical studies
published through July 2026. We first
```

## D003b — B — 局部恢复

操作编号：[1]。

**before**
```tex
review of multi-agent collaborative QA using 78 cited sources from an
85-record bibliography pool, with 13 studies coded as core
evidence published through July 2026. We first

```

**after**
```tex
review of multi-agent collaborative QA based on 78 cited sources from an
85-record bibliography pool, including 13 core empirical studies
published through July 2026. We first
```

## D004 — B — 完整恢复

操作编号：[2]。

**before**
```tex
strong natural-language understanding and generation capabilities relevant
to QA.

```

**after**
```tex
extraordinary natural-language understanding and generation capabilities,
ushering QA systems into a new, agent-centric era.
```

## D005a — A — 必要纠错成果保留；共享片段仅按批准B/C边界恢复

操作编号：[3]。

**before**
```tex
\emph{Third}, a single model may lack sufficient domain coverage for a query
that requires several areas of expertise; combining perspectives is one
possible response whose benefit requires task-level evaluation.

```

**after**
```tex
\emph{Third}, a single model may lack sufficient domain coverage for a query
that requires several areas of expertise.
```

## D005b — B — 局部恢复

操作编号：[3]。

**before**
```tex
\emph{Third}, a single model may lack sufficient domain coverage for a query
that requires several areas of expertise; combining perspectives is one
possible response whose benefit requires task-level evaluation.

```

**after**
```tex
\emph{Third}, a single model may lack sufficient domain coverage for a query
that requires several areas of expertise.
```

## D006 — A — 必要纠错成果保留；共享片段仅按批准B/C边界恢复

操作编号：[]。

**before**
```tex
For example,

```

**after**
```tex
For example,
```

## D007 — C — Q1已执行（按批准方案联动）

操作编号：[4]。

**before**
```tex
Existing surveys cover general LLM-agent construction, communication,
and orchestration
\citep{guo2024llm_multiagent_survey,tran2025multiagent_survey,wang2024survey_autonomous_agents}.
This survey builds on that coverage by connecting collaboration topologies and enabling mechanisms
to QA-specific task and governance requirements and architecture-selection
trade-offs through five related contributions:

```

**after**
```tex
Although several surveys on LLM-based agents exist
\citep{guo2024llm_multiagent_survey,tran2025multiagent_survey,wang2024survey_autonomous_agents},
they primarily address general agent architectures, communication, orchestration,
and foundational capabilities, with some coverage of QA. A systematic account
of collaboration topologies, enabling mechanisms, task and governance
requirements, and architecture-selection trade-offs for QA remains limited.
This survey addresses that gap through five related contributions:
```

## D008 — A — 必要纠错成果保留；共享片段仅按批准B/C边界恢复

操作编号：[]。

**before**
```tex
        QA, based on a source-checked corpus with explicit roles for core empirical

```

**after**
```tex
        QA, based on a source-checked corpus with explicit roles for core empirical
```

## D009a — A — 必要纠错成果保留；共享片段仅按批准B/C边界恢复

操作编号：[]。

**before**
```tex
The historical audit log records an initial candidate set of 108 unique
entries from the authors' working bibliography and checks dated 2 August
2026 using Crossref, OpenAlex, arXiv, and official sources. It records four
corrupted or mismatched records for which an authoritative source was not
confirmed, together with duplicate, uncited, and out-of-scope records. These
historical records are retained in the audit trail; the log alone is not
independent evidence that every publication field was verified.

```

**after**
```tex
The historical audit log records an initial candidate set of 108 unique
entries from the authors' working bibliography and checks dated 2 August
2026 using Crossref, OpenAlex, arXiv, and official sources. It records four
corrupted or mismatched records for which an authoritative source was not
confirmed, together with duplicate, uncited, and out-of-scope records. These
historical records are retained in the audit trail; the log alone is not
independent evidence that every publication field was verified.
```

## D009b — C — Q3已执行（保留当前已符合批准规则的片段）

操作编号：[]。

**before**
```tex
The historical audit log records an initial candidate set of 108 unique
entries from the authors' working bibliography and checks dated 2 August
2026 using Crossref, OpenAlex, arXiv, and official sources. It records four
corrupted or mismatched records for which an authoritative source was not
confirmed, together with duplicate, uncited, and out-of-scope records. These
historical records are retained in the audit trail; the log alone is not
independent evidence that every publication field was verified.

```

**after**
```tex
The historical audit log records an initial candidate set of 108 unique
entries from the authors' working bibliography and checks dated 2 August
2026 using Crossref, OpenAlex, arXiv, and official sources. It records four
corrupted or mismatched records for which an authoritative source was not
confirmed, together with duplicate, uncited, and out-of-scope records. These
historical records are retained in the audit trail; the log alone is not
independent evidence that every publication field was verified.
```

## D010a — C — Q3已执行（保留当前已符合批准规则的片段）

操作编号：[5]。

**before**
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

**after**
```tex
The historical working records list ReConcile
\citep{chen2024reconcile}, Chain-of-Agents \citep{zhang2024chain_agents}, and
CoCoA \citep{jiang2026cocoa} as additions. The source audit confirms their
identities and publication dates; it does not reconstruct the original update
queries, retrieval results, or search dates.

Source-level checks on 8 and 10 October 2026 confirmed corrections in an
85-record bibliography pool with 78 actively cited sources; unavailable
optional fields and source discrepancies remain documented in the audit trail.
```

## D010b — A — 必要纠错成果保留；共享片段仅按批准B/C边界恢复

操作编号：[5]。

**before**
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

**after**
```tex
The historical working records list ReConcile
\citep{chen2024reconcile}, Chain-of-Agents \citep{zhang2024chain_agents}, and
CoCoA \citep{jiang2026cocoa} as additions. The source audit confirms their
identities and publication dates; it does not reconstruct the original update
queries, retrieval results, or search dates.

Source-level checks on 8 and 10 October 2026 confirmed corrections in an
85-record bibliography pool with 78 actively cited sources; unavailable
optional fields and source discrepancies remain documented in the audit trail.
```

## D010c — B — 局部恢复

操作编号：[5]。

**before**
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

**after**
```tex
The historical working records list ReConcile
\citep{chen2024reconcile}, Chain-of-Agents \citep{zhang2024chain_agents}, and
CoCoA \citep{jiang2026cocoa} as additions. The source audit confirms their
identities and publication dates; it does not reconstruct the original update
queries, retrieval results, or search dates.

Source-level checks on 8 and 10 October 2026 confirmed corrections in an
85-record bibliography pool with 78 actively cited sources; unavailable
optional fields and source discrepancies remain documented in the audit trail.
```

## D011 — B — 完整恢复

操作编号：[6]。

**before**
```tex
The core eligibility screen (role \textbf{I}) used five criteria:

```

**after**
```tex
Core included studies (role \textbf{I}) had to satisfy five criteria:
```

## D012 — C — Q2已执行（按批准方案联动）

操作编号：[7, 8]。

**before**
```tex
(4) QA, retrieval-augmented answering, conversational QA, or question-driven domain decision support as a substantive primary evaluation track; and

```

**after**
```tex
(4) QA, retrieval-augmented answering, conversational QA, or question-driven domain decision support as the primary evaluated task; and

QA may be a co-primary evaluated task, but incidental QA demonstrations are insufficient. When both a preprint and a peer-reviewed version of a work existed, the peer-reviewed final publication was preferred.
```

## D013a — A — 必要纠错成果保留；共享片段仅按批准B/C边界恢复

操作编号：[8, 9, 10]。

**before**
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

**after**
```tex
QA may be a co-primary evaluated task, but incidental QA demonstrations are insufficient. When both a preprint and a peer-reviewed version of a work existed, the peer-reviewed final publication was preferred.

The 13 role-I studies
provide the empirical basis for the architecture taxonomy and subsequent
evidence synthesis; other claims are supported by sources appropriate to their scope.
```

## D013b — C — Q2已执行（按批准方案联动）

操作编号：[8, 9]。

**before**
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

**after**
```tex
QA may be a co-primary evaluated task, but incidental QA demonstrations are insufficient. When both a preprint and a peer-reviewed version of a work existed, the peer-reviewed final publication was preferred.

The 13 role-I studies
provide the empirical basis for the architecture taxonomy and subsequent
evidence synthesis; other claims are supported by sources appropriate to their scope.
```

## D013c — B — 局部恢复

操作编号：[9, 10]。

**before**
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

**after**
```tex
QA may be a co-primary evaluated task, but incidental QA demonstrations are insufficient. When both a preprint and a peer-reviewed version of a work existed, the peer-reviewed final publication was preferred.

The 13 role-I studies
provide the empirical basis for the architecture taxonomy and subsequent
evidence synthesis; other claims are supported by sources appropriate to their scope.
```

## D014 — A — 必要纠错成果保留；共享片段仅按批准B/C边界恢复

操作编号：[]。

**before**
```tex
  \caption{Current bibliography pool and evidence-role composition of cited sources. The pool contains 85 records: 78 cited sources and seven uncited records. Under the authors' evidence-role classification, cited sources comprise 13 core studies (I), 15 supporting studies (S), 42 background sources (B), and eight technical resources (T); segment widths in the horizontal bar are proportional to these counts. AI tools assisted with plotting code and layout; counts are computed from the bibliography, active citations, and evidence-role table.}

```

**after**
```tex
  \caption{Current bibliography pool and evidence-role composition of cited sources. The pool contains 85 records: 78 cited sources and seven uncited records. Under the authors' evidence-role classification, cited sources comprise 13 core studies (I), 15 supporting studies (S), 42 background sources (B), and eight technical resources (T); segment widths in the horizontal bar are proportional to these counts. AI tools assisted with plotting code and layout; counts are computed from the bibliography, active citations, and evidence-role table.}
```

## D015 — A — 必要纠错成果保留；共享片段仅按批准B/C边界恢复

操作编号：[]。

**before**
```tex
which introduced an attention-only sequence-transduction architecture; BERT
\citep{devlin2019bert}, which advanced bidirectional pretraining and
task-specific fine-tuning; and GPT-3 \citep{brown2020gpt3} and GPT-4

```

**after**
```tex
which introduced an attention-only sequence-transduction architecture; BERT
\citep{devlin2019bert}, which advanced bidirectional pretraining and
task-specific fine-tuning; and GPT-3 \citep{brown2020gpt3} and GPT-4
```

## D016 — A — 必要纠错成果保留；共享片段仅按批准B/C边界恢复

操作编号：[]。

**before**
```tex
capabilities. Open-weight releases such as LLaMA \citep{touvron2023llama} and
ChatGLM \citep{glm2024chatglm} provide additional options for local
experimentation, while

```

**after**
```tex
capabilities. Open-weight releases such as LLaMA \citep{touvron2023llama} and
ChatGLM \citep{glm2024chatglm} provide additional options for local
experimentation, while
```

## D017 — A — 必要纠错成果保留；共享片段仅按批准B/C边界恢复

操作编号：[]。

**before**
```tex
[原文已删除：此处无当前文字]

```

**after**
```tex
[保留删除或格式成果；见保护验证及实际补丁]
```

## D018a — A — 必要纠错成果保留；共享片段仅按批准B/C边界恢复

操作编号：[11]。

**before**
```tex
\citep{minsky1988society}, multi-agent architectures can combine agents with
individual memory, reflection, and planning, as illustrated in social
simulations \citep{park2023generative_agents}. A single ``generalist'' workflow may combine

```

**after**
```tex
\citep{minsky1988society}, a multi-agent architecture decomposes a complex
task and assigns subtasks to agents with distinct responsibilities. Park et al.'s
social simulations illustrate individual memory, reflection, and planning
\citep{park2023generative_agents}. A single ``generalist'' workflow may combine
```

## D018b — B — 局部恢复

操作编号：[11]。

**before**
```tex
\citep{minsky1988society}, multi-agent architectures can combine agents with
individual memory, reflection, and planning, as illustrated in social
simulations \citep{park2023generative_agents}. A single ``generalist'' workflow may combine

```

**after**
```tex
\citep{minsky1988society}, a multi-agent architecture decomposes a complex
task and assigns subtasks to agents with distinct responsibilities. Park et al.'s
social simulations illustrate individual memory, reflection, and planning
\citep{park2023generative_agents}. A single ``generalist'' workflow may combine
```

## D019 — B — 完整恢复

操作编号：[12]。

**before**
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

**after**
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

## D020 — A — 必要纠错成果保留；共享片段仅按批准B/C边界恢复

操作编号：[]。

**before**
```tex
		control, as specified in the text and Table~\ref{tab:9categories}.}

```

**after**
```tex
		control, as specified in the text and Table~\ref{tab:9categories}.}
```

## D021 — A — 必要纠错成果保留；共享片段仅按批准B/C边界恢复

操作编号：[]。

**before**
```tex
In the multi-agent debate paradigm, several LLM agents generate candidate answers and critique one another across one or more rounds. Representative studies illustrate both the potential and the limits of this design. For example, \citet{du2024multiagent_debate} report improved factuality and reasoning performance on the tasks they evaluate, whereas divergent prompting can mitigate convergence toward similar reasoning paths \citep{liang2024divergent_debate}. ReConcile provides another example by integrating heterogeneous models with confidence-weighted consensus \citep{chen2024reconcile}; inter-model inconsistency and capability imbalance nevertheless remain important considerations \citep{xiong2023inter_consistency}. Accordingly, adding more agents or debate rounds does not reliably boost QA performance; instead, the interaction rules, diversity of evidence, and aggregation procedure determine whether disagreement yields correction, inconsistency, or unnecessary computational cost.

```

**after**
```tex
In the multi-agent debate paradigm, several LLM agents generate candidate answers and critique one another across one or more rounds. Representative studies illustrate both the potential and the limits of this design. For example, \citet{du2024multiagent_debate} report improved factuality and reasoning performance on the tasks they evaluate, whereas divergent prompting can mitigate convergence toward similar reasoning paths \citep{liang2024divergent_debate}. ReConcile provides another example by integrating heterogeneous models with confidence-weighted consensus \citep{chen2024reconcile}; inter-model inconsistency and capability imbalance nevertheless remain important considerations \citep{xiong2023inter_consistency}. Accordingly, adding more agents or debate rounds does not reliably boost QA performance; instead, the interaction rules, diversity of evidence, and aggregation procedure determine whether disagreement yields correction, inconsistency, or unnecessary computational cost.
```

## D022 — C — Q4已执行（保留当前已符合批准规则的片段）

操作编号：[]。

**before**
```tex
Role-conditioned collaboration assigns different prompts or task views to participating agents. For example, CAMEL \citep{li2023camel} employs an "AI User" and an "AI Assistant" paired with inception prompting to maintain role-conditioned interaction. This role pair has asymmetric instructions; role play alone does not establish a flat decision-authority structure. This constitutes an adjacent multi-agent framework and does not serve as direct evidence that role playing improves QA accuracy. 

```

**after**
```tex
Role-conditioned collaboration assigns different prompts or task views to participating agents. For example, CAMEL \citep{li2023camel} employs an "AI User" and an "AI Assistant" paired with inception prompting to maintain role-conditioned interaction. This role pair has asymmetric instructions; role play alone does not establish a flat decision-authority structure. This constitutes an adjacent multi-agent framework and does not serve as direct evidence that role playing improves QA accuracy. 
```

## D023 — A — 必要纠错成果保留；共享片段仅按批准B/C边界恢复

操作编号：[]。

**before**
```tex
CoCoA-zero \citep{jiang2026cocoa}, which coordinates parametric and retrieved
knowledge using three agents at inference time. CoCoA subsequently distils
that collaboration into a single model. These role-I systems differ in their communication

```

**after**
```tex
CoCoA-zero \citep{jiang2026cocoa}, which coordinates parametric and retrieved
knowledge using three agents at inference time. CoCoA subsequently distils
that collaboration into a single model. These role-I systems differ in their communication
```

## D024a — B — 局部恢复

操作编号：[13]。

**before**
```tex
Graph-structured networks represent agents and transitions as an executable graph. For example, LangGraph \citep{langgraph2024} serves as an official technical framework for defining state transitions, loops, and conditional branches; it provides technical evidence (role T), rather than constituting a QA evaluation. GPTSwarm \citep{zhuge2024gptswarm} provides an empirical example of optimising prompts and inter-agent graph connections. A graph representation, edge optimisation, or conditional routing alone does not establish hybrid decision authority; the implementation must actually change who controls decisions.

```

**after**
```tex
Graph-structured networks represent agents and transitions as an executable graph. For example, LangGraph \citep{langgraph2024} serves as an official technical framework for defining state transitions, loops, and conditional branches; it provides technical evidence (role T), rather than constituting a QA evaluation. GPTSwarm \citep{zhuge2024gptswarm} provides another example through an empirical study of agent methodologies that optimises prompts and inter-agent graph connections. A graph representation, edge optimisation, or conditional routing alone does not establish hybrid decision authority; the implementation must actually change who controls decisions.
```

## D024b — C — Q4已执行（按批准方案联动）

操作编号：[13]。

**before**
```tex
Graph-structured networks represent agents and transitions as an executable graph. For example, LangGraph \citep{langgraph2024} serves as an official technical framework for defining state transitions, loops, and conditional branches; it provides technical evidence (role T), rather than constituting a QA evaluation. GPTSwarm \citep{zhuge2024gptswarm} provides an empirical example of optimising prompts and inter-agent graph connections. A graph representation, edge optimisation, or conditional routing alone does not establish hybrid decision authority; the implementation must actually change who controls decisions.

```

**after**
```tex
Graph-structured networks represent agents and transitions as an executable graph. For example, LangGraph \citep{langgraph2024} serves as an official technical framework for defining state transitions, loops, and conditional branches; it provides technical evidence (role T), rather than constituting a QA evaluation. GPTSwarm \citep{zhuge2024gptswarm} provides another example through an empirical study of agent methodologies that optimises prompts and inter-agent graph connections. A graph representation, edge optimisation, or conditional routing alone does not establish hybrid decision authority; the implementation must actually change who controls decisions.
```

## D025 — B — 完整恢复

操作编号：[14]。

**before**
```tex
Adaptive systems can adjust team composition or interaction patterns.

```

**after**
```tex
Adaptive systems adjust team composition or control patterns as tasks evolve.
```

## D026a — A — 必要纠错成果保留；共享片段仅按批准B/C边界恢复

操作编号：[15]。

**before**
```tex
hierarchical" rule. MDAgents \citep{kim2024mdagents} routes medical queries to
solo, multidisciplinary-team, or integrated-care-team pathways according to
complexity under a moderator. This supports adaptive collaboration, but a
persistent moderator means that mode switching alone is insufficient to prove
hybrid authority. State management and performance still require evaluation.

```

**after**
```tex
hybrid authority. Such adaptive mechanisms enhance routing flexibility, yet
introduce extra requirements for state management and performance evaluation.
```

## D026b — C — Q4已执行（保留当前已符合批准规则的片段）

操作编号：[15]。

**before**
```tex
hierarchical" rule. MDAgents \citep{kim2024mdagents} routes medical queries to
solo, multidisciplinary-team, or integrated-care-team pathways according to
complexity under a moderator. This supports adaptive collaboration, but a
persistent moderator means that mode switching alone is insufficient to prove
hybrid authority. State management and performance still require evaluation.

```

**after**
```tex
hybrid authority. Such adaptive mechanisms enhance routing flexibility, yet
introduce extra requirements for state management and performance evaluation.
```

## D026c — B — 局部恢复

操作编号：[15]。

**before**
```tex
hierarchical" rule. MDAgents \citep{kim2024mdagents} routes medical queries to
solo, multidisciplinary-team, or integrated-care-team pathways according to
complexity under a moderator. This supports adaptive collaboration, but a
persistent moderator means that mode switching alone is insufficient to prove
hybrid authority. State management and performance still require evaluation.

```

**after**
```tex
hybrid authority. Such adaptive mechanisms enhance routing flexibility, yet
introduce extra requirements for state management and performance evaluation.
```

## D027a — A — 必要纠错成果保留；共享片段仅按批准B/C边界恢复

操作编号：[16]。

**before**
```tex
For example, LangGraph supports checkpointed state and pausing a workflow
with an interrupt for human review \citep{langgraph2024interrupt}, which may
be useful for high-risk decisions.

```

**after**
```tex
For example, LangGraph supports pausing a workflow at defined breakpoints for
human review \citep{langgraph2024interrupt}, which may be useful for high-risk
decisions.
```

## D027b — B — 局部恢复

操作编号：[16]。

**before**
```tex
For example, LangGraph supports checkpointed state and pausing a workflow
with an interrupt for human review \citep{langgraph2024interrupt}, which may
be useful for high-risk decisions.

```

**after**
```tex
For example, LangGraph supports pausing a workflow at defined breakpoints for
human review \citep{langgraph2024interrupt}, which may be useful for high-risk
decisions.
```

## D028 — C — Q4已执行（按批准方案联动）

操作编号：[17, 38]。

**before**
```tex
Hybrid architectures may be appropriate when heterogeneous task requirements call for transitions between peer deliberation and central decision authority. Their trade-off lies in engineering complexity: dynamic routing, state transitions, and cross-mode information transfer are more difficult to configure, debug, evaluate, and reproduce. A hybrid design is justified when this additional adaptability addresses documented uncertainty or risk, rather than serving as a default replacement for fixed control patterns.

```

**after**
```tex
Hybrid architectures are useful when task requirements are heterogeneous or when the workflow must combine deliberation, controlled execution, and conditional review, provided that decision authority changes across stages or decision states. Their trade-off lies in engineering complexity: dynamic routing, state transitions, and cross-mode information transfer are more difficult to configure, debug, evaluate, and reproduce. A hybrid design is justified when this additional adaptability addresses documented uncertainty or risk, rather than serving as a default replacement for fixed control patterns.

Hybrid architectures are useful when task requirements are heterogeneous or when the workflow must combine deliberation, controlled execution, and conditional review, provided that decision authority changes across stages or decision states.
```

## D029 — C — Q4已执行（按批准方案联动）

操作编号：[18]。

**before**
```tex
Table~\ref{tab:9categories} compares representative control patterns and
related mechanisms. Architecture labels, suitable contexts, and limitations
are the authors' synthesis. Role-paired, configurable, and cross-cutting
entries describe mechanisms or tool capabilities, not additional architecture
classes or evidence that every configuration is hybrid.

```

**after**
```tex
Table~\ref{tab:9categories} compares flat, hierarchical, and hybrid architectures
and their related mechanisms. Architecture labels, suitable contexts, and
limitations are the authors' synthesis; related mechanisms are shown separately
and do not define additional architecture classes.
```

## D030 — C — Q4已执行（按批准方案联动）

操作编号：[19]。

**before**
```tex
  \caption{Representative control patterns and related mechanisms for multi-agent collaborative QA.}

```

**after**
```tex
\begin{table*}[pos=t]
  \centering
  \caption{Comparison of multi-agent collaborative QA architecture classes and related mechanisms.}
  \label{tab:9categories}
  \scriptsize
  \begin{tabular}{p{1.4cm} p{2.0cm} p{2.4cm} p{3.2cm} p{2.3cm} p{2.2cm}}
    \toprule
    \textbf{Architecture} & \textbf{Sub-paradigm / mechanism} &
    \textbf{Representative systems / evidence} &
    \textbf{Coordination and control} &
    \textbf{Suitable contexts} & \textbf{Limitations} \\
    \midrule
    \multicolumn{6}{l}{\textbf{Architecture classes}} \\
    \midrule
    \textbf{Flat} & Multi-agent debate & \citet{du2024multiagent_debate} &
    Peer critique and aggregation; no persistent top-down controller &
    Tasks needing competing factual or reasoning views &
    Coordination cost and aggregation sensitivity \\
    \textbf{Hierarchical} & Manager--executor; staged evidence-processing pipeline &
    MetaGPT; LONGAGENT; Chain-of-Agents; CoCoA-zero
    \citep{hong2024metagpt,zhao2024longagent,zhang2024chain_agents,jiang2026cocoa} &
    Fixed planning, routing or synthesis authority; explicit sequencing over distributed evidence &
    Structured engineering workflows; long-document or knowledge-intensive QA &
    Planner bottleneck, error propagation and information loss at synthesis \\
    \textbf{Hybrid} & Changes in decision authority across stages or decision states &
    Conditional design pattern; no hybrid case under the present ten-case source coding &
    A documented change between peer control and asymmetric decision authority &
    Heterogeneous requirements that call for changing control configurations &
    Routing, state-transition and cross-mode coordination costs require evaluation \\
    \midrule
    \multicolumn{6}{l}{\textbf{Related mechanisms and implementation resources}} \\
    \midrule
    --- & Role-conditioned collaboration & CAMEL \citep{li2023camel} &
    Personas structure interaction; AI User and AI Assistant have asymmetric instructions &
    Exploratory collaboration and prompt-role studies &
    Role playing alone does not establish flat control or QA gains \\
    --- & Group-chat collaboration & AutoGen \citep{wu2024autogen} &
    Developer-defined conversations and speaker selection &
    Applications requiring configurable conversations &
    Architecture depends on the specific configuration \\
    --- & Graph-structured agent networks & GPTSwarm; LangGraph
    \citep{zhuge2024gptswarm,langgraph2024} &
    GPTSwarm DAG connection optimisation; LangGraph loops and conditional routing &
    Workflows with conditional state transitions &
    Graph structure or edge optimisation alone does not establish hybrid authority \\
    --- & Adaptive collaboration-mode switching & MDAgents \citep{kim2024mdagents} &
    Moderator routes solo, multidisciplinary-team or integrated-care-team consultation by complexity &
    Tasks with heterogeneous requirements &
    Changing team composition alone does not establish a change in decision authority \\
    --- & Human-in-the-loop design pattern & LangGraph breakpoints \citep{langgraph2024interrupt} &
    Human review at defined decision points &
    High-risk workflows requiring accountability &
    A fixed approver remains hierarchical; comparative QA safety evidence is limited \\
    \bottomrule
  \end{tabular}
  \par\smallskip\footnotesize
  \textit{Note}: Architecture classes refer to decision authority in a specified
  implementation. The related mechanisms do not by themselves establish a flat
  or hybrid architecture. A hybrid label requires a change in decision authority.
\end{table*}
```

## D031 — C — Q4已执行（按批准方案联动）

操作编号：[19]。

**before**
```tex
    \textbf{Flat} &

```

**after**
```tex
    \textbf{Flat} &
```

## D032a — A — 必要纠错成果保留；共享片段仅按批准B/C边界恢复

操作编号：[19]。

**before**
```tex
    Coordination cost and aggregation sensitivity \\
    \textbf{Role-paired} & Role-conditioned collaboration & CAMEL \citep{li2023camel} & 

```

**after**
```tex
\begin{table*}[pos=t]
  \centering
  \caption{Comparison of multi-agent collaborative QA architecture classes and related mechanisms.}
  \label{tab:9categories}
  \scriptsize
  \begin{tabular}{p{1.4cm} p{2.0cm} p{2.4cm} p{3.2cm} p{2.3cm} p{2.2cm}}
    \toprule
    \textbf{Architecture} & \textbf{Sub-paradigm / mechanism} &
    \textbf{Representative systems / evidence} &
    \textbf{Coordination and control} &
    \textbf{Suitable contexts} & \textbf{Limitations} \\
    \midrule
    \multicolumn{6}{l}{\textbf{Architecture classes}} \\
    \midrule
    \textbf{Flat} & Multi-agent debate & \citet{du2024multiagent_debate} &
    Peer critique and aggregation; no persistent top-down controller &
    Tasks needing competing factual or reasoning views &
    Coordination cost and aggregation sensitivity \\
    \textbf{Hierarchical} & Manager--executor; staged evidence-processing pipeline &
    MetaGPT; LONGAGENT; Chain-of-Agents; CoCoA-zero
    \citep{hong2024metagpt,zhao2024longagent,zhang2024chain_agents,jiang2026cocoa} &
    Fixed planning, routing or synthesis authority; explicit sequencing over distributed evidence &
    Structured engineering workflows; long-document or knowledge-intensive QA &
    Planner bottleneck, error propagation and information loss at synthesis \\
    \textbf{Hybrid} & Changes in decision authority across stages or decision states &
    Conditional design pattern; no hybrid case under the present ten-case source coding &
    A documented change between peer control and asymmetric decision authority &
    Heterogeneous requirements that call for changing control configurations &
    Routing, state-transition and cross-mode coordination costs require evaluation \\
    \midrule
    \multicolumn{6}{l}{\textbf{Related mechanisms and implementation resources}} \\
    \midrule
    --- & Role-conditioned collaboration & CAMEL \citep{li2023camel} &
    Personas structure interaction; AI User and AI Assistant have asymmetric instructions &
    Exploratory collaboration and prompt-role studies &
    Role playing alone does not establish flat control or QA gains \\
    --- & Group-chat collaboration & AutoGen \citep{wu2024autogen} &
    Developer-defined conversations and speaker selection &
    Applications requiring configurable conversations &
    Architecture depends on the specific configuration \\
    --- & Graph-structured agent networks & GPTSwarm; LangGraph
    \citep{zhuge2024gptswarm,langgraph2024} &
    GPTSwarm DAG connection optimisation; LangGraph loops and conditional routing &
    Workflows with conditional state transitions &
    Graph structure or edge optimisation alone does not establish hybrid authority \\
    --- & Adaptive collaboration-mode switching & MDAgents \citep{kim2024mdagents} &
    Moderator routes solo, multidisciplinary-team or integrated-care-team consultation by complexity &
    Tasks with heterogeneous requirements &
    Changing team composition alone does not establish a change in decision authority \\
    --- & Human-in-the-loop design pattern & LangGraph breakpoints \citep{langgraph2024interrupt} &
    Human review at defined decision points &
    High-risk workflows requiring accountability &
    A fixed approver remains hierarchical; comparative QA safety evidence is limited \\
    \bottomrule
  \end{tabular}
  \par\smallskip\footnotesize
  \textit{Note}: Architecture classes refer to decision authority in a specified
  implementation. The related mechanisms do not by themselves establish a flat
  or hybrid architecture. A hybrid label requires a change in decision authority.
\end{table*}
```

## D032b — C — Q4已执行（按批准方案联动）

操作编号：[19]。

**before**
```tex
    Coordination cost and aggregation sensitivity \\
    \textbf{Role-paired} & Role-conditioned collaboration & CAMEL \citep{li2023camel} & 

```

**after**
```tex
\begin{table*}[pos=t]
  \centering
  \caption{Comparison of multi-agent collaborative QA architecture classes and related mechanisms.}
  \label{tab:9categories}
  \scriptsize
  \begin{tabular}{p{1.4cm} p{2.0cm} p{2.4cm} p{3.2cm} p{2.3cm} p{2.2cm}}
    \toprule
    \textbf{Architecture} & \textbf{Sub-paradigm / mechanism} &
    \textbf{Representative systems / evidence} &
    \textbf{Coordination and control} &
    \textbf{Suitable contexts} & \textbf{Limitations} \\
    \midrule
    \multicolumn{6}{l}{\textbf{Architecture classes}} \\
    \midrule
    \textbf{Flat} & Multi-agent debate & \citet{du2024multiagent_debate} &
    Peer critique and aggregation; no persistent top-down controller &
    Tasks needing competing factual or reasoning views &
    Coordination cost and aggregation sensitivity \\
    \textbf{Hierarchical} & Manager--executor; staged evidence-processing pipeline &
    MetaGPT; LONGAGENT; Chain-of-Agents; CoCoA-zero
    \citep{hong2024metagpt,zhao2024longagent,zhang2024chain_agents,jiang2026cocoa} &
    Fixed planning, routing or synthesis authority; explicit sequencing over distributed evidence &
    Structured engineering workflows; long-document or knowledge-intensive QA &
    Planner bottleneck, error propagation and information loss at synthesis \\
    \textbf{Hybrid} & Changes in decision authority across stages or decision states &
    Conditional design pattern; no hybrid case under the present ten-case source coding &
    A documented change between peer control and asymmetric decision authority &
    Heterogeneous requirements that call for changing control configurations &
    Routing, state-transition and cross-mode coordination costs require evaluation \\
    \midrule
    \multicolumn{6}{l}{\textbf{Related mechanisms and implementation resources}} \\
    \midrule
    --- & Role-conditioned collaboration & CAMEL \citep{li2023camel} &
    Personas structure interaction; AI User and AI Assistant have asymmetric instructions &
    Exploratory collaboration and prompt-role studies &
    Role playing alone does not establish flat control or QA gains \\
    --- & Group-chat collaboration & AutoGen \citep{wu2024autogen} &
    Developer-defined conversations and speaker selection &
    Applications requiring configurable conversations &
    Architecture depends on the specific configuration \\
    --- & Graph-structured agent networks & GPTSwarm; LangGraph
    \citep{zhuge2024gptswarm,langgraph2024} &
    GPTSwarm DAG connection optimisation; LangGraph loops and conditional routing &
    Workflows with conditional state transitions &
    Graph structure or edge optimisation alone does not establish hybrid authority \\
    --- & Adaptive collaboration-mode switching & MDAgents \citep{kim2024mdagents} &
    Moderator routes solo, multidisciplinary-team or integrated-care-team consultation by complexity &
    Tasks with heterogeneous requirements &
    Changing team composition alone does not establish a change in decision authority \\
    --- & Human-in-the-loop design pattern & LangGraph breakpoints \citep{langgraph2024interrupt} &
    Human review at defined decision points &
    High-risk workflows requiring accountability &
    A fixed approver remains hierarchical; comparative QA safety evidence is limited \\
    \bottomrule
  \end{tabular}
  \par\smallskip\footnotesize
  \textit{Note}: Architecture classes refer to decision authority in a specified
  implementation. The related mechanisms do not by themselves establish a flat
  or hybrid architecture. A hybrid label requires a change in decision authority.
\end{table*}
```

## D033 — C — Q4已执行（按批准方案联动）

操作编号：[19]。

**before**
```tex
    \textbf{Configurable} & Group-chat collaboration & AutoGen \citep{wu2024autogen}  &

```

**after**
```tex
\begin{table*}[pos=t]
  \centering
  \caption{Comparison of multi-agent collaborative QA architecture classes and related mechanisms.}
  \label{tab:9categories}
  \scriptsize
  \begin{tabular}{p{1.4cm} p{2.0cm} p{2.4cm} p{3.2cm} p{2.3cm} p{2.2cm}}
    \toprule
    \textbf{Architecture} & \textbf{Sub-paradigm / mechanism} &
    \textbf{Representative systems / evidence} &
    \textbf{Coordination and control} &
    \textbf{Suitable contexts} & \textbf{Limitations} \\
    \midrule
    \multicolumn{6}{l}{\textbf{Architecture classes}} \\
    \midrule
    \textbf{Flat} & Multi-agent debate & \citet{du2024multiagent_debate} &
    Peer critique and aggregation; no persistent top-down controller &
    Tasks needing competing factual or reasoning views &
    Coordination cost and aggregation sensitivity \\
    \textbf{Hierarchical} & Manager--executor; staged evidence-processing pipeline &
    MetaGPT; LONGAGENT; Chain-of-Agents; CoCoA-zero
    \citep{hong2024metagpt,zhao2024longagent,zhang2024chain_agents,jiang2026cocoa} &
    Fixed planning, routing or synthesis authority; explicit sequencing over distributed evidence &
    Structured engineering workflows; long-document or knowledge-intensive QA &
    Planner bottleneck, error propagation and information loss at synthesis \\
    \textbf{Hybrid} & Changes in decision authority across stages or decision states &
    Conditional design pattern; no hybrid case under the present ten-case source coding &
    A documented change between peer control and asymmetric decision authority &
    Heterogeneous requirements that call for changing control configurations &
    Routing, state-transition and cross-mode coordination costs require evaluation \\
    \midrule
    \multicolumn{6}{l}{\textbf{Related mechanisms and implementation resources}} \\
    \midrule
    --- & Role-conditioned collaboration & CAMEL \citep{li2023camel} &
    Personas structure interaction; AI User and AI Assistant have asymmetric instructions &
    Exploratory collaboration and prompt-role studies &
    Role playing alone does not establish flat control or QA gains \\
    --- & Group-chat collaboration & AutoGen \citep{wu2024autogen} &
    Developer-defined conversations and speaker selection &
    Applications requiring configurable conversations &
    Architecture depends on the specific configuration \\
    --- & Graph-structured agent networks & GPTSwarm; LangGraph
    \citep{zhuge2024gptswarm,langgraph2024} &
    GPTSwarm DAG connection optimisation; LangGraph loops and conditional routing &
    Workflows with conditional state transitions &
    Graph structure or edge optimisation alone does not establish hybrid authority \\
    --- & Adaptive collaboration-mode switching & MDAgents \citep{kim2024mdagents} &
    Moderator routes solo, multidisciplinary-team or integrated-care-team consultation by complexity &
    Tasks with heterogeneous requirements &
    Changing team composition alone does not establish a change in decision authority \\
    --- & Human-in-the-loop design pattern & LangGraph breakpoints \citep{langgraph2024interrupt} &
    Human review at defined decision points &
    High-risk workflows requiring accountability &
    A fixed approver remains hierarchical; comparative QA safety evidence is limited \\
    \bottomrule
  \end{tabular}
  \par\smallskip\footnotesize
  \textit{Note}: Architecture classes refer to decision authority in a specified
  implementation. The related mechanisms do not by themselves establish a flat
  or hybrid architecture. A hybrid label requires a change in decision authority.
\end{table*}
```

## D034 — A — 必要纠错成果保留；共享片段仅按批准B/C边界恢复

操作编号：[19]。

**before**
```tex
    \multirow{2}{*}{\textbf{Hierarchical}} &

```

**after**
```tex
\begin{table*}[pos=t]
  \centering
  \caption{Comparison of multi-agent collaborative QA architecture classes and related mechanisms.}
  \label{tab:9categories}
  \scriptsize
  \begin{tabular}{p{1.4cm} p{2.0cm} p{2.4cm} p{3.2cm} p{2.3cm} p{2.2cm}}
    \toprule
    \textbf{Architecture} & \textbf{Sub-paradigm / mechanism} &
    \textbf{Representative systems / evidence} &
    \textbf{Coordination and control} &
    \textbf{Suitable contexts} & \textbf{Limitations} \\
    \midrule
    \multicolumn{6}{l}{\textbf{Architecture classes}} \\
    \midrule
    \textbf{Flat} & Multi-agent debate & \citet{du2024multiagent_debate} &
    Peer critique and aggregation; no persistent top-down controller &
    Tasks needing competing factual or reasoning views &
    Coordination cost and aggregation sensitivity \\
    \textbf{Hierarchical} & Manager--executor; staged evidence-processing pipeline &
    MetaGPT; LONGAGENT; Chain-of-Agents; CoCoA-zero
    \citep{hong2024metagpt,zhao2024longagent,zhang2024chain_agents,jiang2026cocoa} &
    Fixed planning, routing or synthesis authority; explicit sequencing over distributed evidence &
    Structured engineering workflows; long-document or knowledge-intensive QA &
    Planner bottleneck, error propagation and information loss at synthesis \\
    \textbf{Hybrid} & Changes in decision authority across stages or decision states &
    Conditional design pattern; no hybrid case under the present ten-case source coding &
    A documented change between peer control and asymmetric decision authority &
    Heterogeneous requirements that call for changing control configurations &
    Routing, state-transition and cross-mode coordination costs require evaluation \\
    \midrule
    \multicolumn{6}{l}{\textbf{Related mechanisms and implementation resources}} \\
    \midrule
    --- & Role-conditioned collaboration & CAMEL \citep{li2023camel} &
    Personas structure interaction; AI User and AI Assistant have asymmetric instructions &
    Exploratory collaboration and prompt-role studies &
    Role playing alone does not establish flat control or QA gains \\
    --- & Group-chat collaboration & AutoGen \citep{wu2024autogen} &
    Developer-defined conversations and speaker selection &
    Applications requiring configurable conversations &
    Architecture depends on the specific configuration \\
    --- & Graph-structured agent networks & GPTSwarm; LangGraph
    \citep{zhuge2024gptswarm,langgraph2024} &
    GPTSwarm DAG connection optimisation; LangGraph loops and conditional routing &
    Workflows with conditional state transitions &
    Graph structure or edge optimisation alone does not establish hybrid authority \\
    --- & Adaptive collaboration-mode switching & MDAgents \citep{kim2024mdagents} &
    Moderator routes solo, multidisciplinary-team or integrated-care-team consultation by complexity &
    Tasks with heterogeneous requirements &
    Changing team composition alone does not establish a change in decision authority \\
    --- & Human-in-the-loop design pattern & LangGraph breakpoints \citep{langgraph2024interrupt} &
    Human review at defined decision points &
    High-risk workflows requiring accountability &
    A fixed approver remains hierarchical; comparative QA safety evidence is limited \\
    \bottomrule
  \end{tabular}
  \par\smallskip\footnotesize
  \textit{Note}: Architecture classes refer to decision authority in a specified
  implementation. The related mechanisms do not by themselves establish a flat
  or hybrid architecture. A hybrid label requires a change in decision authority.
\end{table*}
```

## D035 — A — 必要纠错成果保留；共享片段仅按批准B/C边界恢复

操作编号：[19]。

**before**
```tex
    & Staged evidence-processing pipeline & LONGAGENT; Chain-of-Agents; CoCoA-zero

```

**after**
```tex
\begin{table*}[pos=t]
  \centering
  \caption{Comparison of multi-agent collaborative QA architecture classes and related mechanisms.}
  \label{tab:9categories}
  \scriptsize
  \begin{tabular}{p{1.4cm} p{2.0cm} p{2.4cm} p{3.2cm} p{2.3cm} p{2.2cm}}
    \toprule
    \textbf{Architecture} & \textbf{Sub-paradigm / mechanism} &
    \textbf{Representative systems / evidence} &
    \textbf{Coordination and control} &
    \textbf{Suitable contexts} & \textbf{Limitations} \\
    \midrule
    \multicolumn{6}{l}{\textbf{Architecture classes}} \\
    \midrule
    \textbf{Flat} & Multi-agent debate & \citet{du2024multiagent_debate} &
    Peer critique and aggregation; no persistent top-down controller &
    Tasks needing competing factual or reasoning views &
    Coordination cost and aggregation sensitivity \\
    \textbf{Hierarchical} & Manager--executor; staged evidence-processing pipeline &
    MetaGPT; LONGAGENT; Chain-of-Agents; CoCoA-zero
    \citep{hong2024metagpt,zhao2024longagent,zhang2024chain_agents,jiang2026cocoa} &
    Fixed planning, routing or synthesis authority; explicit sequencing over distributed evidence &
    Structured engineering workflows; long-document or knowledge-intensive QA &
    Planner bottleneck, error propagation and information loss at synthesis \\
    \textbf{Hybrid} & Changes in decision authority across stages or decision states &
    Conditional design pattern; no hybrid case under the present ten-case source coding &
    A documented change between peer control and asymmetric decision authority &
    Heterogeneous requirements that call for changing control configurations &
    Routing, state-transition and cross-mode coordination costs require evaluation \\
    \midrule
    \multicolumn{6}{l}{\textbf{Related mechanisms and implementation resources}} \\
    \midrule
    --- & Role-conditioned collaboration & CAMEL \citep{li2023camel} &
    Personas structure interaction; AI User and AI Assistant have asymmetric instructions &
    Exploratory collaboration and prompt-role studies &
    Role playing alone does not establish flat control or QA gains \\
    --- & Group-chat collaboration & AutoGen \citep{wu2024autogen} &
    Developer-defined conversations and speaker selection &
    Applications requiring configurable conversations &
    Architecture depends on the specific configuration \\
    --- & Graph-structured agent networks & GPTSwarm; LangGraph
    \citep{zhuge2024gptswarm,langgraph2024} &
    GPTSwarm DAG connection optimisation; LangGraph loops and conditional routing &
    Workflows with conditional state transitions &
    Graph structure or edge optimisation alone does not establish hybrid authority \\
    --- & Adaptive collaboration-mode switching & MDAgents \citep{kim2024mdagents} &
    Moderator routes solo, multidisciplinary-team or integrated-care-team consultation by complexity &
    Tasks with heterogeneous requirements &
    Changing team composition alone does not establish a change in decision authority \\
    --- & Human-in-the-loop design pattern & LangGraph breakpoints \citep{langgraph2024interrupt} &
    Human review at defined decision points &
    High-risk workflows requiring accountability &
    A fixed approver remains hierarchical; comparative QA safety evidence is limited \\
    \bottomrule
  \end{tabular}
  \par\smallskip\footnotesize
  \textit{Note}: Architecture classes refer to decision authority in a specified
  implementation. The related mechanisms do not by themselves establish a flat
  or hybrid architecture. A hybrid label requires a change in decision authority.
\end{table*}
```

## D036 — C — Q4已执行（按批准方案联动）

操作编号：[19]。

**before**
```tex
    \multirow{3}{*}{\shortstack{\textbf{Cross-}\\\textbf{cutting}}} &

```

**after**
```tex
\begin{table*}[pos=t]
  \centering
  \caption{Comparison of multi-agent collaborative QA architecture classes and related mechanisms.}
  \label{tab:9categories}
  \scriptsize
  \begin{tabular}{p{1.4cm} p{2.0cm} p{2.4cm} p{3.2cm} p{2.3cm} p{2.2cm}}
    \toprule
    \textbf{Architecture} & \textbf{Sub-paradigm / mechanism} &
    \textbf{Representative systems / evidence} &
    \textbf{Coordination and control} &
    \textbf{Suitable contexts} & \textbf{Limitations} \\
    \midrule
    \multicolumn{6}{l}{\textbf{Architecture classes}} \\
    \midrule
    \textbf{Flat} & Multi-agent debate & \citet{du2024multiagent_debate} &
    Peer critique and aggregation; no persistent top-down controller &
    Tasks needing competing factual or reasoning views &
    Coordination cost and aggregation sensitivity \\
    \textbf{Hierarchical} & Manager--executor; staged evidence-processing pipeline &
    MetaGPT; LONGAGENT; Chain-of-Agents; CoCoA-zero
    \citep{hong2024metagpt,zhao2024longagent,zhang2024chain_agents,jiang2026cocoa} &
    Fixed planning, routing or synthesis authority; explicit sequencing over distributed evidence &
    Structured engineering workflows; long-document or knowledge-intensive QA &
    Planner bottleneck, error propagation and information loss at synthesis \\
    \textbf{Hybrid} & Changes in decision authority across stages or decision states &
    Conditional design pattern; no hybrid case under the present ten-case source coding &
    A documented change between peer control and asymmetric decision authority &
    Heterogeneous requirements that call for changing control configurations &
    Routing, state-transition and cross-mode coordination costs require evaluation \\
    \midrule
    \multicolumn{6}{l}{\textbf{Related mechanisms and implementation resources}} \\
    \midrule
    --- & Role-conditioned collaboration & CAMEL \citep{li2023camel} &
    Personas structure interaction; AI User and AI Assistant have asymmetric instructions &
    Exploratory collaboration and prompt-role studies &
    Role playing alone does not establish flat control or QA gains \\
    --- & Group-chat collaboration & AutoGen \citep{wu2024autogen} &
    Developer-defined conversations and speaker selection &
    Applications requiring configurable conversations &
    Architecture depends on the specific configuration \\
    --- & Graph-structured agent networks & GPTSwarm; LangGraph
    \citep{zhuge2024gptswarm,langgraph2024} &
    GPTSwarm DAG connection optimisation; LangGraph loops and conditional routing &
    Workflows with conditional state transitions &
    Graph structure or edge optimisation alone does not establish hybrid authority \\
    --- & Adaptive collaboration-mode switching & MDAgents \citep{kim2024mdagents} &
    Moderator routes solo, multidisciplinary-team or integrated-care-team consultation by complexity &
    Tasks with heterogeneous requirements &
    Changing team composition alone does not establish a change in decision authority \\
    --- & Human-in-the-loop design pattern & LangGraph breakpoints \citep{langgraph2024interrupt} &
    Human review at defined decision points &
    High-risk workflows requiring accountability &
    A fixed approver remains hierarchical; comparative QA safety evidence is limited \\
    \bottomrule
  \end{tabular}
  \par\smallskip\footnotesize
  \textit{Note}: Architecture classes refer to decision authority in a specified
  implementation. The related mechanisms do not by themselves establish a flat
  or hybrid architecture. A hybrid label requires a change in decision authority.
\end{table*}
```

## D037 — A — 必要纠错成果保留；共享片段仅按批准B/C边界恢复

操作编号：[19]。

**before**
```tex
    DAG connection optimization in GPTSwarm; loops and conditional routing in LangGraph &

```

**after**
```tex
\begin{table*}[pos=t]
  \centering
  \caption{Comparison of multi-agent collaborative QA architecture classes and related mechanisms.}
  \label{tab:9categories}
  \scriptsize
  \begin{tabular}{p{1.4cm} p{2.0cm} p{2.4cm} p{3.2cm} p{2.3cm} p{2.2cm}}
    \toprule
    \textbf{Architecture} & \textbf{Sub-paradigm / mechanism} &
    \textbf{Representative systems / evidence} &
    \textbf{Coordination and control} &
    \textbf{Suitable contexts} & \textbf{Limitations} \\
    \midrule
    \multicolumn{6}{l}{\textbf{Architecture classes}} \\
    \midrule
    \textbf{Flat} & Multi-agent debate & \citet{du2024multiagent_debate} &
    Peer critique and aggregation; no persistent top-down controller &
    Tasks needing competing factual or reasoning views &
    Coordination cost and aggregation sensitivity \\
    \textbf{Hierarchical} & Manager--executor; staged evidence-processing pipeline &
    MetaGPT; LONGAGENT; Chain-of-Agents; CoCoA-zero
    \citep{hong2024metagpt,zhao2024longagent,zhang2024chain_agents,jiang2026cocoa} &
    Fixed planning, routing or synthesis authority; explicit sequencing over distributed evidence &
    Structured engineering workflows; long-document or knowledge-intensive QA &
    Planner bottleneck, error propagation and information loss at synthesis \\
    \textbf{Hybrid} & Changes in decision authority across stages or decision states &
    Conditional design pattern; no hybrid case under the present ten-case source coding &
    A documented change between peer control and asymmetric decision authority &
    Heterogeneous requirements that call for changing control configurations &
    Routing, state-transition and cross-mode coordination costs require evaluation \\
    \midrule
    \multicolumn{6}{l}{\textbf{Related mechanisms and implementation resources}} \\
    \midrule
    --- & Role-conditioned collaboration & CAMEL \citep{li2023camel} &
    Personas structure interaction; AI User and AI Assistant have asymmetric instructions &
    Exploratory collaboration and prompt-role studies &
    Role playing alone does not establish flat control or QA gains \\
    --- & Group-chat collaboration & AutoGen \citep{wu2024autogen} &
    Developer-defined conversations and speaker selection &
    Applications requiring configurable conversations &
    Architecture depends on the specific configuration \\
    --- & Graph-structured agent networks & GPTSwarm; LangGraph
    \citep{zhuge2024gptswarm,langgraph2024} &
    GPTSwarm DAG connection optimisation; LangGraph loops and conditional routing &
    Workflows with conditional state transitions &
    Graph structure or edge optimisation alone does not establish hybrid authority \\
    --- & Adaptive collaboration-mode switching & MDAgents \citep{kim2024mdagents} &
    Moderator routes solo, multidisciplinary-team or integrated-care-team consultation by complexity &
    Tasks with heterogeneous requirements &
    Changing team composition alone does not establish a change in decision authority \\
    --- & Human-in-the-loop design pattern & LangGraph breakpoints \citep{langgraph2024interrupt} &
    Human review at defined decision points &
    High-risk workflows requiring accountability &
    A fixed approver remains hierarchical; comparative QA safety evidence is limited \\
    \bottomrule
  \end{tabular}
  \par\smallskip\footnotesize
  \textit{Note}: Architecture classes refer to decision authority in a specified
  implementation. The related mechanisms do not by themselves establish a flat
  or hybrid architecture. A hybrid label requires a change in decision authority.
\end{table*}
```

## D038 — A — 必要纠错成果保留；共享片段仅按批准B/C边界恢复

操作编号：[19]。

**before**
```tex
    Moderator routes solo or team consultation according to complexity &

```

**after**
```tex
\begin{table*}[pos=t]
  \centering
  \caption{Comparison of multi-agent collaborative QA architecture classes and related mechanisms.}
  \label{tab:9categories}
  \scriptsize
  \begin{tabular}{p{1.4cm} p{2.0cm} p{2.4cm} p{3.2cm} p{2.3cm} p{2.2cm}}
    \toprule
    \textbf{Architecture} & \textbf{Sub-paradigm / mechanism} &
    \textbf{Representative systems / evidence} &
    \textbf{Coordination and control} &
    \textbf{Suitable contexts} & \textbf{Limitations} \\
    \midrule
    \multicolumn{6}{l}{\textbf{Architecture classes}} \\
    \midrule
    \textbf{Flat} & Multi-agent debate & \citet{du2024multiagent_debate} &
    Peer critique and aggregation; no persistent top-down controller &
    Tasks needing competing factual or reasoning views &
    Coordination cost and aggregation sensitivity \\
    \textbf{Hierarchical} & Manager--executor; staged evidence-processing pipeline &
    MetaGPT; LONGAGENT; Chain-of-Agents; CoCoA-zero
    \citep{hong2024metagpt,zhao2024longagent,zhang2024chain_agents,jiang2026cocoa} &
    Fixed planning, routing or synthesis authority; explicit sequencing over distributed evidence &
    Structured engineering workflows; long-document or knowledge-intensive QA &
    Planner bottleneck, error propagation and information loss at synthesis \\
    \textbf{Hybrid} & Changes in decision authority across stages or decision states &
    Conditional design pattern; no hybrid case under the present ten-case source coding &
    A documented change between peer control and asymmetric decision authority &
    Heterogeneous requirements that call for changing control configurations &
    Routing, state-transition and cross-mode coordination costs require evaluation \\
    \midrule
    \multicolumn{6}{l}{\textbf{Related mechanisms and implementation resources}} \\
    \midrule
    --- & Role-conditioned collaboration & CAMEL \citep{li2023camel} &
    Personas structure interaction; AI User and AI Assistant have asymmetric instructions &
    Exploratory collaboration and prompt-role studies &
    Role playing alone does not establish flat control or QA gains \\
    --- & Group-chat collaboration & AutoGen \citep{wu2024autogen} &
    Developer-defined conversations and speaker selection &
    Applications requiring configurable conversations &
    Architecture depends on the specific configuration \\
    --- & Graph-structured agent networks & GPTSwarm; LangGraph
    \citep{zhuge2024gptswarm,langgraph2024} &
    GPTSwarm DAG connection optimisation; LangGraph loops and conditional routing &
    Workflows with conditional state transitions &
    Graph structure or edge optimisation alone does not establish hybrid authority \\
    --- & Adaptive collaboration-mode switching & MDAgents \citep{kim2024mdagents} &
    Moderator routes solo, multidisciplinary-team or integrated-care-team consultation by complexity &
    Tasks with heterogeneous requirements &
    Changing team composition alone does not establish a change in decision authority \\
    --- & Human-in-the-loop design pattern & LangGraph breakpoints \citep{langgraph2024interrupt} &
    Human review at defined decision points &
    High-risk workflows requiring accountability &
    A fixed approver remains hierarchical; comparative QA safety evidence is limited \\
    \bottomrule
  \end{tabular}
  \par\smallskip\footnotesize
  \textit{Note}: Architecture classes refer to decision authority in a specified
  implementation. The related mechanisms do not by themselves establish a flat
  or hybrid architecture. A hybrid label requires a change in decision authority.
\end{table*}
```

## D039a — A — 必要纠错成果保留；共享片段仅按批准B/C边界恢复

操作编号：[19]。

**before**
```tex
    & Human-in-the-loop design pattern & LangGraph interrupts \citep{langgraph2024interrupt} &

```

**after**
```tex
\begin{table*}[pos=t]
  \centering
  \caption{Comparison of multi-agent collaborative QA architecture classes and related mechanisms.}
  \label{tab:9categories}
  \scriptsize
  \begin{tabular}{p{1.4cm} p{2.0cm} p{2.4cm} p{3.2cm} p{2.3cm} p{2.2cm}}
    \toprule
    \textbf{Architecture} & \textbf{Sub-paradigm / mechanism} &
    \textbf{Representative systems / evidence} &
    \textbf{Coordination and control} &
    \textbf{Suitable contexts} & \textbf{Limitations} \\
    \midrule
    \multicolumn{6}{l}{\textbf{Architecture classes}} \\
    \midrule
    \textbf{Flat} & Multi-agent debate & \citet{du2024multiagent_debate} &
    Peer critique and aggregation; no persistent top-down controller &
    Tasks needing competing factual or reasoning views &
    Coordination cost and aggregation sensitivity \\
    \textbf{Hierarchical} & Manager--executor; staged evidence-processing pipeline &
    MetaGPT; LONGAGENT; Chain-of-Agents; CoCoA-zero
    \citep{hong2024metagpt,zhao2024longagent,zhang2024chain_agents,jiang2026cocoa} &
    Fixed planning, routing or synthesis authority; explicit sequencing over distributed evidence &
    Structured engineering workflows; long-document or knowledge-intensive QA &
    Planner bottleneck, error propagation and information loss at synthesis \\
    \textbf{Hybrid} & Changes in decision authority across stages or decision states &
    Conditional design pattern; no hybrid case under the present ten-case source coding &
    A documented change between peer control and asymmetric decision authority &
    Heterogeneous requirements that call for changing control configurations &
    Routing, state-transition and cross-mode coordination costs require evaluation \\
    \midrule
    \multicolumn{6}{l}{\textbf{Related mechanisms and implementation resources}} \\
    \midrule
    --- & Role-conditioned collaboration & CAMEL \citep{li2023camel} &
    Personas structure interaction; AI User and AI Assistant have asymmetric instructions &
    Exploratory collaboration and prompt-role studies &
    Role playing alone does not establish flat control or QA gains \\
    --- & Group-chat collaboration & AutoGen \citep{wu2024autogen} &
    Developer-defined conversations and speaker selection &
    Applications requiring configurable conversations &
    Architecture depends on the specific configuration \\
    --- & Graph-structured agent networks & GPTSwarm; LangGraph
    \citep{zhuge2024gptswarm,langgraph2024} &
    GPTSwarm DAG connection optimisation; LangGraph loops and conditional routing &
    Workflows with conditional state transitions &
    Graph structure or edge optimisation alone does not establish hybrid authority \\
    --- & Adaptive collaboration-mode switching & MDAgents \citep{kim2024mdagents} &
    Moderator routes solo, multidisciplinary-team or integrated-care-team consultation by complexity &
    Tasks with heterogeneous requirements &
    Changing team composition alone does not establish a change in decision authority \\
    --- & Human-in-the-loop design pattern & LangGraph breakpoints \citep{langgraph2024interrupt} &
    Human review at defined decision points &
    High-risk workflows requiring accountability &
    A fixed approver remains hierarchical; comparative QA safety evidence is limited \\
    \bottomrule
  \end{tabular}
  \par\smallskip\footnotesize
  \textit{Note}: Architecture classes refer to decision authority in a specified
  implementation. The related mechanisms do not by themselves establish a flat
  or hybrid architecture. A hybrid label requires a change in decision authority.
\end{table*}
```

## D039b — B — 局部恢复

操作编号：[19]。

**before**
```tex
    & Human-in-the-loop design pattern & LangGraph interrupts \citep{langgraph2024interrupt} &

```

**after**
```tex
\begin{table*}[pos=t]
  \centering
  \caption{Comparison of multi-agent collaborative QA architecture classes and related mechanisms.}
  \label{tab:9categories}
  \scriptsize
  \begin{tabular}{p{1.4cm} p{2.0cm} p{2.4cm} p{3.2cm} p{2.3cm} p{2.2cm}}
    \toprule
    \textbf{Architecture} & \textbf{Sub-paradigm / mechanism} &
    \textbf{Representative systems / evidence} &
    \textbf{Coordination and control} &
    \textbf{Suitable contexts} & \textbf{Limitations} \\
    \midrule
    \multicolumn{6}{l}{\textbf{Architecture classes}} \\
    \midrule
    \textbf{Flat} & Multi-agent debate & \citet{du2024multiagent_debate} &
    Peer critique and aggregation; no persistent top-down controller &
    Tasks needing competing factual or reasoning views &
    Coordination cost and aggregation sensitivity \\
    \textbf{Hierarchical} & Manager--executor; staged evidence-processing pipeline &
    MetaGPT; LONGAGENT; Chain-of-Agents; CoCoA-zero
    \citep{hong2024metagpt,zhao2024longagent,zhang2024chain_agents,jiang2026cocoa} &
    Fixed planning, routing or synthesis authority; explicit sequencing over distributed evidence &
    Structured engineering workflows; long-document or knowledge-intensive QA &
    Planner bottleneck, error propagation and information loss at synthesis \\
    \textbf{Hybrid} & Changes in decision authority across stages or decision states &
    Conditional design pattern; no hybrid case under the present ten-case source coding &
    A documented change between peer control and asymmetric decision authority &
    Heterogeneous requirements that call for changing control configurations &
    Routing, state-transition and cross-mode coordination costs require evaluation \\
    \midrule
    \multicolumn{6}{l}{\textbf{Related mechanisms and implementation resources}} \\
    \midrule
    --- & Role-conditioned collaboration & CAMEL \citep{li2023camel} &
    Personas structure interaction; AI User and AI Assistant have asymmetric instructions &
    Exploratory collaboration and prompt-role studies &
    Role playing alone does not establish flat control or QA gains \\
    --- & Group-chat collaboration & AutoGen \citep{wu2024autogen} &
    Developer-defined conversations and speaker selection &
    Applications requiring configurable conversations &
    Architecture depends on the specific configuration \\
    --- & Graph-structured agent networks & GPTSwarm; LangGraph
    \citep{zhuge2024gptswarm,langgraph2024} &
    GPTSwarm DAG connection optimisation; LangGraph loops and conditional routing &
    Workflows with conditional state transitions &
    Graph structure or edge optimisation alone does not establish hybrid authority \\
    --- & Adaptive collaboration-mode switching & MDAgents \citep{kim2024mdagents} &
    Moderator routes solo, multidisciplinary-team or integrated-care-team consultation by complexity &
    Tasks with heterogeneous requirements &
    Changing team composition alone does not establish a change in decision authority \\
    --- & Human-in-the-loop design pattern & LangGraph breakpoints \citep{langgraph2024interrupt} &
    Human review at defined decision points &
    High-risk workflows requiring accountability &
    A fixed approver remains hierarchical; comparative QA safety evidence is limited \\
    \bottomrule
  \end{tabular}
  \par\smallskip\footnotesize
  \textit{Note}: Architecture classes refer to decision authority in a specified
  implementation. The related mechanisms do not by themselves establish a flat
  or hybrid architecture. A hybrid label requires a change in decision authority.
\end{table*}
```

## D040a — A — 必要纠错成果保留；共享片段仅按批准B/C边界恢复

操作编号：[20]。

**before**
```tex
communication, aggregation, state-management, and inference costs. Reported
multi-agent failure modes \citep{han2024mast} motivate checking whether
additional coordination provides useful benefits. As a design criterion,
this review requires expected gains in coverage, reliability, or adaptability
to justify the resource burden. Assessment should include latency, token use,
tool calls, monitoring, and recovery overhead.

```

**after**
```tex
communication, aggregation, state-management, and inference costs. A
collaborative design is justified only when expected gains in coverage,
reliability, or adaptability offset those costs, as a criterion of this review.
Reported multi-agent failure modes motivate this assessment \citep{han2024mast}.
Assessment should include latency, token use, tool calls, monitoring, and recovery overhead.
```

## D040b — B — 局部恢复

操作编号：[20]。

**before**
```tex
communication, aggregation, state-management, and inference costs. Reported
multi-agent failure modes \citep{han2024mast} motivate checking whether
additional coordination provides useful benefits. As a design criterion,
this review requires expected gains in coverage, reliability, or adaptability
to justify the resource burden. Assessment should include latency, token use,
tool calls, monitoring, and recovery overhead.

```

**after**
```tex
communication, aggregation, state-management, and inference costs. A
collaborative design is justified only when expected gains in coverage,
reliability, or adaptability offset those costs, as a criterion of this review.
Reported multi-agent failure modes motivate this assessment \citep{han2024mast}.
Assessment should include latency, token use, tool calls, monitoring, and recovery overhead.
```

## D041 — C — Q4已执行（保留当前已符合批准规则的片段）

操作编号：[]。

**before**
```tex
when independent perspectives are valuable; hybrid control is a candidate
when changing requirements necessitate a change in decision authority.
Conditional review under a fixed approver remains hierarchical. Compare the
selected design with a single-agent baseline using task quality, latency,
cost, provenance, and failure-recovery measures.

```

**after**
```tex
when independent perspectives are valuable; hybrid control is a candidate
when changing requirements necessitate a change in decision authority.
Conditional review under a fixed approver remains hierarchical. Compare the
selected design with a single-agent baseline using task quality, latency,
cost, provenance, and failure-recovery measures.
```

## D042 — C — Q5已执行（按批准方案联动）

操作编号：[21, 39]。

**before**
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

**after**
```tex
The approach is verified for interpretive consistency by comparing its
inferred architectures with ten published systems. This purposive sample was
selected because the systems report agent roles and control flow with enough
detail for coding and cover different domains, process structures, and risk
levels. The comparison does not evaluate system performance, establish causal
benefit, or claim external validity. It contains both core QA studies and
supporting workflow examples and is not independent validation. The proposed
labels and criterion profiles are retained, while reported workflows are
coded by decision authority.
Flat control has no persistent top-down controller; hierarchical control has
stable routing, approval, or final-decision authority; hybrid control requires
a demonstrated change in that authority. Iteration, voting, multiple roles,
and graph structure alone are insufficient.

Three mutually exclusive ratings are applied in order. A case is broadly
aligned when the proposed and source-coded overall categories agree and the
reported workflow does not contradict their defining control features.
When the categories differ, partial alignment requires a substantive local
mechanism compatible with the proposed category and an explicit overall
control conflict; otherwise the case is divergent. For a flat recommendation,
partial alignment requires all three conditions: (F1) at least two expert
roles contribute their own analyses; (F2) they review the same report under
the same acceptance or rejection rule, without an exclusive expert reviewer;
and (F3) objections feed report revision and renewed review. An iteration
limit is permitted, so unanimity is not guaranteed. For a hierarchical
recommendation, local compatibility requires fixed delegation, routing,
approval, or synthesis authority in a substantive sub-process. For a hybrid
recommendation, it requires an actual change in decision-authority
configuration within a reported sub-process. Insufficient method evidence
would leave a case unscored and require reporting the scored denominator.

Six cases are broadly aligned, two are partially aligned, and two are
divergent under the coding used here. MedAgents and LLM-MedQA retain
hierarchical overall control while supporting equal-participation expert
review locally. These local mechanisms explain partial alignment with a
flat recommendation; they do not establish a flat or hybrid overall
architecture. LegalGraphRAG and EduPlanner remain divergent. Du et al.'s
peer debate is flat at the macro level but uses iterative convergence;
EduPlanner and Financial Reflection QA combine convergent objectives with
evaluator or critic feedback. These boundary cases show that competing
requirements can make a single categorical label insufficient and that a
multi-label description of control flow may sometimes be preferable,
provided that overall authority and local mechanisms are distinguished.
Financial Reflection QA remains hierarchical despite critic feedback.
Nine reported workflows
are coded hierarchical and one flat; this sample therefore does not validate
the hybrid category. All ten cases have sufficient method evidence for this
limited comparison. The comparison is retrospective and was not blind or
preregistered; these ratings are descriptive, not prediction accuracy or
evidence of an effective architecture-selection policy.

The approach is verified for interpretive consistency by comparing its
inferred architectures with ten published systems. This purposive sample was
selected because the systems report agent roles and control flow with enough
detail for coding and cover different domains, process structures, and risk
levels. The comparison does not evaluate system performance, establish causal
benefit, or claim external validity. It contains both core QA studies and
supporting workflow examples and is not independent validation. The proposed
labels and criterion profiles are retained, while reported workflows are
coded by decision authority.
```

## D043 — C — Q5已执行（按批准方案联动）

操作编号：[21, 40]。

**before**
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

**after**
```tex
The approach is verified for interpretive consistency by comparing its
inferred architectures with ten published systems. This purposive sample was
selected because the systems report agent roles and control flow with enough
detail for coding and cover different domains, process structures, and risk
levels. The comparison does not evaluate system performance, establish causal
benefit, or claim external validity. It contains both core QA studies and
supporting workflow examples and is not independent validation. The proposed
labels and criterion profiles are retained, while reported workflows are
coded by decision authority.
Flat control has no persistent top-down controller; hierarchical control has
stable routing, approval, or final-decision authority; hybrid control requires
a demonstrated change in that authority. Iteration, voting, multiple roles,
and graph structure alone are insufficient.

Three mutually exclusive ratings are applied in order. A case is broadly
aligned when the proposed and source-coded overall categories agree and the
reported workflow does not contradict their defining control features.
When the categories differ, partial alignment requires a substantive local
mechanism compatible with the proposed category and an explicit overall
control conflict; otherwise the case is divergent. For a flat recommendation,
partial alignment requires all three conditions: (F1) at least two expert
roles contribute their own analyses; (F2) they review the same report under
the same acceptance or rejection rule, without an exclusive expert reviewer;
and (F3) objections feed report revision and renewed review. An iteration
limit is permitted, so unanimity is not guaranteed. For a hierarchical
recommendation, local compatibility requires fixed delegation, routing,
approval, or synthesis authority in a substantive sub-process. For a hybrid
recommendation, it requires an actual change in decision-authority
configuration within a reported sub-process. Insufficient method evidence
would leave a case unscored and require reporting the scored denominator.

Six cases are broadly aligned, two are partially aligned, and two are
divergent under the coding used here. MedAgents and LLM-MedQA retain
hierarchical overall control while supporting equal-participation expert
review locally. These local mechanisms explain partial alignment with a
flat recommendation; they do not establish a flat or hybrid overall
architecture. LegalGraphRAG and EduPlanner remain divergent. Du et al.'s
peer debate is flat at the macro level but uses iterative convergence;
EduPlanner and Financial Reflection QA combine convergent objectives with
evaluator or critic feedback. These boundary cases show that competing
requirements can make a single categorical label insufficient and that a
multi-label description of control flow may sometimes be preferable,
provided that overall authority and local mechanisms are distinguished.
Financial Reflection QA remains hierarchical despite critic feedback.
Nine reported workflows
are coded hierarchical and one flat; this sample therefore does not validate
the hybrid category. All ten cases have sufficient method evidence for this
limited comparison. The comparison is retrospective and was not blind or
preregistered; these ratings are descriptive, not prediction accuracy or
evidence of an effective architecture-selection policy.

architecture. LegalGraphRAG and EduPlanner remain divergent. Du et al.'s
peer debate is flat at the macro level but uses iterative convergence;
EduPlanner and Financial Reflection QA combine convergent objectives with
evaluator or critic feedback. These boundary cases show that competing
requirements can make a single categorical label insufficient and that a
multi-label description of control flow may sometimes be preferable,
provided that overall authority and local mechanisms are distinguished.
Financial Reflection QA remains hierarchical despite critic feedback.
Nine reported workflows
```

## D044 — A — 必要纠错成果保留；共享片段仅按批准B/C边界恢复

操作编号：[]。

**before**
```tex
    \textbf{Inferred versus source-based architecture coding} & \textbf{Match} \\

```

**after**
```tex
    \textbf{Inferred versus source-based architecture coding} & \textbf{Match} \\
```

## D045a — C — Q5已执行（按批准方案联动）

操作编号：[22]。

**before**
```tex
    MedAgents \citep{tang2024medagents} & Multi-specialty medical QA; high complexity and moderate risk & Flat versus hierarchical staged synthesis & $\times$ \\
    LLM-MedQA \citep{tang2025llmmedqa} & Standardised medical MCQ; convergent objective with diverse views & Flat versus hierarchical voting pipeline & $\times$ \\
    LegalGraphRAG \citep{legalgraphrag2026} & Legal verdict prediction; high risk and structured retrieval & Hybrid versus hierarchical graph audit chain & $\times$ \\
    Triad \citep{hu2024triad} & Knowledge-base QA; standardised Text-to-SPARQL workflow & Hierarchical versus hierarchical pipeline & $\checkmark$ \\

```

**after**
```tex
Flat versus hierarchical staged synthesis & $\triangle$

Flat versus hierarchical voting pipeline & $\triangle$
```

## D045b — C — Q5已执行（按批准方案联动）

操作编号：[23]。

**before**
```tex
    MedAgents \citep{tang2024medagents} & Multi-specialty medical QA; high complexity and moderate risk & Flat versus hierarchical staged synthesis & $\times$ \\
    LLM-MedQA \citep{tang2025llmmedqa} & Standardised medical MCQ; convergent objective with diverse views & Flat versus hierarchical voting pipeline & $\times$ \\
    LegalGraphRAG \citep{legalgraphrag2026} & Legal verdict prediction; high risk and structured retrieval & Hybrid versus hierarchical graph audit chain & $\times$ \\
    Triad \citep{hu2024triad} & Knowledge-base QA; standardised Text-to-SPARQL workflow & Hierarchical versus hierarchical pipeline & $\checkmark$ \\

```

**after**
```tex
Flat versus hierarchical staged synthesis & $\triangle$

Flat versus hierarchical voting pipeline & $\triangle$
```

## D045c — C — Q5已执行（保留当前已符合批准规则的片段）

操作编号：[22, 23]。

**before**
```tex
    MedAgents \citep{tang2024medagents} & Multi-specialty medical QA; high complexity and moderate risk & Flat versus hierarchical staged synthesis & $\times$ \\
    LLM-MedQA \citep{tang2025llmmedqa} & Standardised medical MCQ; convergent objective with diverse views & Flat versus hierarchical voting pipeline & $\times$ \\
    LegalGraphRAG \citep{legalgraphrag2026} & Legal verdict prediction; high risk and structured retrieval & Hybrid versus hierarchical graph audit chain & $\times$ \\
    Triad \citep{hu2024triad} & Knowledge-base QA; standardised Text-to-SPARQL workflow & Hierarchical versus hierarchical pipeline & $\checkmark$ \\

```

**after**
```tex
Flat versus hierarchical staged synthesis & $\triangle$

Flat versus hierarchical voting pipeline & $\triangle$
```

## D045d — A — 必要纠错成果保留；共享片段仅按批准B/C边界恢复

操作编号：[22, 23]。

**before**
```tex
    MedAgents \citep{tang2024medagents} & Multi-specialty medical QA; high complexity and moderate risk & Flat versus hierarchical staged synthesis & $\times$ \\
    LLM-MedQA \citep{tang2025llmmedqa} & Standardised medical MCQ; convergent objective with diverse views & Flat versus hierarchical voting pipeline & $\times$ \\
    LegalGraphRAG \citep{legalgraphrag2026} & Legal verdict prediction; high risk and structured retrieval & Hybrid versus hierarchical graph audit chain & $\times$ \\
    Triad \citep{hu2024triad} & Knowledge-base QA; standardised Text-to-SPARQL workflow & Hierarchical versus hierarchical pipeline & $\checkmark$ \\

```

**after**
```tex
Flat versus hierarchical staged synthesis & $\triangle$

Flat versus hierarchical voting pipeline & $\triangle$
```

## D046a — A — 必要纠错成果保留；共享片段仅按批准B/C边界恢复

操作编号：[]。

**before**
```tex
    Multiagent debate (Du) \citep{du2024multiagent_debate} & Factual QA and reasoning; peer exchange & Flat versus flat iterative debate & $\checkmark$ \\

```

**after**
```tex
    Multiagent debate (Du) \citep{du2024multiagent_debate} & Factual QA and reasoning; peer exchange & Flat versus flat iterative debate & $\checkmark$ \\
```

## D046b — C — Q5已执行（保留当前已符合批准规则的片段）

操作编号：[]。

**before**
```tex
    Multiagent debate (Du) \citep{du2024multiagent_debate} & Factual QA and reasoning; peer exchange & Flat versus flat iterative debate & $\checkmark$ \\

```

**after**
```tex
    Multiagent debate (Du) \citep{du2024multiagent_debate} & Factual QA and reasoning; peer exchange & Flat versus flat iterative debate & $\checkmark$ \\
```

## D047a — A — 必要纠错成果保留；共享片段仅按批准B/C边界恢复

操作编号：[]。

**before**
```tex
    Financial Reflection QA \citep{fatemi2024financialqa} & Numerical QA; convergence with critic feedback & Hierarchical versus hierarchical critic feedback & $\checkmark$ \\

```

**after**
```tex
    Financial Reflection QA \citep{fatemi2024financialqa} & Numerical QA; convergence with critic feedback & Hierarchical versus hierarchical critic feedback & $\checkmark$ \\
```

## D047b — C — Q5已执行（保留当前已符合批准规则的片段）

操作编号：[]。

**before**
```tex
    Financial Reflection QA \citep{fatemi2024financialqa} & Numerical QA; convergence with critic feedback & Hierarchical versus hierarchical critic feedback & $\checkmark$ \\

```

**after**
```tex
    Financial Reflection QA \citep{fatemi2024financialqa} & Numerical QA; convergence with critic feedback & Hierarchical versus hierarchical critic feedback & $\checkmark$ \\
```

## D048a — C — Q5已执行（按批准方案联动）

操作编号：[24, 42]。

**before**
```tex
  \textit{Note}: $\checkmark$ = exact category agreement; $\times$ = different
  categories. Proposed labels are retained from the preceding draft;
  source-based labels are the authors' retrospective control-flow coding.
  Neither label nor agreement establishes selection accuracy or safety.
  Triad is a single-agent, three-role supporting study (S), outside the
  13 core studies. ChatDev, AgentCoder, and EduPlanner are also supporting
  workflow examples. Criterion profiles are illustrative author judgments.

```

**after**
```tex
\textit{Note}: $\checkmark$ = broadly aligned; $\triangle$ = partially aligned;
  $\times$ = divergent, under the ordered rules in the text. Proposed labels
  are retained from the preceding draft; source-based labels and ratings are
  the authors' retrospective coding. Partial alignment denotes local
  organisational compatibility despite an overall control conflict.
  MedAgents was checked against its ACL 2024 method and Algorithm~1;
  LLM-MedQA against the IJCNN 2025 paper, Sections~III-A--F and Algorithm~1
  (physical pages 3--6). Neither labels nor ratings
  establish prediction accuracy, selection effectiveness, or safety.

  LLM-MedQA against the IJCNN 2025 paper, Sections~III-A--F and Algorithm~1
  (physical pages 3--6).
```

## D048b — A — 必要纠错成果保留；共享片段仅按批准B/C边界恢复

操作编号：[24, 42]。

**before**
```tex
  \textit{Note}: $\checkmark$ = exact category agreement; $\times$ = different
  categories. Proposed labels are retained from the preceding draft;
  source-based labels are the authors' retrospective control-flow coding.
  Neither label nor agreement establishes selection accuracy or safety.
  Triad is a single-agent, three-role supporting study (S), outside the
  13 core studies. ChatDev, AgentCoder, and EduPlanner are also supporting
  workflow examples. Criterion profiles are illustrative author judgments.

```

**after**
```tex
\textit{Note}: $\checkmark$ = broadly aligned; $\triangle$ = partially aligned;
  $\times$ = divergent, under the ordered rules in the text. Proposed labels
  are retained from the preceding draft; source-based labels and ratings are
  the authors' retrospective coding. Partial alignment denotes local
  organisational compatibility despite an overall control conflict.
  MedAgents was checked against its ACL 2024 method and Algorithm~1;
  LLM-MedQA against the IJCNN 2025 paper, Sections~III-A--F and Algorithm~1
  (physical pages 3--6). Neither labels nor ratings
  establish prediction accuracy, selection effectiveness, or safety.

  LLM-MedQA against the IJCNN 2025 paper, Sections~III-A--F and Algorithm~1
  (physical pages 3--6).
```

## D049a — C — Q4已执行（按批准方案联动）

操作编号：[25]。

**before**
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

**after**
```tex
high-risk, cross-domain consultation, parallel specialist analysis may improve
coverage, but final decisions require an explicit review boundary. A fixed
review or human-approval boundary remains hierarchical; hybrid control is a
plausible candidate only when decision authority changes. Standardised,
evidence-grounded QA generally supports a hierarchical RAG baseline with
source and citation checks. Open-ended educational or legal tasks may benefit
from bounded peer critique, but legal use additionally requires auditability
and human accountability. These examples illustrate how task and governance
requirements constrain the design space; they do not imply one universally
```

## D049b — B — 局部恢复

操作编号：[25]。

**before**
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

**after**
```tex
high-risk, cross-domain consultation, parallel specialist analysis may improve
coverage, but final decisions require an explicit review boundary. A fixed
review or human-approval boundary remains hierarchical; hybrid control is a
plausible candidate only when decision authority changes. Standardised,
evidence-grounded QA generally supports a hierarchical RAG baseline with
source and citation checks. Open-ended educational or legal tasks may benefit
from bounded peer critique, but legal use additionally requires auditability
and human accountability. These examples illustrate how task and governance
requirements constrain the design space; they do not imply one universally
```

## D050a — A — 必要纠错成果保留；共享片段仅按批准B/C边界恢复

操作编号：[26, 41]。

**before**
```tex
Industry initiatives address different parts of the interface problem.
Anthropic introduced the Model Context Protocol (MCP)
\citep{anthropic2024mcp} to standardise connections to external tools and data
sources. Google's Agent2Agent (A2A) protocol \citep{google2025a2a} supports
communication and task coordination between agents across frameworks and
vendors. These interfaces can support heterogeneous multi-agent QA systems.

```

**after**
```tex
With the rapid development of multi-agent ecosystems, interoperability barriers have arisen between agents developed by different vendors.
To address this issue, the industry has initiated efforts to standardize communication protocols. For example, 

For example, Anthropic introduced
```

## D050b — B — 局部恢复

操作编号：[26, 41]。

**before**
```tex
Industry initiatives address different parts of the interface problem.
Anthropic introduced the Model Context Protocol (MCP)
\citep{anthropic2024mcp} to standardise connections to external tools and data
sources. Google's Agent2Agent (A2A) protocol \citep{google2025a2a} supports
communication and task coordination between agents across frameworks and
vendors. These interfaces can support heterogeneous multi-agent QA systems.

```

**after**
```tex
With the rapid development of multi-agent ecosystems, interoperability barriers have arisen between agents developed by different vendors.
To address this issue, the industry has initiated efforts to standardize communication protocols. For example, 

For example, Anthropic introduced
```

## D051 — A — 必要纠错成果保留；共享片段仅按批准B/C边界恢复

操作编号：[]。

**before**
```tex
by explicitly separating planning from solving and reducing missing-step
errors on the evaluated reasoning tasks.

```

**after**
```tex
by explicitly separating planning from solving and reducing missing-step
errors on the evaluated reasoning tasks.
```

## D052a — A — 必要纠错成果保留；共享片段仅按批准B/C边界恢复

操作编号：[27]。

**before**
```tex
After decomposition, the system must assign sub-tasks to suitable agents.
For example, MetaGPT \citep{hong2024metagpt} organises agents through
predefined software-engineering roles, while AgentVerse
\citep{chen2024agentverse} recruits experts by generating task-specific
expertise descriptions and adjusts team composition using evaluation
feedback. These mechanisms guide which agents contribute to a task;
their scheduling efficiency requires separate evaluation.

```

**after**
```tex
After decomposition, the system must assign sub-tasks to the most suitable
agents.
```

## D052b — B — 局部恢复

操作编号：[27]。

**before**
```tex
After decomposition, the system must assign sub-tasks to suitable agents.
For example, MetaGPT \citep{hong2024metagpt} organises agents through
predefined software-engineering roles, while AgentVerse
\citep{chen2024agentverse} recruits experts by generating task-specific
expertise descriptions and adjusts team composition using evaluation
feedback. These mechanisms guide which agents contribute to a task;
their scheduling efficiency requires separate evaluation.

```

**after**
```tex
After decomposition, the system must assign sub-tasks to the most suitable
agents.
```

## D053a — A — 必要纠错成果保留；共享片段仅按批准B/C边界恢复

操作编号：[28]。

**before**
```tex
In complex collaboration, designers may provide a shared evidence repository
when agents need access to the same verified information. A graph, vector
store, document store, or their combination is an implementation choice,
rather than a requirement that every system use a global knowledge graph.
New agents may reuse relevant context subject to provenance and access
checks. Whether this reduces repeated retrieval or inconsistent answers
requires measurement; synchronisation is not automatically real time.

```

**after**
```tex
In complex collaboration, knowledge need not be siloed within individual
agents. The system can provide a shared knowledge graph when collaborative
nodes need access to critical facts. By constructing a shared graph-vector
database, newly spawned sub-agents can reuse the team's cumulative knowledge,
potentially reducing redundant retrieval and cognitive divergence; these
effects and synchronisation latency require evaluation.
```

## D053b — B — 局部恢复

操作编号：[28]。

**before**
```tex
In complex collaboration, designers may provide a shared evidence repository
when agents need access to the same verified information. A graph, vector
store, document store, or their combination is an implementation choice,
rather than a requirement that every system use a global knowledge graph.
New agents may reuse relevant context subject to provenance and access
checks. Whether this reduces repeated retrieval or inconsistent answers
requires measurement; synchronisation is not automatically real time.

```

**after**
```tex
In complex collaboration, knowledge need not be siloed within individual
agents. The system can provide a shared knowledge graph when collaborative
nodes need access to critical facts. By constructing a shared graph-vector
database, newly spawned sub-agents can reuse the team's cumulative knowledge,
potentially reducing redundant retrieval and cognitive divergence; these
effects and synchronisation latency require evaluation.
```

## D054 — A — 必要纠错成果保留；共享片段仅按批准B/C边界恢复

操作编号：[]。

**before**
```tex
current QA session. For example, MemGPT \citep{packer2023memgpt} draws on
operating-system memory hierarchies to manage a limited main context and
external memory. Function calls control information transfer between them,
while a FIFO message queue and recursive summaries manage dialogue context
under the context-window limit.

```

**after**
```tex
current QA session. For example, MemGPT \citep{packer2023memgpt} draws on
operating-system memory hierarchies to manage a limited main context and
external memory. Function calls control information transfer between them,
while a FIFO message queue and recursive summaries manage dialogue context
under the context-window limit.
```

## D055a — A — 必要纠错成果保留；共享片段仅按批准B/C边界恢复

操作编号：[29]。

**before**
```tex
Long-term memory can retain historical experiences and domain knowledge in
external stores \citep{zhang2024memory_survey}. Vector retrieval is one way
to access such information: Retrieval-Augmented Generation (RAG)
\citep{lewis2020rag,gao2024rag_survey} augments generation with retrieved
documents. As one illustrative multi-agent implementation, a retrieval agent
can select the Top-$k$ relevant documents from knowledge base $\mathcal{D}$

```

**after**
```tex
Long-term memory can rely on vector databases to store historical
experiences and external domain knowledge \citep{zhang2024memory_survey}.
A representative access mechanism is Retrieval-Augmented Generation (RAG)
\citep{lewis2020rag,gao2024rag_survey}, through which multi-agent QA systems
can access long-term memory. In an illustrative implementation, a retrieval
agent can select the Top-$k$ relevant documents from knowledge base $\mathcal{D}$
```

## D055b — B — 局部恢复

操作编号：[29]。

**before**
```tex
Long-term memory can retain historical experiences and domain knowledge in
external stores \citep{zhang2024memory_survey}. Vector retrieval is one way
to access such information: Retrieval-Augmented Generation (RAG)
\citep{lewis2020rag,gao2024rag_survey} augments generation with retrieved
documents. As one illustrative multi-agent implementation, a retrieval agent
can select the Top-$k$ relevant documents from knowledge base $\mathcal{D}$

```

**after**
```tex
Long-term memory can rely on vector databases to store historical
experiences and external domain knowledge \citep{zhang2024memory_survey}.
A representative access mechanism is Retrieval-Augmented Generation (RAG)
\citep{lewis2020rag,gao2024rag_survey}, through which multi-agent QA systems
can access long-term memory. In an illustrative implementation, a retrieval
agent can select the Top-$k$ relevant documents from knowledge base $\mathcal{D}$
```

## D056 — A — 必要纠错成果保留；共享片段仅按批准B/C边界恢复

操作编号：[]。

**before**
```tex
evolved from passive retrieval to active variants. Self-RAG
\citep{asai2024selfrag} uses reflection tokens to decide when to retrieve and
to critique generated passages, while FLARE \citep{jiang2023active_rag}
triggers retrieval when predicted upcoming text contains low-confidence
tokens and then regenerates that text. These controls can inform retrieval
components in a multi-agent workflow.

```

**after**
```tex
evolved from passive retrieval to active variants. Self-RAG
\citep{asai2024selfrag} uses reflection tokens to decide when to retrieve and
to critique generated passages, while FLARE \citep{jiang2023active_rag}
triggers retrieval when predicted upcoming text contains low-confidence
tokens and then regenerates that text. These controls can inform retrieval
components in a multi-agent workflow.
```

## D057 — B — 完整恢复

操作编号：[30]。

**before**
```tex
Chain-of-Thought (CoT) prompting \citep{wei2022chain_of_thought}
can improve performance on evaluated arithmetic, commonsense, and symbolic
reasoning tasks.

```

**after**
```tex
Chain-of-Thought (CoT) prompting \citep{wei2022chain_of_thought} has
greatly unlocked the reasoning potential of LLMs.
```

## D058 — A — 必要纠错成果保留；共享片段仅按批准B/C边界恢复

操作编号：[]。

**before**
```tex
In the single-model baseline, $K$ reasoning paths
$\{(r_k, a_k)\}_{k=1}^{K}$ are sampled for the same question, and majority
voting selects the final answer:

```

**after**
```tex
In the single-model baseline, $K$ reasoning paths
$\{(r_k, a_k)\}_{k=1}^{K}$ are sampled for the same question, and majority
voting selects the final answer:
```

## D059 — A — 必要纠错成果保留；共享片段仅按批准B/C边界恢复

操作编号：[]。

**before**
```tex
Chain-of-Agents \citep{zhang2024chain_agents} distributes evidence processing
across worker agents, while Tree of Thoughts
\citep{yao2023tree_of_thoughts} and Graph of Thoughts
\citep{besta2024graph_of_thoughts} organise intermediate reasoning states as
search structures.

```

**after**
```tex
Chain-of-Agents \citep{zhang2024chain_agents} distributes evidence processing
across worker agents, while Tree of Thoughts
\citep{yao2023tree_of_thoughts} and Graph of Thoughts
\citep{besta2024graph_of_thoughts} organise intermediate reasoning states as
search structures.
```

## D060a — A — 必要纠错成果保留；共享片段仅按批准B/C边界恢复

操作编号：[31]。

**before**
```tex
Reflection and critique are possible approaches to factual-error reduction;
they do not guarantee correctness or replace checking the underlying evidence.

```

**after**
```tex
To suppress hallucination, agents may use iterative self-examination.
```

## D060b — B — 局部恢复

操作编号：[31]。

**before**
```tex
Reflection and critique are possible approaches to factual-error reduction;
they do not guarantee correctness or replace checking the underlying evidence.

```

**after**
```tex
To suppress hallucination, agents may use iterative self-examination.
```

## D061 — A — 必要纠错成果保留；共享片段仅按批准B/C边界恢复

操作编号：[]。

**before**
```tex
Chain-of-Verification \citep{dhuliawala2023chain_of_verification} drafts an
answer, plans verification questions, answers them independently, and then
revises the original answer. This procedure targets factual errors; dedicated
critic agents are a possible multi-agent extension that requires evaluation.

```

**after**
```tex
Chain-of-Verification \citep{dhuliawala2023chain_of_verification} drafts an
answer, plans verification questions, answers them independently, and then
revises the original answer. This procedure targets factual errors; dedicated
critic agents are a possible multi-agent extension that requires evaluation.
```

## D062 — A — 必要纠错成果保留；共享片段仅按批准B/C边界恢复

操作编号：[]。

**before**
```tex
\begin{figure*}[pos=t,width=\textwidth]

```

**after**
```tex
\begin{figure*}[pos=t,width=\textwidth]
```

## D063 — A — 必要纠错成果保留；共享片段仅按批准B/C边界恢复

操作编号：[]。

**before**
```tex
\includegraphics[width=0.94\textwidth]{classify.jpg}

```

**after**
```tex
\includegraphics[width=0.94\textwidth]{classify.jpg}
```

## D064 — A — 必要纠错成果保留；共享片段仅按批准B/C边界恢复

操作编号：[]。

**before**
```tex
\end{figure*}

```

**after**
```tex
\end{figure*}
```

## D065 — A — 必要纠错成果保留；共享片段仅按批准B/C边界恢复

操作编号：[]。

**before**
```tex
\begin{table*}[pos=t,width=\textwidth]

```

**after**
```tex
\begin{table*}[pos=t,width=\textwidth]
```

## D066 — A — 必要纠错成果保留；共享片段仅按批准B/C边界恢复

操作编号：[]。

**before**
```tex
  \small

```

**after**
```tex
  \small
```

## D067 — A — 必要纠错成果保留；共享片段仅按批准B/C边界恢复

操作编号：[]。

**before**
```tex
  \begin{tabularx}{\textwidth}{>{\raggedright\arraybackslash}p{2.6cm}
                  >{\raggedright\arraybackslash}p{2.0cm}
                  >{\raggedright\arraybackslash}X
                  >{\raggedright\arraybackslash}X
                  >{\raggedright\arraybackslash}X
                  >{\raggedright\arraybackslash}X}

```

**after**
```tex
  \begin{tabularx}{\textwidth}{>{\raggedright\arraybackslash}p{2.6cm}
                  >{\raggedright\arraybackslash}p{2.0cm}
                  >{\raggedright\arraybackslash}X
                  >{\raggedright\arraybackslash}X
                  >{\raggedright\arraybackslash}X
                  >{\raggedright\arraybackslash}X}
```

## D068 — C — Q4已执行（按批准方案联动）

操作编号：[33, 34]。

**before**
```tex
    CAMEL \citep{li2023camel} & Role-paired workflow &

```

**after**
```tex
    CAMEL \citep{li2023camel} & Role-paired workflow &
```

## D069 — A — 必要纠错成果保留；共享片段仅按批准B/C边界恢复

操作编号：[]。

**before**
```tex
      Role-conditioned dialogue context &

```

**after**
```tex
      Role-conditioned dialogue context &
```

## D070 — A — 必要纠错成果保留；共享片段仅按批准B/C边界恢复

操作编号：[]。

**before**
```tex
      Within-phase dialogue; cross-phase solutions &

```

**after**
```tex
      Within-phase dialogue; cross-phase solutions &
```

## D071 — A — 必要纠错成果保留；共享片段仅按批准B/C边界恢复

操作编号：[]。

**before**
```tex
      Shared message pool and project documents &

```

**after**
```tex
      Shared message pool and project documents &
```

## D072 — C — Q4已执行（按批准方案联动）

操作编号：[33, 34]。

**before**
```tex
    AgentVerse \citep{chen2024agentverse} & Adaptive role pipeline &

```

**after**
```tex
    AgentVerse \citep{chen2024agentverse} & Adaptive role pipeline &
```

## D073 — A — 必要纠错成果保留；共享片段仅按批准B/C边界恢复

操作编号：[]。

**before**
```tex
      Conversation and evaluation context &

```

**after**
```tex
      Conversation and evaluation context &
```

## D074a — A — 必要纠错成果保留；共享片段仅按批准B/C边界恢复

操作编号：[]。

**before**
```tex
    LangGraph \citep{langgraph2024,langgraph2024interrupt} & Configurable state graph &

```

**after**
```tex
    LangGraph \citep{langgraph2024,langgraph2024interrupt} & Configurable state graph &
```

## D074b — C — Q4已执行（按批准方案联动）

操作编号：[33, 34]。

**before**
```tex
    LangGraph \citep{langgraph2024,langgraph2024interrupt} & Configurable state graph &

```

**after**
```tex
    LangGraph \citep{langgraph2024,langgraph2024interrupt} & Configurable state graph &
```

## D075a — C — Q4已执行（按批准方案联动）

操作编号：[33, 34]。

**before**
```tex
    GPTSwarm \citep{zhuge2024gptswarm} & Optimizable agent graph &
      DAG information flow &
      Prompt and edge optimization &
      Node input--output histories &
      MMLU QA; graph optimization \\

```

**after**
```tex
    GPTSwarm \citep{zhuge2024gptswarm} & Optimizable agent graph &
      Computational graph connections &
      Automatic graph-structure search &
      Intra-node state &
      MMLU QA; graph optimization \\

implementation dimensions: control / organisation, communication,

\textbf{Framework} & \textbf{Control / organisation}
```

## D075b — A — 必要纠错成果保留；共享片段仅按批准B/C边界恢复

操作编号：[32, 33, 34]。

**before**
```tex
    GPTSwarm \citep{zhuge2024gptswarm} & Optimizable agent graph &
      DAG information flow &
      Prompt and edge optimization &
      Node input--output histories &
      MMLU QA; graph optimization \\

```

**after**
```tex
    GPTSwarm \citep{zhuge2024gptswarm} & Optimizable agent graph &
      Computational graph connections &
      Automatic graph-structure search &
      Intra-node state &
      MMLU QA; graph optimization \\

implementation dimensions: control / organisation, communication,

\textbf{Framework} & \textbf{Control / organisation}
```

## D075c — B — 局部恢复

操作编号：[32]。

**before**
```tex
    GPTSwarm \citep{zhuge2024gptswarm} & Optimizable agent graph &
      DAG information flow &
      Prompt and edge optimization &
      Node input--output histories &
      MMLU QA; graph optimization \\

```

**after**
```tex
    GPTSwarm \citep{zhuge2024gptswarm} & Optimizable agent graph &
      Computational graph connections &
      Automatic graph-structure search &
      Intra-node state &
      MMLU QA; graph optimization \\

implementation dimensions: control / organisation, communication,

\textbf{Framework} & \textbf{Control / organisation}
```

## D076 — A — 必要纠错成果保留；共享片段仅按批准B/C边界恢复

操作编号：[]。

**before**
```tex
  \end{tabularx}
\end{table*}

```

**after**
```tex
  \end{tabularx}
\end{table*}
```

## D077 — A — 必要纠错成果保留；共享片段仅按批准B/C边界恢复

操作编号：[]。

**before**
```tex
    Document ingestion, retrieval, and configurable RAG components \\

```

**after**
```tex
    Document ingestion, retrieval, and configurable RAG components \\
```

## D078 — B — 完整恢复

操作编号：[35]。

**before**
```tex
Table~\ref{tab:benchmark_resources} summarizes these resources and their
primary evaluation roles.

```

**after**
```tex
[保留删除或格式成果；见保护验证及实际补丁]
```

## D079 — A — 必要纠错成果保留；共享片段仅按批准B/C边界恢复

操作编号：[]。

**before**
```tex
critic feedback and answer revision. These cases illustrate why a single

```

**after**
```tex
critic feedback and answer revision. These cases illustrate why a single
```

## D080a — A — 必要纠错成果保留；共享片段仅按批准B/C边界恢复

操作编号：[36]。

**before**
```tex
resolving dependencies or disagreement. If each of $N$ agents sends one
message to every other agent, there are $N(N-1)$ directed message deliveries
per round. Actual token and latency costs also depend on message length,
scheduling, and context handling. Scaling experiments illustrate
task-dependent benefits and topology-dependent context costs

```

**after**
```tex
resolving dependencies or disagreement. In a fully connected broadcast
topology, potential pairwise messages per round grow quadratically with team
size, potentially increasing token and latency costs without guaranteeing information gain
```

## D080b — B — 局部恢复

操作编号：[36]。

**before**
```tex
resolving dependencies or disagreement. If each of $N$ agents sends one
message to every other agent, there are $N(N-1)$ directed message deliveries
per round. Actual token and latency costs also depend on message length,
scheduling, and context handling. Scaling experiments illustrate
task-dependent benefits and topology-dependent context costs

```

**after**
```tex
resolving dependencies or disagreement. In a fully connected broadcast
topology, potential pairwise messages per round grow quadratically with team
size, potentially increasing token and latency costs without guaranteeing information gain
```

## D081 — A — 必要纠错成果保留；共享片段仅按批准B/C边界恢复

操作编号：[]。

**before**
```tex
modes. Conventional benchmarks and agent environments measure answer
correctness, supporting-fact accuracy, or task completion
\citep{hendrycks2021mmlu,yang2018hotpotqa,liu2024agentbench,mialon2024gaia};
these outcome measures alone do not establish whether debate added independent
evidence, whether a long-context chain lost a decisive fact, or whether a
critic detected and corrected an error. Additional reasoning rounds

```

**after**
```tex
modes. Conventional benchmarks and agent environments measure answer
correctness, supporting-fact accuracy, or task completion
\citep{hendrycks2021mmlu,yang2018hotpotqa,liu2024agentbench,mialon2024gaia};
these outcome measures alone do not establish whether debate added independent
evidence, whether a long-context chain lost a decisive fact, or whether a
critic detected and corrected an error. Additional reasoning rounds
```

## D082 — A — 必要纠错成果保留；共享片段仅按批准B/C边界恢复

操作编号：[]。

**before**
```tex
\citep{han2024mast}, suggesting that process-level measures of contribution,
complementarity, and error correction could complement outcome measures.

```

**after**
```tex
\citep{han2024mast}, suggesting that process-level measures of contribution,
complementarity, and error correction could complement outcome measures.
```

## D083 — A — 必要纠错成果保留；共享片段仅按批准B/C边界恢复

操作编号：[]。

**before**
```tex
appropriate to the decision. Medical and legal QA provide application
contexts for these proposed oversight requirements
\citep{tang2024medagents,cui2023chatlaw}. Frameworks support configurable
interaction and workflow control \citep{duan2024langgraph_crewai,
langgraph2024interrupt}. Their use still requires designers to specify when
intervention is useful, what can be revised, and how the intervention affects
subsequent reasoning. Oversight that

```

**after**
```tex
appropriate to the decision. Medical and legal QA provide application
contexts for these proposed oversight requirements
\citep{tang2024medagents,cui2023chatlaw}. Frameworks support configurable
interaction and workflow control \citep{duan2024langgraph_crewai,
langgraph2024interrupt}. Their use still requires designers to specify when
intervention is useful, what can be revised, and how the intervention affects
subsequent reasoning. Oversight that
```

## D084a — B — 局部恢复

操作编号：[37]。

**before**
```tex
retrospective diagnostic comparison rather than independent validation; it contains
no source-coded hybrid example. Broader

```

**after**
```tex
verification exercise rather than independent confirmation of general validity;
the three-tier ratings describe organisational compatibility, and this sample
contains no source-coded hybrid example. Broader
```

## D084b — C — Q5已执行（按批准方案联动）

操作编号：[37]。

**before**
```tex
retrospective diagnostic comparison rather than independent validation; it contains
no source-coded hybrid example. Broader

```

**after**
```tex
verification exercise rather than independent confirmation of general validity;
the three-tier ratings describe organisational compatibility, and this sample
contains no source-coded hybrid example. Broader
```

## D085 — A — 必要纠错成果保留；共享片段仅按批准B/C边界恢复

操作编号：[]。

**before**
```tex
\texttt{search\_log.csv}. The current field-level and claim-level audit tables
are \texttt{reference\_field\_audit.csv} and
\texttt{citation\_claim\_audit.csv}; they record unresolved
optional publication fields, documented version selections, and evidence boundaries.

```

**after**
```tex
\texttt{search\_log.csv}. The current field-level and claim-level audit tables
are \texttt{reference\_field\_audit.csv} and
\texttt{citation\_claim\_audit.csv}; they record unresolved
optional publication fields, documented version selections, and evidence boundaries.
```

## D086 — A — 必要纠错成果保留；共享片段仅按批准B/C边界恢复

操作编号：[]。

**before**
```tex
reference formatting, and with plotting code and layout for the data-derived
reference-corpus diagram (Fig.~\ref{fig:reference_corpus}), and used Nano Banana to generate the initial draft of
an explanatory architecture schematic during drafting.

```

**after**
```tex
reference formatting, and with plotting code and layout for the data-derived
reference-corpus diagram (Fig.~\ref{fig:reference_corpus}), and used Nano Banana to generate the initial draft of
an explanatory architecture schematic during drafting.
```

## D087 — A — 必要纠错成果保留；共享片段仅按批准B/C边界恢复

操作编号：[]。

**before**
```tex
\printbibliography

```

**after**
```tex
\printbibliography
```
