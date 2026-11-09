r"""
Урок "Списки", шаг 6
https://stepik.org/lesson/2493454/step/6

В первой строке различные слова через пробел (не меньше двух), во второй новое слово.
Создайте из первой строки список `letters`. Вставьте новое слово на позицию 1 с помощью `.insert()`,
затем удалите последнее слово исходной строки с помощью `.remove()`. Выведите итоговый список.
🔑 Подсказка
Последнее слово запомните до вставки, например `last = letters[-1]`. Затем вызовите
`letters.insert(1, new)` и `letters.remove(last)`.
"""

letters = input().split()
new = input()
last = letters[-1]
letters.insert(1, new)
letters.remove(last)
print(letters)
