def counter(start):
	def inc(step=1):
		nonlocal start
		start += step
		print(start)

	return inc

my_inc = counter(5)

my_inc(2)
my_inc(2)
my_inc()

# at this point, free variable still available

# another closure
another_inc = counter(100)
print(my_inc)
print(another_inc)

# show different free variable instances
my_inc(2)
another_inc()