# 1. Присвойте двум переменным любые числовые значения.
# 2. Составьте четыре сложных логических выражения с помощью оператора and, два из
# которых должны давать истину, а два других - ложь.
# 3. Аналогично выполните п. 2, но уже используя оператор or.
# 4. Попробуйте использовать в сложных логических выражениях работу с переменными
# строкового типа.
area = 99
house = 44
flat = 80
street = "Filimonova"
name = "Ivan"
# AND:
print((area <= 100 and house <= 45) and area == 99)
print((house == 44 and area < 100) and area != 98)
print((area <= 100 and house <= 45) and (house == 40))
print((area <= 50 and house >= 45) and (house == 40))
# OR:
print((area < 100 or house > 45) or area == 99)
print((house <= 44 or area == 100) or area != 99)
print((area > 100 or house == 45) or (area == 140))
print((area <= 50 or house >= 45) or (house == 40))
# STRING
print((name == "Ivan" or street == "Esenina") or name != "Kolya")
print((name != "Ivan" or street == "Esenina") or name == "Kolya")
print((name == "Ivan" and street == "Esenina") and name != "Kolya")
print((name == "Ivan" and street != "Esenina") and name != "Kolya")
