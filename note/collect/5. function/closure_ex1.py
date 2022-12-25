def outer():
	a = 25
	name = "python"

	def inner(prefix):
		# variable name is non-local variable
		print(prefix, name)

	# inner: closure: function + free variables (name)
	return inner

my_func = outer()
print(my_func)
my_func("name is")