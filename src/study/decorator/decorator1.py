# show how decorator enhance a function

def my_decorator(func):
    def wrap_func():
        print("*********************")  # eg add another for func function
        func()
        print("*********************")
    return wrap_func

@my_decorator
def hello():
    print("helllooo")

@my_decorator
def bye():
    print("see ya later!!!")

hello()
bye()