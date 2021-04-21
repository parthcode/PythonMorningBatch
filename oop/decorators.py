import time


def validate(function_value):
    t1 = time.time()
    function_value()
    t2 = time.time()
    print("Time taken is :", t2 - t1)


@validate
def display():
    for i in range(5):
        time.sleep(0.2)
