username = input("What is your name?")
password = input("Type your password:")

password_length = len(password)
hidden_password = '*' * password_length

print(f"Hey {username}, your password {hidden_password} is {password_length} letters long")