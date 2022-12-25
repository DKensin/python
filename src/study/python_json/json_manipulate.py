import json

# open json file
file = "database.json"
with open(file, 'r') as json_file:
    book_data = json.load(json_file)
    # print(book_data)

# convert python object to json
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON, use indent to more readable
y = json.dumps(x, indent=4)

# the result is a JSON string:
print(y)