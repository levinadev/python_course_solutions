r"""
Урок "Словари", шаг 11
https://stepik.org/lesson/2493458/step/11

Дан словарь `settings = {"volume": 50, "brightness": 70}`. На вход подаётся строка, в ней новые
настройки в виде пар `ключ=значение` через пробел (значения в виде целых чисел).
Создайте из них словарь `new_settings` и, используя метод `.update()`, добавьте его пары в
`settings` (совпадающие ключи перезапишутся). Выведите итоговый словарь.
🔑 Подсказка
Каждую пару разбейте по знаку равенства, `pair.split("=")`, значение переведите через `int()`. Затем
вызовите `settings.update(new_settings)` и выведите `settings`.
"""

settings = {"volume": 50, "brightness": 70}
new_settings = {}
for pair in input().split():
    key, value = pair.split("=")
    new_settings[key] = int(value)
settings.update(new_settings)
print(settings)
