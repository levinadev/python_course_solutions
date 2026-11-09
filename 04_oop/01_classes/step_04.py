r"""
Урок "Классы: конструктор, атрибуты и методы", шаг 4
https://stepik.org/lesson/2493476/step/4

Создайте класс `User` с конструктором, принимающим имя, и методом `change_name(new_name)`, который
изменяет имя пользователя.
Считайте исходное и новое имя (каждое с новой строки). Создайте объект с исходным именем, измените
имя на новое и выведите сначала старое имя, а затем новое, каждое на отдельной строке, обращаясь к
атрибуту объекта.
🔑 Подсказка
Метод `change_name` записывает новое имя в `self.name`. Старое имя выведите через `user.name` до
вызова метода, новое после.
"""

class User:
    def __init__(self, name):
        self.name = name

    def change_name(self, new_name):
        self.name = new_name


user = User(input())
print(user.name)
user.change_name(input())
print(user.name)
