#!/usr/bin/env python3
"""
Simple test to start Flask app and check routes
"""

import sys
import os
import threading
import time
import requests

# Add current directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app import app, init_database

def start_flask_app():
    """Start Flask app in a separate thread"""
    app.run(debug=False, host='127.0.0.1', port=5000, use_reloader=False)

def test_routes():
    """Test key routes"""
    time.sleep(2)  # Give Flask time to start
    
    base_url = 'http://127.0.0.1:5000'
    
    test_routes = [
        '/',
        '/admin/login',
        '/employee/login'
    ]
    
    print("Testing routes...")
    for route in test_routes:
        try:
            url = base_url + route
            response = requests.get(url, timeout=5)
            print(f"✓ {route} - Status: {response.status_code}")
        except Exception as e:
            print(f"✗ {route} - Error: {e}")

if __name__ == '__main__':
    # Initialize database if needed
    if not os.path.exists('work_tracker.db'):
        print("Initializing database...")
        init_database()
    
    print("Starting Flask application...")
    
    # Start Flask in background thread
    flask_thread = threading.Thread(target=start_flask_app, daemon=True)
    flask_thread.start()
    
    # Test routes
    test_routes()
    
    print("\n" + "="*50)
    print("🚀 Flask application is running!")
    print("📊 Open: http://127.0.0.1:5000")
    print("👤 Admin: mahesh.butani / m.butani@321")
    print("="*50)
    
    # Keep main thread alive
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nShutting down...")
        sys.exit(0)
