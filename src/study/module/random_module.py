import random

# print(random)
# help(random)
# print(dir(random))

# random a number from 0 to 1
print(random.random())

# random a int number in a range
print(random.randint(1, 10))

# choice a item in a list
print(random.choice([1,2,3,4,5,6]))
print(random.choice(['a', 'b', 'c', 'd']))

my_list = [1,2,3,4,5,6,7]
random.shuffle(my_list) # shuffle a list
print(my_list)