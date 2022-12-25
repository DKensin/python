# set
my_set = {1,2,3,4,5,5}
print(my_set)

my_list = [1,2,1,3,4,4,4,5,5]
my_set = set(my_list)   # away to remove duplicate
print(my_set)

new_set = my_set.copy()

set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8,9}
set1 = set1 & set2
print(set1)