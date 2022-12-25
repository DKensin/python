is_old = True
is_licenced = True

if is_old:
    print('You are old enough to driver')
elif is_licenced:
    print('You can driver now!')
else:
    print('Check')

# ternary operator
is_friend = True
can_message = "message allowed" if is_friend else "not allowed to message"
print(can_message)

# short circuiting
is_friend = True
is_user = False

if is_friend and is_old:
    print("best friend forever")

# logical operator
print(1 < 2 < 3 < 4)
