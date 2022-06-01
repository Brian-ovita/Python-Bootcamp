from random import randint

comp_number = randint(1,1000)

active = False
while not active:
    user_input = int(input("Guess a number between 1 and 1000: "))
    if user_input == comp_number:
        print("Yay!!! You guessed correctly")
        active = True
    elif user_input > comp_number:
        print("Number guessed greater than computer number")
    elif user_input < comp_number:
        print("Number guessed less than computer number")
    else:
        print("Error: Invalid input")
        