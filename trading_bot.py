import logging
from datetime import datetime

# Setup logging
logging.basicConfig(filename='bot_log.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def place_order(order_type, symbol, quantity, price):
    """
    Simulates placing a mock order
    """
    if quantity <= 0 or price <= 0:
        raise ValueError("Quantity and price must be greater than zero.")

    message = f"Order placed: {order_type.upper()} {quantity} {symbol} at ${price}"
    logging.info(message)
    return message

def main():
    print("🔹 Welcome to Kanan's Mock Crypto Trading Bot 🔹")
    print("This is a simulation — no real orders are placed.")
    print("Press Ctrl+C to exit.\n")

    while True:
        try:
            order_type = input("Enter order type (buy/sell): ").strip().lower()
            if order_type not in ['buy', 'sell']:
                raise ValueError("Invalid order type. Must be 'buy' or 'sell'.")

            symbol = input("Enter crypto symbol (e.g., BTCUSDT): ").strip().upper()
            quantity = float(input("Enter quantity: "))
            price = float(input("Enter price (USD): "))

            result = place_order(order_type, symbol, quantity, price)
            print("valid", result)

        except ValueError as ve:
            print("not valid Error:", ve)
            logging.error(f"Invalid input: {ve}")

        except KeyboardInterrupt:
            print("\n Exiting bot. Goodbye!")
            break

if __name__ == "__main__":
    main()
