# 🚀 Binance Futures Testnet Trading Bot (Python CLI)

A professional Python-based command-line trading bot that connects to the **Binance Futures Testnet**.

This project allows users to simulate crypto futures trading by placing and managing orders through a structured CLI interface.

It demonstrates **API integration, modular architecture, validation, logging, and error handling** in a real-world trading system setup.

---

## 📌 Features

- 📈 Place Market Orders  
- 📊 Place Limit Orders  
- 🔁 Buy / Sell Support  
- 📂 View Open Orders  
- ❌ Cancel Existing Orders  
- ✅ Input Validation for Safe Execution  
- 🪵 Structured Logging of API Requests & Responses  
- ⚠️ Error Handling for API & Runtime Issues  
- 🧩 Clean Modular Code Architecture  

---

## 🛠 Tech Stack

- Python 3.x  
- python-binance  
- python-dotenv  

---

## 📁 Project Structure
trading-bot-binance/
│
├── src/
│   └── trading_bot/
│       ├── __init__.py
│       │
│       ├── core/
│       │   ├── client.py              # Binance API connection & requests
│       │   ├── orders.py              # Order placement & management logic
│       │
│       ├── cli/
│       │   └── cli.py                # Command-line interface
│       │
│       ├── utils/
│       │   ├── validators.py         # Input validation
│       │   ├── logging_config.py     # Logging setup
│       │
│       └── config.py                # Loads environment variables
│
├── tests/                            # (Future scope: unit tests)
│
├── logs/
│   └── bot.log                       # Runtime logs
│
├── .env
├── .gitignore
├── requirements.txt
├── README.md
└── main.py                           # Entry point
---

## ⚙️ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Niranjana-M/trading-bot-binance.git
cd trading-bot-binance
2️⃣ Install Dependencies
pip install -r requirements.txt
🔐 Environment Setup

Create a .env file in the root directory:

API_KEY=your_api_key
API_SECRET=your_api_secret

⚠️ Use Binance Futures Testnet API keys only (not real funds)

🚀 Usage
📈 Place Market Order
       python cli.py --action place --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
📊 Place Limit Order
       python cli.py --action place --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 100000
📂 View Open Orders
       python cli.py --action open --symbol BTCUSDT
❌ Cancel Order
      python cli.py --action cancel --symbol BTCUSDT --orderid 123456789

📊 Logging
All API interactions, responses, and errors are stored in:
       bot.log

⚠️ Disclaimer

==>This project is for educational and testing purposes only.
==>It uses the Binance Futures Testnet and does not involve real money trading.

🔮 Future Improvements

Stop-Loss / Take-Profit Orders
Trading Strategy Automation
Telegram Alerts Integration
Web Dashboard UI
Real-Time Market Data Visualization

👨‍💻 Author
Niranjana M
---
