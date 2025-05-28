# Hotel Reservation Management System

A comprehensive web application for managing hotel reservations, rooms, and customers.

## Features

- User authentication and role-based access control
- Room management (add, edit, delete, view)
- Customer management (add, edit, delete, view)
- Reservation handling (create, edit, cancel, check-in, check-out)
- Dashboard with statistics and recent activity
- Search functionality for rooms, customers, and reservations

## Technologies Used

- **Backend**: Flask (Python web framework)
- **Database**: SQLAlchemy with SQLite
- **Frontend**: HTML, CSS, JavaScript
- **UI Framework**: Bootstrap 4
- **Charts**: Chart.js
- **Icons**: Font Awesome

## Setup and Installation

1. Clone this repository:
   ```
   git clone <https://github.com/ozgucdlg/Hotel-Reservation-Management-System-.git>
   cd hotel-reservation-system
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install flask flask-sqlalchemy werkzeug
   ```

4. Initialize the database (first time only):
   ```
   python init_db.py
   ```

5. Run the application:
   ```
   python app.py
   ```

6. Open your browser and navigate to `http://127.0.0.1:5000/`

## Project Structure

```
hotel-reservation-system/
├── app.py                  # Main application file
├── models.py               # Database models
├── init_db.py              # Database initialization script
├── static/                 # Static files (CSS, JS)
│   ├── css/                # CSS files
│   │   └── style.css       # Main stylesheet
│   └── js/                 # JavaScript files
├── templates/              # HTML templates
│   ├── base.html           # Base template with common elements
│   ├── index.html          # Home page
│   ├── login.html          # Login page
│   ├── dashboard.html      # Dashboard page
│   ├── rooms.html          # Room management
│   ├── customers.html      # Customer management
│   └── ...                 # Other templates
└── README.md               # This file
```

## Usage

### Admin Access

To access the admin dashboard, use the following credentials:
- Username: admin
- Password: adminpass

### Adding Rooms

1. Log in as an admin
2. Navigate to "Rooms" in the navigation menu
3. Click "Add New Room"
4. Fill in the room details
5. Click "Add Room"

### Making Reservations

1. Log in as an admin
2. Navigate to "Reservations" in the navigation menu
3. Click "Add New Reservation"
4. Select a customer, room, and date range
5. Click "Create Reservation"

## License

This project is licensed under the MIT License - see the LICENSE file for details. 
