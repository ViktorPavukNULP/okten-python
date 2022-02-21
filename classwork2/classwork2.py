# создать декоратор который будет считать сколько раз была запущена функция
# и будет выводит это значение после каждого запуска функции

def decor(func):
    counter = 0

    def inner():
        nonlocal counter
        counter += 1
        print('Counter:', counter)
        func()
        print('-' * 20)

    return inner


@decor
def func1():
    print('func1')


@decor
def func2():
    print('func2')


func1()
func2()
func1()
func2()
