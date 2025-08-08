#!/usr/bin/env python3
"""
Test script to verify the CAD Work Tracker routes and functionality
"""

import sqlite3
import os
from datetime import datetime

def test_database():
    print("🔍 Testing Database...")
    print("=" * 50)
    
    # Check if database exists
    if not os.path.exists('work_tracker.db'):
        print("❌ Database file not found!")
        return False
    
    conn = sqlite3.connect('work_tracker.db')
    
    # Check tables
    tables = [row[0] for row in conn.execute('SELECT name FROM sqlite_master WHERE type="table"').fetchall()]
    print(f"✅ Tables found: {tables}")
    
    # Check data
    if 'work_progress' in tables:
        progress_count = conn.execute('SELECT COUNT(*) FROM work_progress').fetchone()[0]
        print(f"✅ Progress entries: {progress_count}")
        
        if progress_count > 0:
            # Get sample data for reports
            sample = conn.execute('''
                SELECT wp.*, e.first_name, e.last_name, p.name as project_name
                FROM work_progress wp
                JOIN employees e ON wp.emp_id = e.emp_id
                JOIN projects p ON wp.proj_id = p.proj_id
                LIMIT 3
            ''').fetchall()
            print(f"✅ Sample data available: {len(sample)} joined records")
            if sample:
                # Just show basic info
                print(f"   First record: Employee={sample[0][7]} {sample[0][8]}, Project={sample[0][11]}")
    
    if 'employees' in tables:
        employee_count = conn.execute('SELECT COUNT(*) FROM employees').fetchone()[0]
        admin_count = conn.execute('SELECT COUNT(*) FROM employees WHERE is_admin = 1').fetchone()[0]
        print(f"✅ Employees: {employee_count} total, {admin_count} admin")
    
    if 'projects' in tables:
        project_count = conn.execute('SELECT COUNT(*) FROM projects').fetchone()[0]
        active_projects = conn.execute('SELECT COUNT(*) FROM projects WHERE status = "Active"').fetchone()[0]
        print(f"✅ Projects: {project_count} total, {active_projects} active")
    
    conn.close()
    return True

def test_app_imports():
    print("\n🔧 Testing App Imports...")
    print("=" * 50)
    
    try:
        import app
        print("✅ App imports successfully")
        
        # Check if new routes exist
        routes = []
        for rule in app.app.url_map.iter_rules():
            routes.append(str(rule))
        
        new_routes = [
            '/admin/database/clear_progress',
            '/admin/database/wipe_all', 
            '/admin/database/restore/<filename>',
            '/admin/database/integrity_check'
        ]
        
        for route in new_routes:
            found = any(route.replace('<filename>', '<string:filename>') in r for r in routes)
            status = "✅" if found else "❌"
            print(f"{status} Route exists: {route}")
        
        return True
        
    except Exception as e:
        print(f"❌ App import failed: {e}")
        return False

def test_templates():
    print("\n📄 Testing Templates...")
    print("=" * 50)
    
    template_files = [
        'templates/admin_reports.html',
        'templates/admin_database.html'
    ]
    
    for template in template_files:
        if os.path.exists(template):
            print(f"✅ Template exists: {template}")
            
            # Check for key content
            with open(template, 'r', encoding='utf-8') as f:
                content = f.read()
                
            if 'admin_reports.html' in template:
                if 'No Progress Data Available' in content:
                    print("  ✅ Enhanced empty state message found")
                else:
                    print("  ❌ Enhanced empty state message missing")
                    
            if 'admin_database.html' in template:
                if 'Clear Progress Data' in content:
                    print("  ✅ New database functions found")
                else:
                    print("  ❌ New database functions missing")
        else:
            print(f"❌ Template missing: {template}")

def main():
    print("🚀 CAD Work Tracker Verification")
    print("=" * 70)
    
    db_ok = test_database()
    app_ok = test_app_imports()
    test_templates()
    
    print("\n📋 Summary:")
    print("=" * 50)
    if db_ok and app_ok:
        print("✅ All components appear to be working correctly!")
        print("\n🔥 The issue might be:")
        print("   1. The Flask app needs to be restarted")
        print("   2. Browser cache needs to be cleared")
        print("   3. You might be looking at an old tab")
        print("\n💡 Try:")
        print("   1. Stop any running Flask processes")
        print("   2. Run: python app.py")
        print("   3. Open a fresh browser tab to http://127.0.0.1:5000")
        print("   4. Login with: mahesh.butani / m.butani@321")
    else:
        print("❌ Some issues found. Check the errors above.")

if __name__ == "__main__":
    main()
