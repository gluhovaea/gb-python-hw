"""
3.Задание: Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
"""

month = int(input("1-12 >>> "))

while month not in range(1, 13):
    print("Такого месяца не существует")
    month = int(input("1-12 >>> "))

# dict
year_dict = {"winter": (1, 2, 12),
             "spring": (3, 4, 5),
             "summer": (6, 7, 8),
             "autumn": (9, 10, 11)}

for key in year_dict.keys():
    if month in year_dict[key]:
        print(key)

# list
year_list = ['зима', 'весна', 'лето', 'осень']

year_ind = month // 3 % 4
print(f"Время года: {year_list[year_ind]}")

# В результате получилось:
# 1-12 >>> 13
# Такого месяца не существует
# 1-12 >>> 7
# summer
# Время года: лето
