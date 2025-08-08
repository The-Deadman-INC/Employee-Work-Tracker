import os
import sys

print("🔍 Quick App Check")
print("=" * 40)

# Check if files exist
files_to_check = [
    ('app.py', 'Main application'),
    ('work_tracker.db', 'Database file'),
    ('templates/admin_reports.html', 'Reports template'),
    ('templates/admin_database.html', 'Database template')
]

for file_path, description in files_to_check:
    if os.path.exists(file_path):
        size = os.path.getsize(file_path)
        print(f"✅ {description}: {file_path} ({size} bytes)")
    else:
        print(f"❌ {description}: {file_path} - NOT FOUND")

print("\n🔧 Testing App Import...")
try:
    import app
    print("✅ App imports successfully")
    
    # Check for new functions
    functions_to_check = [
        'clear_progress_data',
        'wipe_database', 
        'restore_database',
        'integrity_check'
    ]
    
    for func_name in functions_to_check:
        if hasattr(app, func_name):
            print(f"✅ Function exists: {func_name}")
        else:
            print(f"❌ Function missing: {func_name}")
            
except Exception as e:
    print(f"❌ App import failed: {e}")

print("\n💡 To test the app:")
print("1. Run: python app.py")
print("2. Open: http://127.0.0.1:5000")
print("3. Login: mahesh.butani / m.butani@321")
