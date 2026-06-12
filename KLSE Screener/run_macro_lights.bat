@echo off
title KLSE 7-Light Macro Regime Board

echo Checking dependencies...
py -m pip install --quiet yfinance pandas curl_cffi

echo.
echo Running the 7-light macro regime board (Sunday weekly routine)...
echo Takes 1-2 minutes (downloads KLCI, S+P, USD/MYR + 100-stock universe).
echo.
py "%~dp0macro_lights.py"

echo.
echo Done. Press any key to close.
pause >nul
