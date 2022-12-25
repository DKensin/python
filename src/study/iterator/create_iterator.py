class MyLoop:
    def __init__(self, num):
        self.number = num
    
    def __iter__(self):
        self.current = 0
        return self
    
    def __next__(self):
        if (self.current < self.number):
            self.previous = self.current
            self.current += 1
            return self.previous
        else:
            raise StopIteration

my_loop = MyLoop(3)

# can use loop
print("use for loop:")
for item in my_loop:
    print(item)

print("use for loop:")
for item in my_loop:
    print(item)

# use iterator object
print("use iterator")
my_iterator = my_loop.__iter__()
# print(my_iterator.__next__())
# print(my_iterator.__next__())
# print(my_iterator.__next__())
for item in my_iterator:
    print(item)
