from faker import Faker
import random


fake = Faker('ru_RU')

def generate_courier():
    return {
        "login": fake.user_name(),
        "password": fake.password(),
        "firstName": fake.first_name()
    }

def generate_order(colors=None):
    return {
        "firstName": fake.first_name(),
        "lastName": fake.last_name(),
        "address": fake.address(),
        "metroStation": str(random.randint(1, 10)),
        "phone": fake.phone_number(),
        "rentTime": random.randint(1, 10),
        "deliveryDate": fake.future_date().isoformat(),
        "comment": fake.sentence(),
        "color": colors
    }