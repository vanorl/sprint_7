import requests
from urls import BASE_URL, COURIER_URL

class CourierMethods:
    @staticmethod
    def create_courier(data):
        return requests.post(f"{BASE_URL}{COURIER_URL}", json=data)

    @staticmethod
    def delete_courier(courier_id):
        return requests.delete(f"{BASE_URL}{COURIER_URL}/{courier_id}")
