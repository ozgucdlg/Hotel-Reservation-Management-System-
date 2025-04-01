from extensions import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)
    
    def __repr__(self):
        return f'<User {self.username}>'

class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    room_number = db.Column(db.String(10), unique=True, nullable=False)
    room_type = db.Column(db.String(50), nullable=False)  # Single, Double, Suite, etc.
    price = db.Column(db.Float, nullable=False)
    capacity = db.Column(db.Integer, nullable=False, default=1)
    is_available = db.Column(db.Boolean, default=True)
    
    # Relationship with Reservation
    reservations = db.relationship('Reservation', backref='room', lazy=True)
    
    def __repr__(self):
        return f'<Room {self.room_number}>'

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)
    
    # Relationship with Reservation
    reservations = db.relationship('Reservation', backref='customer', lazy=True)
    
    def __repr__(self):
        return f'<Customer {self.first_name} {self.last_name}>'

class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    room_id = db.Column(db.Integer, db.ForeignKey('room.id'), nullable=False)
    check_in = db.Column(db.DateTime, nullable=False)
    check_out = db.Column(db.DateTime, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)
    status = db.Column(db.String(20), default='confirmed')  # confirmed, checked_in, checked_out, cancelled
    total_price = db.Column(db.Float, nullable=True)
    
    def __repr__(self):
        return f'<Reservation {self.id}>'
    
    def calculate_total_price(self):
        # Calculate the number of days between check-in and check-out
        delta = self.check_out - self.check_in
        days = delta.days
        
        # Get the room price
        room_price = self.room.price
        
        # Calculate total price
        self.total_price = days * room_price
        return self.total_price 