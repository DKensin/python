print(type("hi hello there"))

long_string = '''
WOW
0 0
---
'''
print(long_string)

first_name = "Ngo"
last_name = "Toan"
full_name = first_name + " " + last_name
print(full_name)

# formatted strings
name = "Johnny"
age = 55
print("Hi " + name + ". You are " + str(age) + " years old")
print(f"Hi {name}. You are {age} years old")    # formatted string
print("Hi {}. You are {} years old".format(name, age))
print("Hi {1}. You are {0} years old".format(name, age))
print("Hi {new_name}. You are {new_age} years old".format(new_name="Toan", new_age="24"))   # tupe

# string index
selfist = "01234567"
# [start:stop:step]
print(selfist[0:8:2])
print(selfist[1:])
print(selfist[:4])
print(selfist[-1])
print(selfist[::-1])    # print reserve