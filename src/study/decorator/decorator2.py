# show decorator pattern

def my_decorator(func):
    def wrap_func(*args, **kwargs):
        print("******************")
        print(*args, **kwargs)      # unpacking
        print("******************")
    return wrap_func

@my_decorator
def hello(greeting, emoji=':)'):
    print(greeting, emoji)

hello("hiiiiii")