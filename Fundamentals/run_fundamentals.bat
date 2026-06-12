@echo off
title KLSE Fundamental Data Fetcher (v2 — quality models)
cd /d "%~dp0"
echo ============================================================
echo  KLSE Fundamental Data Fetcher v2
echo  Fetching financial metrics + quality scores (KC Chong /
echo  Cold Eye / MONEY / Tong tier) for all 100 universe stocks
echo ============================================================
echo.
py fetch_fundamentals_v2.py
echo.
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: Script failed. Check the output above.
    pause
    exit /b 1
)
echo Done. Opening report...
pause
