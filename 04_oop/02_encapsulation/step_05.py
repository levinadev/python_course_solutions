r"""
Урок "Инкапсуляция", шаг 5
https://stepik.org/lesson/2493478/step/5

Создайте класс `User` с приватным атрибутом `__name`. Конструктор принимает имя. Добавьте геттер
`@property` для доступа к имени.
Считайте имя, создайте объект и выведите имя через геттер.
🔑 Подсказка
Геттер это метод с декоратором `@property`, который возвращает `self.__name`. Назовите его `name`,
тогда имя читается как обычный атрибут, `user.name`.
"""

class User:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name


user = User(input())
print(user.name)
