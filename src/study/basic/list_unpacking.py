# list unpacking
a,b,c, *_, d = [1,2,3,4,5,6,7,8,9]
# a,b,c = 1,2,3: still work -> still a list

print(a)
print(b)
print(c)
print(_)
print(d)