# lambda exercise

# square
my_list = [5,4,3]
square = map(lambda item: item**2, my_list)
print(list(square))

# List sorting: based on second element of each tupple
arr = [(0,2), (4,3), (9,9), (10,-1)]
arr.sort(key=lambda x: x[1])  # based on the key
print(arr)