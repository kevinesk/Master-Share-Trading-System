@echo off
:: ============================================================
::  Upgrade all Python dependencies (run monthly, NOT daily).
::  Daily runners deliberately do not auto-upgrade, so a breaking
::  yfinance release can never kill the screener mid-week.
::  If something breaks after upgrading, the date of this run is
::  your first suspect.
:: ============================================================
title Update Python dependencies

echo Upgrading yfinance pandas numpy curl_cffi anthropic beautifulsoup4 certifi...
py -m pip install --upgrade yfinance pandas numpy curl_cffi anthropic beautifulsoup4 certifi

echo.
echo Done. Run RUN_DAILY.bat once now to confirm everything still works.
pause >nul
