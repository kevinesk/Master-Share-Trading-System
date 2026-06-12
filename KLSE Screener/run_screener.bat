@echo off
title KLSE Daily Screener

echo Checking dependencies (no auto-upgrade — run update_deps.bat to upgrade)...
py -m pip install --quiet yfinance pandas numpy curl_cffi

echo.
echo Running KLSE Daily Screener...
echo This will take 1-3 minutes (parallel download of 100 stocks).
echo.
py "%~dp0klse_screener.py"

echo.
echo Done. Press any key to close.
pause >nul
