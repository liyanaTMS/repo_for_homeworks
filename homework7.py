#1 Создать лямда функцию, которая принимает на вход имя и выводит его в формате Hello, {name
print('Enter your name:')
lambda1 = lambda name: print(f"Hello, {name}")
lambda1(name = input())
# second variant
(lambda name: print(f"Hello, {name}"))("Liana")


#2 Создать лямда функцию, которая принимает на вход список имен и выводит их в формате "Hello, {name}", в другой список
spisok1 = ["Lera", "Vasya", "Alina", "Olya"]
i = 0
spisok2 = []
for el in spisok1:
    lambda1 = lambda s: spisok2.append("Hello, " + s[i])
    lambda1(s=spisok1)
    i+=1
print("Spisok1: ", spisok1)
print("Spisok2: ", spisok2)


# 3 Напишите генератор который принимает список numbers = [34.6, -230.4, 44.9, 68.3, -12.2, 44.6, 12.7] и возвращает новый список только с положительными числами
def create_generator(list):
    positive_numbers = []
    for el in list:
        if el >= 0:
            positive_numbers.append(el)
    yield positive_numbers
numbers = [34.6, -230.4, 44.9, 68.3, -12.2, 44.6, 12.7]
my_generator = create_generator(numbers)
print(my_generator)
for i in my_generator:
    print (i)



#4 Необходимо составить список чисел которые указывают на длину слов в строке sentence = "thequick brown box jumps over the lazy dog", но только сли слово не "the" с обработкой исключений
sentence = "thequick brown box jumps over the lazy dog"
sentence_split = sentence.split()
numbers_list = []

for word in sentence_split:
    try:
        if word == "the":
            raise
        numbers_list.append(len(word))
    except:
        print(" 'the' was found")

print(numbers_list)




