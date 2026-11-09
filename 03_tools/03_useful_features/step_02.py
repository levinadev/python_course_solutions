r"""
Урок "Полезные возможности Python", шаг 2
https://stepik.org/lesson/2493471/step/2

Даны две строки. В первой названия фруктов через пробел, во второй их вес (целые числа через пробел,
столько же).
Используя функцию `zip()`, выведите пары в формате `Фрукт: {fruit}, Вес: {weight}`, каждую на
отдельной строке.
🔑 Подсказка
`zip(fruits, weights)` соединяет списки попарно. В цикле `for fruit, weight in zip(fruits, weights)`
пара сразу попадает в две переменные.
"""

fruits = input().split()
weights = input().split()
for fruit, weight in zip(fruits, weights):
    print(f"Фрукт: {fruit}, Вес: {weight}")
