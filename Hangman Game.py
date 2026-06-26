'''
Project Name: HANGMAN GAME

Author: Saran Selvam

Description: 1.Hangman is a word-guessing game where the player guesses one letter at a time to reveal a hidden word.
             2.Each incorrect guess reduces the number of remaining chances, bringing the player closer to losing the game.
             3.The player wins by guessing all the letters correctly before running out of attempts.

'''

import random

words = [
    "python",
    "hacker",
    "internet",
    "hangman",
    "animal",
    "java"
]

lives = 6

word = random.choice(words)

guessed_word = ["_"] * len(word)

guessed_letters = []

print("===== HANGMAN GAME =====")

print("You have only 6 Chance.")

while lives > 1 and "_" in guessed_word:
    print(" ".join(guessed_word))

    if not guessed_letters:
        print("Guessed Letters: None")
    else:
        print("Guessed Letters:", " ".join(guessed_letters))

    guess = str(input("Enter a letter: ")).lower()

    # Validate input
    if len(guess) != 1:
        print("Please enter only one alphabet.")
        continue

    # Check repeated guess
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Correct guess
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
        
    else:
        lives -= 1
        print("Incorrect!")

#Result
if "_" not in guessed_word:
    print("\nCongratulations! You guessed the word:", word.upper())
else:
    print("\nGame Over!")
    print("The word was:", word.upper())


        

        


   


    