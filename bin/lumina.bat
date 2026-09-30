@echo off
set PATH=C:\Program Files\nodejs;%PATH%
set PYTHONPATH=%~dp0..;%PYTHONPATH%
python "%~dp0..\lumina\cli.py" %*
