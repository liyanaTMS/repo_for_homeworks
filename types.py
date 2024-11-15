# 1
# Перевести строку в массив
# "Robin Singh" => ["Robin”, “Singh"]
# "I love arrays they are my favorite" => ["I", "love", "arrays", "they", "are", "my", "favorite"
str1 = "Robin Singh"
str2 = "I love arrays they are my favorite"
print(str1.split(None, 2))
print(str2.split(None, -1))

#2
# Дан список: [‘Ivan’, ‘Ivanou’], и 2 строки: Minsk, Belarus
# Напечатайте текст: “Привет, Ivan Ivanou! Добро пожаловать в Minsk Belarus”
spisok = ['Ivan', 'Ivanou']
stroka1 = 'Minsk'
stroka2 = 'Belarus'
print(f"Привет, {spisok[0]} {spisok[0]}! Добро пожаловать в {stroka1} {stroka2}")

#3
# 3. Дан список ["I", "love", "arrays", "they", "are", "my", "favorite"] сделайте из него
# строку => "I love arrays they are my favorite
spisok1 = ["I", "love", "arrays", "they", "are", "my", "favorite"]
print(' '.join(spisok1))

#4
# Создайте список из 10 элементов, вставьте на 3-ю позицию новое значение,
# удалите элемент из списка под индексом 6
spisok2 = ["1a", "love", "4r", "they", 13, "stroka", "favorite", 22, 45, 8888]
spisok2[2] = 'running'
spisok2.pop(6)
print(spisok2)

#5
# Есть 2 словаря
# a = { 'a': 1, 'b': 2, 'c': 3}
# b = { 'c': 3, 'd': 4,'e': 5}
# Необходимо их объединить по ключам, а значения ключей поместить в список, если у
# одного словаря есть ключ "а", а у другого нету, то поставить значение None на
# соответствующую позицию(1-я позиция для 1-ого словаря, вторая для 2-ого)
# ab = {'a': [1, None], 'b': [2, None], 'c': [3, 3], 'd': [None, 4], 'e': [None, 5]}
a = { 'a': 1, 'b': 2, 'c': 3}
b = { 'c': 3, 'd': 4,'e': 5}
key_list = []
for key in a:
    key_list.append(key)
for key in b:
    key_list.append(key)
key_list_set = set(key_list)
result_massive = {}
for val in key_list_set:
    result_massive[val] = [a.get(val), b.get(val)]
print("Result: ", result_massive)

