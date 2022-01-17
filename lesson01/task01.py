"""
1.
Задание: Поработайте с переменными, создайте несколько, выведите на экран,
запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.
"""

text_variable = "Spiderman"
integer_variable = 78
float_variable = 27.5
boolean_variable = True
print ("Созданы переменные: ", text_variable, ",", integer_variable, ",", float_variable, ",", boolean_variable)


user_name= str(input("Как вас зовут? "))
user_sername= str(input("Какая у вас фамилия? "))
user_age= int(input("Сколько вам полных лет? "))
user_number= int(input("Введите любое целое число: "))
print ("Здравствуйте, ", user_name, user_sername, ".", "Вам ", user_age, "полных лет.", "И вы выбрали число ", user_number, ".")
