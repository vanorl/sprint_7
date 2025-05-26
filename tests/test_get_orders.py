import allure
import data
from orders_methods import OrderMethods


class TestOrderList:
    @allure.title("Получение списка заказов")
    def test_get_orders_returns_list(self):
        with allure.step("Проверяем код ответа и что в теле ответа возвращается список заказов"):
            list_response = OrderMethods.get_orders()
            assert list_response.status_code == data.GetOrdersResponse.status_code
            assert isinstance(list_response.json().get(data.GetOrdersResponse.required_key), list)
