COURIER_TEMPLATE = {
    "login": "ninja",
    "password": "1234",
    "firstName": "saske"
}

ORDER_TEMPLATE = {
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2020-06-06",
    "comment": "Saske, come back to Konoha",
    "color": ["BLACK"]
}

class SuccessCreatedCourierResponse:
    status_code = 201
    body = {"ok": True}

class DuplicatedCourierResponse:
    status_code = 409
    body = {"message": "Этот логин уже используется"}

class CourierWithMissingFieldResponse:
    status_code = 400
    body = {"message": "Недостаточно данных для создания учетной записи"}

class SuccessLoginResponse:
    status_code = 200
    required_key = 'id'

class LoginWithMissingFieldResponse:
    status_code = 400
    body = {"message":  "Недостаточно данных для входа"}

class LoginWithWrongCredsResponse:
    status_code = 404
    body = {"message": "Учетная запись не найдена"}

class SuccessCreatedOrderResponse:
    status_code = 201
    required_key = 'track'

class GetOrdersResponse:
    status_code = 200
    required_key = 'orders'
