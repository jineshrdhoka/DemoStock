# Stock Trading Platform

## Overview
This is a full-fledged stock trading web application with a Flask backend and a modern UI. The platform allows users to trade stocks, options, and futures. It includes a user dashboard, admin panel, leaderboard, trading page, and portfolio tracking with proper authentication and market rules applied.

## Project Structure
```
stock_trading_platform/
│── app.py                     # Flask backend
│── config.py                  # Configuration settings
│── database.db                # SQLite database
│── requirements.txt           # Python dependencies
│── static/
│   ├── styles.css             # UI styles (Dark Mode, Responsive)
│   ├── script.js              # Frontend logic (Trading, Charts)
│── templates/
│   ├── index.html             # Dashboard (Stock List, Buy/Sell)
│   ├── stock.html             # Stock Details (Charts, Trading)
│   ├── trading.html           # Trading Page (F&O, Orders)
│   ├── portfolio.html         # Portfolio (User Holdings, P/L)
│   ├── admin.html             # Admin Panel (User Management)
│   ├── leaderboard.html       # Leaderboard (Top Traders)
│   ├── login.html             # Login Page
│── README.md                  # Setup Instructions
```

## Features
1. **Backend - Flask API (app.py)**
   - User authentication (Login/Logout)
   - Admin and regular user roles
   - Trading logic: Buying, Selling, Futures & Options
   - Admin Panel for user management
   - Fetch live stock data from NSE/BSE APIs
   - Session handling for security
   - API routes for frontend interaction

2. **Frontend - UI Pages (templates/)**
   - `index.html`: Dashboard with stock indices, trending stocks, and news feed
   - `stock.html`: Detailed stock information with TradingView charts
   - `trading.html`: Trading page for placing Buy/Sell orders
   - `portfolio.html`: User holdings with profit/loss tracking
   - `leaderboard.html`: Top traders leaderboard
   - `admin.html`: Admin Panel for user management
   - `login.html`: Login functionality

3. **Styling & Functionality**
   - HTML/CSS/JavaScript with Bootstrap for responsive design
   - Dark Mode toggle
   - Chart.js or TradingView API for stock charts
   - AJAX/Fetch API for live updates

4. **Database (database.db)**
   - SQLite schema with `users`, `stocks`, `transactions`, and `leaderboard` tables

5. **Additional Features**
   - Session management
   - Admin leaderboard access
   - Stock price fetching every 20 minutes
   - User authentication using Flask sessions
   - Take-Profit & Stop-Loss orders
   - Trade history UI with filters
   - Customizable account balance in Admin Panel
   - Mobile-friendly UI with optimized responsiveness

## Setup Instructions
1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/stock_trading_platform.git
   cd stock_trading_platform
   ```

2. **Create and activate a virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the SQLite database**
   ```bash
   flask db init
   flask db migrate -m "Initial migration."
   flask db upgrade
   ```

5. **Run the application**
   ```bash
   flask run
   ```

6. **Access the application**
   Open a web browser and go to `http://127.0.0.1:5000`

## Contributing
- Fork the repository
- Create a new branch (`git checkout -b feature-branch`)
- Commit your changes (`git commit -am 'Add new feature'`)
- Push to the branch (`git push origin feature-branch`)
- Create a new Pull Request

## License
This project is licensed under the MIT License.