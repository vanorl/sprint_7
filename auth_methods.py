import requests

from urls import BASE_URL, COURIER_URL, COURIER_LOGIN_URL

class AuthMethods:
    @staticmethod
    def login_courier(credentials):
        return requests.post(f"{BASE_URL}{COURIER_URL}{COURIER_LOGIN_URL}", json=credentials)
