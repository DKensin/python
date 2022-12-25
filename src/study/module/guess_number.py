import random

answer = random.randint(1,4)

while True:
    try:
        guess = int(input('guess a number 1~4:  '))
        if 0 < guess < 5:
            if guess == answer:
                print("You're a genious")
                break
        else:
            print("Hey, I said 1~4")
    except ValueError:
        print("please enter a number:   ")