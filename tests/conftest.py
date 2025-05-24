import pytest
from generators import generate_courier
from courier_methods import CourierMethods
from auth_methods import AuthMethods

@pytest.fixture
def courier_data():
    return generate_courier()

@pytest.fixture
def created_courier(courier_data):
    CourierMethods.create_courier(courier_data)
    yield courier_data
    login_response = AuthMethods.login_courier(courier_data)
    courier_id = login_response.json().get("id")
    CourierMethods.delete_courier(courier_id)
