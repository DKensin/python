from shopping.more_shopping import more_shopping_cart

print(more_shopping_cart)
print(more_shopping_cart.buy("banana"))

# show how to avoid name collision
print(more_shopping_cart.max())
print(max([1,2,3])) # build-in function

print(__name__)