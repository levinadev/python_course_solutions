r"""
Урок "Работа со списками продвинутая", шаг 4
https://stepik.org/lesson/2493456/step/4

В первой строке слова через пробел (без повторов), во второй слово `search`.
Найдите индекс слова `search` в списке. Если слово найдено, выведите `Найдено на позиции {index}`,
иначе выведите `Не найдено`. Используйте цикл с `enumerate()` для поиска.
🔑 Подсказка
До цикла заведите переменную `found = False`. В цикле `for index, word in enumerate(words)` при
совпадении выведите позицию и поставьте `found = True`. Если после цикла слово так и не нашлось,
выведите "Не найдено".
"""

words = input().split()
search = input()
found = False
for index, word in enumerate(words):
    if word == search:
        print(f"Найдено на позиции {index}")
        found = True
        break
if not found:
    print("Не найдено")
