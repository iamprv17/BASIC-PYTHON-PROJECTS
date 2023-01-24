#Guess the number game.

import random

# generate a random number between 1 and 100
number = random.randint(1, 100)

# set the initial number of guesses
guesses = 0

# start the game loop
while True:
    # get the player's guess
    guess = int(input("Guess a number between 1 and 100: "))

    # increment the number of guesses
    guesses += 1

    # check if the guess is correct
    if guess == number:
        print("Congratulations! You guessed the number in", guesses, "tries.")
        break
    # check if the guess is too high
    elif guess > number:
        print("Too high! Try again.")
    # otherwise, the guess must be too low
    else:
        print("Too low! Try again.")
