# lambda function
from functools import reduce
my_list = [1,3,6]

double = map(lambda item: item*2, my_list)
print(list(double))

only_odd = filter(lambda item: item%2 != 0, my_list)
print(list(only_odd))

initial_value = 5
sum = reduce(lambda acc,item: acc+item, my_list)
print(sum)