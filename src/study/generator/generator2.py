def generator(num):
    for item in range(num):
        yield item*2

g = generator(100)  # g now become a generator
print(next(g))
print(next(g))
print(next(g))