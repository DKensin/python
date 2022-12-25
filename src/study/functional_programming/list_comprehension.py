# comprehension
my_list = []

for char in "hello":
    my_list.append(char)

print(my_list)

# use list comprehension
compre_list = [char for char in "hello"]
print(compre_list)

# anothher example
my_list2 = [num**2 for num in range(0,100) if num%2 == 0]
print(my_list2)