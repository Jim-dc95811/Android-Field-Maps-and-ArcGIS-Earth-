@echo off
cd /d "%~dp0"
python "URL_QR_MAKER.py"
if errorlevel 1 pause
