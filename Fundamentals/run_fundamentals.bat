@echo off
title KLSE Fundamental Data Fetcher
cd /d "%~dp0"
echo ============================================================
echo  KLSE Fundamental Data Fetcher
echo  Fetching financial metrics for all 100 universe stocks...
echo ============================================================
echo.
py fetch_fundamentals.py
echo.
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: Script failed. Check the output above.
    pause
    exit /b 1
)
echo Done. Opening report...
pause
