a = 1

def my_func():
	a = 9
	return a

print(my_func())
print(a)

# global keyword
total = 0
def count():
	global total
	total += 1
	return total


count()
count()
count()
print(count())