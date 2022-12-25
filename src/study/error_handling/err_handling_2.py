def func(num1, num2):
	try:
		return num1/num2
	except (TypeError, ZeroDivisionError) as err:	# combine some type errors together
		print(err)

print(func(1, 0))