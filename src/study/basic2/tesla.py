#1. Wrap the above code in a function called check_driver_age(). Whenever you call this function, you will get prompted for age. 
# Notice the benefit in having check_driver_age() instead of copying and pasting the function everytime?

#2 Instead of using the input(). Now, make the check_driver_age() function accept an argument of age, so that if you enter:
#check_driver_age(92);
#it returns "Powering On. Enjoy the ride!"
#also make it so that the default age is set to 0 if no argument is given.

def check_driver_age(age=0):
	if ((0 < int(age)) and (int(age) < 100)):
		if (int(age) < 18):
			print("Sorry, you are too young to drive this car. Powering off")
		elif (int(age) == 18):
			print("Congratulations on your first year of driving. Enjoy the ride!")
		elif (int(age) > 18):
			print("Powering On. Enjoy the ride!")
		else:
			pass

age = input("What is your age?: ");
check_driver_age(age)
