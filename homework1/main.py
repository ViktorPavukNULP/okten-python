#
# #ДЗ
#
# strings
#
# 1)написати прогу яка вибирає зі введеної строки цифри і виводить їх через кому,
# наприклад:
# st = 'as 23 fdfdg544' введена строка
# 2,3,5,4,4        #вивело в консолі.

# st = 'as 23 fdfdg544'
# numbers = []
#
# for el in st:
#     if el in '1234567890':
#         numbers.append(el)
#
# print(*numbers, sep=', ')

# #################################################################################
# 2)написати прогу яка вибирає зі введеної строки числа і виводить їх
# так як вони написані
# наприклад:
# st = 'as 23 fdfdg544 34' #введена строка
# 23, 544, 34              #вивело в консолі

# st = 'as 23 fdfdg544 34'
# i = 0
# numbers = []
# while i < len(st):
#     number = ''
#     while i < len(st) and st[i].isdigit():
#         number += st[i]
#         i += 1
#     if number:
#         numbers.append(number)
#     i+=1
#
# print(*numbers, sep=', ')

# #################################################################################
#
# list comprehension
#
# 1)есть строка:
# greeting = 'Hello, world'
# записать каждый символ в лист поменяв его на верхний регистр
# пример:
# ['H', 'E', 'L', 'L', 'O', ',', ' ', 'W', 'O', 'R', 'L', 'D']

# greeting = 'Hello, world'
# string_list = [letter.upper() for letter in greeting]
# print(string_list)

#
# 2) с диапазона от 0-50 записать в лист только не парные числа, при этом возвести их в квадрат
# пример:
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, ...]

# odd_squared_array = [number ** 2 for number in range(50) if number % 2 != 0]
# print(odd_squared_array)

# function
#
# - створити функцію яка виводить ліст

# def print_list(_list):
#     print(*_list, sep=', ')
#
#
# arr = [1,2,3,4]
# print_list(arr)

# - створити функцію яка приймає три числа та виводить та повертає найменьше.

# def min_of_3(a, b, c):
#     if a < b:
#         if a < c:
#             print(a)
#             return a
#         print(c)
#         return c
#     elif b < c:
#         print(b)
#         return (c)
#     print(c)
#     return (c)
#
#
# min_of_3(4, 4, 2)

# - створити функцію яка приймає три числа та виводить та повертає найбільше.

# def max_of_3(a, b, c):
#     if a > b:
#         if a > c:
#             print(a)
#             return a
#         print(c)
#         return c
#     elif b > c:
#         print(b)
#         return (c)
#     print(c)
#     return (c)
#
#
# max_of_3(4, 5, 7)

# - створити функцію яка приймає будь-яку кількість чисел, повертає найменьше, а виводить найбільше

# def return_min_print_max(*args):
#     _min = args[0]
#     _max = args[0]
#     for element in args:
#         if element < _min:
#             _min = element
#         if element > _max:
#             _max = element
#     print(_max)
#     return _min
#
#
# print(return_min_print_max(1, 2, 3, 4, -1, 0, 23))

# - створити функцію яка виводить ліст

# def print_list(_list):
#     print(*_list, sep=', ')
#
#
# arr = [1,2,3,4]
# print_list(arr)

# - створити функцію яка повертає найбільше число з ліста

# def list_max(_list):
#     _max = _list[0]
#     for element in _list:
#         if element > _max:
#             _max = element
#     return _max
#
#
# arr = [1,22,3,4]
# print(list_max(arr))

# - створити функцію яка повертає найменьше число з ліста

# def list_min(_list):
#     _min = _list[0]
#     for element in _list:
#         if element < _min:
#             _min = element
#     return _min
#
#
# arr = [1,22,3,4]
# print(list_min(arr))

# - створити функцію яка приймає ліст чисел та складає значення елементів ліста та повертає його.

# def list_sum(_list):
#     _sum = 0
#     for element in _list:
#         _sum += element
#     return _sum
#
#
# arr = [1,22,3,4]
# print(list_sum(arr))

# - створити функцію яка приймає ліст чисел та повертає середнє арифметичне його значень.

# def list_mean(_list):
#     _sum = 0
#     for element in _list:
#         _sum += element
#     return _sum/len(_list)
#
#
# arr = [1,22,3,4]
# print(list_mean(arr))

# #################################################################################################
# 1)Дан лист:
# list = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]


# - найти min число в листе

# _min = list[0]
# for element in list:
#     if element < _min:
#         _min = element
# print(_min)
# print(min(list))

# - удалить все дубликаты в листе

# new_list = []
# for element in list:
#     if element not in new_list:
#         new_list.append(element)
#
# print(new_list)

# - заменить каждое четвертое значение на "Х"

# for i in range(0, len(list), 4):
#     list[i] = 'X'
#
# print(list)
# 2)вывести на экран пустой квадрат из "*" сторона которого указана в переменой:

# def print_square(a):
#     print('*'*a)
#     for i in range(a-2):
#         print('*',' '*(a-2),'*', sep='')
#     print('*'*a)
#
#
# print_square(25)

# 3) вывести табличку умножения с помощью цикла while

# i = 1
# j = 1
# n = 10
# while i < n:
#     while j < n:
#         print(f'{i * j :^3}', end=' ')
#         j += 1
#     j=1
#     i += 1
#     print()
#
# - вывести элемент листа, значение которого ближе всего к среднему арифметическому всех элементов этого же листа
# пример:
# [1, 2, 3, 4, 5, 6, 7, 8, 9] => 5
# [-1, -2, 3, 4, 555] => 4
# [5, 5, 5, 5] => 5
# [-10, 5, 5] => 5

# def list_mean(_list):
#     _sum = 0
#     for element in _list:
#         _sum += element
#     return _sum / len(_list)
#
#
# def close_to_mean(_list):
#     mean = list_mean(_list)
#     min_dif = abs(mean - _list[0])
#     res = _list[0]
#     for element in _list:
#         dif = abs(mean - element)
#         if dif < min_dif:
#             min_dif = dif
#             res = element
#     return res


# print(close_to_mean([1, 2, 3, 4, 5, 6, 7, 8, 9]))
# print(close_to_mean([-1, -2, 3, 4, 555]))
# print(close_to_mean([5, 5, 5, 5]))
# print(close_to_mean([-10, 5, 5]))

# 4) переделать первое задание под меню с помощью цикла

list = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]

def list_min(_list):
    _min = list[0]
    for element in list:
        if element < _min:
            _min = element
    return _min


def remove_duplicates(_list):
    new_list = []
    for element in list:
        if element not in new_list:
            new_list.append(element)
    return new_list


def insert_X(_list):
    new_list = _list.copy()
    for i in range(0, len(_list), 4):
        new_list[i] = 'X'
    return new_list

def list_mean(_list):
    _sum = 0
    for element in _list:
        _sum += element
    return _sum / len(_list)


def close_to_mean(_list):
    mean = list_mean(_list)
    min_dif = abs(mean - _list[0])
    res = _list[0]
    for element in _list:
        dif = abs(mean - element)
        if dif < min_dif:
            min_dif = dif
            res = element
    return res

while True:
    print("1. найти min число в листе")
    print("2. удалить все дубликаты в листе")
    print("3. заменить каждое четвертое значение на \"Х\"")
    print("4. вывести элемент листа, значение которого ближе всего к среднему арифметическому всех элементов этого же листа")
    print("5. выход")
    action = input("Сделайте выбор: ")
    if action == "1":
        print(list_min(list))
    elif action == "2":
        print(remove_duplicates(list))
    elif action == "3":
        print(insert_X(list))
    elif action == "4":
        print(close_to_mean(list))
    elif action == "5":
        break
    else:
        print("Неверная команда")