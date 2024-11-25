# 1 Дан файл целых чисел, содержащий не менее четырех элементов.
# Вывести первый, второй, предпоследний и последний элементы данного
# файла. Если чисел меньше 3 выводить ошибку
with open("task1.txt", 'r') as f:
    line = f.readline()
    data_list = line.split()
    data_list_int = list(map(int, data_list))
    count = len(data_list_int)

    if count < 3:
        print("Error: number of elements in file < 3")
    else:
        print("The first element: ", data_list_int[0])
        print("The second element: ", data_list_int[1])
        print("The penultimate element: ", data_list_int[-2])
        print("The last element: ", data_list_int[-1])


#2 Дан файл целых чисел. Создать два новых файла, первый из которых
# содержит четные числа из исходного файла, а второй — нечетные (в том
# же порядке). Если четные или нечетные числа в исходном файле
# отсутствуют, то соответствующий результирующий файл оставить
# пустым.
def chet_nechet(stroka):
    print("File: ", stroka)
    data_list = stroka.split()
    data_list_int = list(map(int, data_list))
    massiv_chetnyh = []
    massiv_nechetnyh = []
    for el in data_list_int:
        if el % 2 == 0:
            massiv_chetnyh.append(el)
        else:
            massiv_nechetnyh.append(el)

    massiv_chetnyh_str = list(map(str, massiv_chetnyh))
    massiv_nechetnyh_str = list(map(str, massiv_nechetnyh))
    str_chetnyh = (" ".join(massiv_chetnyh_str))
    print("File chetnyh:", str_chetnyh)
    str_nechetnyh = (" ".join(massiv_nechetnyh_str))
    print("File nechetnyh:", str_nechetnyh)

    return str_chetnyh, str_nechetnyh

with open("task2.txt", 'r') as f:
    line = f.readline()
    chetnye, nechetnye = chet_nechet(line)
with open("task2_result_chetnyh.txt", "w") as f1:
    f1.write(chetnye)
with open("task2_result_nechetnyh.txt", "w") as f2:
    f2.write(nechetnye)


#3 Дан файл вещественных чисел. Заменить в нем все элементы на их квадраты.
def square(stroka):
    print("Elements of file:", stroka)
    data_list_int = map(int, stroka.split())
    squared_list = [el ** 2 for el in data_list_int]
    squared_list_str = map(str, squared_list)
    str_new = (" ".join(squared_list_str))
    print("Square of elements:", str_new)
    return str_new

with open("task3.txt", 'r') as f:
    line = f.readline()
    result = square(line)
with open("task3.txt", "w") as f1:
    f1.write(result)


# 4 Даны два файла произвольного типа. Поменять местами их
# содержимое. Файлы должны быть бинарного типа
FILENAME = "task4_1.bin"
FILENAME1 = "task4_2.bin"

with open(FILENAME, "wb") as f:
    f.writelines(
        [
            "This is file 1\n".encode(),
            "The end of file 1\n".encode()
        ]
    )
with open(FILENAME1, "wb") as f1:
    f1.writelines(
        [
            "This is file 2\n".encode(),
            "The end of file 2\n".encode()
        ]
    )

with open(FILENAME, "rb") as f:
    file1_content = []
    for line in f:
        line = line.decode()
        file1_content.append(line)
    print("Content of file1:", file1_content)
with open(FILENAME1, "rb") as f1:
    file2_content = []
    for line in f1:
        line = line.decode()
        file2_content.append(line)
    print("Content of file2:", file2_content)

with open(FILENAME, "wb") as f:
    for line in file2_content:
        f.write(line.encode())
with open(FILENAME1, "wb") as f1:
    for line in file1_content:
        f1.write(line.encode())

print("After files' content was changed:")
with open(FILENAME, "rb") as f:
    file1_content = []
    for line in f:
        line = line.decode()
        file1_content.append(line)
    print("Content of file1:", file1_content)
with open(FILENAME1, "rb") as f1:
    file2_content = []
    for line in f1:
        line = line.decode()
        file2_content.append(line)
    print("Content of file2:", file2_content)