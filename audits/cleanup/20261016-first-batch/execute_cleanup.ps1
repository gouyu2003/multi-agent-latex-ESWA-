param([switch]$Apply)
$ErrorActionPreference = 'Stop'
$workspaceRoot = [IO.Path]::GetFullPath((Join-Path $PSScriptRoot '..\..\..'))
$rootPrefix = $workspaceRoot + [IO.Path]::DirectorySeparatorChar
$batchRelative = 'audits/cleanup/20261016-first-batch'
$manifestPath = Join-Path $PSScriptRoot 'cleanup_manifest.json'
$validatedParents = New-Object 'System.Collections.Generic.HashSet[string]' ([StringComparer]::OrdinalIgnoreCase)

function Get-SafePath([string]$Relative) {
    $absolute = [IO.Path]::GetFullPath((Join-Path $workspaceRoot $Relative))
    if (-not $absolute.StartsWith($rootPrefix, [StringComparison]::OrdinalIgnoreCase)) { throw "Outside workspace: $Relative" }
    $gitRoot = Join-Path $workspaceRoot '.git'
    if ($absolute.Equals($gitRoot, [StringComparison]::OrdinalIgnoreCase) -or $absolute.StartsWith($gitRoot + '\', [StringComparison]::OrdinalIgnoreCase)) { throw 'Git metadata is excluded' }
    $ancestor = $absolute
    while ($ancestor -and -not $ancestor.Equals($workspaceRoot, [StringComparison]::OrdinalIgnoreCase)) {
        if ($validatedParents.Add($ancestor) -and (Test-Path -LiteralPath $ancestor)) {
            $item = Get-Item -LiteralPath $ancestor -Force
            if (($item.Attributes -band [IO.FileAttributes]::ReparsePoint) -ne 0) { throw "Reparse point excluded: $ancestor" }
            $resolved = (Resolve-Path -LiteralPath $ancestor).ProviderPath
            if (-not $resolved.StartsWith($rootPrefix, [StringComparison]::OrdinalIgnoreCase)) { throw "Resolved path escaped workspace: $ancestor" }
        }
        $ancestor = [IO.Path]::GetDirectoryName($ancestor)
    }
    return $absolute
}

function Relative-Name([string]$Absolute) { return $Absolute.Substring($workspaceRoot.Length + 1).Replace('\', '/') }
function File-Record([IO.FileInfo]$File, [string]$Category) {
    return [pscustomobject]@{ path=(Relative-Name $File.FullName); bytes=$File.Length; sha256=(Get-FileHash -LiteralPath $File.FullName -Algorithm SHA256).Hash.ToLowerInvariant(); category=$Category }
}
function Write-Json([string]$Path, $Value) {
    [IO.File]::WriteAllText($Path, (($Value | ConvertTo-Json -Depth 8) + "`n"), (New-Object Text.UTF8Encoding($false)))
}

if (Test-Path -LiteralPath $manifestPath) { throw 'A cleanup record already exists; do not rerun this batch.' }
$retainedImage = Get-SafePath 'archive/figures/fig_architecture_tradeoffs.jpg'
$duplicateImage = Get-SafePath 'archive/figures/Design logic and trade-offs among flat, hierarchical, and hybrid architectures for multi-agent collaborative QA.jpg'
if ((Get-FileHash -LiteralPath $retainedImage -Algorithm SHA256).Hash -ne (Get-FileHash -LiteralPath $duplicateImage -Algorithm SHA256).Hash) { throw 'Images are not identical' }
if (-not (Test-Path -LiteralPath (Get-SafePath 'build/manuscript.pdf'))) { throw 'The retained manuscript PDF is missing' }
if (-not (Test-Path -LiteralPath (Get-SafePath 'tests/apa7'))) { throw 'Original APA fixtures are missing' }
if (Test-Path -LiteralPath (Join-Path $workspaceRoot 'manuscript.synctex(busy)')) { throw 'An editor compilation is active; wait for it to finish.' }

$directories = @()
foreach ($cacheRoot in @('tools', '.cache/python')) {
    $directories += @(Get-ChildItem -LiteralPath (Get-SafePath $cacheRoot) -Directory -Filter '__pycache__' -Recurse -Force | ForEach-Object {
        [pscustomobject]@{ relative=(Relative-Name $_.FullName); category='python_bytecode' }
    })
}
$directories += [pscustomobject]@{ relative='build/apa7_regression'; category='generated_apa_tests' }
$individualFiles = @(
    [pscustomobject]@{ relative='.cache/python/figure1/wheels/matplotlib.json'; category='incomplete_download_metadata' },
    [pscustomobject]@{ relative='.cache/python/figure1/mplconfig/fontlist-v3.11.0.json'; category='font_cache' },
    [pscustomobject]@{ relative=(Relative-Name $duplicateImage); category='identical_duplicate_image' }
)
foreach ($extension in @('abs','aux','bbl','bcf','blg','log','out','pdf','run.xml','synctex.gz')) {
    $individualFiles += [pscustomobject]@{ relative=('manuscript.' + $extension); category='root_generated_artifact' }
}
$rows = @()
foreach ($directory in $directories) {
    $target = Get-SafePath $directory.relative
    if (Test-Path -LiteralPath $target) {
        $rows += @(Get-ChildItem -LiteralPath $target -File -Recurse -Force | ForEach-Object { File-Record $_ $directory.category })
    }
}
foreach ($file in $individualFiles) {
    $target = Get-SafePath $file.relative
    if (Test-Path -LiteralPath $target) { $rows += File-Record (Get-Item -LiteralPath $target) $file.category }
}
if (($rows.path | Sort-Object -Unique).Count -ne $rows.Count) { throw 'Overlapping deletion candidates' }

# The user's second batch is explicitly protected, including all its file bytes.
$protectedRoots = @('build/history','build/editor_generated_20261016','.cache/previews/conference9_rendered','archive/chapters','archive/templates')
$protected = @()
foreach ($relative in $protectedRoots) {
    $target = Get-SafePath $relative
    if (Test-Path -LiteralPath $target) {
        $protected += @(Get-ChildItem -LiteralPath $target -File -Recurse -Force | ForEach-Object { File-Record $_ 'second_batch_preserved' })
    }
}
$protected += File-Record (Get-Item -LiteralPath $retainedImage) 'retained_duplicate_copy'
foreach ($row in $rows) {
    foreach ($relative in $protectedRoots) {
        if ($row.path -eq $relative -or $row.path.StartsWith($relative + '/', [StringComparison]::OrdinalIgnoreCase)) { throw "Protected item selected: $($row.path)" }
    }
}
$totalBytes = ($rows | Measure-Object bytes -Sum).Sum
$rows | Group-Object category | ForEach-Object { [pscustomobject]@{ category=$_.Name; files=$_.Count; MiB=[math]::Round(($_.Group | Measure-Object bytes -Sum).Sum / 1MB, 3) } } | Format-Table -AutoSize
Write-Output "Selected $($rows.Count) files, $([math]::Round($totalBytes / 1MB, 2)) MiB; protected $($protected.Count) files."
if (-not $Apply) { return }

$manifest = [ordered]@{
    schema_version=1; status='planned'; created_utc=[DateTime]::UtcNow.ToString('o');
    authorization='User explicitly requested the long-name duplicate JPG and the first batch only; keep the second batch.';
    files=$rows; total_files=$rows.Count; total_bytes=$totalBytes; protected_files=$protected.Count
}
Write-Json $manifestPath $manifest
Write-Json (Join-Path $PSScriptRoot 'protected_files_before.json') $protected

# Native PowerShell deletion only; all recursive targets were resolved and checked above.
foreach ($directory in ($directories | Sort-Object { $_.relative.Length } -Descending)) {
    $target = Get-SafePath $directory.relative
    if (Test-Path -LiteralPath $target) { Remove-Item -LiteralPath $target -Recurse -Force }
}
foreach ($file in $individualFiles) {
    $target = Get-SafePath $file.relative
    if (Test-Path -LiteralPath $target) { Remove-Item -LiteralPath $target -Force }
}
foreach ($row in $rows) {
    if (Test-Path -LiteralPath (Get-SafePath $row.path)) { throw "Cleanup incomplete: $($row.path)" }
}
foreach ($row in $protected) {
    $target = Get-SafePath $row.path
    if (-not (Test-Path -LiteralPath $target) -or (Get-FileHash -LiteralPath $target -Algorithm SHA256).Hash.ToLowerInvariant() -ne $row.sha256) { throw "Protected file changed: $($row.path)" }
}
$manifest.status = 'complete'
$manifest.completed_utc = [DateTime]::UtcNow.ToString('o')
$manifest.protected_files_sha256_unchanged = $true
Write-Json $manifestPath $manifest
$registryPath = Join-Path $workspaceRoot 'audits/cleanup/approved_deletions.json'
$batches = @()
if (Test-Path -LiteralPath $registryPath) { $batches += @((Get-Content -LiteralPath $registryPath -Raw | ConvertFrom-Json).batches) }
$batches += ($batchRelative + '/cleanup_manifest.json')
Write-Json $registryPath ([ordered]@{ schema_version=1; batches=$batches })
Write-Output 'Cleanup complete; every protected file retained with the same SHA-256.'
