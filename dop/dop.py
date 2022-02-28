# //////////////////////////////////////////////////////////////////////////////////////////////
#
# // Cоздать функцию которая принимает число и возвращает  текст как в примере:
# //     3275  —>  "3000 + 200 + 70 +5"

def expanded_form(number: int) -> str:
    number_string: str = str(number)
    if number_string == '0':
        return '0'
    number_len: int = len(number_string)
    result_string: str = ''
    for n, letter in enumerate(number_string):
        if letter == '0':
            continue
        result_string += letter + ('0' * (number_len - n - 1))
        result_string += " + "
    return result_string[:-3]


# print(expanded_form(3275))

# //////////////////////////////////////////////////////////////////////////////////////////////
#
# // Дан массив целых чисел, найдите тот, который встречается нечетное количество раз.
# // Всегда будет только одно целое число, которое встречается нечетное количество раз
# //     [1,2,3,4,5,2,4,1,3] -> 5

arr = [1, 2, 3, 4, 5, 2, 4, 1, 3]


def occur_odd(arr: list[int]):
    for element in arr:
        if arr.count(element) % 2:
            return element


# print(occur_odd(arr))

# //////////////////////////////////////////////////////////////////////////////////////////////
#
# // Знайти анаграму.
# //     Перевірити чи слово має в собі такі самі літери як і поеперднє слово.
# //
# //     ANAGRAM | MGANRAA -> true
# // EXIT | AXET -> false
# // GOOD | DOGO -> true

def find_anagram(word1: str, word2: str):
    if len(word1) != len(word2):
        return False
    for letter in word1:
        if letter in word2:
            word2 = word2.replace(letter, '', 1)
        else:
            return False
    return True


# print(find_anagram('EXIT', 'AXET'))
# print(find_anagram('GOOD', 'DOGO'))


# //////////////////////////////////////////////////////////////////////////////////////////////
#
# // Точная степень двойки
# // Дано натуральное число N.
# //     Выведите слово YES, если число N является точной степенью двойки, или слово NO в противном случае.
# //     Операцией возведения в степень пользоваться нельзя!

def is_power_of_2(number):
    while (number > 2):
        number /= 2
    if number == 2.0:
        print('Yes')
    else:
        print('No')


# is_power_of_2(16)
# is_power_of_2(10)
# is_power_of_2(0)
# is_power_of_2(2)
# is_power_of_2(244)
# is_power_of_2(256)

# //////////////////////////////////////////////////////////////////////////////////////////////
#
# //  Сумма цифр числа
# // Дано натуральное число N. Вычислите сумму его цифр.
# //     При решении этой задачи нельзя использовать строки,
# //     списки, массивы ну и циклы, разумеется.
# //     Рекурсія)


# def digits_sum(number):
#     if number < 10:
#         return number
#     return number % 10 + digits_sum(number // 10)
#
#
# print(digits_sum(3200123))

# //////////////////////////////////////////////////////////////////////////////////////////////
#
# // Палиндром
#    // Дано слово, состоящее только из строчных латинских букв. Проверьте, является ли это слово палиндромом. Выведите YES или NO.
#   //     При решении этой задачи нельзя пользоваться циклами, в решениях на питоне нельзя использовать срезы с шагом, отличным от 1.

# def palindrom(string):
#     new_str = string.lower()
#     print("YES" if new_str == ''.join(reversed(new_str)) else 'NO')
#
#
# palindrom('ARA')
#
#   //////////////////////////////////////////////////////////////////////////////////////////////
#
#   // Количество единиц
#   // Дана последовательность натуральных чисел  в строке, завершающаяся двумя числами 0 подряд.
#   // Определите, сколько раз в этой последовательности встречается число 1. Числа, идущие после двух нулей, необходимо игнорировать.
#   //
#   // 2176491947586100 -> 3

def count_ones(number_str):
    counter = 0
    for i in range(len(number_str)-1):
        if number_str[i] != '0':
            if number_str[i] == '1':
                counter += 1
        elif number_str[i+1] == '0':
            break
    return counter


print(count_ones('2176491947586100'))
#   //////////////////////////////////////////////////////////////////////////////////////////////
#   // Вирівняти багаторівневий масив в однорівневий
#   [1,3, ['Hello, 'Wordd', [9,6,1]], ['oops'], 9] -> [1, 3, 'Hello, 'Wordd', 9, 6, 1, 'oops', 9]
# // flat використовувати заборонено.
#
# //////////////////////////////////////////////////////////////////////////////////////////////
#
# // Знайти набільший елемент в масиві за допомогою reduce
# //     [1,6,9,0,17,88,4,7] -> 88
#
# /////////////////////////////////////////////////////////////////////////////////////////
#
# вивести послідовність Фібоначі, кількість вказана в знінній,
# наприклад: x = 10 -> 1 1 2 3 5 8 13 21 34 55
# (число з послідовності - це сума попередніх двох чисел)
#
# /////////////////////////////////////////////////////////////////////////////////////////
#
# порахувати кількість парних і непарних цифр числа,
# наприклад: х = 225688 -> п = 5, н = 1;
# х = 33294 -> п = 2, н = 3
#
# /////////////////////////////////////////////////////////////////////////////////////////
#
# прога, що виводить кількість кожного символа з введеної строки,
# наприклад:
# st = 'as 23 fdfdg544' #введена строка
#
# 'a' -> 1  #вивело в консолі
# 's' -> 1
# ' ' -> 2
# '2' -> 1
# '3' -> 1
# 'f' -> 2
# 'd' -> 2
# 'g' -> 1
# '5' -> 1
# '4' -> 2
#
# /////////////////////////////////////////////////////////////////////////////////////////
#
# генерируем лист с непарных чисел в порядке возрастания [1,3,5,7,9.....n]
# задача сделать c него лист листов такого плана:
#
# [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]  => [ [1], [3,5], [7,9,11], [13,15,17,19] ]
# [1, 3, 5, 7, 9, 11] => [[1], [3, 5], [7, 9, 11]]
# [1, 3, 5, 7, 9]  => [ [1], [3,5], [7,9]]
# [1, 3, 5, 7, 9, 11, 13]  => [[1], [3, 5], [7, 9, 11], [13]]
