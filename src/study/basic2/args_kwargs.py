def super_func(name, *args, i='hi', **kwargs):
	print(args)		# tuple
	print(kwargs)	# dict
	total = 0
	for items in kwargs.values():
		total += items
	return sum(args) + total

print(super_func('Toan', 1,2,3,4,5, num1=5, num2=10))

# rule: params, *args, default params, **kwargs