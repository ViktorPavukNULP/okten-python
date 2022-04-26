import time
import math
import multiprocessing
from multiprocessing import freeze_support


def time_decor(func):
    def inner(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        print(time.time() - start)

    return inner


def worker(num):
    res = str(math.sqrt(math.sqrt(math.sqrt(((num * 2) / 5) * 15)))) + 'H'
    return res


@time_decor
def main_thread():
    print('Main')
    numbers = range(2000000)
    with open('file1.txt', 'w') as file:
        for number in numbers:
            res = worker(number)
            file.write(f'{res}\n')


@time_decor
def mp():
    print('mp')
    count = multiprocessing.cpu_count()
    print(count, 'CPU')
    with multiprocessing.Pool(count) as p:
        numbers = range(2000000)
        with open('file2.txt', 'w') as file:
            results = p.map(worker, numbers)
            for result in results:
                file.write(f'{result}\n')



if __name__ == '__main__':
    main_thread()
    # freeze_support()
    mp()