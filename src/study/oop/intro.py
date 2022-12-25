class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	@classmethod
	def add_things(cls, num1, num2):
		return cls("Teddy", num1 + num2)

player = Person.add_things(2,3)
print(player.name)
print(player.age)

print(isinstance(player, object))