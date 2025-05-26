import pytest
import allure
import data
from generators import generate_courier
from courier_methods import CourierMethods


class TestCourierCreate:

    @allure.title("Курьера можно создать при передаче валидных данных")
    def test_create_courier_success(self, cleanup_courier):
        with allure.step("Генерируем данные курьера"):
            courier_data = generate_courier()

        with allure.step("Отправляем запрос на создание курьера"):
            response = CourierMethods.create_courier(courier_data)

        cleanup_courier["courier_data"] = courier_data #после выполнения теста в фикстуру cleanup_courier передатутся данные о курьере для его удаления после теста

        with allure.step("Проверяем код ответа и что курьер успешно создан"):
            assert response.status_code == data.SuccessCreatedCourierResponse.status_code
            assert response.json() == data.SuccessCreatedCourierResponse.body


    @allure.title("Нельзя создать двух одинаковых курьеров")
    def test_create_courier_duplicate(self, cleanup_courier):
        with allure.step("Генерируем данные курьера"):
            courier_data = generate_courier()

        with allure.step("Создаём первого курьера"):
            CourierMethods.create_courier(courier_data)

        with allure.step("Пытаемся создать второго курьера с теми же данными"):
            duplicate_response = CourierMethods.create_courier(courier_data)

        cleanup_courier["courier_data"] = courier_data

        with allure.step("Проверяем, что вернулась ошибка и сообщение"):
            assert duplicate_response.status_code == data.DuplicatedCourierResponse.status_code
            assert duplicate_response.json() == data.DuplicatedCourierResponse.body


    @allure.title("Создание курьера с пропущенным полем возвращает ошибку")
    @pytest.mark.parametrize("missing_field", ["login", "password"])
    def test_create_courier_missing_required_fields(self, missing_field):
        with allure.step(f"Генерируем данные курьера и удаляем поле '{missing_field}'"):
            courier_data = generate_courier()
            courier_data.pop(missing_field)

        with allure.step("Пытаемся создать курьера с неполными данными"):
            response = CourierMethods.create_courier(courier_data)

        with allure.step("Проверяем, что вернулась ошибка и сообщение"):
            assert response.status_code == data.CourierWithMissingFieldResponse.status_code
            assert response.json() == data.CourierWithMissingFieldResponse.body
