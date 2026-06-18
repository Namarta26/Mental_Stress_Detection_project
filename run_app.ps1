$ProjectRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$PythonPath = Join-Path $ProjectRoot "venv\Scripts\python.exe"

Set-Location $ProjectRoot

if (-not (Test-Path $PythonPath)) {
    Write-Error "Virtual environment not found. Expected: $PythonPath"
    exit 1
}

& $PythonPath app.py
