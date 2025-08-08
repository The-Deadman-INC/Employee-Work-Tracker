#!/usr/bin/env python3
"""
CAD Work Tracker - Final Integration Test
This script tests all major functionality to ensure proper linking
"""
import sqlite3
import requests
import time
import subprocess
import sys
from threading import Thread

class SystemTester:
    def __init__(self):
        self.base_url = "http://127.0.0.1:5000"
        self.session = requests.Session()
        self.flask_process = None
    
    def start_flask_app(self):
        """Start Flask application in background"""
        print("🚀 Starting Flask application...")
        try:
            self.flask_process = subprocess.Popen([sys.executable, 'app.py'], 
                                                stdout=subprocess.PIPE, 
                                                stderr=subprocess.PIPE)
            time.sleep(3)  # Wait for Flask to start
            return True
        except Exception as e:
            print(f"❌ Failed to start Flask: {e}")
            return False
    
    def test_launcher_page(self):
        """Test main launcher page"""
        print("\n🔍 Testing Launcher Page...")
        try:
            response = self.session.get(self.base_url)
            if response.status_code == 200:
                if "Admin Login" in response.text and "Employee Login" in response.text:
                    print("✅ Launcher page working - buttons found")
                    return True
                else:
                    print("⚠️  Launcher page loads but missing buttons")
                    return False
            else:
                print(f"❌ Launcher page failed: {response.status_code}")
                return False
        except Exception as e:
            print(f"❌ Error accessing launcher: {e}")
            return False
    
    def test_admin_login(self):
        """Test admin login functionality"""
        print("\n🔍 Testing Admin Login...")
        try:
            # Get login page
            response = self.session.get(f"{self.base_url}/admin/login")
            if response.status_code != 200:
                print("❌ Admin login page not accessible")
                return False
            
            # Attempt login
            login_data = {
                'username': 'mahesh.butani',
                'password': 'm.butani@321'
            }
            response = self.session.post(f"{self.base_url}/admin/login", data=login_data)
            
            if response.status_code == 302 or "dashboard" in response.url:
                print("✅ Admin login successful")
                return True
            else:
                print("❌ Admin login failed")
                return False
        except Exception as e:
            print(f"❌ Error testing admin login: {e}")
            return False
    
    def test_admin_pages(self):
        """Test all admin pages are accessible"""
        print("\n🔍 Testing Admin Pages...")
        
        admin_pages = [
            ('/admin/dashboard', 'Dashboard'),
            ('/admin/reports', 'Reports'),
            ('/admin/projects', 'Projects'),
            ('/admin/employees', 'Employees'),
            ('/admin/database', 'Database')
        ]
        
        results = []
        for url, name in admin_pages:
            try:
                response = self.session.get(f"{self.base_url}{url}")
                if response.status_code == 200:
                    print(f"✅ {name} page accessible")
                    results.append(True)
                else:
                    print(f"❌ {name} page failed: {response.status_code}")
                    results.append(False)
            except Exception as e:
                print(f"❌ Error accessing {name}: {e}")
                results.append(False)
        
        return all(results)
    
    def test_employee_login(self):
        """Test employee login functionality"""
        print("\n🔍 Testing Employee Login...")
        try:
            # Logout first
            self.session.get(f"{self.base_url}/logout")
            
            # Get employee login page
            response = self.session.get(f"{self.base_url}/employee/login")
            if response.status_code != 200:
                print("❌ Employee login page not accessible")
                return False
            
            # Check if dropdown exists
            if "subeesh" in response.text.lower():
                print("✅ Employee login page has dropdown")
                return True
            else:
                print("⚠️  Employee login page missing dropdown")
                return False
        except Exception as e:
            print(f"❌ Error testing employee login: {e}")
            return False
    
    def test_database_connectivity(self):
        """Test database operations"""
        print("\n🔍 Testing Database Connectivity...")
        try:
            conn = sqlite3.connect('work_tracker.db')
            cursor = conn.cursor()
            
            # Test basic queries
            cursor.execute("SELECT COUNT(*) FROM employees")
            emp_count = cursor.fetchone()[0]
            
            cursor.execute("SELECT COUNT(*) FROM projects")
            proj_count = cursor.fetchone()[0]
            
            cursor.execute("SELECT COUNT(*) FROM work_progress")
            progress_count = cursor.fetchone()[0]
            
            print(f"✅ Database accessible:")
            print(f"   📊 {emp_count} employees")
            print(f"   📊 {proj_count} projects") 
            print(f"   📊 {progress_count} progress entries")
            
            conn.close()
            return True
        except Exception as e:
            print(f"❌ Database error: {e}")
            return False
    
    def cleanup(self):
        """Clean up test resources"""
        if self.flask_process:
            self.flask_process.terminate()
            print("\n🧹 Flask application stopped")
    
    def run_all_tests(self):
        """Run complete test suite"""
        print("=" * 60)
        print("🧪 CAD WORK TRACKER - COMPREHENSIVE INTEGRATION TEST")
        print("=" * 60)
        
        all_passed = True
        
        # Test database first
        all_passed &= self.test_database_connectivity()
        
        # Start Flask app
        if not self.start_flask_app():
            print("❌ Cannot start Flask - stopping tests")
            return False
        
        try:
            # Test web functionality
            all_passed &= self.test_launcher_page()
            all_passed &= self.test_admin_login()
            all_passed &= self.test_admin_pages()
            all_passed &= self.test_employee_login()
            
        finally:
            self.cleanup()
        
        print("\n" + "=" * 60)
        if all_passed:
            print("🎉 ALL TESTS PASSED - SYSTEM FULLY OPERATIONAL!")
            print("🚀 Ready for production use!")
        else:
            print("⚠️  SOME TESTS FAILED - REVIEW ISSUES ABOVE")
        print("=" * 60)
        
        return all_passed

def main():
    tester = SystemTester()
    return tester.run_all_tests()

if __name__ == '__main__':
    success = main()
    sys.exit(0 if success else 1)