#1 Написать обычную функцию для факториала, генератор и рекурсию.
import time

print("First task:")
def factorial(n):
    if n == 0:
        return 1
    else:
         return n * factorial(n-1)

start_time = time.perf_counter()
print("Start time = ", start_time)

result = factorial(5)

end_time = time.perf_counter()
print("End time = ", end_time)
function_time = end_time - start_time
print("Function time is: ", function_time)
print(result)


def time_decorator(func):

    def wrapper(*args, **kwargs):
        print("----------------------------------------------------------")
        start_time = time.perf_counter()
        print("Start time = ", start_time)
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        print("End time = ", end_time)
        function_time = end_time - start_time
        print("Function time is: ", function_time)
        return result
    return wrapper


@time_decorator
def just_function(n):
    buffer = 1
    for el in range(2, n+1):
        buffer = buffer*el
    return buffer

print(just_function(5))


@time_decorator
def create_generator(n):
    buffer = 1
    for el in range(2, n+1):
        buffer = buffer*el
    yield buffer

my_generator = create_generator(5)

print(my_generator)
for i in my_generator:
    print(i)


# 2 Напишите декоратор, который проверял бы тип параметров функции, конвертировал их если надо и складывал
print("Second task:")
def typed(type):
    def actual_decorator(func):
        def wrapper(*args, **kwargs):
            new_args = []
            if type == "str":
                check_type = str
            elif type == "int":
                check_type = int
            elif type == "float":
                check_type = float

            for arg in args:
                if isinstance(arg, check_type):
                    new_args.append(arg)
                else:
                    new_args.append(check_type(arg))

            return func(*new_args, **kwargs)
        return wrapper
    return actual_decorator

@typed(type='str')
def add_two_symbols(a, b):
    return a + b
print(add_two_symbols("3", 5))
print("-------------------------------------------")
print(add_two_symbols(5, 5))
print("-------------------------------------------")
print(add_two_symbols('a', 'b'))

@typed(type='int')
def add_three_symbols(a, b, c):
    return a + b + c
print("-------------------------------------------")
print(add_three_symbols(5, 6, 7))
print("-------------------------------------------")
print(add_three_symbols("3", 5, 0))


@typed(type='float')
def add_three_symbols(a, b, c):
    return a + b + c
print("-------------------------------------------")
print(add_three_symbols(0.1, 0.2, 0.4))


#3 На вход подается некоторое количество разделенных пробелом целых чисел(каждое не меньше нуля и не больше 19).
# Выведите их через пробел в порядке лексикографического возрастания на английском
print("Third task:")
number_names = {
                0: 'zero',
                1: 'one',
                2: 'two',
                3: 'three',
                4: 'four',
                5: 'five',
                6: 'six',
                7: 'seven',
                8: 'eight',
                9: 'nine',
                10: 'ten',
                11: 'eleven',
                12: 'twelve',
                13: 'thirteen',
                14: 'fourteen',
                15: 'fifteen',
                16: 'sixteen',
                17: 'seventeen',
                18: 'eighteen',
                19: 'nineteen',
                }
date = "5 8 9 10 11 7 6 9 1 3 15 19 2 3 4 8 0 9 1 3 16 14 12 18 2 11 0 9 8 18"
date_split = date.split()
new_date_split = []
for el in date_split:
    new_date_split.append(int(el))
new_date_sorted = sorted(new_date_split, key = lambda x: number_names[x] )
new_date_sorted_str = []
for el in new_date_sorted:
    new_date_sorted_str.append(str(el))
print(" ".join(new_date_sorted_str))



