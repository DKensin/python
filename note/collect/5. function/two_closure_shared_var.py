# 2 closures reference the same free variable: start variable
def counter(start):
	def inc1(step=1):
		nonlocal start
		start += step
		print(start)

	def inc2(step=1):
		nonlocal start
		start += step
		print(start)

	return inc1, inc2

my_inc, another_inc = counter(5)
my_inc()		# 6
another_inc()	# 7