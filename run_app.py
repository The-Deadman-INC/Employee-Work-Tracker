import subprocess
import sys
import os

# Change to the correct directory
os.chdir(r"y:\CAD STANDARDS\Python\Work Tracker")

# Start Flask app
try:
    print("Starting Flask application...")
    print("Access at: http://127.0.0.1:5000")
    print("Use Ctrl+C to stop")
    
    # Run the Flask app
    result = subprocess.run([sys.executable, "app.py"], check=True)
except KeyboardInterrupt:
    print("\nApplication stopped.")
except Exception as e:
    print(f"Error starting application: {e}")
