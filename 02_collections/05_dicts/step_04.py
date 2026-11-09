r"""
Урок "Словари", шаг 4
https://stepik.org/lesson/2493458/step/4

Дан словарь `city = {"name": "Москва", "population": 13000000, "country": "Россия"}`. Считайте имя
мэра и выполните три действия.
- Добавьте ключ `"mayor"` со считанным значением.
- Удалите ключ `"population"` с помощью `del`.
- Выведите итоговый словарь.
🔑 Подсказка
`city["mayor"] = input()` добавляет ключ, `del city["population"]` удаляет его. Потом выведите
словарь целиком.
"""

city = {"name": "Москва", "population": 13000000, "country": "Россия"}
city["mayor"] = input()
del city["population"]
print(city)
