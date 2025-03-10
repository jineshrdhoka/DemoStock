from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import requests
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    role = db.Column(db.String(50), nullable=False)
    balance = db.Column(db.Float, nullable=False, default=0)

class Stock(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    symbol = db.Column(db.String(10), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    stock_id = db.Column(db.Integer, db.ForeignKey('stock.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    date = db.Column(db.DateTime, default=datetime.datetime.utcnow)

class Leaderboard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    profit = db.Column(db.Float, nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
@login_required
def index():
    stocks = Stock.query.all()
    return render_template('index.html', stocks=stocks)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        if user and bcrypt.check_password_hash(user.password, password):
            login_user(user)
            if user.role == 'admin':
                return redirect(url_for('admin'))
            else:
                return redirect(url_for('index'))
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/admin')
@login_required
def admin():
    if current_user.role != 'admin':
        return redirect(url_for('index'))
    users = User.query.all()
    return render_template('admin.html', users=users)

@app.route('/buy_stock', methods=['POST'])
@login_required
def buy_stock():
    stock_id = request.form.get('stock_id')
    quantity = request.form.get('quantity')
    stock = Stock.query.get(stock_id)
    total_price = stock.price * int(quantity)
    if current_user.balance >= total_price:
        current_user.balance -= total_price
        transaction = Transaction(user_id=current_user.id, stock_id=stock.id, quantity=quantity, price=stock.price)
        db.session.add(transaction)
        db.session.commit()
        return jsonify({'status': 'success', 'message': 'Stock purchased successfully'})
    else:
        return jsonify({'status': 'error', 'message': 'Insufficient balance'})

@app.route('/sell_stock', methods=['POST'])
@login_required
def sell_stock():
    stock_id = request.form.get('stock_id')
    quantity = request.form.get('quantity')
    stock = Stock.query.get(stock_id)
    total_price = stock.price * int(quantity)
    current_user.balance += total_price
    transaction = Transaction(user_id=current_user.id, stock_id=stock.id, quantity=-int(quantity), price=stock.price)
    db.session.add(transaction)
    db.session.commit()
    return jsonify({'status': 'success', 'message': 'Stock sold successfully'})

@app.route('/portfolio')
@login_required
def portfolio():
    transactions = Transaction.query.filter_by(user_id=current_user.id).all()
    return render_template('portfolio.html', transactions=transactions)

@app.route('/leaderboard')
@login_required
def leaderboard():
    leaders = Leaderboard.query.order_by(Leaderboard.profit.desc()).all()
    return render_template('leaderboard.html', leaders=leaders)

@app.route('/stock/<int:stock_id>')
@login_required
def stock(stock_id):
    stock = Stock.query.get(stock_id)
    return render_template('stock.html', stock=stock)

@app.route('/trading')
@login_required
def trading():
    stocks = Stock.query.all()
    return render_template('trading.html', stocks=stocks)

def fetch_stock_prices():
    # Function to fetch live stock prices from NSE/BSE APIs
    pass

if __name__ == '__main__':
    app.run(debug=True)