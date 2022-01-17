"""
3.Задание: Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
"""

user_number = input("Введите целое число >>> ")

if not user_number.isdigit():  # проверка на то, что введенное значение - целое число
    print("Вы ввели неверный формат числа.")
    exit()

# Вариант 1 через диапазон
result = 0
for x in range(1, 4):
    result += int(user_number * x)

print(result)

# Вариант 2
summa = int(user_number) + int(user_number*2) + int(user_number*3)
print(f"{user_number}+{user_number*2}+{user_number*3} = {summa} ")
