@echo off
title KLSE Daily Screener

echo Installing / updating dependencies...
py -m pip install --quiet --upgrade yfinance pandas numpy curl_cffi

echo.
echo Running KLSE Daily Screener...
echo This will take 1-3 minutes (parallel download of 60 stocks).
echo.
py "%~dp0klse_screener.py"

echo.
echo Done. Press any key to close.
pause >nul
