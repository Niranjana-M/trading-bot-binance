📈 Binance Futures Trading Bot

A professional Python command-line trading bot developed for Binance Futures Testnet / Demo Trading.

This project demonstrates API integration, automated order execution, input validation, and structured CLI-based trading system design.

✨ Features
Place MARKET orders
Place LIMIT orders
Supports BUY and SELL positions
View open orders
Cancel existing orders
Input validation
Exception handling
API request/response logging
Clean modular architecture
🛠 Tech Stack
Python 3.x
python-binance
python-dotenv
📁 Project Structure
trading_bot/
│── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── validators.py
│   ├── logging_config.py
│── cli.py
│── requirements.txt
│── README.md
│── bot.log
│── .gitignore
⚙️ Installation
pip install -r requirements.txt
🔐 Environment Setup

Create a .env file:

API_KEY=your_api_key
API_SECRET=your_api_secret
🚀 Usage
Place Market Order
python cli.py --action place --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
Place Limit Order
python cli.py --action place --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 100000
View Open Orders
python cli.py --action open --symbol BTCUSDT
Cancel Order
python cli.py --action cancel --symbol BTCUSDT --orderid 123456789
📊 Logging

All API requests, responses, and errors are stored in:

bot.log
⚠️ Assumptions
Uses Binance Futures Testnet (Demo Trading)
LIMIT orders remain open until executed or cancelled
API keys are stored securely in .env
📌 Future Improvements
Stop-Limit orders
Take-Profit / Stop-Loss
Telegram alerts
Automated trading strategies
Web dashboard UI
👨‍💻 Author

Niranjana M
