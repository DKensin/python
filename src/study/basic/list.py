from types import new_class


list1 = [1,2,3,4,5]
list2 = ['a', 'b', 'c']
list3 = ['a', 1,2, True]

list1[0] = 0
print(list1[0])

amazon_cart = [
    "notebooks",
    "sunglasses",
    "toys",
    "grapes"
]

# list slicing
print(amazon_cart[0::2])

# list is mutable
amazon_cart[0] = "laptop"   # point to somewhere in memory
print(amazon_cart)

new_cart = amazon_cart          # assign, not coppy
new_cart_copy = amazon_cart[:]  # create a coppy
new_cart[0] = "gum"

print(new_cart)
print(amazon_cart)  # change new_card also change amazon_cart
