import pytest
from courier_methods import CourierMethods
from auth_methods import AuthMethods
from generators import generate_courier
from orders_methods import OrderMethods


@pytest.fixture
def created_courier():
    courier_data = generate_courier()
    CourierMethods.create_courier(courier_data)
    yield courier_data
    login_response = AuthMethods.login_courier(courier_data)
    courier_id = login_response.json().get("id")
    CourierMethods.delete_courier(courier_id)


@pytest.fixture
def cleanup_courier(): #Фикстура для удаления курьера после теста
    courier_body = {}
    yield courier_body
    courier_data = courier_body.get("courier_data")
    if courier_data:
        login_response = AuthMethods.login_courier(courier_data)
        if login_response.status_code == 200:
            courier_id = login_response.json().get("id")
            CourierMethods.delete_courier(courier_id)


@pytest.fixture
def cleanup_order(): #Фикстура для отмены заказа после теста
    order_body = {}
    yield order_body
    track = order_body.get("track")
    if track:
        OrderMethods.cancel_order(track)
