def multiply_by2(number):
    return number*2
my_list = [1,2,3]
new_list = map(multiply_by2, my_list)
print(new_list)
print(list(new_list))