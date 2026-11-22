@echo off
title Wedding Invitation - Vinay ^& Isha
echo ========================================================
echo   Launching Cloned Wedding Invitation (Watermark Removed)
echo   Couple: Vinay ^& Isha
echo   Date: 16 February 2027
echo ========================================================
echo.
echo Starting local server at http://localhost:8080 ...
start http://localhost:8080/
python "%~dp0server.py" 8080
pause
