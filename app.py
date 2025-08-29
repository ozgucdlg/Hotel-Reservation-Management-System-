from flask import Flask, render_template, request, redirect, url_for, flash, session
from datetime import datetime
import os
from werkzeug.security import generate_password_hash, check_password_hash
from extensions import db
from models import User, Room, Customer, Reservation

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'hotelreservationsystem'

# Configure database
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'hotel.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize extensions with app
db.init_app(app)

# Create database tables
with app.app_context():
    db.create_all()

# Context processors for templates
@app.context_processor
def inject_now():
    return {'now': datetime.now}

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        user = User.query.filter_by(username=username).first()
        
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            flash('Logged in successfully!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password', 'danger')
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('Logged out successfully!', 'success')
    return redirect(url_for('index'))

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        flash('Please login to access the dashboard', 'danger')
        return redirect(url_for('login'))
    
    # Count total rooms, reservations, and customers
    total_rooms = Room.query.count()
    total_reservations = Reservation.query.count()
    total_customers = Customer.query.count()
    
    # Get recent reservations
    recent_reservations = Reservation.query.order_by(Reservation.created_at.desc()).limit(5).all()
    
    return render_template('dashboard.html', 
                          total_rooms=total_rooms,
                          total_reservations=total_reservations,
                          total_customers=total_customers,
                          recent_reservations=recent_reservations)

# Room management routes
@app.route('/rooms')
def rooms():
    if 'user_id' not in session:
        flash('Please login to access this page', 'danger')
        return redirect(url_for('login'))
    
    rooms = Room.query.all()
    return render_template('rooms.html', rooms=rooms)

@app.route('/rooms/add', methods=['GET', 'POST'])
def add_room():
    if 'user_id' not in session:
        flash('Please login to access this page', 'danger')
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        room_number = request.form.get('room_number')
        room_type = request.form.get('room_type')
        price = request.form.get('price')
        capacity = request.form.get('capacity')
        
        room = Room(
            room_number=room_number,
            room_type=room_type,
            price=price,
            capacity=capacity
        )
        
        db.session.add(room)
        db.session.commit()
        
        flash('Room added successfully!', 'success')
        return redirect(url_for('rooms'))
    
    return render_template('add_room.html')

# Reservation routes
@app.route('/reservations')
def reservations():
    if 'user_id' not in session:
        flash('Please login to access this page', 'danger')
        return redirect(url_for('login'))
    
    reservations = Reservation.query.all()
    return render_template('reservations.html', reservations=reservations)

@app.route('/reservations/add', methods=['GET', 'POST'])
def add_reservation():
    if 'user_id' not in session:
        flash('Please login to access this page', 'danger')
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        customer_id = request.form.get('customer_id')
        room_id = request.form.get('room_id')
        check_in = datetime.strptime(request.form.get('check_in'), '%Y-%m-%d')
        check_out = datetime.strptime(request.form.get('check_out'), '%Y-%m-%d')
        
        reservation = Reservation(
            customer_id=customer_id,
            room_id=room_id,
            check_in=check_in,
            check_out=check_out,
            created_at=datetime.now()
        )
        
        db.session.add(reservation)
        db.session.commit()
        
        flash('Reservation added successfully!', 'success')
        return redirect(url_for('reservations'))
    
    customers = Customer.query.all()
    rooms = Room.query.all()
    return render_template('add_reservation.html', customers=customers, rooms=rooms)

# Customer routes
@app.route('/customers')
def customers():
    if 'user_id' not in session:
        flash('Please login to access this page', 'danger')
        return redirect(url_for('login'))
    
    customers = Customer.query.all()
    return render_template('customers.html', customers=customers)

@app.route('/customers/add', methods=['GET', 'POST'])
def add_customer():
    if 'user_id' not in session:
        flash('Please login to access this page', 'danger')
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        
        customer = Customer(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone
        )
        
        db.session.add(customer)
        db.session.commit()
        
        flash('Customer added successfully!', 'success')
        return redirect(url_for('customers'))
    
    return render_template('add_customer.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_ENV') == 'development'
    app.run(host='0.0.0.0', port=port, debug=debug) 