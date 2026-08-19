@echo off
setlocal
cd /d "%~dp0"
title ArcGIS Earth PRAVE Live - SELF TEST

where py >nul 2>nul
if %errorlevel%==0 (
    py "AE_PRAVE_LIVE_v0_1_0_TEST.py" --self-test
) else (
    python "AE_PRAVE_LIVE_v0_1_0_TEST.py" --self-test
)

echo.
pause
endlocal
