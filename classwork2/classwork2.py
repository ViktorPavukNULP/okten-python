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


# func1()
# func2()
# func1()
# func2()

# кому это очень легко то сделайте функцию на замыкания которая будет возвращать декоратор
# который будет считать общее количество запущенных  функций декорированных этим декоратором

def make_decorator():
    counter = 0

    def decorator(func):
        def inner():
            nonlocal counter
            counter += 1
            print('Counter:', counter)
            func()
            print('-' * 20)

        return inner

    return decorator


decor = make_decorator()


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
