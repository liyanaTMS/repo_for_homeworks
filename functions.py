def peremennie(*args, **kwargs):
    """
    1. Переменной var_int присвойте значение 10, var_float - значение 8.4, var_str - "No".
    2. Измените значение, хранимое в переменной var_int, увеличив его в 3.5 раза,
    результат свяжите с переменной big_int.
    3. Измените значение, хранимое в переменной var_float, уменьшив его на единицу,
    результат свяжите с той же переменной.
    4. Разделите var_int на var_float, а затем big_int на var_float. Результат данных
    выражений не привязывайте ни к каким переменным.
    5. Измените значение переменной var_str на "NoNoYesYesYes". При формировании
    нового значения используйте операции конкатенации (+) и повторения строки (*).
    6. Выведите значения всех переменных.
    """
    var_int = 10
    var_float = 8.4
    var_str = "No"
    big_int = var_int * 3.5
    var_float = var_float - 1
    var_str_yes = "Yes"
    var_str_changed = var_str*2 + var_str_yes*3

    return var_int, var_float, var_str,  var_str_changed, big_int, var_int/var_float, big_int/var_float

result = peremennie()
print(result)


def cycle_while(s1, s2):
    """
    2. Поле засеяли цветами двух сортов на площади S1 и S2. Каждый год
    площадь цветов первого сорта увеличивается вдвое, а площадь второго сорта
    увеличивается втрое. Через сколько лет площадь первых сортов будет
    составлять меньше 10% от площади вторых сортов.
    """
    s1 = 13
    s2 = 22
    year = 0
    while s1 >= 0.1 * s2:
        year += 1
        s1 = s1 * 2
        s2 = s2 * 3
    return year

result = cycle_while(13, 22)
print("Year: ", result)


def types_5_task(*args, **kwargs):
    """
    Есть 2 словаря
    a = { 'a': 1, 'b': 2, 'c': 3}
    b = { 'c': 3, 'd': 4,'e': 5}
    Необходимо их объединить по ключам, а значения ключей поместить в список, если у
    одного словаря есть ключ "а", а у другого нету, то поставить значение None на
    соответствующую позицию(1-я позиция для 1-ого словаря, вторая для 2-ого)
    ab = {'a': [1, None], 'b': [2, None], 'c': [3, 3], 'd': [None, 4], 'e': [None, 5]}
    """
    a = { 'a': 1, 'b': 2, 'c': 3}
    b = { 'c': 3, 'd': 4,'e': 5}
    key_list = []
    for key in a:
        key_list.append(key)
    for key in b:
        key_list.append(key)
    key_list_set = set(key_list)
    result_massive = {}
    for i in key_list_set:
        result_massive[i] = [a.get(i), b.get(i)]
    return result_massive

result = types_5_task()
print("Result: ", result)


def usloviya_2_task(*args):
    """
    2. Даны три целых числа. Найти количество положительных чисел в исходном наборе.
    """
    count = 0
    for arg in args:
        if arg > 0:
            count = count + 1
    return count

result = usloviya_2_task(1, 44, -12)
print("The number of positive numbers is: ", result)


def cycle_for(*args):
    """
    2. Найти сумму всех натуральных чисел в от A до B
    """
    sum = 0
    for i in range(args[0], args[1]):
        sum = sum + i
    sum_with_b = sum + args[1]
    return sum_with_b

result = cycle_for(1,99)
print("Summa chisel:", result)

















