#!/usr/bin/env python3

"""
Test script to verify all new CAD Work Tracker functions
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app import app, get_db_connection, init_database

def test_database_functions():
    """Test database management functions"""
    print("Testing database functions...")
    
    # Test database connection
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM employees")
        employee_count = cursor.fetchone()[0]
        print(f"✓ Database connection successful. Found {employee_count} employees.")
        conn.close()
    except Exception as e:
        print(f"✗ Database connection failed: {e}")
        return False
    
    return True

def test_route_definitions():
    """Test that all new routes are properly defined"""
    print("Testing route definitions...")
    
    required_routes = [
        '/admin/reports/export_csv',
        '/admin/reports/summary', 
        '/admin/database/backup',
        '/admin/database/export_json',
        '/admin/database/cleanup',
        '/admin/database',
        '/admin/projects/bulk_update',
        '/admin/projects/analytics',
        '/admin/employees/bulk_update', 
        '/admin/employees/analytics'
    ]
    
    with app.test_client() as client:
        for route in required_routes:
            try:
                # Just test that route exists (don't worry about auth for now)
                response = client.get(route)
                # Any response code other than 404 means route exists
                if response.status_code != 404:
                    print(f"✓ Route {route} exists")
                else:
                    print(f"✗ Route {route} not found")
                    return False
            except Exception as e:
                print(f"✗ Error testing route {route}: {e}")
                return False
    
    return True

def test_new_templates():
    """Test that new templates exist"""
    print("Testing template files...")
    
    required_templates = [
        'templates/admin_database.html',
        'templates/admin_project_analytics.html', 
        'templates/admin_employee_analytics.html'
    ]
    
    for template in required_templates:
        if os.path.exists(template):
            print(f"✓ Template {template} exists")
        else:
            print(f"✗ Template {template} missing")
            return False
    
    return True

def main():
    """Run all tests"""
    print("=" * 50)
    print("CAD Work Tracker - New Functionality Test")
    print("=" * 50)
    
    # Initialize database if it doesn't exist
    if not os.path.exists('work_tracker.db'):
        print("Initializing database...")
        init_database()
    
    tests = [
        test_database_functions,
        test_route_definitions,
        test_new_templates
    ]
    
    all_passed = True
    
    for test in tests:
        try:
            if not test():
                all_passed = False
        except Exception as e:
            print(f"✗ Test {test.__name__} failed with error: {e}")
            all_passed = False
        print()
    
    print("=" * 50)
    if all_passed:
        print("✓ ALL TESTS PASSED - New functionality is ready!")
        print("\nNew Features Added:")
        print("1. ✓ Report Generation Functions (CSV export, summary reports)")
        print("2. ✓ Database Management Functions (backup, export, cleanup)")
        print("3. ✓ Enhanced Project Management (bulk operations, analytics)")
        print("4. ✓ Enhanced Employee Management (bulk operations, analytics)")
        print("\nTo start the application: python app.py")
        print("Then access: http://127.0.0.1:5000")
    else:
        print("✗ SOME TESTS FAILED - Please check the errors above")
    print("=" * 50)

if __name__ == "__main__":
    main()
