import sqlite3

# Check database contents
conn = sqlite3.connect('work_tracker.db')

# Get tables
tables = [row[0] for row in conn.execute('SELECT name FROM sqlite_master WHERE type="table"').fetchall()]
print('Tables:', tables)

if 'work_progress' in tables:
    progress_count = conn.execute('SELECT COUNT(*) FROM work_progress').fetchone()[0]
    print('Progress entries:', progress_count)
    
    # Get some sample data
    sample_data = conn.execute('SELECT * FROM work_progress LIMIT 3').fetchall()
    print('Sample progress data:', len(sample_data), 'entries')

if 'employees' in tables:
    employee_count = conn.execute('SELECT COUNT(*) FROM employees').fetchone()[0]
    print('Employee count:', employee_count)

if 'projects' in tables:
    project_count = conn.execute('SELECT COUNT(*) FROM projects').fetchone()[0]
    print('Project count:', project_count)

conn.close()
