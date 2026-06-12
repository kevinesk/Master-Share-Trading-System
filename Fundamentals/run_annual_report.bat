@echo off
title KLSE Annual Report Analyzer
cd /d "%~dp0"
echo ============================================================
echo  KLSE Annual Report Analyzer
echo  Powered by Claude AI
echo ============================================================
echo.
echo  Usage examples:
echo    py annual_report.py 1023           (CIMB)
echo    py annual_report.py MAYBANK        (by name)
echo    py annual_report.py 1023 --year 2023
echo.
echo  NOTE: Requires ANTHROPIC_API_KEY to be set.
echo        Set it once with: setx ANTHROPIC_API_KEY "sk-ant-..."
echo.

if "%~1"=="" (
    set /p STOCK_CODE="Enter stock code or name: "
) else (
    set STOCK_CODE=%~1
)

py annual_report.py %STOCK_CODE% %2 %3
echo.
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: Script failed. Check the output above.
    pause
    exit /b 1
)
pause
