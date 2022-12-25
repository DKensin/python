# dictionary
dictionary = {
    'a': [1,2,3],
    'b': "hello",
    'c': True
}

my_list = [
    {
        'a': [1,2,3],
        'b': "hello",
        'c': True
    },
    {
        'e': [4,5,6],
        'f': "world",
        'g': False
    }
]

print(my_list[1]['e'])

# method
user = {
    'baseket': [1,2,3],
    'greet': 'hello',
    'age': 20
}

print(user.get('age', 55))  # if 'age' not exist in user, use 55 value
print('hello' in user.keys())
print('hello' in user.values())
print(user.items())

user2 = dict(name='Toan')
print(user2)
