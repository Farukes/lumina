# Lumina Windows PowerShell One-Liner Installer
# Usage:
#   irm https://raw.githubusercontent.com/Farukes/lumina/main/install.ps1 | iex

Write-Host "⚡ LUMINA WINDOWS INSTALLER // WORLD-CLASS FRONTEND ENGINE" -ForegroundColor Cyan
Write-Host "==========================================================" -ForegroundColor DarkGray

$PythonCmd = Get-Command python -ErrorAction SilentlyContinue
if (-not $PythonCmd) {
    Write-Host "Error: Python 3 is required. Please install Python from https://python.org" -ForegroundColor Red
    exit 1
}

$InstallScriptUrl = "https://raw.githubusercontent.com/Farukes/lumina/main/install.py"
$TempScript = [System.IO.Path]::GetTempFileName() + ".py"

try {
    Write-Host "Fetching Lumina installer..." -ForegroundColor Gray
    Invoke-WebRequest -Uri $InstallScriptUrl -OutFile $TempScript -UseBasicParsing
    python $TempScript
} catch {
    Write-Host "Local installation fallback..." -ForegroundColor Yellow
    if (Test-Path "install.py") {
        python install.py
    } else {
        Write-Host "Error downloading installer: $_" -ForegroundColor Red
    }
} finally {
    if (Test-Path $TempScript) {
        Remove-Item -Force $TempScript -ErrorAction SilentlyContinue
    }
}
