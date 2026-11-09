r"""
Урок "Наследование", шаг 2
https://stepik.org/lesson/2493479/step/2

Создайте класс `Person` с конструктором, принимающим имя (`name`), и методом `introduce()`, который
выводит `Меня зовут {name}`.
Создайте класс `Student`, который наследует от `Person` и ничего не переопределяет. Считайте имя,
создайте объект `Student` и вызовите метод `introduce()`.
🔑 Подсказка
Родительский класс пишется в скобках после имени, `class Student(Person):`. Тело класса не может
быть пустым, поставьте в него `pass`.
"""

class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"Меня зовут {self.name}")


class Student(Person):
    pass


Student(input()).introduce()
