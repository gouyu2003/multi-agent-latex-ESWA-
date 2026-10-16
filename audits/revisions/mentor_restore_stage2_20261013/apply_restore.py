from pathlib import Path
import json, hashlib, re, difflib

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
items = {x['id']: x for x in json.loads((OUT/'plan_items.json').read_text(encoding='utf8'))}
before_bytes = (OUT/'protection/manuscript.tex').read_bytes()
assert (ROOT/'manuscript.tex').read_bytes() == before_bytes, 'Concurrent manuscript change; stop'
text = before_bytes.decode('utf8').replace('\r\n','\n')
operations = []

def replace(ids, old, new):
    global text
    old = old.rstrip('\n'); new = new.rstrip('\n')
    assert text.count(old) == 1, (ids, 'Expected unique source fragment', text.count(old), old[:100])
    start = text.index(old)
    operations.append({'ids':ids.split(','), 'before':old, 'after':new, 'line_at_operation':text[:start].count('\n')+1})
    text = text[:start] + new + text[start+len(old):]

def block(did, new=None, ids=None):
    x = items[did]
    replace(ids or did, x['pre_restore_plan'], x['mentor'] if new is None else new)

block('D003b', 'review of multi-agent collaborative QA based on 78 cited sources from an\n85-record bibliography pool, including 13 core empirical studies\npublished through July 2026. We first')
block('D004')
block('D005b', r'''\emph{Third}, a single model may lack sufficient domain coverage for a query
that requires several areas of expertise.''')
block('D007', r'''Although several surveys on LLM-based agents exist
\citep{guo2024llm_multiagent_survey,tran2025multiagent_survey,wang2024survey_autonomous_agents},
they primarily address general agent architectures, communication, orchestration,
and foundational capabilities, with some coverage of QA. A systematic account
of collaboration topologies, enabling mechanisms, task and governance
requirements, and architecture-selection trade-offs for QA remains limited.
This survey addresses that gap through five related contributions:''')
old = items['D010c']['pre_restore_plan']; keep = old.split('\n\nSource-level checks')[0]
block('D010c', keep + '''\n\nSource-level checks on 8 and 10 October 2026 confirmed corrections in an
85-record bibliography pool with 78 actively cited sources; unavailable
optional fields and source discrepancies remain documented in the audit trail.''')
block('D011')
block('D012', r'''(4) QA, retrieval-augmented answering, conversational QA, or question-driven domain decision support as the primary evaluated task; and''')
replace('D012,D013b', 'When both a preprint and a peer-reviewed version of a work existed, the peer-reviewed final publication was preferred.', 'QA may be a co-primary evaluated task, but incidental QA demonstrations are insufficient. When both a preprint and a peer-reviewed version of a work existed, the peer-reviewed final publication was preferred.')
replace('D013b,D013c', '''The 13 role-I studies
were reassessed against these five criteria and retain their labels.
QA need not be their sole task, but incidental QA demonstrations are
insufficient for inclusion.''', '''The 13 role-I studies
provide the empirical basis for the architecture taxonomy and subsequent
evidence synthesis; other claims are supported by sources appropriate to their scope.''')
replace('D013c', 'Other claims use sources appropriate to their scope.\n', '')
block('D018b', r'''\citep{minsky1988society}, a multi-agent architecture decomposes a complex
task and assigns subtasks to agents with distinct responsibilities. Park et al.'s
social simulations illustrate individual memory, reflection, and planning
\citep{park2023generative_agents}. A single ``generalist'' workflow may combine''')
block('D019')
block('D024a', items['D024a']['mentor'].rstrip() + ' A graph representation, edge optimisation, or conditional routing alone does not establish hybrid decision authority; the implementation must actually change who controls decisions.', ids='D024a,D024b')
block('D025')
replace('D026c', 'hybrid authority. State management and performance still require evaluation.', 'hybrid authority. Such adaptive mechanisms enhance routing flexibility, yet\nintroduce extra requirements for state management and performance evaluation.')
block('D027b', items['D027b']['mentor'].replace('langgraph2024}', 'langgraph2024interrupt}'))
block('D028', items['D028']['mentor'].replace('when the workflow must combine deliberation, controlled execution, and conditional review.', 'when the workflow must combine deliberation, controlled execution, and conditional review through changes in decision authority.'))
replace('D029', r'''Table~\ref{tab:9categories} compares representative control patterns and
related mechanisms. Architecture labels, suitable contexts, and limitations
are the authors' synthesis. Role-paired, configurable, and cross-cutting
entries describe mechanisms or tool capabilities, not additional architecture
classes or evidence that every configuration is hybrid.''', r'''Table~\ref{tab:9categories} compares flat, hierarchical, and hybrid architectures
and their related mechanisms. Architecture labels, suitable contexts, and
limitations are the authors' synthesis; related mechanisms are shown separately
and do not define additional architecture classes.''')
start = text.index(r'\begin{table*}', text.index(r'\label{sec:arch_comparison}'))
end = text.index(r'\end{table*}', start) + len(r'\end{table*}')
replace('D030,D031,D032b,D033,D036,D039b', text[start:end], r'''\begin{table*}[pos=t]
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
\end{table*}''')
block('D040b', r'''communication, aggregation, state-management, and inference costs. A
collaborative design is justified only when expected gains in coverage,
reliability, or adaptability offset those costs, as a criterion of this review.
Reported multi-agent failure modes motivate this assessment \citep{han2024mast}.
Assessment should include latency, token use, tool calls, monitoring, and recovery overhead.''')
# D041's existing authority-change and fixed-approver rules implement the approved Q4 boundary.
old_start = text.index('The approach is examined for interpretive consistency using ten published')
old_end = text.index(r'\begin{table*}', old_start)
replace('D042,D043', text[old_start:old_end], r'''The approach is examined for interpretive consistency using ten published
systems. This purposive sample contains both core QA studies and supporting
workflow examples; it does not evaluate performance, establish causal benefit,
or provide independent validation. The proposed labels and criterion profiles
are retained, while reported workflows are coded by decision authority.
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
peer debate remains flat despite repeated rounds, and Financial Reflection
QA remains hierarchical despite critic feedback. Nine reported workflows
are coded hierarchical and one flat; this sample therefore does not validate
the hybrid category. All ten cases have sufficient method evidence for this
limited comparison. The comparison is retrospective and was not blind or
preregistered; these ratings are descriptive, not prediction accuracy or
evidence of an effective architecture-selection policy.

''')
replace('D045a', r'Flat versus hierarchical staged synthesis & $\times$', r'Flat versus hierarchical staged synthesis & $\triangle$')
replace('D045b', r'Flat versus hierarchical voting pipeline & $\times$', r'Flat versus hierarchical voting pipeline & $\triangle$')
# Other eight symbols already implement the approved mutually exclusive scoring.
replace('D048a', r'''\textit{Note}: $\checkmark$ = exact category agreement; $\times$ = different
  categories. Proposed labels are retained from the preceding draft;
  source-based labels are the authors' retrospective control-flow coding.
  Neither label nor agreement establishes selection accuracy or safety.''', r'''\textit{Note}: $\checkmark$ = broadly aligned; $\triangle$ = partially aligned;
  $\times$ = divergent, under the ordered rules in the text. Proposed labels
  are retained from the preceding draft; source-based labels and ratings are
  the authors' retrospective coding. Partial alignment denotes local
  organisational compatibility despite an overall control conflict.
  MedAgents was checked against its ACL 2024 method and Algorithm~1;
  LLM-MedQA against the v1 preprint, Sections~III-A--F and Algorithm~1,
  without a new check of the final conference PDF. Neither labels nor ratings
  establish prediction accuracy, selection effectiveness, or safety.''')
block('D049b', r'''high-risk, cross-domain consultation, parallel specialist analysis may improve
coverage, but final decisions require an explicit review boundary. A fixed
review or human-approval boundary remains hierarchical; hybrid control is a
plausible candidate only when decision authority changes. Standardised,
evidence-grounded QA generally supports a hierarchical RAG baseline with
source and citation checks. Open-ended educational or legal tasks may benefit
from bounded peer critique, but legal use additionally requires auditability
and human accountability. These examples illustrate how task and governance
requirements constrain the design space; they do not imply one universally''', ids='D049a,D049b')
replace('D050b', 'Industry initiatives address different parts of the interface problem.\n', '''With the rapid development of multi-agent ecosystems, interoperability barriers have arisen between agents developed by different vendors.
To address this issue, the industry has initiated efforts to standardize communication protocols. For example, ''')
replace('D052b', 'After decomposition, the system must assign sub-tasks to suitable agents.', 'After decomposition, the system must assign sub-tasks to the most suitable\nagents.')
block('D053b', '''In complex collaboration, knowledge need not be siloed within individual
agents. The system can provide a shared knowledge graph when collaborative
nodes need access to critical facts. By constructing a shared graph-vector
database, newly spawned sub-agents can reuse the team's cumulative knowledge,
potentially reducing redundant retrieval and cognitive divergence; these
effects and synchronisation latency require evaluation.''')
block('D055b', r'''Long-term memory can rely on vector databases to store historical
experiences and external domain knowledge \citep{zhang2024memory_survey}.
A representative access mechanism is Retrieval-Augmented Generation (RAG)
\citep{lewis2020rag,gao2024rag_survey}, through which multi-agent QA systems
can access long-term memory. In an illustrative implementation, a retrieval
agent can select the Top-$k$ relevant documents from knowledge base $\mathcal{D}$''')
block('D057')
block('D060b', '''To suppress hallucination, agents may use iterative self-examination.''')
block('D075c', r'''    GPTSwarm \citep{zhuge2024gptswarm} & Optimizable agent graph &
      Computational graph connections &
      Automatic graph-structure search &
      Intra-node state &
      MMLU QA; graph optimization \\''')
replace('D075b', 'implementation dimensions: control\narchitecture, communication,', 'implementation dimensions: control / organisation, communication,')
replace('D071,D074b,D075b', r'\textbf{Framework} & \textbf{Architecture}', r'\textbf{Framework} & \textbf{Control / organisation}')
block('D078', '')
block('D080b', '''resolving dependencies or disagreement. In a fully connected broadcast
topology, potential pairwise messages per round grow quadratically with team
size, potentially increasing token and latency costs without guaranteeing information gain''')
block('D084a', '''verification exercise rather than independent confirmation of general validity;
the three-tier ratings describe organisational compatibility, and this sample
contains no source-coded hybrid example. Broader''', ids='D084a,D084b')

def citation_keys(s):
    return set(k.strip() for m in re.finditer(r'\\cite(?:p|t)?(?:\[[^\]]*\])*\{([^}]+)\}',s) for k in m[1].split(','))
assert citation_keys(text)==citation_keys(before_bytes.decode('utf8')), 'Citation key set changed'
for pattern in [r'\\iffalse\b.*?\\fi\b',r'\\section\{Conclusion\}.*?\\section\*\{Acknowledgements\}']:
    a=re.findall(pattern,before_bytes.decode('utf8').replace('\r\n','\n'),re.S); b=re.findall(pattern,text,re.S)
    assert a==b, ('Protected section changed',pattern)
new_bytes=text.replace('\n','\r\n').encode('utf8') if b'\r\n' in before_bytes else text.encode('utf8')
(OUT/'candidate.tex').write_bytes(new_bytes)
(OUT/'operations.json').write_text(json.dumps(operations,ensure_ascii=False,indent=2),encoding='utf8')
(OUT/'before_after.patch').write_text(''.join(difflib.unified_diff(before_bytes.decode('utf8').splitlines(True),new_bytes.decode('utf8').splitlines(True),fromfile='pre_restore/manuscript.tex',tofile='restored/manuscript.tex')),encoding='utf8')
assert (ROOT/'manuscript.tex').read_bytes()==before_bytes, 'Concurrent change before write; stop'
(ROOT/'manuscript.tex').write_bytes(new_bytes)
print('Applied operations:',len(operations),'SHA256:',hashlib.sha256(new_bytes).hexdigest())
