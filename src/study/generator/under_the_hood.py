def show_for_work(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(iterator) # point to same memory
            print(next(iterator))
        except StopIteration:
            break

class MyGenerator:
    def __init__(self, first, last):
        self.current = first
        self.first = first
        self.last = last
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current < self.last:
            number = self.current
            self.current += 1
            return number
        raise StopIteration

# show_for_work([1,2,3])
gen = MyGenerator(0, 10)
for item in gen:
    print(item)