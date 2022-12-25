new_list = []

def multiply_by2(list_number):
    for number in list_number:
        new_list.append(number * 2) # This function interact with outside function scope -> side effect
    return new_list

print(multiply_by2([1,2,3]))