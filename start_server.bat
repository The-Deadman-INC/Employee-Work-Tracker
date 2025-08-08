@echo off
title CAD Work Tracker Server
echo =====================================
echo     CAD Work Tracker Server
echo =====================================
echo.
echo Starting the CAD Work Tracker application...
echo.
echo The application will be available at:
echo   Local:   http://localhost:5000
echo   Network: http://%COMPUTERNAME%:5000
echo.
echo Press Ctrl+C to stop the server
echo.

cd /d "%~dp0"
python app.py

pause
