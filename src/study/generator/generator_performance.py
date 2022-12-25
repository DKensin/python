# show power of generator

from time import time

def measure_time(func):
    def wrap_func(*args, **kwargs):
        t1 = time()
        func(*args, **kwargs)
        t2 = time()
        print(f"took {t2-t1} s")
    return wrap_func

@measure_time
def long_time1():
    print('1')
    for i in range(100000000):
        i*5

@measure_time
def long_time2():
    print('2')
    for i in list(range(100000000)):  # took more time
        i*5

long_time1()
long_time2()