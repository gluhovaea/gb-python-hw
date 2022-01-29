"""
2.Задание: Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""

# Вариант 1

def user_info(first_name: str = None,
         last_name: str = None,
         year: int = None,
         city: str = None,
         phone: str = None,
         email: str = None):
    return f"{first_name} {last_name} ({year}), {city}, {phone}, {email}"


user_first_name = input("Имя >>> ")
user_last_name = input("Фамилия >>> ")
user_year = int(input("Год рождения >>> "))
user_city = input("Город >>> ")
user_email = input("Email >>> ")
user_phone = input("Номер телефона >>> ")

print(
    user_info(first_name=user_first_name, last_name=user_last_name,
         year=user_year, city=user_city, email=user_email,
         phone=user_phone)
)


# Вариант 2

def about_user(**kwargs):
    return f"{kwargs['first_name']} {kwargs['last_name']} ({kwargs['year']}), {kwargs['city']}, {kwargs['email']}, {kwargs['phone']}"


user_first_name = input("Имя >>> ")
user_last_name = input("Фамилия >>> ")
user_year = int(input("Год рождения >>> "))
user_city = input("Город >>> ")
user_email = input("Email >>> ")
user_phone = input("Номер телефона >>> ")

print(
    about_user(first_name=user_first_name, last_name=user_last_name,
         year=user_year, city=user_city, email=user_email,
         phone=user_phone)
)


# Пример того, что получилось в результате:
# Имя >>> Ivan
# Фамилия >>> Ivanov
# Год рождения >>> 1983
# Город >>> Moscow
# Email >>> Ivanchik@mail
# Номер телефона >>> 89111001010
# Ivan Ivanov (1983), Moscow, 89111001010, Ivanchik@mail
# Имя >>> Sveta
# Фамилия >>> Petrova
# Год рождения >>> 1985
# Город >>> Petersburg
# Email >>> SvetkaPP@mail
# Номер телефона >>> 89111101112
# Sveta Petrova (1985), Petersburg, SvetkaPP@mail, 89111101112






