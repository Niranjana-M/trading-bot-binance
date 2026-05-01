from binance.client import Client
import logging

class BinanceBot:
    def __init__(self, api_key, api_secret):
        self.client = Client(api_key, api_secret)
        self.client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

    def place_order(self, symbol, side, order_type, quantity, price=None):
        params = {
            "symbol": symbol,
            "side": side,
            "type": order_type,
            "quantity": quantity
        }

        if order_type == "LIMIT":
            params["price"] = price
            params["timeInForce"] = "GTC"

        logging.info(f"Placing order: {params}")
        return self.client.futures_create_order(**params)

    def get_open_orders(self, symbol):
        logging.info(f"Fetching open orders for {symbol}")
        return self.client.futures_get_open_orders(symbol=symbol)

    def cancel_order(self, symbol, order_id):
        logging.info(f"Cancelling order {order_id}")
        return self.client.futures_cancel_order(
            symbol=symbol,
            orderId=order_id
        )