r"""
Урок "Словари", шаг 8
https://stepik.org/lesson/2493458/step/8

На вход подаётся строка, в ней пары `ключ=значение` через пробел (ключи не повторяются). Создайте из
них словарь `country` (значения в виде строк).
Используя метод `.items()`, выведите все пары в формате `Ключ: {key}, Значение: {value}` (каждая
пара на отдельной строке).
🔑 Подсказка
Каждую пару разбейте по знаку равенства, `pair.split("=")`, и запишите в словарь. Цикл `for key,
value in country.items()` даёт ключ и значение сразу.
"""

country = {}
for pair in input().split():
    key, value = pair.split("=")
    country[key] = value
for key, value in country.items():
    print(f"Ключ: {key}, Значение: {value}")
