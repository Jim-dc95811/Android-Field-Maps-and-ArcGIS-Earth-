@echo off
setlocal
cd /d "%~dp0"
title ArcGIS Earth PRAVE Live - v0.1.0 TEST

where py >nul 2>nul
if %errorlevel%==0 (
    py "AE_PRAVE_LIVE_v0_1_0_TEST.py"
) else (
    python "AE_PRAVE_LIVE_v0_1_0_TEST.py"
)

set EXITCODE=%errorlevel%
echo.
echo ArcGIS Earth PRAVE Live exited with code %EXITCODE%.
pause
exit /b %EXITCODE%
