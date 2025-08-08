# CAD Work Tracker

A web-based application for tracking monthly work progress of CAD Operators across multiple projects.

## Features

### Admin (Contracts Manager) Features:
- **Dashboard**: Overview of projects, employees, and recent submissions
- **Project Management**: View and manage all ongoing projects
- **Employee Management**: View all CAD operators and administrators
- **Reports & Analytics**: Generate and export work progress reports
- **Database Management**: Built-in SQLite database for local storage

### Employee (CAD Operator) Features:
- **Monthly Progress Entry**: Submit work completion percentage for each project
- **Real-time Progress Bars**: Visual feedback while entering progress
- **Project Overview**: View assigned projects with timelines and client information
- **Progress Summary**: Monthly statistics and completion tracking

## Installation & Setup

### Prerequisites
- Python 3.7 or higher
- Windows (configured for local server deployment)

### Installation Steps

1. **Install Python Dependencies**:
   ```powershell
   cd "Y:\CAD STANDARDS\Python\Work Tracker"
   pip install -r requirements.txt
   ```

2. **Run the Application**:
   ```powershell
   python app.py
   ```

3. **Access the Application**:
   - Open your web browser
   - Navigate to: `http://localhost:5000`
   - Or access from other computers: `http://[SERVER-IP]:5000`

## Default Login Credentials

### Admin Access:
- **Username**: mahesh.butani
- **Password**: m.butani@321

### Employee Access (Password Format: firstname.firstletter@321):
- **Shaji Narayanan**: shaji.narayanan / shaji.n@321
- **Shajimon**: shajimon / shajimon.@321
- **Ibrahim P.K**: ibrahim.pk / ibrahim.p@321
- **Mohamed Kaleefa**: mohamed.kaleefa / mohamed.k@321
- **Subeesh Puthiyedath**: subeesh.puthiyedath / subeesh.p@321
- **Najeeb E.K**: najeeb.ek / najeeb.e@321
- **Shakil Ahmed**: shakil.ahmed / shakil.a@321
- **Roy Mathew**: roy.mathew / roy.m@321
- **Suhaib Rahman**: suhaib.rahman / suhaib.r@321

## Project Structure

```
Work Tracker/
│
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── work_tracker.db       # SQLite database (auto-created)
├── README.md             # This file
│
└── templates/            # HTML templates
    ├── base.html         # Base template with navigation
    ├── launcher.html     # Landing page
    ├── login.html        # Login page
    ├── admin_dashboard.html     # Admin dashboard
    ├── admin_projects.html      # Project management
    ├── admin_employees.html     # Employee management
    ├── admin_reports.html       # Reports and analytics
    └── employee_dashboard.html  # Employee progress entry
```

## Database Schema

### Tables:
1. **employees**: Employee information and login credentials
2. **projects**: Project details, timelines, and clients
3. **work_progress**: Monthly progress submissions (percentage per project per employee)

## Usage Instructions

### For Contracts Manager (Admin):

1. **Login** with admin credentials
2. **Dashboard**: View overview statistics and recent submissions
3. **Projects**: Manage ongoing projects and view project details
4. **Employees**: View all CAD operators and their information
5. **Reports**: Generate monthly reports and export to Excel/CSV

### For CAD Operators (Employees):

1. **Login** with your company email and password
2. **View Projects**: See all active projects assigned to the team
3. **Enter Progress**: Input work completion percentage for each project
4. **Submit**: Save your monthly progress (can be updated multiple times)
5. **Track Progress**: View your submission history and progress summary

## Monthly Workflow

1. **Beginning of Month**: CAD operators log in to submit previous month's progress
2. **Progress Entry**: Each operator enters completion percentage for their assigned projects
3. **Submission**: Operators can update and resubmit progress throughout the month
4. **Report Generation**: Contracts Manager generates monthly reports for contractual purposes
5. **Export**: Data can be exported to Excel for further analysis

## Technical Details

- **Backend**: Python Flask framework
- **Frontend**: HTML5, Bootstrap 5, JavaScript
- **Database**: SQLite (file-based, stored locally)
- **Authentication**: Session-based with password hashing
- **Responsive Design**: Works on desktop, tablet, and mobile devices

## Security Features

- Password hashing using Werkzeug security
- Session-based authentication
- Role-based access control (Admin vs Employee)
- Input validation and sanitization

## Deployment on Local Server

1. **Install on Server**: Copy the entire project folder to your local server
2. **Configure Network**: Ensure port 5000 is accessible on your network
3. **Start Application**: Run `python app.py` on the server
4. **Access from Workstations**: Use `http://[SERVER-IP]:5000` from any computer on the network

## Customization

### Adding New Employees:
- Currently done through database or admin interface (to be implemented)
- Default password for new employees: `password123`

### Adding New Projects:
- Projects can be added through the admin interface
- Include project ID, name, client, timeline, and team size

### Modifying Progress Periods:
- System automatically tracks by month/year
- Historical data is preserved for reporting

## Troubleshooting

### Common Issues:

1. **Database Not Found**: Database is auto-created on first run
2. **Login Failed**: Check email and password (case-sensitive)
3. **Page Not Loading**: Ensure Flask server is running
4. **Network Access**: Check firewall settings for port 5000

### Support:
Contact IT support for technical assistance or credential resets.

## Future Enhancements

- Advanced project assignment (employee-specific)
- Email notifications for submission deadlines
- Advanced reporting with charts and graphs
- Bulk data import/export functionality
- User profile management
- Password reset functionality
