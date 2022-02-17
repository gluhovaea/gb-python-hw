"""
4.Задание: Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).

Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Вызовите методы и покажите результат.
"""

class Car:
    speed: int
    color: str
    name: str
    is_police = bool

    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"{self.name} {self.color}: Машина поехала")

    def stop(self):
        print(f"{self.name} {self.color}: Машина остановилась")

    def turn(self, direction):
        print(f"{self.name} {self.color}: Машина повернула ", direction)

    def show_speed(self):
        print(f"{self.name} {self.color}: Текущая скорость атомобиля: ", self.speed)


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f"{self.name} {self.color}: Для TownCar превышение скорости")
        else:
            print(f"{self.name} {self.color}: Для TownCar скорость в пределах нормы")


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f"{self.name} {self.color}: Для WorkCar превышение скорости")
        else:
            print(f"{self.name} {self.color}: Для WorkCar скорость в пределах нормы")


class PoliceCar(Car):
    def __init__(self, color, name, is_police):
        self.is_police = is_police
        super().__init__(color, name, float('inf'), True)


my_car = Car(55, "white", "Kia")
print(my_car.go(), my_car.stop(), my_car.turn("направо"), my_car.show_speed())
my_town_car = TownCar(52, "black", "Ford")
my_town_car.show_speed()
my_work_car = WorkCar(60, "green", "Honda")
my_work_car.show_speed()


# В результате получилось:
# Kia white: Машина поехала
# Kia white: Машина остановилась
# Kia white: Машина повернула  направо
# Kia white: Текущая скорость атомобиля:  55
# None None None None
# Ford black: Для TownCar скорость в пределах нормы
# Honda green: Для WorkCar превышение скорости
