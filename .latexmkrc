# Project-only configuration: latexmk detects biblatex's .bcf and runs Biber.
$pdf_mode = 1;
$out_dir = 'build/latex';
$biber = 'biber %O %B';
$bibtex_use = 2;
