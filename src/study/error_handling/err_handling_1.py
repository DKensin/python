while True:
	try:
		age = int(input("What is your age? "))
		idiot = 10/age
	except ValueError:
		print("Please enter a number!")
		continue
	except ZeroDivisionError:
		print("Please enter age > 0")
		break
	else:
		print("thank you!!!")
		break
	finally:
		print("I really done!")
	print("Can you hear me?")
