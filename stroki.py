# #1 1. Свяжите переменную с любой строкой, состоящей не менее чем из 8 символов.
# Извлеките из строки первый символ, затем последний, третий с начала и третий с
# конца. Измерьте длину вашей строки.
print("Task1*****************************")
# str = "My son is Valentin"
# print("1 symbol: ", str[0])
# print("last symbol: ", str[17])
# print("3 from the beginning symbol: ", str[2])
# print("3 from the end symbol: ", str[15])
# print("Length of str: ", len(str))

#2 2. Присвойте произвольную строку длиной 10-15 символов переменной и извлеките из
# нее следующие срезы:
# ● первые восемь символов
# ● четыре символа из центра строки
# ● символы с индексами кратными трем
# ● переверните строку
print("Task2*****************************")
str = "My son is Valentin"
print("first 8 symbols:", str[0:8])
print("symbols deleted by 3:", str[3::3])
print("centre of str:", str[7:11])
print("reversed str:", str[::-1])

#3 Есть строка: “my name is name”. Напечатайте ее, но вместо 2ого “name” вставьте ваше имя.
print("Task3*****************************")
str = "my name is name"
my_name = "Liana"
print(str[:10], my_name )

#4 4. Есть строка: test_tring = "Hello world!", необходимо
# ● напечатать на каком месте находится буква w
# ● кол-во букв l
# ● Проверить начинается ли строка с подстроки: “Hello”
# ● Проверить заканчивается ли строка подстрокой: “qwe”
print("Task4*****************************")
test_string = "Hello world!"
print("Letter 'w' has index: ", test_string.index("w"))
count_of_l = test_string.count("l")
print("Count of 'l':", count_of_l)
start_with = test_string.startswith("Hello")
print("test_string starts with 'Hello':", start_with)
end_with = test_string.endswith("qwe")
print("test_string ends with 'qwe':", end_with)
