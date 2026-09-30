$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$ProjectRoot = Split-Path -Parent $ScriptDir
$env:PYTHONPATH = "$ProjectRoot;$env:PYTHONPATH"
python "$ProjectRoot\lumina\cli.py" @args
