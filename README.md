# 📈 Binance Futures Trading Bot (Testnet)

A professional Python-based command-line trading bot that connects to the **Binance Futures Testnet**.  
It allows users to simulate crypto trading by placing and managing futures orders through a structured CLI interface.

This project demonstrates API integration, modular design, input validation, and error handling in a real-world trading system setup.

---

## 🚀 Features

- Place Market Orders  
- Place Limit Orders  
- Supports BUY / SELL trades  
- View Open Orders  
- Cancel existing orders  
- Input validation for safe execution  
- Structured logging of API requests and responses  
- Error handling for API and runtime issues  
- Clean modular code architecture  

---

## 🛠 Tech Stack

- Python 3.x  
- python-binance  
- python-dotenv  

---
##📁 Project Structure


trading_bot/
│
├── bot/
│ ├── init.py
│ ├── client.py
│ ├── validators.py
│ ├── logging_config.py
│
├── cli.py
├── requirements.txt
├── .env
├── .gitignore
├── bot.log
└── README.md


---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/Niranjana-M/trading-bot-binance.git
cd trading-bot-binance

Install dependencies:

pip install -r requirements.txt
🔐 Environment Setup

Create a .env file in the root directory:

API_KEY=your_api_key
API_SECRET=your_api_secret

⚠️ Use Binance Futures Testnet API keys only

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

All API interactions, responses, and errors are stored in:

bot.log
⚠️ Disclaimer

This project is for educational and testing purposes only.
It uses Binance Futures Testnet and does not involve real trading funds.

📌 Future Improvements
Stop-Loss / Take-Profit orders
Trading strategy automation
Telegram alerts
Web dashboard UI
Real-time market data visualization

👨‍💻 Author

Niranjana M

## 📁 Project Structure
