import threading
import time

# def show(n):
#     for i in range(n):
#         print(i, threading.current_thread().name)
#         time.sleep(1)
#
#
# thread1 = threading.Thread(target=show, args=(8,), name='thr1', daemon=True)
# # thread2 = threading.Thread(target=show, args=(4,), name='thr2', daemon=True)
#
# thread1.start()
# # thread2.start()
# # thread1.join()
# # thread2.join()
#
# time.sleep(4)
# print('Main Thread')
# print('Main Thread')
# print('Main Thread')
# print('Main Thread')


count = 0
lock = threading.Lock()


def counter():
    with lock:
        global count
        count += 1
        print(count)


list_thread = []
for _ in range(1000):
    thread = threading.Thread(target=counter)
    list_thread.append(thread)
    thread.start()

for item in list_thread:
    item.join()