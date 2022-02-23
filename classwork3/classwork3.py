# Создать класс Rectangle:
# -конструктор принимает две стороны x,y
# -описать арифметические методы:
#   + сума площадей двух экземпляров класса
#   - разница площадей
#   == или площади равны
#   != не равны
#   >, < меньше или больше
#   при вызове метода len() подсчитывать сумму сторон

class Rectangle:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.area = x * y

    def __add__(self, other):
        return self.area + other.area

    def __sub__(self, other):
        return self.area - other.area

    def __eq__(self, other):
        return self.area == other.area

    def __ne__(self, other):
        return self.area != other.area

    def __gt__(self, other):
        return self.area > other.area

    def __lt__(self, other):
        return self.area < other.area

    def __len__(self):
        return self.x + self.y


rect1 = Rectangle(3, 2)
rect2 = Rectangle(2, 2)

# print(rect1 + rect2)
# print(rect1 - rect2)
# print(rect1 == rect2)
# print(rect1 != rect2)
# print(rect1 > rect2)
# print(rect1 < rect2)
# print(len(rect1))


#   ###############################################################################
#
# создать класс Human (name, age)
# создать два класса Prince и Cinderella:
# у золушки должно быть имя возраст и размер ноги
# у принца имя, возраст и размер найденной туфельки, так же должен быть метод который принимает лист золушек и ищет ту самую
# класса золушки должна быть переменная count которая будет считать сколько экземпляров класса золушка было создано
# и метод класса который будет показывать это количество

class Human:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


class Cinderella(Human):
    counter = 0
    
    def __init__(self, name, age, foot_size: int):
        super().__init__(name, age)
        self.foot_size = foot_size
        Cinderella.counter += 1
    
    def show_counter(self):
        print(Cinderella.counter)


class Prince(Human):
    def __init__(self, name, age, shoe: int):
        super().__init__(name, age)
        self.shoe = shoe

    def find_the_one(self, list_of_girls: list[Cinderella]):
        for girl in list_of_girls:
            if girl.foot_size == self.shoe:
                print('Ура, знайдено', girl.name)
                return girl
        print('Не знайдено')


Dima = Prince('Dima', 22, 37)
Tanya = Cinderella('Tanya', 31, 38)
Marta = Cinderella('Marta', 21, 39)
Olya = Cinderella('Olya', 19, 37)
Nastya = Cinderella('Nastya', 23, 41)
Petya = Cinderella('Petya', 25, 44)

Nastya.show_counter()

Dima.find_the_one([Tanya, Marta, Olya, Nastya])


