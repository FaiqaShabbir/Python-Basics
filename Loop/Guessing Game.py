import random

extent = 20
to_be_guessed = int(extent * random.random()) + 1
# print(to_be_guessed)
guess = 0

while guess != to_be_guessed:
    guess = int(input("New Number: "))
    if guess > 0:
        if guess > to_be_guessed:
            print("Number too large!")
        elif guess < to_be_guessed:
            print("Number too small!")
    else:
        print("Sorry that you are giving up!")
        break
else:
    print("Congratulation! You made it.")
