my_file = open("data.txt")  # create a file object
print(my_file)
print(my_file.readlines())
my_file.seek(0)             # change cursor
print(my_file.readline())
my_file.close()