import requests
from urls import BASE_URL, ORDERS_URL, ORDERS_CANCEL_URL

class OrderMethods:
    @staticmethod
    def create_order(data):
        return requests.post(f"{BASE_URL}{ORDERS_URL}", json=data)

    @staticmethod
    def cancel_order(track_id):
        return requests.put(f"{BASE_URL}{ORDERS_URL}{ORDERS_CANCEL_URL}", params={"track": track_id})

    @staticmethod
    def get_orders():
        return requests.get(f"{BASE_URL}{ORDERS_URL}")
