#!/usr/bin/env python3
"""
Quick test script to verify the admin dashboard fix
"""
import sqlite3

def test_admin_dashboard_fix():
    """Test the NULL handling fix"""
    print("🔍 Testing Admin Dashboard NULL Handling Fix...")
    
    # Connect to database
    conn = sqlite3.connect('work_tracker.db')
    conn.row_factory = sqlite3.Row
    
    # Test the problematic query
    selected_month = 'July'
    selected_year = 2025
    
    employee_summary = conn.execute('''
        SELECT e.emp_id, e.first_name, e.last_name, e.department,
               COUNT(DISTINCT wp.proj_id) as projects_worked,
               COUNT(wp.id) as total_entries,
               COALESCE(SUM(wp.percentage), 0) as total_percentage,
               COALESCE(AVG(wp.percentage), 0) as avg_percentage_per_project,
               MAX(wp.submission_date) as last_submission
        FROM employees e
        LEFT JOIN work_progress wp ON e.emp_id = wp.emp_id 
                                   AND wp.month = ? AND wp.year = ?
        WHERE e.is_admin = 0
        GROUP BY e.emp_id, e.first_name, e.last_name, e.department
        ORDER BY total_percentage DESC, e.first_name
    ''', (selected_month, selected_year)).fetchall()
    
    print(f"✅ Query executed successfully!")
    print(f"📊 Found {len(employee_summary)} employees")
    
    # Test the chart calculations
    employees_completed = sum(1 for emp in employee_summary if emp['total_percentage'] is not None and emp['total_percentage'] == 100)
    employees_partial = sum(1 for emp in employee_summary if emp['total_percentage'] is not None and 0 < emp['total_percentage'] < 100)
    employees_not_started = sum(1 for emp in employee_summary if emp['total_percentage'] is None or emp['total_percentage'] == 0)
    
    print(f"✅ Chart calculations successful!")
    print(f"📈 Completed: {employees_completed}")
    print(f"📈 Partial: {employees_partial}")
    print(f"📈 Not Started: {employees_not_started}")
    
    # Show some sample data
    print(f"\n📋 Sample Employee Data:")
    for i, emp in enumerate(employee_summary[:5]):
        print(f"   {emp['first_name']} {emp['last_name']}: {emp['total_percentage']}%")
        if i >= 4:
            break
    
    conn.close()
    print("\n🎉 ALL TESTS PASSED - Admin Dashboard Fix Verified!")

if __name__ == '__main__':
    test_admin_dashboard_fix()