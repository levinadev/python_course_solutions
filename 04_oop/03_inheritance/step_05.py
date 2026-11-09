r"""
Урок "Наследование", шаг 5
https://stepik.org/lesson/2493479/step/5

Создайте класс `Employee` с конструктором, принимающим имя (`name`). Создайте класс `Developer`,
который наследует от `Employee`, в конструкторе принимает имя и язык программирования (`language`),
вызывает конструктор родителя через `super().__init__(name)` и сохраняет язык в атрибут
`self.language`.
Считайте имя и язык (каждое с новой строки), создайте объект `Developer` и выведите имя и язык через
пробел.
🔑 Подсказка
В `__init__` класса `Developer` первой строкой вызовите `super().__init__(name)`, затем сохраните
`self.language`. Имя и язык выведите одним `print()` через запятую, он сам поставит между ними
пробел.
"""

class Employee:
    def __init__(self, name):
        self.name = name


class Developer(Employee):
    def __init__(self, name, language):
        super().__init__(name)
        self.language = language


dev = Developer(input(), input())
print(dev.name, dev.language)
