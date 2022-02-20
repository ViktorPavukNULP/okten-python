from __future__ import annotations

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
    todo_list: list[str] = []

    def add_todo(todo: str) -> None:
        todo_list.append(todo)

    def get_all() -> list[str]:
        return todo_list

    return {"add_todo": add_todo, "get_all": get_all}


notebook1 = notebook()
notebook1["add_todo"]("Wake up")
notebook1["add_todo"]("Learn python")
notebook1["add_todo"]("Learn javascript")
notebook1["add_todo"]("Eat")
notebook1["add_todo"]("Sleep")
print(notebook1["get_all"]())

# 3) создать функцию которая будет возвращать сумму разрядов числа в виде строки (тоже с типизацией)

def expanded_form(number: int | str) -> str:
    number_string: str = str(number)
    number_len: int = len(number_string)
    result_string: str = ''
    for n, letter in enumerate(number_string):
        if letter == '0':
            continue
        result_string += letter+('0'*(number_len-n-1))
        result_string += " + "
    return result_string[:-3]


print(expanded_form(12))
print(expanded_form(42))
print(expanded_form(70304))
print(expanded_form("10302910"))

# Пример:
#
# expanded_form(12) # return '10 + 2'
# expanded_form(42) # return '40 + 2'
# expanded_form(70304) # return '70000 + 300 + 4'
