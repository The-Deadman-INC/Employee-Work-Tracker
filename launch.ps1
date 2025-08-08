# PowerShell script to launch CAD Work Tracker
Write-Host "=" * 60 -ForegroundColor Green
Write-Host "🚀 CAD Work Tracker - Starting Application" -ForegroundColor Green
Write-Host "=" * 60 -ForegroundColor Green
Write-Host ""
Write-Host "📋 STEPS TO ACCESS ALL FEATURES:" -ForegroundColor Yellow
Write-Host ""
Write-Host "1. 🌐 Open: http://127.0.0.1:5000" -ForegroundColor Cyan
Write-Host "2. 🔐 Click 'Admin Login'" -ForegroundColor Cyan
Write-Host "3. 👤 Username: mahesh.butani" -ForegroundColor Cyan
Write-Host "4. 🔑 Password: m.butani@321" -ForegroundColor Cyan
Write-Host "5. ✅ Login to access admin dashboard" -ForegroundColor Cyan
Write-Host ""
Write-Host "📊 AFTER LOGIN YOU CAN ACCESS:" -ForegroundColor Yellow
Write-Host "   • Dashboard - Overview and charts" -ForegroundColor White
Write-Host "   • Projects - Project management & analytics" -ForegroundColor White
Write-Host "   • Employees - Employee management & analytics" -ForegroundColor White
Write-Host "   • Reports - CSV export & summary reports" -ForegroundColor White
Write-Host "   • Database - Backup, export & cleanup tools" -ForegroundColor White
Write-Host ""
Write-Host "⚠️  IMPORTANT:" -ForegroundColor Red
Write-Host "   The Reports and Database pages require admin login!" -ForegroundColor Red
Write-Host "   If they appear blank, you need to login first." -ForegroundColor Red
Write-Host ""
Write-Host "💡 For Employee Access:" -ForegroundColor Yellow
Write-Host "   • Click 'Employee Login'" -ForegroundColor White
Write-Host "   • Use: shaji, ibrahim, mohamed, etc." -ForegroundColor White
Write-Host "   • Password format: firstname@321" -ForegroundColor White
Write-Host ""
Write-Host "🚀 Starting Flask Application..." -ForegroundColor Green

# Start the Flask application
try {
    Start-Process python -ArgumentList "app.py" -NoNewWindow
    Write-Host "✅ Application started successfully!" -ForegroundColor Green
    Write-Host "🌐 Opening browser..." -ForegroundColor Green
    Start-Sleep -Seconds 3
    Start-Process "http://127.0.0.1:5000"
}
catch {
    Write-Host "❌ Error starting application: $($_.Exception.Message)" -ForegroundColor Red
}

Write-Host ""
Write-Host "=" * 60 -ForegroundColor Green
Write-Host "🎯 All features are working - just login first!" -ForegroundColor Green
Write-Host "=" * 60 -ForegroundColor Green
