# Enhanced CAD Work Tracker Launcher
Write-Host "========================================" -ForegroundColor Cyan
Write-Host " CAD Work Tracker - Enhanced Version" -ForegroundColor Yellow
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Check Python
Write-Host "Checking Python..." -ForegroundColor Green
try {
    $pythonVersion = python --version 2>&1
    Write-Host "✅ $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "❌ Python not found!" -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}

# Check files
Write-Host ""
Write-Host "Checking application files..." -ForegroundColor Green

$files = @(
    @("app.py", "Main application"),
    @("work_tracker.db", "Database"),
    @("templates\admin_reports.html", "Reports template"),
    @("templates\admin_database.html", "Database template")
)

foreach ($file in $files) {
    if (Test-Path $file[0]) {
        $size = (Get-Item $file[0]).Length
        Write-Host "✅ $($file[1]): $($file[0]) ($size bytes)" -ForegroundColor Green
    } else {
        Write-Host "❌ $($file[1]): $($file[0]) - NOT FOUND" -ForegroundColor Red
    }
}

Write-Host ""
Write-Host "🆕 NEW FEATURES AVAILABLE:" -ForegroundColor Yellow
Write-Host "  • Enhanced Reports Page with data visualization" -ForegroundColor White
Write-Host "  • Comprehensive Database Management" -ForegroundColor White
Write-Host "  • Clear Progress Data functionality" -ForegroundColor White
Write-Host "  • Complete Database Wipe option" -ForegroundColor White
Write-Host "  • Backup and Restore capabilities" -ForegroundColor White
Write-Host "  • Database Integrity Check" -ForegroundColor White
Write-Host "  • Sample Data Reset" -ForegroundColor White

Write-Host ""
Write-Host "🔐 Admin Login Credentials:" -ForegroundColor Cyan
Write-Host "   Username: mahesh.butani" -ForegroundColor White
Write-Host "   Password: m.butani@321" -ForegroundColor White

Write-Host ""
Write-Host "🚀 Starting Enhanced Flask Application..." -ForegroundColor Green

# Start Flask app in background
Start-Process python -ArgumentList "app.py" -NoNewWindow

# Wait for server to start
Write-Host "Waiting for server to start..." -ForegroundColor Yellow
Start-Sleep -Seconds 3

# Open browser
Write-Host "🌐 Opening browser..." -ForegroundColor Green
Start-Process "http://127.0.0.1:5000"

Write-Host ""
Write-Host "✅ Application should now be running!" -ForegroundColor Green
Write-Host "📋 To test the new features:" -ForegroundColor Yellow
Write-Host "   1. Login with admin credentials above" -ForegroundColor White
Write-Host "   2. Check 'Reports' page - should show data or helpful empty state" -ForegroundColor White
Write-Host "   3. Check 'Database' page - should show new management functions" -ForegroundColor White
Write-Host ""
Write-Host "⚠️  If you still see old content:" -ForegroundColor Red
Write-Host "   1. Hard refresh browser (Ctrl+F5)" -ForegroundColor White
Write-Host "   2. Clear browser cache" -ForegroundColor White
Write-Host "   3. Try incognito/private browsing mode" -ForegroundColor White

Read-Host "Press Enter to exit"
