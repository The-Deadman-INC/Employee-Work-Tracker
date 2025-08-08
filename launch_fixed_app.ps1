#!/usr/bin/env powershell
<#
.SYNOPSIS
    Enhanced launcher for CAD Work Tracker with employee dashboard fix
.DESCRIPTION
    Stops any running Flask processes and starts the application fresh
#>

# Colors for output
$Green = "`e[32m"
$Red = "`e[31m"
$Yellow = "`e[33m"
$Blue = "`e[34m"
$Reset = "`e[0m"

Write-Host "${Blue}============================================================${Reset}"
Write-Host "${Blue}         CAD WORK TRACKER - EMPLOYEE FIX LAUNCHER${Reset}"
Write-Host "${Blue}============================================================${Reset}"

# Stop any existing Flask processes
Write-Host "${Yellow}Stopping any running Flask processes...${Reset}"
try {
    taskkill /f /im python.exe 2>$null
    Start-Sleep -Seconds 2
    Write-Host "${Green}✅ Processes stopped${Reset}"
} catch {
    Write-Host "${Yellow}No processes to stop${Reset}"
}

# Check if all files are in place
Write-Host "${Yellow}Checking application files...${Reset}"

$files = @(
    "app.py",
    "work_tracker.db",
    "templates/employee_dashboard.html",
    "templates/admin_reports.html"
)

$allFilesOk = $true
foreach ($file in $files) {
    if (Test-Path $file) {
        $size = (Get-Item $file).Length
        Write-Host "${Green}✅ $file (${size:N0} bytes)${Reset}"
    } else {
        Write-Host "${Red}❌ Missing: $file${Reset}"
        $allFilesOk = $false
    }
}

if (-not $allFilesOk) {
    Write-Host "${Red}Some files are missing! Please check the installation.${Reset}"
    exit 1
}

# Start Flask application
Write-Host "${Yellow}Starting Flask application...${Reset}"
Write-Host "${Blue}============================================================${Reset}"

try {
    python app.py
} catch {
    Write-Host "${Red}Error starting Flask: $_${Reset}"
    Write-Host "${Yellow}Make sure Python is installed and in PATH${Reset}"
}
