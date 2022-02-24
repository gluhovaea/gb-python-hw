"""
7.Задание: Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку
методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа)
и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.
"""


class ComplexNumber:
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b
        self.x = 'a + b * i'

    def __add__(self, other):
        print(f'Сумма x1 и x2 равна')
        return f'x = {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        print(f'Произведение x1 и x2 равно')
        return f'x = {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i'

    def __str__(self):
        return f'x = {self.a} + {self.b} * i'


x_1 = ComplexNumber(1, -2)
x_2 = ComplexNumber(3, 4)
print(x_1)
print(x_1 + x_2)
print(x_1 * x_2)

# результате получилось:
# x = 1 + -2 * i
# Сумма x1 и x2 равна
# x = 4 + 2 * i
# Произведение x1 и x2 равно
# x = 11 + -6 * i

