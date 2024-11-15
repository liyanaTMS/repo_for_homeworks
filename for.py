# 1. Даны два целых числа A и B (A < B). Найти сумму всех целых чисел от A до B
# включительно.
print("Task1*****************************")
a = 3
b = 9
sum = 0
for i in range(a,b):
    sum = sum + i
sum_with_b = sum + b
print("Summa chisel:", sum_with_b)


# 2. Найти сумму всех натуральных чисел в от A до B
print("Task2*****************************")
a = 1
b = 99
sum = 0
for i in range(a,b):
    sum = sum + i
sum_with_b = sum + b
print("Summa chisel:", sum_with_b)



# 3. Найти произведение положительных, сумму и количество отрицательных
# из 10 введенных целых значений.
print("Task3*****************************")
# print("Enter 10 numbers (positive or negative) using 'enter' button:")
# list_values = [ int(input()) for i in range(1,11) ]
# print(list_values)
# umnoz = 1
# sum = 0
# count = 0
# for i in list_values:
#     if i > 0:
#         umnoz = umnoz * i
#     else:
#         sum = sum + i
#         count = count + 1
# print("Proizvedenie: ", umnoz)
# print("Sum: ", sum)
# print("Count:  ", count)



# 4. Дан словарь пловцов с их результатами. Напечатать лучший результат
# заплыва среди 6 участников.
# Бекиш Александр - 21,07
# Будник Алексей - 20,34
# Гребень Анастасия - 22,12
# Давидович Татьяна - 30
# Дешук Дмитрий - 24.01
# Казак Анна - 28,17
print("Task4*****************************")
swimmers = {"Бекиш Александр" : "21,07",
"Бекиш Александр" : "21,07",
"Гребень Анастасия" : "22,12",
"Давидович Татьяна" : "30",
"Дешук Дмитрий" : "24.01",
"Казак Анна" : "28,17",
"Будник Алексей" : "20,34"
}
min_swimmer = min(swimmers)
print("The best swimming result is: ", swimmers[min_swimmer])