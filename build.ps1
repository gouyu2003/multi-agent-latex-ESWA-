param([string]$OutputDirectory = 'build/latex')
$ErrorActionPreference = 'Stop'
$projectRoot = $PSScriptRoot
$buildDirectory = [IO.Path]::GetFullPath((Join-Path $projectRoot $OutputDirectory))
if (-not $buildDirectory.StartsWith($projectRoot + [IO.Path]::DirectorySeparatorChar, [StringComparison]::OrdinalIgnoreCase)) {
    throw 'Build output must remain inside this project.'
}
New-Item -ItemType Directory -Path $buildDirectory -Force | Out-Null
$pdfEngine = (Get-Command pdflatex -ErrorAction Stop).Source
$bibEngine = (Get-Command biber -ErrorAction Stop).Source
$oldLocale = @($env:LC_ALL, $env:LC_CTYPE, $env:LANG)
$oldInputs = @($env:TEXINPUTS, $env:BIBINPUTS)
try {
    $env:LC_ALL = 'C'; $env:LC_CTYPE = 'C'; $env:LANG = 'C'
    $env:TEXINPUTS = "$buildDirectory;$projectRoot;"; $env:BIBINPUTS = "$buildDirectory;$projectRoot;"
    Push-Location -LiteralPath $projectRoot
    foreach ($buildStage in @('pass1','biber','pass2','pass3')) {
        if ($buildStage -eq 'biber') {
            Push-Location -LiteralPath $buildDirectory
            try { & $bibEngine manuscript 2>&1 | Out-File -LiteralPath (Join-Path $buildDirectory 'manuscript.biber.console.txt') -Encoding utf8 }
            finally { Pop-Location }
        } else {
            & $pdfEngine -synctex=1 -interaction=nonstopmode -halt-on-error -file-line-error -recorder "-output-directory=$buildDirectory" manuscript.tex *> (Join-Path $buildDirectory "manuscript.$buildStage.console.txt")
        }
        if ($LASTEXITCODE -ne 0) { throw "Build failed at $buildStage; inspect $buildDirectory" }
        Write-Output "Completed $buildStage"
    }
    # Keep auxiliary files in the build directory; publish only the final PDF.
    $publishedDirectory = Join-Path $projectRoot 'build'
    New-Item -ItemType Directory -Path $publishedDirectory -Force | Out-Null
    Copy-Item -LiteralPath (Join-Path $buildDirectory 'manuscript.pdf') -Destination (Join-Path $publishedDirectory 'manuscript.pdf')
} finally {
    Pop-Location
    $env:LC_ALL, $env:LC_CTYPE, $env:LANG = $oldLocale
    $env:TEXINPUTS, $env:BIBINPUTS = $oldInputs
}
