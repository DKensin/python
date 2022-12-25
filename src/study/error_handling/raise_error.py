while True:
	try:
		age = int(input("What is your age? "))
		idiot = 10/age
		# raise ValueError("Value error happen!")
		raise Exception("An exception occur!")
	except ZeroDivisionError:
		print("Please enter age > 0")
	else:
		print("thank you!!!")
		break
