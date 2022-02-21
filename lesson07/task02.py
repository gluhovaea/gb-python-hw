"""
2.Задание: Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3).
Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта,
проверить на практике работу декоратора @property.
"""

from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def get_sum_of_cloth(self):
        pass


class Coat(Clothes):
    def __init__(self, size):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if size < 1:
            self.__size = 1
        elif size > 60:
            self.__size = 60
        else:
            self.__size = size

    def get_sum_of_cloth(self):
        return round(self.__size / 6.5 + 0.5, 2)


class Suit(Clothes):
    def __init__(self, height):
        self.height = height

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if height < 1:
            self.__height = 1
        else:
            self.__height = height

    def get_sum_of_cloth(self):
        return 2 * (self.__height / 100) + 0.3


coat = Coat(48)
print(f'Размер пальто: {coat.size}')
print(f'Нужно ткани для пальто: {coat.get_sum_of_cloth()}')
suit = Suit(180)
print(f'Рост для костюма: {suit.height}')
print(f'Нужно ткани для костюма: {suit.get_sum_of_cloth()}')

