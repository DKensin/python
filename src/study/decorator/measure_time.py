# show an application of use decorator: measure time of a function

from time import time

def measure_time(func):
    def wrap_func(*args, **kwargs):
        t1 = time()
        func(*args, **kwargs)
        t2 = time()
        print(f"took {t2-t1} s")
    return wrap_func

@measure_time
def my_func():
    for i in range(100000000):
        i*5

my_func()