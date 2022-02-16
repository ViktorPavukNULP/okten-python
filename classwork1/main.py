# створити пустый список users_list = []
#
# стврорити меню в якому потрібно реалізувати:
#
# 1) додававання нового юзера
# 2) вивід всіх юзерів
# 3) вивід всіх юзерів за віком
# 4) видалення юзера по id
# 5) заміна статуса юзера на протилежний
# 6) вихід з меню
#
# приклад юзера {'id':1,'name':'Max', 'age':35,'status':False}

users_list = [
    {'id': 0, 'name': 'Max', 'age': 3, 'status': False},
    {'id': 1, 'name': 'Petya', 'age': 5, 'status': True},
    {'id': 2, 'name': 'Andriy', 'age': 2, 'status': False},
    {'id': 3, 'name': 'Katya', 'age': 8, 'status': False},

]


def add_user(name, age, status):
    if len(users_list):
        new_user_id = users_list[-1]["id"] + 1
    else:
        new_user_id = 0
    users_list.append({"id": new_user_id, "name": name, "age": age, "status": status})


def print_user_list(_list):
    for row in _list:
        print(row)


def print_user_list_ordered():
    new_list = sorted(users_list, key=lambda user: user['age'])
    print_user_list(new_list)


def delete_user(id):
    for n, user in enumerate(users_list):
        if user["id"] == id:
            users_list.pop(n)


def change_status(id):
    for user in users_list:
        if user["id"] == id:
            user["status"] = not user["status"]


while True:
    print("1) додававання нового юзера")
    print("2) вивід всіх юзерів")
    print("3) вивід всіх юзерів за віком")
    print("4) видалення юзера по id")
    print("5) заміна статуса юзера на протилежний")
    print("6) вихід")
    action = input("Виберіть дію: ")

    if action == "1":
        name = input("Введіть ім'я: ")
        age = int(input("Введіть вік: "))
        status = True if input("Введіть статус (1 або 0): ") == "1" else False
        add_user(name, age, status)
    elif action == "2":
        print_user_list(users_list)
    elif action == "3":
        print_user_list_ordered()
    elif action == "4":
        id_to_delete = int(input("Введіть ід юзера: "))
        delete_user(id_to_delete)
    elif action == "5":
        id_status_change = int(input("Введіть ід юзера: "))
        change_status(id_status_change)
    elif action == "6":
        break
    else:
        print("Невірна дія")
