# Multi-agent collaborative QA — ESWA manuscript

This repository manages the LaTeX manuscript in
`D:\multi-agent review_joural\ESWA_Submission_caomodify`.
The initial commit preserves the manuscript sources and supporting materials
before subsequent revisions.

## Files

- `manuscript.tex`: main manuscript entry point.
- `references.bib`: bibliography source.
- `ch*_en.tex`: chapter files retained from the existing folder.
- `cas-dc.cls`, `cas-common.sty`, `cas-model2-names.bst`: local LaTeX template files.
- Figure files (`.jpg`, `.png`, `.svg`, and figure `.pdf` files): manuscript assets
  and retained figure variants.
- Root CSV files, `Highlights.txt`, `reference_audit_report.md`, and `audit_work/`:
  supporting data and existing audit records.
- `tools/`: reference-audit and figure-generation Python scripts.

Historical figure variants and chapter files are retained. Inclusion in Git does
not imply that every retained file is referenced by the current manuscript.

## Build

With a working local LaTeX installation, compile from the repository root:

```text
pdflatex manuscript.tex
bibtex manuscript
pdflatex manuscript.tex
pdflatex manuscript.tex
```

The repository setup does not compile or validate the manuscript. Generated
`manuscript.pdf`, `manuscript.bbl`, LaTeX auxiliary files, `tmp/` previews, and
Python bytecode are ignored. They remain available locally; submission packages
can include generated outputs separately. Figure PDFs are tracked.

## Revision workflow

1. Make one coherent manuscript revision.
2. Review `git status --short` and `git diff`.
3. Stage only the intended files with `git add -- <file paths>`.
4. Review `git diff --cached` before committing.
5. Commit with a message describing the revision, then push to GitHub.

Saving a file, committing a version, and pushing that version are separate steps.
