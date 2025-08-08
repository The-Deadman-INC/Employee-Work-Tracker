@echo off
echo ========================================
echo  CAD Work Tracker - Enhanced Version
echo ========================================
echo.

echo Checking Python...
python --version
if %errorlevel% neq 0 (
    echo ERROR: Python not found!
    pause
    exit /b 1
)

echo.
echo Checking application files...
if not exist "app.py" (
    echo ERROR: app.py not found!
    pause
    exit /b 1
)

if not exist "templates\admin_reports.html" (
    echo ERROR: admin_reports.html template missing!
    pause
    exit /b 1
)

echo.
echo Starting Enhanced CAD Work Tracker...
echo Features available:
echo - Enhanced Reports Page
echo - Comprehensive Database Management
echo - Clear Progress Data
echo - Wipe Database
echo - Backup and Restore
echo - Integrity Check
echo.
echo Admin Login: mahesh.butani / m.butani@321
echo.
echo Opening browser in 3 seconds...
timeout /t 3 /nobreak > nul
start "" "http://127.0.0.1:5000"

echo.
echo Starting Flask server...
python app.py

pause
