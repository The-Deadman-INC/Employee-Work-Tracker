#!/usr/bin/env python3
"""
Debug the reports data
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app import app, get_db_connection

def debug_reports_data():
    conn = get_db_connection()
    
    # Get progress data for reports
    progress_data = conn.execute('''
        SELECT wp.*, e.first_name, e.last_name, p.name as project_name, p.client
        FROM work_progress wp
        JOIN employees e ON wp.emp_id = e.emp_id
        JOIN projects p ON wp.proj_id = p.proj_id
        ORDER BY wp.year DESC, wp.month DESC, e.first_name
    ''').fetchall()
    
    print(f"Progress data count: {len(progress_data)}")
    
    if progress_data:
        print("Sample data:")
        for i, row in enumerate(progress_data[:3]):
            print(f"  Row {i+1}: {dict(row)}")
    
    # Get unique months/years for filtering
    months_years = conn.execute('''
        SELECT DISTINCT month, year FROM work_progress 
        ORDER BY year DESC, 
        CASE month 
            WHEN 'January' THEN 1 WHEN 'February' THEN 2 WHEN 'March' THEN 3
            WHEN 'April' THEN 4 WHEN 'May' THEN 5 WHEN 'June' THEN 6
            WHEN 'July' THEN 7 WHEN 'August' THEN 8 WHEN 'September' THEN 9
            WHEN 'October' THEN 10 WHEN 'November' THEN 11 WHEN 'December' THEN 12
        END DESC
    ''').fetchall()
    
    print(f"Months/Years count: {len(months_years)}")
    for row in months_years:
        print(f"  {dict(row)}")
    
    conn.close()

if __name__ == '__main__':
    debug_reports_data()
