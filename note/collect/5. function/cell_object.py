def counter(start):
	def inc(step=1):
		nonlocal start
		start = start + step
		print(start)

	return inc

my_inc = counter(start=5)

my_inc()	# 6
my_inc()	# 7

"""
Focus line 4 (modify nonlocal variable: start)
	- first, since start + step, it will create new object
	- second, because assign back to start, start will reference to new object
	- that mean?:
		+ start in inner function point to new object
		+ start in outer function point to old object?
	- both of them point to same object:
		+ to achieve this, Python used cell object
"""

# how to inspect cell object
# get list of free variables
print(my_inc.__code__.co_freevars)

# get cell object: show that cell object not change, only change free variable
my_inc()
print(my_inc.__closure__)
my_inc()
print(my_inc.__closure__)
my_inc()
print(my_inc.__closure__)