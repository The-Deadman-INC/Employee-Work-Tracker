#!/usr/bin/env python3
"""
Launch script for CAD Work Tracker
"""

from app import app, init_database
import os

if __name__ == '__main__':
    # Initialize database if it doesn't exist
    if not os.path.exists('work_tracker.db'):
        print("Initializing database...")
        init_database()
        print("Database initialized successfully!")
    
    print("=" * 60)
    print("🚀 CAD Work Tracker Application Starting...")
    print("=" * 60)
    print("✓ All new functions added successfully:")
    print("  • Report Generation (CSV export, summary reports)")
    print("  • Database Management (backup, export, cleanup)")
    print("  • Enhanced Project Management (bulk operations, analytics)")
    print("  • Enhanced Employee Management (bulk operations, analytics)")
    print("")
    print("🌐 Access the application at: http://127.0.0.1:5000")
    print("👤 Admin Login: mahesh.butani / m.butani@321")
    print("👥 Employee Login: Use employee usernames with @321 passwords")
    print("=" * 60)
    
    # Start the Flask application
    app.run(debug=True, host='0.0.0.0', port=5000)
