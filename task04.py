"""
4.Задание: Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
"""

user_input = input("Введите целое положительное число >>> ")

if not user_input.isdigit():   # проверка на то, что введенное значение - целое число
    print("Вы ввели неверный формат числа.")
    exit()

# Вариант 1
number = int(user_input)

maximum = number % 10  # выделяем последнюю цифру числа и предполагаем, что она максимальна
number //= 10  # избавились от последней цифры в числе, т.е. если было 123456, то теперь 12345

while number and maximum != 9:
    if number % 10 > maximum:  # если следующая цифра оказывается больше последней цифры, то...
        maximum = number % 10  # ...то записываем её в максимум
    number //= 10
print(f"max = {maximum}")

# Вариант 2
number = int(user_input)
max_num = 0

while number and max_num != 9:
    print(number)
    current = number % 10
    number = number // 10
    max_num = current if current > max_num else max_num

print(max_num)
