import allure
import pytest
import data
from orders_methods import OrderMethods
from generators import generate_order

class TestOrder:

    @allure.title("Создание заказа с параметрами цвета")
    @pytest.mark.parametrize("colors", [["BLACK"], ["GREY"], ["BLACK", "GREY"], []])
    def test_create_order(self, colors, cleanup_order):
        with allure.step(f"Генерируем данные заказа с цветами: {colors}"):
            order_data = generate_order(colors=colors)

        with allure.step("Отправляем POST-запрос на создание заказа"):
            response = OrderMethods.create_order(order_data)

        cleanup_order["track"] = response.json()["track"]

        with allure.step(f"Проверяем код ответа и что в теле ответа есть ключ {data.SuccessCreatedOrderResponse.required_key}"):
            assert response.status_code == data.SuccessCreatedOrderResponse.status_code
            assert data.SuccessCreatedOrderResponse.required_key in response.json()
