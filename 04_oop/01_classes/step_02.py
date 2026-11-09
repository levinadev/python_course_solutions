r"""
Урок "Классы: конструктор, атрибуты и методы", шаг 2
https://stepik.org/lesson/2493476/step/2

Создайте класс `User`, который в конструкторе принимает имя (`name`) и возраст (`age`) и имеет метод
`info()`, выводящий строку `Имя: {name}, Возраст: {age}`.
Считайте имя и возраст (каждое с новой строки), создайте объект `User` и вызовите метод `info()`.
🔑 Подсказка
В `__init__` сохраните параметры в атрибуты `self.name` и `self.age`. Метод `info(self)` берёт их
через `self` и выводит f-строкой.
"""

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"Имя: {self.name}, Возраст: {self.age}")


user = User(input(), int(input()))
user.info()
