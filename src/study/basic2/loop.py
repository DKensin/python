for item in "Zero":
    print(item)

for item in (1,2,3):
    print(item)

print('My last index = ', item)

user = {
    'name': "Toan",
    'age': 25,
    'can_swim': True
# }

for item in user.items():
    print(item)         # return each key-value in tuple
    key, value = item   # unpacking
    print(key, value)

for key, value in user.items():
    print(key, value)

for item in user:
    print(item)    # loop over the keys

for item in user.keys():
    print(item)

for item in user.values():
    print(item)    # return value