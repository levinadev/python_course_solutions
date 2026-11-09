r"""
Урок "Полиморфизм", шаг 3
https://stepik.org/lesson/2493480/step/3

Создайте класс `Car` с конструктором, принимающим марку (`brand`), и методом `info()`, который
выводит `Машина: {brand}`. Создайте класс `Bicycle` с таким же конструктором и методом `info()`,
который выводит `Велосипед: {brand}`.
В первой строке количество транспортных средств `n`, далее `n` строк вида `car Toyota` или `bicycle
Giant`. Создайте список `vehicles` и в цикле вызовите метод `info()` для каждого объекта.
🔑 Подсказка
Разберите каждую строку через `.split()` и по первому слову выберите класс, `Car` или `Bicycle`.
Потом в цикле по списку вызовите `info()`, у каждого объекта он свой.
"""

class Car:
    def __init__(self, brand):
        self.brand = brand

    def info(self):
        print(f"Машина: {self.brand}")


class Bicycle:
    def __init__(self, brand):
        self.brand = brand

    def info(self):
        print(f"Велосипед: {self.brand}")


vehicles = []
for _ in range(int(input())):
    kind, brand = input().split()
    if kind == "car":
        vehicles.append(Car(brand))
    else:
        vehicles.append(Bicycle(brand))
for v in vehicles:
    v.info()
