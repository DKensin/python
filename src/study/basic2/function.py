#parameters
# default parameters: name='Toan' is default parameter
def say_hello(name='Toan', emoji='^^'):
    print(f"Helloooo {name} {emoji}")

#arguments
say_hello("Toan", ':)')

# keyword arguments
say_hello(emoji=':v', name="Hien")

# show default parameter
say_hello('Someone')