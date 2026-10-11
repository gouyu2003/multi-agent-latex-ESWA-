param([string]$OutputDirectory = 'tmp/apa7_build')
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
            try { & $bibEngine manuscript *> (Join-Path $buildDirectory 'manuscript.biber.console.txt') }
            finally { Pop-Location }
        } else {
            & $pdfEngine -interaction=nonstopmode -halt-on-error -file-line-error -recorder "-output-directory=$buildDirectory" manuscript.tex *> (Join-Path $buildDirectory "manuscript.$buildStage.console.txt")
        }
        if ($LASTEXITCODE -ne 0) { throw "Build failed at $buildStage; inspect $buildDirectory" }
        Write-Output "Completed $buildStage"
    }
    # Publish matching generated artifacts together; sources stay untouched.
    foreach ($buildExtension in @('pdf','bbl','aux','bcf','run.xml','out','log','blg','fls')) {
        $builtFile = Join-Path $buildDirectory "manuscript.$buildExtension"
        if (Test-Path -LiteralPath $builtFile) {
            Copy-Item -LiteralPath $builtFile -Destination (Join-Path $projectRoot "manuscript.$buildExtension")
        }
    }
} finally {
    Pop-Location
    $env:LC_ALL, $env:LC_CTYPE, $env:LANG = $oldLocale
    $env:TEXINPUTS, $env:BIBINPUTS = $oldInputs
}
