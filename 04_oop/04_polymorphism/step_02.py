r"""
Урок "Полиморфизм", шаг 2
https://stepik.org/lesson/2493480/step/2

Создайте класс `Square` с конструктором, принимающим сторону (`side`), и методом `area()`, который
возвращает `side * side`. Создайте класс `Triangle` с конструктором, принимающим основание (`base`)
и высоту (`height`), и методом `area()`, который возвращает `base * height / 2`.
В первой строке количество фигур `n`, далее `n` строк вида `square 4` или `triangle 6 3`. Создайте
список фигур `figures`, затем в цикле вызовите метод `area()` для каждого объекта и выведите
результат на отдельной строке.
🔑 Подсказка
Каждую строку разбейте через `.split()`. Если первое слово `"square"`, создайте `Square` из второго
числа, иначе `Triangle` из второго и третьего. Числа переведите через `int()`, а объекты добавляйте
в список через `append()`.
"""

class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side


class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height / 2


figures = []
for _ in range(int(input())):
    parts = input().split()
    if parts[0] == "square":
        figures.append(Square(int(parts[1])))
    else:
        figures.append(Triangle(int(parts[1]), int(parts[2])))
for figure in figures:
    print(figure.area())
