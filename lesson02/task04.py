"""
4.Задание: Пользователь вводит строку из нескольких слов, разделённых пробелами.
Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
Если слово длинное, выводить только первые 10 букв в слове.
"""

user_word = input("Введите несколько слов через пробел >>> ").split(" ")

for ind, value in enumerate(user_word):
    print(f"{ind+1} >>> {value[:10]}")

# В результате получилось:
# Введите несколько слов через пробел >>> hello world !!! 123456789123456789 qwerty
# 1 >>> hello
# 2 >>> world
# 3 >>> !!!
# 4 >>> 1234567891
# 5 >>> qwerty





