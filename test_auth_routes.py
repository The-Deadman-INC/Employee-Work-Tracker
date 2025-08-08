#!/usr/bin/env python3
"""
Test script with simulated admin login
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app import app

# Test with admin session
with app.test_client() as client:
    # Simulate admin login session
    with client.session_transaction() as sess:
        sess['user_id'] = 'ADMIN001'
        sess['user_name'] = 'Mahesh Butani'
        sess['is_admin'] = 1
    
    print("Testing admin routes with authentication...")
    
    # Test reports route
    response = client.get('/admin/reports')
    print(f"GET /admin/reports - Status: {response.status_code}")
    if response.status_code == 200:
        print("✓ Reports page loads successfully!")
        # Check if data is present
        content = response.data.decode()
        if 'Progress Reports' in content:
            print("✓ Reports page contains expected content")
        else:
            print("✗ Reports page missing expected content")
    else:
        print(f"✗ Reports page failed: {response.data.decode()[:200]}")
    
    # Test database route
    response = client.get('/admin/database')
    print(f"GET /admin/database - Status: {response.status_code}")
    if response.status_code == 200:
        print("✓ Database page loads successfully!")
        # Check if data is present
        content = response.data.decode()
        if 'Database Management' in content:
            print("✓ Database page contains expected content")
        else:
            print("✗ Database page missing expected content")
    else:
        print(f"✗ Database page failed: {response.data.decode()[:200]}")

print("\nAuthenticated route testing complete!")
