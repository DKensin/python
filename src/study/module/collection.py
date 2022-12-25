from collections import Counter, defaultdict, OrderedDict

my_list = [1,1,2,2,3,3,3,4,4,4,4,4,4]
my_sentence = "something random when thinking about python"
# count quatity of each element
print(Counter(my_list))
print(Counter(my_sentence))

my_dict = {'a':1, 'b':2}
# print(my_dict['c']) # will get key error
dictionary = defaultdict(lambda: "not exist", my_dict)
print(dictionary['c'])

# with normal dict: order not affect
d1 = {'c': 3}
d1['a'] = 1
d1['b'] = 2

d2 = {'c': 3}
d2['b'] = 2
d2['a'] = 1

print(d2 == d1)

# when need order of list
d3 = OrderedDict()
d3['a'] = 1
d3['b'] = 2

d4 = OrderedDict()
d4['b'] = 2
d4['a'] = 1

print(d3 == d4)