import requests

from data import BASE_URL

class AuthMethods:
    @staticmethod
    def login_courier(credentials):
        return requests.post(f"{BASE_URL}/courier/login", json=credentials)
