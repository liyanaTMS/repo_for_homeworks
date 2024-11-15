# 1. Дано целое число. Если оно является положительным, то прибавить к нему 1; в
# противном случае не изменять его. Вывести полученное число.
print("Task1*****************************")
num = 15
if num > 0:
    num = num + 1
print(num)




# 2. Даны три целых числа. Найти количество положительных чисел в исходном наборе.
print("Task2*****************************")
numbers = [1, 44, -12]
count = 0
for num in numbers:
    if num > 0:
        count = count + 1
print("The number of positive numbers is: ", count)



# 3. Дан номер года (положительное целое число). Определить количество дней в
# этом году, учитывая, что обычный год насчитывает 365 дней, а високосный — 366
# дней. Високосным считается год, делящийся на 4, за исключением тех годов, которые
# делятся на 100 и не делятся на 400 (например, годы 300, 1300 и 1900 не являются
# високосными, а 1200 и 2000 являются).
print("Task3*****************************")
year = 1988
if (year % 4 == 0):
    if (year % 100 == 0):
        if (year % 400> 0):
            print("Year is not visokosniy. Number of days is: ", 365)
        else:
            print("Year is visokosniy. Number of days is: ", 366)
    else:
        print("Year is not visokosniy. Number of days is: ", 365)
else:
    print("Year is not visokosniy. Number of days is: ", 365)

# 4. Дано целое число в диапазоне 1–7. Вывести строку — название дня недели,
# соответствующее данному числу (1 — «понедельник», 2 — «втор- ник» и т. д.).
print("Task4*****************************")
number = 6
days = {1: "monday",
        2: "tuesday",
        3: "wednesday",
        4: "thursday",
        5: "friday",
        6: "saturday",
        7: "sunday"}
if number in days.keys():
    print(number, "-",  days[number])

# 5. Единицы массы пронумерованы следующим образом: 1 — килограмм, 2 —
# миллиграмм, 3 — грамм, 4 — тонна, 5 — центнер. Дан номер едини- цы массы (целое
# число в диапазоне 1–5) и масса тела в этих единицах (вещественное число). Найти
# массу тела в килограммах.
print("Task5*****************************")
edinicy = {
        1: "kg",
        2: "miligramm",
        3: "gramm",
        4: "tonna",
        5: "centner"
}
perevod = {
        1: 1,
        2: 0.000001,
        3: 0.001,
        4: 1000,
        5: 100
}
number = 3
weight = 2
if number in edinicy.keys():
    print(weight, edinicy[number], "=",  weight*perevod[number], 'kg')
