r"""
Урок "Списки", шаг 4
https://stepik.org/lesson/2493454/step/4

В первой строке целые числа через пробел, во второй число `x`.
Создайте из первой строки список `numbers`, добавьте в него `x` с помощью метода `.append()`,
выведите получившийся список, а затем его длину.
Список чисел можно получить строкой `numbers = [int(x) for x in input().split()]`
🔑 Подсказка
Число x тоже переведите через `int()`, иначе в список попадёт строка. После `numbers.append(x)`
выведите список, а затем `len(numbers)`.
"""

numbers = [int(x) for x in input().split()]
x = int(input())
numbers.append(x)
print(numbers)
print(len(numbers))
