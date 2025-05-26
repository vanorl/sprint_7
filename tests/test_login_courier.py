import allure
import pytest
import data
from auth_methods import AuthMethods
from courier_methods import CourierMethods
from generators import generate_courier

class TestCourierAuth:

    @allure.title(f"Курьер может авторизоваться по логину и паролю, успешный ответ содержит {data.SuccessLoginResponse.required_key}")
    def test_login_success(self, created_courier):
        with allure.step("Пытаемся авторизоваться с валидными данными"):
            response = AuthMethods.login_courier(created_courier)

        with allure.step(F"Проверяем код ответа и что авторизация успешна и возвращается {data.SuccessLoginResponse.required_key}"):
            assert response.status_code == data.SuccessLoginResponse.status_code
            assert data.SuccessLoginResponse.required_key in response.json()

    @allure.title("Попытка авторизации без логина или пароля возвращает ошибку")
    @pytest.mark.parametrize("payload", [
        {"password": "1234"},     # нет логина
        {"login": "ninja"}        # нет пароля
    ])
    def test_login_missing_required_fields(self, payload):
        with allure.step("Пытаемся авторизоваться без обязательного поля"):
            response = AuthMethods.login_courier(payload)

        with allure.step("Проверяем, что возвращается ошибка и сообщение о нехватке данных"):
            assert response.status_code == data.LoginWithMissingFieldResponse.status_code
            assert response.json() == data.LoginWithMissingFieldResponse.body

    @allure.title("Авторизация с неправильным паролем возвращает 404")
    def test_login_invalid_password(self, created_courier):
        bad_data = {
            "login": created_courier["login"],
            "password": "wrong_password"
        }

        with allure.step("Пытаемся авторизоваться с неправильным паролем"):
            response = AuthMethods.login_courier(bad_data)

        with allure.step("Проверяем, что возвращается ошибка и сообщение"):
            assert response.status_code == data.LoginWithWrongCredsResponse.status_code
            assert response.json() == data.LoginWithWrongCredsResponse.body

    @allure.title("Авторизация под несуществующим курьером возвращает ошибку") #для уверенности, что курьера точно не существует - сначала его создаем, потом удаляем и пробуем залогиниться под ним
    def test_login_deleted_user(self):
        with allure.step("Создаём курьера и получаем его данные"):
            courier_data = generate_courier()
            CourierMethods.create_courier(courier_data)

        with allure.step("Удаляем курьера"):
            courier_id = AuthMethods.login_courier(courier_data).json().get("id")
            CourierMethods.delete_courier(courier_id)

        with allure.step("Пытаемся авторизоваться после удаления курьера"):
            response = AuthMethods.login_courier(courier_data)

        with allure.step("Проверяем, что возвращается ошибка и сообщение"):
            assert response.status_code == data.LoginWithWrongCredsResponse.status_code
            assert response.json() == data.LoginWithWrongCredsResponse.body
