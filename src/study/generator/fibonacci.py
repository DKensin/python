# create function print nth fib1 sequential
def fib1(number):
    a = 0
    b = 1
    for i in range(number):
        yield a
        temp = a    # key: not modify a until a+b
        a = b
        b += temp

def fib2(number):
    a = 0
    b = 1
    list_fib = []
    for i in range(number):
        list_fib.append(a)
        temp = a    # key: not modify a until a+b
        a = b
        b += temp
    return list_fib

for item in fib1(20):
    print(item)

# print(fib2(1000))