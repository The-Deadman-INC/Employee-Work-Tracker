#!/usr/bin/env python3
"""
Debug script to test specific routes
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app import app

# Test the routes directly
with app.test_client() as client:
    print("Testing admin routes...")
    
    # Test main route
    response = client.get('/')
    print(f"GET / - Status: {response.status_code}")
    
    # Test admin login (should work)
    response = client.get('/admin/login')
    print(f"GET /admin/login - Status: {response.status_code}")
    
    # Test reports route (this is the problematic one)
    response = client.get('/admin/reports')
    print(f"GET /admin/reports - Status: {response.status_code}")
    if response.status_code != 200:
        print(f"Error: {response.data.decode()}")
    
    # Test database route
    response = client.get('/admin/database')  
    print(f"GET /admin/database - Status: {response.status_code}")
    if response.status_code != 200:
        print(f"Error: {response.data.decode()}")

print("\nRoute testing complete!")
