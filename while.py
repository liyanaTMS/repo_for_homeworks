# 1. Дано число N. Найти произведение всех чисел от 0 до N.
print("1task-------------------------")
n = 15
proizvedenie = 1
while n > 0:
    proizvedenie = proizvedenie * n
    n = n -1
print("The result: ")
print(proizvedenie)

# 2. Поле засеяли цветами двух сортов на площади S1 и S2. Каждый год
# площадь цветов первого сорта увеличивается вдвое, а площадь второго сорта
# увеличивается втрое. Через сколько лет площадь первых сортов будет
# составлять меньше 10% от площади вторых сортов.
print("2task-------------------------")
s1 = 13
s2 = 22
year = 0
while s1 >= 0.1 * s2:
    year += 1
    s1 = s1 * 2
    s2 = s2 * 3
print("Year: ", year)

# 3. Дано целое число N (>0). Используя операции деления нацело и взятия
# остатка от деления, найти количество и сумму его цифр.
print("3task-------------------------")
n = 1234
count = 0
summ = 0
while n:
    a = n % 10
    count += 1
    summ = summ + a
    b = n // 10
    n = b
print("Numbers: ", count)
print("Summ: ", summ)

# 4. Деду M лет, а внуку N лет. Через сколько лет дед станет вдвое старше
# внука. И сколько при этом лет будет деду и внуку
print("4task-------------------------")
m = 40
n = 13
year = 0
while m != 2*n:
    year += 1
    m = m + 1
    n = n + 1
print(f"In {year} years Grandpa will have twice grandson's age")
print(f"Grandpa will be {m} years old")
print(f"Grandson will be {n} years old")