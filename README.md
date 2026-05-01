# Binance Futures Trading Bot

A professional Python command-line trading bot developed for Binance Futures Testnet / Demo Trading.  
This project allows users to place and manage futures orders through a clean CLI interface with proper validation, structured logging, and error handling.

---

## Features

- Place MARKET orders
- Place LIMIT orders
- Supports BUY and SELL
- View open orders
- Cancel existing orders
- Input validation
- Exception handling
- API request/response logging
- Clean modular code structure

---

## Tech Stack

- Python 3.x
- python-binance
- python-dotenv

---

## Project Structure

```text
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
Installation

Clone or download the project, then install dependencies:

pip install -r requirements.txt
Environment Setup

Create a .env file in the root folder:

API_KEY=your_api_key
API_SECRET=your_api_secret
Usage
Place Market Order
python cli.py --action place --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
Place Limit Order
python cli.py --action place --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 100000
View Open Orders
python cli.py --action open --symbol BTCUSDT
Cancel Order
python cli.py --action cancel --symbol BTCUSDT --orderid 123456789
Sample Output
=======================================================
 Binance Futures Demo Trading Bot
=======================================================

Order Placed Successfully
----------------------------------------
Order ID : 13097000111
Symbol   : BTCUSDT
Status   : FILLED
Side     : BUY
Type     : MARKET
Qty      : 0.001
----------------------------------------
Logging

All API requests, responses, and errors are stored in:

bot.log
Error Handling

The application handles:

Invalid order side (must be BUY / SELL)
Invalid order type (must be MARKET / LIMIT)
Missing price for LIMIT orders
Invalid quantity
API errors
Network connection failures
Assumptions
Uses Binance Futures Testnet / Demo Trading environment
LIMIT orders remain open until matched or cancelled
API credentials are stored securely in .env
Assignment Coverage

✔ Place Market Orders
✔ Place Limit Orders
✔ BUY / SELL Support
✔ CLI Input
✔ Validation
✔ Logging
✔ Error Handling
✔ Structured Code

Future Improvements
Stop-Limit order support
Take-Profit / Stop-Loss orders
Telegram alerts
Trading strategy automation
Web dashboard UI
Author

Niranjana M