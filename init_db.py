from app import app
from extensions import db
from models import User, Room, Customer
from werkzeug.security import generate_password_hash
from datetime import datetime

def init_db():
    with app.app_context():
        # Create all tables
        db.create_all()
        
        # Check if admin user already exists
        admin = User.query.filter_by(username='admin').first()
        if not admin:
            # Create admin user
            admin = User(
                username='admin',
                password=generate_password_hash('adminpass'),
                email='admin@hotel.com',
                created_at=datetime.now()
            )
            db.session.add(admin)
            
            # Add sample rooms
            rooms = [
                Room(room_number='101', room_type='Single', price=79.99, capacity=1),
                Room(room_number='102', room_type='Single', price=79.99, capacity=1),
                Room(room_number='201', room_type='Double', price=99.99, capacity=2),
                Room(room_number='202', room_type='Double', price=99.99, capacity=2),
                Room(room_number='301', room_type='Deluxe', price=149.99, capacity=2),
                Room(room_number='302', room_type='Suite', price=199.99, capacity=4)
            ]
            db.session.add_all(rooms)
            
            # Add sample customers
            customers = [
                Customer(first_name='John', last_name='Doe', email='john@example.com', phone='555-123-4567'),
                Customer(first_name='Jane', last_name='Smith', email='jane@example.com', phone='555-987-6543'),
                Customer(first_name='Robert', last_name='Johnson', email='robert@example.com', phone='555-456-7890')
            ]
            db.session.add_all(customers)
            
            db.session.commit()
            print("Database initialized with admin user, sample rooms and customers.")
        else:
            print("Admin user already exists. Database initialization skipped.")

if __name__ == '__main__':
    init_db() 