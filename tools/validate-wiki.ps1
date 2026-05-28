#!/usr/bin/env pwsh
# validate-wiki.ps1 — Run wiki maintenance checks; exit 1 on errors.
# Usage: pwsh tools/validate-wiki.ps1 [-PendingDir PATH]

param(
    [string]$PendingDir = ""
)

$ErrorActionPreference = "Stop"
$repoRoot = Split-Path -Parent $PSScriptRoot
Set-Location $repoRoot

# Build scan args
$scanArgs = @("tools/wiki_maintain.py", "scan")
if ($PendingDir -ne "") {
    $scanArgs += @("--pending-dir", $PendingDir)
}

# Run scan — capture output and display it
$output = python @scanArgs 2>&1
$scanExitCode = $LASTEXITCODE
$output | Write-Host

# Parse totals line: "totals: errors=N warnings=M info=P"
$totalsLine = $output | Where-Object { $_ -match "^totals:" } | Select-Object -First 1
$errorCount = 0
if ($totalsLine -match "errors=(\d+)") {
    $errorCount = [int]$matches[1]
}

# Fail if scan process crashed (non-zero exit, no errors parsed)
if ($errorCount -eq 0 -and $scanExitCode -ne 0) {
    Write-Host ""
    Write-Host "=== validate-wiki summary ==="
    Write-Host ""
    Write-Host "FAIL: wiki_maintain.py exited with code $scanExitCode (scan did not complete)." -ForegroundColor Red
    exit 1
}

# Fail if totals line was not found at all
if ($null -eq $totalsLine -or $totalsLine -eq "") {
    Write-Host ""
    Write-Host "=== validate-wiki summary ==="
    Write-Host ""
    Write-Host "FAIL: 'totals:' line not found in scan output." -ForegroundColor Red
    exit 1
}

Write-Host ""
Write-Host "=== validate-wiki summary ==="
Write-Host "total errors: $errorCount"

if ($errorCount -gt 0) {
    Write-Host ""
    Write-Host "FAIL: $errorCount error(s) found." -ForegroundColor Red
    exit 1
} else {
    Write-Host ""
    Write-Host "PASS: No errors." -ForegroundColor Green
    exit 0
}
