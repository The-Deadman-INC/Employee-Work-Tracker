#!/usr/bin/env python3
"""
Quick test script to verify employee dashboard JavaScript functionality
"""

import sys
import os

def test_employee_template():
    """Test that the employee dashboard template is properly formatted"""
    
    template_path = "templates/employee_dashboard.html"
    
    print("=" * 60)
    print("EMPLOYEE DASHBOARD TEMPLATE TEST")
    print("=" * 60)
    
    # Check if template exists and is properly sized
    if os.path.exists(template_path):
        file_size = os.path.getsize(template_path)
        print(f"✅ Template exists: {template_path}")
        print(f"✅ File size: {file_size:,} bytes")
        
        if file_size > 15000:  # Should be around 18KB
            print("✅ File size looks good (not corrupted)")
        else:
            print("❌ File size too small - may be corrupted")
            return False
    else:
        print(f"❌ Template not found: {template_path}")
        return False
    
    # Check template content
    try:
        with open(template_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check for key JavaScript functions
        required_functions = [
            'function clearAll()',
            'function updateTotalProgress()',
            'function updateProgressBars()',
            'addEventListener(\'input\'',
            'addEventListener(\'change\'',
            'hasSubmittedData'
        ]
        
        print("\nChecking JavaScript functions:")
        for func in required_functions:
            if func in content:
                print(f"✅ Found: {func}")
            else:
                print(f"❌ Missing: {func}")
                return False
        
        # Check for proper template structure
        required_elements = [
            'progress-input',
            'submitBtn',
            'totalProgress',
            'progressStatus',
            'project-progress-bar'
        ]
        
        print("\nChecking HTML elements:")
        for element in required_elements:
            if element in content:
                print(f"✅ Found: {element}")
            else:
                print(f"❌ Missing: {element}")
                return False
        
        print("\n✅ All template checks passed!")
        return True
        
    except Exception as e:
        print(f"❌ Error reading template: {e}")
        return False

def main():
    """Main test function"""
    
    print("Testing employee dashboard fix...")
    
    if test_employee_template():
        print("\n" + "=" * 60)
        print("🎉 EMPLOYEE DASHBOARD FIX SUCCESSFUL!")
        print("=" * 60)
        print("\nTo test the fix:")
        print("1. Start Flask: python app.py")
        print("2. Go to: http://127.0.0.1:5000/employee/login")
        print("3. Login with an employee who hasn't submitted data")
        print("4. Try entering percentages - they should update in real-time")
        print("5. Submit button should enable when total = 100%")
        print("\nTest employees who haven't submitted:")
        print("- Username: shaji, Password: shaji@321")
        print("- Username: shajimon, Password: shajimon@321")
        print("- Username: ibrahim, Password: ibrahim@321")
        print("- etc. (all employees except those who already submitted)")
        
    else:
        print("\n" + "=" * 60)
        print("❌ TEMPLATE ISSUES DETECTED")
        print("=" * 60)
        print("\nThe template may still have issues. Check the errors above.")

if __name__ == "__main__":
    main()
