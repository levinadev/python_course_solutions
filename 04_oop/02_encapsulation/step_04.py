r"""
Урок "Инкапсуляция", шаг 4
https://stepik.org/lesson/2493478/step/4

Создайте класс `User` с приватным атрибутом `__password`. Конструктор принимает пароль и сохраняет
его в приватный атрибут.
Создайте объект `User("12345")` и попытайтесь вывести `user.__password`. Перехватите ошибку
`AttributeError` с помощью `try-except` и выведите `Нет доступа к паролю`.
🔑 Подсказка
Обращение к `user.__password` снаружи класса вызывает `AttributeError`. Поместите
`print(user.__password)` в `try`, а сообщение выведите в `except AttributeError`.
"""

class User:
    def __init__(self, password):
        self.__password = password


user = User("12345")
try:
    print(user.__password)
except AttributeError:
    print("Нет доступа к паролю")
