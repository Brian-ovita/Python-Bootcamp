import random
from words import words
word = random.choice(words)
guessed, lives, game_over = [], 8, False
guesses = ["-"]*len(word)

while not game_over:
    hidden_word = " ".join(guesses)
    print("Lives left:",lives,"\nand the letters already guessed:",guessed)
    print("Word to guess:",hidden_word)
    user_letter = input("Guess a letter or type quit: ").lower()
    if user_letter == 'quit':
        game_over = True
        print("Thank you for using our software.")   
    elif user_letter in word and user_letter not in guessed:
        for i in range(len(word)):
            if word[i] == user_letter:
                guesses[i] = user_letter
    elif user_letter in guessed:
        print("You already guessed that")
    else:
        lives -= 1
        if user_letter not in guessed:
            guessed.append(user_letter)
    if lives <= 0:
        print("You lost all your lives, You lose!")
        game_over = True
    elif word == "".join(guesses):
        print(f"Yay!!!, you guessed {word} correctly")
        game_over = True