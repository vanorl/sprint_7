import pytest
import allure
from generators import generate_courier
from courier_methods import CourierMethods
from auth_methods import AuthMethods


class TestCourierCreate:

    @allure.title("Курьера можно создать при передаче валидных данных")
    def test_create_courier_success(self):
        with allure.step("Генерируем данные курьера"):
            courier_data = generate_courier()

        with allure.step("Отправляем запрос на создание курьера"):
            response = CourierMethods.create_courier(courier_data)

        with allure.step("Проверяем, что курьер успешно создан"):
            assert response.status_code == 201
            assert response.json() == {"ok": True}

        with allure.step("Удаляем созданного курьера"):
            courier_id = AuthMethods.login_courier(courier_data).json().get("id")
            CourierMethods.delete_courier(courier_id)

    @allure.title("Нельзя создать двух одинаковых курьеров")
    def test_create_courier_duplicate(self):
        with allure.step("Генерируем данные курьера"):
            courier_data = generate_courier()

        with allure.step("Создаём первого курьера"):
            CourierMethods.create_courier(courier_data)

        with allure.step("Пытаемся создать второго курьера с теми же данными"):
            duplicate_response = CourierMethods.create_courier(courier_data)

        with allure.step("Проверяем, что вернулась ошибка 409"):
            assert duplicate_response.status_code == 409
            assert "уже используется" in duplicate_response.json().get("message", "")

        with allure.step("Удаляем первого курьера"):
            courier_id = AuthMethods.login_courier(courier_data).json().get("id")
            CourierMethods.delete_courier(courier_id)

    @allure.title("Создание курьера с пропущенным полем возвращает ошибку")
    @pytest.mark.parametrize("missing_field", ["login", "password"])
    def test_create_courier_missing_required_fields(self, missing_field):
        with allure.step(f"Генерируем данные курьера и удаляем поле '{missing_field}'"):
            courier_data = generate_courier()
            courier_data.pop(missing_field)

        with allure.step("Пытаемся создать курьера с неполными данными"):
            response = CourierMethods.create_courier(courier_data)

        with allure.step("Проверяем, что вернулась ошибка 400 и сообщение о недостаточных данных"):
            assert response.status_code == 400
            assert "Недостаточно данных" in response.json().get("message", "")
