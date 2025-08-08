#!/usr/bin/env python3
"""
Quick test script to verify the enhanced CAD Work Tracker application
"""

import subprocess
import sys
import time
import webbrowser
import os

def main():
    print("🚀 Starting Enhanced CAD Work Tracker...")
    print("=" * 60)
    
    # Check if we're in the right directory
    if not os.path.exists('app.py'):
        print("❌ app.py not found! Make sure you're in the correct directory.")
        sys.exit(1)
    
    # Check if database exists
    if not os.path.exists('work_tracker.db'):
        print("📝 Database not found. It will be created automatically.")
    
    try:
        # Start the Flask application
        print("🔧 Starting Flask server...")
        process = subprocess.Popen([sys.executable, 'app.py'], 
                                 stdout=subprocess.PIPE, 
                                 stderr=subprocess.PIPE)
        
        # Wait a moment for the server to start
        time.sleep(3)
        
        # Check if process is still running
        if process.poll() is None:
            print("✅ Flask server started successfully!")
            print("\n📊 Enhanced Features Available:")
            print("  • Reports page with data visualization")
            print("  • Comprehensive database management")
            print("  • Backup and restore functionality")
            print("  • Data clearing and wiping options")
            print("  • Integrity checking")
            print("  • CSV export with filtering")
            print("\n🔐 Admin Login:")
            print("  Username: mahesh.butani")
            print("  Password: m.butani@321")
            print("\n🌐 Opening browser to: http://127.0.0.1:5000")
            
            # Open browser
            webbrowser.open('http://127.0.0.1:5000')
            
            print("\n⚠️  Press Ctrl+C to stop the server")
            
            # Wait for user to stop
            try:
                process.wait()
            except KeyboardInterrupt:
                print("\n🛑 Stopping server...")
                process.terminate()
                print("✅ Server stopped successfully!")
        else:
            print("❌ Failed to start Flask server!")
            stdout, stderr = process.communicate()
            if stderr:
                print(f"Error: {stderr.decode()}")
    
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
