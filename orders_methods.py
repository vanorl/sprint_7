import requests
from data import BASE_URL

class OrderMethods:
    @staticmethod
    def create_order(data):
        return requests.post(f"{BASE_URL}/orders", json=data)

    @staticmethod
    def cancel_order(track_id):
        return requests.put(f"{BASE_URL}/orders/cancel", params={"track": track_id})

    @staticmethod
    def get_orders():
        return requests.get(f"{BASE_URL}/orders")
