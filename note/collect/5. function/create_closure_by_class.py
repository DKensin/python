class Counter:
	def __init__(self, start):
		self.start = start

	def inc(self, step=1):
		self.start += step

# this way also create a state to be remembered accross multiple call
my_inc = Counter(5)
my_inc.inc()		# 6
print(my_inc.start)

another_inc = Counter(100)
another_inc.inc()	# 101
print(another_inc.start)