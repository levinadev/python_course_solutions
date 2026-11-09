r"""
Урок "Магические методы", шаг 2
https://stepik.org/lesson/2503553/step/2

Создайте класс `Product` с конструктором, принимающим название (`name`) и цену (`price`), и методом
`__str__`, который возвращает строку `Товар: {name}, Цена: {price} руб.`
Считайте название и цену (целое число), каждое с новой строки. Создайте объект и выведите его через
`print()`.
🔑 Подсказка
`__str__` возвращает строку через `return`, а `print(product)` вызывает его сам. Цену переведите
через `int()`.
"""

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"Товар: {self.name}, Цена: {self.price} руб."


print(Product(input(), int(input())))
