r"""
Урок "Инкапсуляция", шаг 7
https://stepik.org/lesson/2493478/step/7

Создайте класс `Book` с публичным атрибутом `title` (название), приватным атрибутом `__author`
(автор), конструктором, принимающим оба значения, и геттером для `__author`.
Считайте название и автора (каждое с новой строки), создайте объект и выведите название и автора
(через геттер) на отдельных строках.
🔑 Подсказка
Публичный атрибут сохраните как `self.title`, а приватный как `self.__author`. Геттер `author` с
`@property` возвращает `self.__author`.
"""

class Book:
    def __init__(self, title, author):
        self.title = title
        self.__author = author

    @property
    def author(self):
        return self.__author


book = Book(input(), input())
print(book.title)
print(book.author)
