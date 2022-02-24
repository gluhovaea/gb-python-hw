"""
2.Задание: Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать
эту ситуацию и не завершиться с ошибкой.
"""


class DivisionZeroError(Exception):
    pass


def get_numerator() -> int:
    return int(input("Введите числитель >>> "))


def get_denominator() -> int:
    value = int(input("Введите знаменатель >>> "))

    if value == 0:
        raise DivisionZeroError

    return value


while True:
    try:
        numerator = get_numerator()
        denominator = get_denominator()

        print(f"Результат = {numerator / denominator}")
    except DivisionZeroError:
        print("Нуль не может быть в качестве делителя!")
    except KeyboardInterrupt:
        break


#  результате получилось:
# Введите числитель >>> 10
# Введите знаменатель >>> 2
# Результат = 5.0
# Введите числитель >>> 10
# Введите знаменатель >>> 0
# Нуль не может быть в качестве делителя!
# Введите числитель >>>
