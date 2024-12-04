# 1. Классы и наследование
print("Task1:")
class Person:
    country = "Belarus"

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
    def display_info(self):
        print(f"Name: {self.name}, Surname: {self.surname}")

person1 = Person("Ivan", "Ivanov")
person2 = Person("Liana", "Lesnikovich")
print(person1.name, person1.surname, person1.country)
print(person2.name, person2.surname, person2.country)
person1.display_info()
person2.display_info()

class Employee(Person):

    def __init__(self, name, surname, work):
        super().__init__(name, surname)
        self.work = work


empl1 = Employee("Petr", "Petrov", "manager")
print(empl1.name, empl1.surname, empl1.work, empl1.country)
empl1.display_info()

class Student(Employee):
    def __init__(self, name, surname, work, university):
        super().__init__(name, surname, work)
        self.university = university

st1 = Student("Valentin", "Lesnikovich", "Accounter", "Finance Academy")
print(st1.name, st1.surname, st1.work, st1.country, st1.university)
st1.display_info()


# 2. Классы и инкапсуляция. Класс Точка. и его аттрибуты(координаты х, у, х1, у1, х2, у2),
# защищенный метод _print_value, приватный метод __check_value, обычный метод set_coord устанавливает приватные координаты х2, у2,
# метод get_coord возвращает приватные координаты х2, у2
print("--------------------------------------------")
print("Task2:")
class Point:
    def __init__(self, x=0, y=0, x1=0, y1=0, x2=0, y2=0):
        self.x = x
        self.y = y
        self._x1 = x1 #внутри класса и в дочерних, извне можем к ним обратиться
        self._y1 = y1 #внутри класса и в дочерних, извне  можем к ним обратиться
        self.__x2 = x2 #только внутри класса
        self.__y2 = y2 #только внутри класса

    def _print_value(self, a, b):
        print(f"a = {a}, b = {b}")

    def __check_value(self, x):
        return type(x) in (int, float)

    def set_coord(self, x2, y2): #сеттер к приватному аттрибуту(устанавливает координаты).внутри класса обращаемся к приватным аттрибутам чз обычный метод
        if self.__check_value(x2) and self.__check_value(y2):
            self.__x2 = x2
            self.__y2 = y2
        else:
            raise ValueError

    def get_coord(self): #геттер (возвращает координаты)
        return self.__x2, self.__y2

pt = Point(1, 2)
print(pt.x, pt.y)
pt.x = 200
pt.y = "stroka"
print(pt.x, pt.y)

pt1 = Point(1, 2, 8, 12)
print(pt1._x1, pt1._y1) #обращаемся к защищенным аттрибутам из вне

# pt2 = Point(x2=3, y2=5)
# print(pt2.__x2, pt2.__y2) #обращаемся к приватным аттрибутам из вне. Результат: ошибка

pt1.set_coord(10,20) #сеттер позволяет обратиться к приватным аттрибутам
print(pt1.get_coord())

# pt1.set_coord("10",20) #выведет ошибку ValueError
pt1._print_value(17, 18)



# 3. Классы и полиморфизм


from abc import ABC, abstractmethod

class Figure(ABC):
    @abstractmethod
    def get_area(self):
        pass

class Rectangle(Figure):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_area(self):
        return self.a * self.b

class Square(Figure):
    def __init__(self, a):
        self.a = a

    def get_area(self):
        return self.a**2

class Circle(Figure):
    def __init__(self, r):
        self.r = r

    def get_area(self):
        return 3.14 * (self.r**2)


figures = [
    Rectangle(3, 4), Rectangle(12, 5),
    Square(5), Square(7),
    Circle(3), Circle(2)
]

print("---------------------------------")
print("Task3:")
for figure in figures:
    print(figure.get_area())