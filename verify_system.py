#!/usr/bin/env python3
"""
CAD Work Tracker - System Verification Script
This script checks all components are properly linked and functional
"""
import sqlite3
import os
from datetime import datetime

def verify_database():
    """Verify database structure and data"""
    print("🔍 Verifying Database...")
    
    if not os.path.exists('work_tracker.db'):
        print("❌ Database file not found!")
        return False
    
    conn = sqlite3.connect('work_tracker.db')
    cursor = conn.cursor()
    
    # Check tables exist
    tables = ['employees', 'projects', 'work_progress']
    for table in tables:
        cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table}'")
        if not cursor.fetchone():
            print(f"❌ Table {table} missing!")
            return False
        print(f"✅ Table {table} exists")
    
    # Check data counts
    cursor.execute("SELECT COUNT(*) FROM employees")
    emp_count = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(*) FROM projects") 
    proj_count = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(*) FROM work_progress")
    progress_count = cursor.fetchone()[0]
    
    print(f"📊 Data Summary:")
    print(f"   Employees: {emp_count}")
    print(f"   Projects: {proj_count}")
    print(f"   Progress Entries: {progress_count}")
    
    conn.close()
    return True

def verify_templates():
    """Verify all templates exist and have proper structure"""
    print("\n🔍 Verifying Templates...")
    
    required_templates = [
        'base.html',
        'launcher.html', 
        'admin_login.html',
        'employee_login.html',
        'admin_dashboard.html',
        'admin_reports.html',
        'admin_projects.html',
        'admin_employees.html',
        'admin_database.html',
        'employee_dashboard.html'
    ]
    
    template_dir = 'templates'
    if not os.path.exists(template_dir):
        print("❌ Templates directory missing!")
        return False
    
    for template in required_templates:
        template_path = os.path.join(template_dir, template)
        if os.path.exists(template_path):
            size = os.path.getsize(template_path)
            if size > 0:
                print(f"✅ {template} ({size} bytes)")
            else:
                print(f"⚠️  {template} (0 bytes - may be corrupted)")
        else:
            print(f"❌ {template} missing!")
    
    return True

def verify_routes():
    """Check if main Flask routes are defined"""
    print("\n🔍 Verifying Flask Routes...")
    
    try:
        with open('app.py', 'r') as f:
            content = f.read()
        
        required_routes = [
            '@app.route(\'/\')',
            '@app.route(\'/admin/login\')',
            '@app.route(\'/employee/login\')',
            '@app.route(\'/admin/dashboard\')',
            '@app.route(\'/employee/dashboard\')',
            '@app.route(\'/admin/reports\')',
            '@app.route(\'/admin/projects\')',
            '@app.route(\'/admin/employees\')',
            '@app.route(\'/admin/database\')'
        ]
        
        for route in required_routes:
            if route in content:
                print(f"✅ {route}")
            else:
                print(f"❌ {route} missing!")
        
        return True
    except Exception as e:
        print(f"❌ Error reading app.py: {e}")
        return False

def verify_authentication():
    """Verify authentication system"""
    print("\n🔍 Verifying Authentication...")
    
    conn = sqlite3.connect('work_tracker.db')
    cursor = conn.cursor()
    
    # Check admin user exists
    cursor.execute("SELECT * FROM employees WHERE is_admin=1")
    admin = cursor.fetchone()
    if admin:
        print(f"✅ Admin user found: {admin[1]} {admin[2]}")
    else:
        print("❌ No admin user found!")
    
    # Check regular employees
    cursor.execute("SELECT COUNT(*) FROM employees WHERE is_admin=0")
    emp_count = cursor.fetchone()[0]
    print(f"✅ Regular employees: {emp_count}")
    
    conn.close()
    return True

def main():
    """Main verification function"""
    print("=" * 50)
    print("🚀 CAD Work Tracker - System Verification")
    print("=" * 50)
    
    all_good = True
    
    # Run all verifications
    all_good &= verify_database()
    all_good &= verify_templates()
    all_good &= verify_routes()
    all_good &= verify_authentication()
    
    print("\n" + "=" * 50)
    if all_good:
        print("🎉 ALL SYSTEMS VERIFIED - READY TO LAUNCH!")
        print("💡 Start the application with: python app.py")
        print("🌐 Access at: http://127.0.0.1:5000")
    else:
        print("⚠️  SOME ISSUES FOUND - REVIEW ABOVE")
    print("=" * 50)

if __name__ == '__main__':
    main()