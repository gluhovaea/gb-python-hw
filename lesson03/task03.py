"""
3.Задание: Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""

# Вариант 1

def my_func(first, second, third):
    numbers = [first, second, third]
    numbers.remove(min(numbers))

    return sum(numbers)

a, b, c = int(input("Число a = ")), int(input("Число b = ")), int(input("Число c = "))

print(my_func(a, b, c))


# Вариант 2

my_func_lambda = lambda a, b, c: max(a + b, b + c, c + a)

print(my_func_lambda(10, 5, 60))

# Пример того, что получилось в результате:
# Число a = 2
# Число b = 10
# Число c = 25
# 35
# 70
