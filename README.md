**Mock Crypto Trading Bot – Internship Project**
**Author:** Kanan  
**Project:** Python Developer Internship Task  
**Status:** Completed 

##  Overview
This is a **mock crypto trading bot** built in Python as part of the Binance internship assignment.  
It simulates placing market orders and logs all trade activity — no real API connection is used.

##  Features
- Takes user input to simulate trades
- Validates inputs (order type, price, quantity)
- Logs trades and errors to a log file
- Easy to test without any API or account

##  Folder Structure
crypto_bot_kanan/
├── trading_bot.py # Main Python bot
├── requirements.txt # Dependency list
├── README.md # This file
└── bot_log.log # Auto-generated trade log

##  How to Run

1. Open terminal in this folder  
2. Run:
python trading_bot.py
Enter values when prompted:
Order type: buy or sell
Symbol: BTCUSDT, ETHUSDT, etc.
Quantity: e.g., 0.5
Price: e.g., 30000
Check bot_log.log to see trade logs

Example Output
🔹 Welcome to Kanan's Mock Crypto Trading Bot 🔹
This is a simulation — no real orders are placed.
Press Ctrl+C to exit.

Enter order type (buy/sell): buy
Enter crypto symbol (e.g., BTCUSDT): BTCUSDT
Enter quantity: 0.5
Enter price (USD): 30000
Order placed: BUY 0.5 BTCUSDT at $30000.0
 Requirements
Install Python 3.7 or above.
No external packages required other than standard datetime.

**Notes
This project simulates trading logic and is not connected to Binance API, due to Testnet API restrictions.
It demonstrates understanding of:

Python I/O
Error handling
Logging
Basic CLI interaction

Contact
If you have questions, feel free to contact Kanan during the internship process.
THANKYOU
