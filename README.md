# 🚀 Binance Futures Testnet Trading Bot (Python CLI)

A professional Python-based command-line trading bot that connects to the **Binance Futures Testnet (USDT-M)**.

It allows users to simulate crypto trading by placing and managing futures orders using a simple CLI interface.

This project demonstrates:
- Binance API integration
- CLI-based application design
- Modular Python structure
- Error handling & logging
- Real-world trading simulation (testnet)

---

# 📂 Project Structure


trading_bot/
│
├── cli.py # Main entry point (CLI interface)
├── bot/ # Core trading logic
├── .env # API keys (NOT pushed to GitHub)
├── requirements.txt # Dependencies
├── bot.log # Logs
├── output.log
├── README.md


---

# ⚙️ Setup Instructions

## 1. Clone Repository
```bash
git clone <your-repo-url>
cd trading_bot
2. Install Dependencies
pip install -r requirements.txt
3. Setup Environment Variables

Create a .env file:

API_KEY=your_binance_testnet_api_key
API_SECRET=your_binance_testnet_secret_key

🚀 How to Run:

📌 Place MARKET Order
    python cli.py --action place --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
📌 Place LIMIT Order
    python cli.py --action place --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.001 --price 75000
📊 View Open Orders
    python cli.py --action open --symbol BTCUSDT
❌ Cancel Order
    python cli.py --action cancel --symbol BTCUSDT --orderid <ORDER_ID>

⚠️ Important Notes

Use Binance Futures Testnet only
Minimum order notional must be ≥ 50 USDT
LIMIT orders must follow market price rules
Keep .env file private (DO NOT upload to GitHub)

🧠 Features

✔ Market Orders (BUY / SELL)
✔ Limit Orders
✔ Order Management
✔ CLI-based interface
✔ Error handling
✔ API logging
✔ Testnet trading simulation

📸 Screenshots

Add screenshots of:

Market order execution"C:\Users\mnira\OneDrive\Videos\Pictures\Screenshots\Screenshot (37).png"
Limit order execution"C:\Users\mnira\OneDrive\Videos\Pictures\Screenshots\Screenshot (38).png"
Open orders"C:\Users\mnira\OneDrive\Videos\Pictures\Screenshots\Screenshot (39).png"
Cancel order result

🛠️ Tech Stack
Python 3
Binance Futures Testnet API
CLI (argparse)
dotenv
requests

👨‍💻 Author
Niranjana M
Developed as a Python trading bot project for learning API integration and real-world trading systems.

⭐ Future Improvements
Web dashboard (Flask / React)
Auto risk management
Strategy engine
Real-time price tracking
