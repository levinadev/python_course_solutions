r"""
Урок "Классы: конструктор, атрибуты и методы", шаг 3
https://stepik.org/lesson/2493476/step/3

Создайте класс `User` с конструктором, принимающим имя и возраст, и методом `have_birthday()`,
который увеличивает возраст на 1.
Считайте имя, возраст и число `n` (каждое с новой строки). Создайте объект, вызовите метод
`have_birthday()` `n` раз и выведите возраст.
🔑 Подсказка
Внутри `have_birthday` увеличьте `self.age` на 1. Возраст переведите через `int()`, а метод вызовите
в цикле `for i in range(n)`. После цикла выведите `user.age`.
"""

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def have_birthday(self):
        self.age += 1


user = User(input(), int(input()))
for _ in range(int(input())):
    user.have_birthday()
print(user.age)
