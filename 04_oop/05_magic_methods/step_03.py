r"""
Урок "Магические методы", шаг 3
https://stepik.org/lesson/2503553/step/3

Создайте класс `Product` с конструктором, принимающим название (`name`) и цену (`price`), и методом
`__eq__`, который сравнивает два товара по названию и цене.
Даны две строки вида `название цена` (название из одного слова, цена целым числом). Создайте два
объекта и выведите результат сравнения `product1 == product2`.
🔑 Подсказка
`__eq__(self, other)` возвращает результат сравнения `self.name == other.name and self.price ==
other.price`. Тогда `product1 == product2` вызовет этот метод.
"""

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __eq__(self, other):
        return self.name == other.name and self.price == other.price


name1, price1 = input().split()
name2, price2 = input().split()
product1 = Product(name1, int(price1))
product2 = Product(name2, int(price2))
print(product1 == product2)
