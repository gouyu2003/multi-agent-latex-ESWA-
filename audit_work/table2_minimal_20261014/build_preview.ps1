param([string]$Stage = 'all')
$ErrorActionPreference = 'Stop'
$taskRoot = [IO.Path]::GetFullPath((Join-Path $PSScriptRoot '../..'))
$taskBuild = Join-Path $taskRoot 'tmp/table2_minimal_20261014_build'
New-Item -ItemType Directory -Path $taskBuild -Force | Out-Null
$savedLocale = @($env:LC_ALL, $env:LC_CTYPE, $env:LANG)
$savedInputs = @($env:TEXINPUTS, $env:BIBINPUTS)
try {
    $env:LC_ALL = 'C'; $env:LC_CTYPE = 'C'; $env:LANG = 'C'
    $env:TEXINPUTS = "$taskBuild;$taskRoot;"; $env:BIBINPUTS = "$taskBuild;$taskRoot;"
    Push-Location -LiteralPath $taskRoot
    $taskStages = if ($Stage -eq 'all') { @('pass1','biber','pass2','pass3') } else { @($Stage) }
    foreach ($taskPass in $taskStages) {
        if ($taskPass -eq 'biber') {
            Push-Location -LiteralPath $taskBuild
            try { & biber manuscript *> (Join-Path $taskBuild 'manuscript.biber.console.txt') }
            finally { Pop-Location }
        } else {
            & pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -recorder "-output-directory=$taskBuild" manuscript.tex *> (Join-Path $taskBuild "manuscript.$taskPass.console.txt")
        }
        if ($LASTEXITCODE -ne 0) { throw "Build failed at $taskPass; inspect $taskBuild" }
        Write-Output "Completed $taskPass"
    }
} finally {
    Pop-Location
    $env:LC_ALL, $env:LC_CTYPE, $env:LANG = $savedLocale
    $env:TEXINPUTS, $env:BIBINPUTS = $savedInputs
}
