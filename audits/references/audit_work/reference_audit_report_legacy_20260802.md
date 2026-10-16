# Reference and Literature-Method Audit

## Scope

- Audit date: 2 August 2026.
- Starting local candidate set: 108 unique BibTeX records.
- Targeted update additions: 3 records.
- Row-level audit coverage: 111 records.
- Final active bibliography: 75 source-verified records.
- Excluded starting records: 36, comprising 32 verified but unused/out-of-scope
  records and 4 records whose corrupted or unmatched metadata could not be
  verified.

The row-level evidence, official source URL, metadata decision, evidence role,
and current citation count are recorded in `literature_audit.csv`. Search
queries and their purposes are recorded in `search_log.csv`.

## Review Design

The manuscript now describes the work as a structured evidence-mapping review,
not an exhaustive PRISMA systematic review. Every starting entry was checked by
title, first author, year, venue, and persistent identifier using Crossref,
OpenAlex, arXiv, official proceedings, publisher pages, or official project
documentation. Targeted gap searches added ReConcile, Chain-of-Agents, and
CoCoA.

Eligibility and evidence roles are explicit:

- `I`: 14 core empirical studies that directly instantiate and evaluate
  multi-agent QA or collaborative reasoning systems.
- `S`: 14 supporting multi-agent systems or application studies.
- `B`: 41 background sources, including models, datasets, single-agent methods,
  and reviews.
- `T`: 6 official technical or software sources.
- `X`: excluded records retained only in the audit trail.

## Main Corrections

- Removed the unsupported claim that 78 papers constituted the included study
  sample. The manuscript now distinguishes 14 core empirical studies from 61
  supporting, background, and technical sources.
- Removed the abstract promise of a dedicated benchmark-dataset and evaluation-
  protocol review that the article did not contain.
- Corrected the application-domain summary so it matches the manuscript.
- Replaced sampling-style or unverifiable search counts with a reproducible
  targeted-search log that does not claim an exhaustive hit count.
- Corrected metadata for final versions and official records, including
  AutoGen, MetaGPT, multi-agent debate, LONGAGENT, ChatDev, MAST, GenMentor,
  EduPlanner, LegalGraphRAG, and other entries marked `Corrected` in the CSV.
- Added the missing AutoGen author Jiale Liu and adopted the official COLM 2024
  title and author list.
- Replaced all 19 truncated `and others` BibTeX author fields with complete
  official author lists or the official group author for GPT-4 and ChatGLM.
- Removed duplicate, unused, malformed, and unverifiable entries from the active
  BibTeX while retaining their audit decisions in the CSV.
- Restored three cited survey records that an inline `%` inside a multi-key
  citation had previously hidden from the citation inventory; the active corpus
  and all reported counts now include those sources.
- Corrected citation-to-claim mismatches involving AutoGen, ChatDev, DSPy,
  Self-Consistency, Chain-of-Agents, LONGAGENT, Reflexion, and Self-Refine.
- Replaced the claimed 70% external-validation result with an explicitly
  author-coded diagnostic stress test: five broadly aligned, three partially
  aligned, and two divergent cases.
- Corrected MedAgents and LLM-MedQA from oversimplified flat-voting labels to
  multi-stage hybrid workflows consistent with their published methods.
- Corrected the cited workplace productivity result to the final 2025 QJE
  article's 15% average increase in issues resolved per hour in the studied
  firm, rather than generalising it to all deployments.

## Unverifiable Starting Records

The following four records could not be matched to an authoritative source and
were not cited in the manuscript:

- `li2024trustworthy_medical_qa`
- `qin2024multiagent_survey_cn`
- `ruanjianbao2024code_gen_survey`
- `zhao2023llm_survey_cn`

## Reproducibility Outputs

- `literature_audit.csv`: one row per audited record, with official source and
  metadata decision.
- `search_log.csv`: source, query, purpose, and additions for each search step.
- `references.bib`: final 75-entry active bibliography.
- `figure_source_data.csv`: exact counts used in the two literature figures.
- `tools/finalize_reference_audit.py`: regenerates the audit table and active
  BibTeX from the preserved inventory and verification cache.
- `tools/generate_reference_figures.py`: regenerates the evidence-flow and
  publication-distribution figures.
- `tools/static_reference_checks.py`: checks citation/BibTeX consistency,
  duplicate keys and DOIs, required fields, source links, stale claims, and
  Highlights length.

## Final Static Check

The final automated check requires all of the following:

- 75 BibTeX entries, 75 unique keys, and 75 cited keys;
- no undefined citations and no uncited active entries;
- no duplicate keys or duplicate DOIs;
- no active entry missing title, author, year, DOI/URL;
- no active entry with an `and others`-truncated author field;
- no verified audit row missing an official source;
- no active audit row left unverified;
- no mismatch between active audit metadata and the final BibTeX record;
- no citation argument containing an inline comment that can hide citation keys;
- no stale 78-paper, 70%, 7/10, or old MAST-percentage claims;
- three to five Highlights, each no longer than 85 characters.

The machine-readable result is saved as
`audit_work/static_reference_checks.json`.

## Limitations

This audit verifies bibliographic existence, metadata, evidence roles, and the
fit between cited sources and the manuscript claims examined here. The update
search was targeted rather than database-exhaustive, screening and coding were
not independently duplicated by two reviewers, and the ten-case architecture
comparison remains author-coded. The manuscript now states these boundaries
instead of presenting the corpus or stress test as exhaustive external
validation.
