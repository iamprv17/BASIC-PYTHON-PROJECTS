#Hangman game

import random

# list of words to be used in the game
words = ["python", "programming", "code", "computer", "science"]

# select a random word from the list
word = random.choice(words)

# initialize a list of underscores the same length as the word
display = ["_"] * len(word)

# initialize a list to store the letters guessed
guesses = []

# set the number of lives/guesses the player has
lives = 6

# start the game loop
while lives > 0:
    # print the word with underscores
    print(" ".join(display))
    print("Guesses:", " ".join(guesses))
    print("Lives:", lives)
    # get player's guess
    guess = input("Guess a letter: ").lower()
    if guess in guesses:
        print("You already guessed that letter. Try again.")
    elif guess in word:
        # update the display list with the guessed letter
        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess
        if "_" not in display:
            print("Congratulations! You guessed the word:", word)
            break
    else:
        lives -= 1
        if lives == 0:
            print("You lost! The word was:", word)
        else:
            print("Incorrect guess.")
            guesses.append(guess)
