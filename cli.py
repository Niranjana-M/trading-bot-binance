import argparse
import os
import sys
from dotenv import load_dotenv

from bot.client import BinanceBot
from bot.validators import validate_side, validate_order_type, validate_quantity
from bot.logging_config import setup_logger

load_dotenv(dotenv_path=".env")
setup_logger()

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")


def print_header():
    print("=" * 55)
    print(" Binance Futures Demo Trading Bot ")
    print("=" * 55)


def main():
    print_header()

    parser = argparse.ArgumentParser(description="Binance Futures CLI Bot")
    parser.add_argument("--action", required=True,
                        choices=["place", "open", "cancel"])

    parser.add_argument("--symbol")
    parser.add_argument("--side")
    parser.add_argument("--type")
    parser.add_argument("--quantity", type=float)
    parser.add_argument("--price", type=float)
    parser.add_argument("--orderid")

    args = parser.parse_args()

    try:
        if not API_KEY or not API_SECRET:
            raise ValueError("Missing API credentials in .env")

        bot = BinanceBot(API_KEY, API_SECRET)

        if args.action == "place":
            validate_side(args.side)
            validate_order_type(args.type)
            validate_quantity(args.quantity)

            if args.type.upper() == "LIMIT" and not args.price:
                raise ValueError("Price required for LIMIT order")

            result = bot.place_order(
                symbol=args.symbol.upper(),
                side=args.side.upper(),
                order_type=args.type.upper(),
                quantity=args.quantity,
                price=args.price
            )

            print("\nOrder Placed Successfully")
            print("-" * 40)
            print("Order ID :", result.get("orderId"))
            print("Status   :", result.get("status"))
            print("Type     :", result.get("type"))
            print("Side     :", result.get("side"))
            print("Qty      :", result.get("executedQty"))
            print("-" * 40)

        elif args.action == "open":
            result = bot.get_open_orders(args.symbol.upper())
            print("\nOpen Orders:")
            for order in result:
                print(
                    f"ID: {order['orderId']} | "
                    f"Type: {order['type']} | "
                    f"Price: {order['price']} | "
                    f"Status: {order['status']}"
                )

        elif args.action == "cancel":
            result = bot.cancel_order(
                args.symbol.upper(),
                args.orderid
            )
            print("\nOrder Cancelled Successfully")
            print("Order ID:", result.get("orderId"))
            print("Status  :", result.get("status"))

    except Exception as e:
        print("\nOperation Failed")
        print("Reason:", str(e))
        sys.exit(1)


if __name__ == "__main__":
    main()