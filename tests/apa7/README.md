# Final project APA regression tests

Run from the repository root:

```powershell
python -B tools/run_apa_tests.py
```

Requirements: the validated TeX Live 2026 installation at
`D:\texlive\2026\bin\windows`, Biber 2.22, biblatex 3.22a,
biblatex-apa 9.20 and Python with PyMuPDF. No install or global configuration
changes are performed. Biber must run outside the restricted Codex Windows
sandbox, where its packaged DLL has a known relocation failure.

The runner copies fixtures to ignored `tmp/apa7_regression/`, executes
pdfLaTeX → Biber → pdfLaTeX → pdfLaTeX, and validates 14 core rules and
15 extended cases using the current `eswa-apa-config.tex` and sourcemap.
Core boundary fixtures include synthetic records (including the fake
`10.1000/test` DOI); these do not enter the manuscript bibliography.
The real type fixture contains 13 exact original records, adapted by the
same project map. `pool78` and `commands78` use the original full database,
and `pool85` separately previews all 85 keys without citing unused works in
the manuscript. Fixture copies do not change the 85-record production pool.

`validate.py` records expected output, actual PDF text, PDF font spans and
hyperlink targets. Output tables alone do not certify publication metadata;
the 78-entry and conference evidence ledgers in `apa7_audit/` remain separate.
