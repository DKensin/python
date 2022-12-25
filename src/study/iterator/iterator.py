mytuple = ("apple", "banana", "cherry")
my_iterator = iter(mytuple) # return tuple_iterator object

print(next(my_iterator))        # way 1
print(my_iterator.__next__())   # way 2
print(my_iterator.__next__())