from collections.abc import Callable
# написать функцию на замыкания которая будет в себе хранить лист дел, вам нужно реализовать два метода
# - первый записывает в эту переменную запись
# - второй возвращает все записи
#
# запишите 5 тудушек
# и выведете все
#
# 2) протипизировать первое задание

def notebook() -> dict[str, Callable]:
    todo_list = []

    def add_todo(todo: str) -> None:
        todo_list.append(todo)

    def get_all() -> None:
        print("Todo list:")
        for row in todo_list:
            print('-', row)

    return {"add_todo": add_todo, "get_all": get_all}


notebook1 = notebook()
notebook1["add_todo"]("Wake up")
notebook1["add_todo"]("Learn python")
notebook1["add_todo"]("Learn javascript")
notebook1["add_todo"]("Eat")
notebook1["add_todo"]("Sleep")
notebook1["get_all"]()

# 3) создать функцию которая будет возвращать сумму разрядов числа в виде строки (тоже с типизацией)

def expanded_form(number: int) -> str:
    number_string = str(number)
    number_len = len(number_string)
    result_string = ''
    for n, letter in enumerate(number_string):
        if letter == '0':
            continue
        result_string += letter+('0'*(number_len-n-1))
        if n != number_len-1:
            result_string += " + "
    return result_string


print(expanded_form(12))
print(expanded_form(42))
print(expanded_form(70304))

# Пример:
#
# expanded_form(12) # return '10 + 2'
# expanded_form(42) # return '40 + 2'
# expanded_form(70304) # return '70000 + 300 + 4'
