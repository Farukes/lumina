@echo off
set PYTHONPATH=%~dp0..;%PYTHONPATH%
python "%~dp0..\lumina\cli.py" %*
