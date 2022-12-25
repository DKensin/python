def highest_even(list_number):
	max_even = 0
	for number in list_number:
		if (number % 2 == 0):
			if (max_even < number):
				max_even = number
	return max_even

# another way
def highest_even(list_number):
	evens = []
	for item in list_number:
		if item % 2 == 0:
			evens.append(item)
	return max(evens)

my_list = [10,2,3,4,8,11]
print(highest_even(my_list))