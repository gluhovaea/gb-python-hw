"""
1.Задание: Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""

import sys


def salary():
    file, time, money, bonus = sys.argv
    return int(time) * int(money) + int(bonus)


print(f"заработная плата сотрудника = {salary()}")

# C:\Users\Ringo-nout-2\PycharmProjects\gb-python-hw\venv\Scripts\python.exe C:/Users/Ringo-nout-2/PycharmProjects/gb-python-hw/lesson04/task01.py 40 1700 12000
# заработная плата сотрудника = 80000



