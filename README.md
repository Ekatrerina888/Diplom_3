# Diplom_3

UI-автотесты для веб-приложения Stellar Burgers.

## Проверяемая функциональность

### Основная функциональность

- переход по клику на «Конструктор»;
- переход по клику на «Лента заказов»;
- открытие всплывающего окна с деталями ингредиента;
- закрытие всплывающего окна по клику на крестик;
- увеличение счётчика ингредиента после добавления в заказ.

### Раздел «Лента заказов»

- увеличение счётчика «Выполнено за всё время» после создания заказа;
- увеличение счётчика «Выполнено за сегодня» после создания заказа;
- появление номера созданного заказа в разделе «В работе».

## Технологии

- Python
- Pytest
- Selenium
- Requests
- Allure
- Page Object Model

## Установка зависимостей

pip install -r requirements.txt

## Запуск тестов в Google Chrome

pytest --browser chrome

## Запуск тестов в Mozilla Firefox

pytest --browser firefox

## Запуск тестов c Allure

pytest --browser chrome --alluredir=allure_results
pytest --browser firefox --alluredir=allure_results