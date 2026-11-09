r"""
Урок "Магические методы", шаг 4
https://stepik.org/lesson/2503553/step/4

Создайте класс `Product` с конструктором, принимающим название (`name`) и цену (`price`), и методом
`__add__`, который складывает цены двух товаров и возвращает сумму.
Даны две строки вида `название цена` (название из одного слова, цена целым числом). Создайте два
товара и выведите результат сложения `product1 + product2`.
🔑 Подсказка
`__add__(self, other)` возвращает сумму `self.price + other.price`. Каждую строку ввода разбейте
через `.split()`, цену переведите через `int()`.
"""

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __add__(self, other):
        return self.price + other.price


name1, price1 = input().split()
name2, price2 = input().split()
print(Product(name1, int(price1)) + Product(name2, int(price2)))
