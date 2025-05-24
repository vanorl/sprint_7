# Автотесты api сайта аренды самокатов

## Что реализовано

- Проверки ручки `"POST /api/v1/courier"` — создание курьера
- Проверки ручки `"POST /api/v1/courier/login"` — логин курьера
- Проверки ручки `"POST /api/v1/orders"` — создание заказа
- Проверка ручки `"GET /api/v1/orders"` — получение списка заказов

## Как запустить проект

1. Клонируйте репозиторий:
   ```bash
   git clone <ссылка_на_репозиторий>
   cd <название_проекта>
2. Создайте и активируйте виртуальное окружение
   ```bash
   python -m venv .venv
   source .venv/Scripts/activate
3. Установите зависимости
   ```bash
   pip install -r requirements.txt
4. Запустите тесты с генерацией отчета allure
   ```bash
   pytest tests/ --alluredir=allure_results
   allure serve allure_results