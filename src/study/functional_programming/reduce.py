# reduce function
from functools import reduce

my_list = [1,2,3]

def accumulator(acc, item): # acc: initial value
    print(acc, item)
    return acc + item

initial_value = 10
result = reduce(accumulator, my_list, initial_value)
print(result)