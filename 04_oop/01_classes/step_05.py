r"""
Урок "Классы: конструктор, атрибуты и методы", шаг 5
https://stepik.org/lesson/2493476/step/5

Создайте класс `Car`, который в конструкторе принимает марку (`brand`) и модель (`model`) и имеет
метод `info()`, выводящий строку `Машина: {brand} {model}`.
Считайте марку и модель (каждое с новой строки), создайте объект `Car` и вызовите метод `info()`.
🔑 Подсказка
Конструктор сохраняет марку и модель в `self.brand` и `self.model`, а `info()` выводит их f-строкой
через пробел.
"""

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def info(self):
        print(f"Машина: {self.brand} {self.model}")


car = Car(input(), input())
car.info()
