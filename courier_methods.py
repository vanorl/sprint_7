import requests
from data import BASE_URL

class CourierMethods:
    @staticmethod
    def create_courier(data):
        return requests.post(f"{BASE_URL}/courier", json=data)

    @staticmethod
    def delete_courier(courier_id):
        return requests.delete(f"{BASE_URL}/courier/{courier_id}")
