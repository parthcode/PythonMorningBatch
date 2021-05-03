import time
from threading import Thread


def function_one():
    for i in range(5):
        time.sleep(0.2)


def function_two():
    for i in range(5):
        time.sleep(0.3)


t1 = time.time()
thread_1 = Thread(target=function_one)
thread_2 = Thread(target=function_two)
thread_1.start()
thread_2.start()
thread_1.join()
thread_2.join()
t2 = time.time()
print("Time take is :", t2 - t1)
