import allure
from orders_methods import OrderMethods


class TestOrderList:

    @allure.title("Получение списка заказов")
    def test_get_orders_returns_list(self):
        with allure.step("Проверяем, что в теле ответа возвращается список заказов"):
            list_response = OrderMethods.get_orders()
            assert list_response.status_code == 200
            assert isinstance(list_response.json().get("orders"), list)
