# filter
my_list = [1,2,3,4]

def only_odd(item):
    return item % 2 != 0

new_list = filter(only_odd, my_list)

print(new_list)
print(list(new_list))
