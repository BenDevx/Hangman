word_list = ["pineapple", "orange", "mango", "apple", "pear"]
print(word_list)

import random
word = random.choice(word_list)
print(word)

guess = input("Enter a single letter: ")
print(f"You entered: {guess}")

if len(guess) == 1 and guess.isalpha():
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")




while True:
    guess = input("Guess a letter: ")

    if len(guess) == 1 and guess.isalpha():
        print("Good guess!")
        break
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")



import random

# Define a list of words
word_list = ["pineapple", "orange", "mango", "apple", "pear"]

# Randomly choose a secret word
secret_word = random.choice(word_list)

# Continuously prompt the user until a valid guess is made
while True:
    guess = input("Guess a letter: ")

    # Validate the input
    if len(guess) == 1 and guess.isalpha():
        # Check if the guess is in the secret word
        if guess in secret_word:
            print(f"Good guess! '{guess}' is in the word.")
        else:
            print(f"Sorry, '{guess}' is not in the word. Try again.")
        break  # Exit the loop after the first valid guess
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")




import random

# Define a list of words
word_list = ["pineapple", "orange", "mango", "apple", "pear"]
secret_word = random.choice(word_list)

# Define check_guess function
def check_guess(guess):
    # Convert guess to lowercase
    guess = guess.lower()
    if guess in secret_word:
        print(f"Good guess! '{guess}' is in the word.")
    else:
        print(f"Sorry, '{guess}' is not in the word. Try again.")

# Define ask_for_input function
def ask_for_input():
    while True:
        # Prompt the user for input
        guess = input("Guess a letter: ")

        # Validate input
        if len(guess) == 1 and guess.isalpha():
            # Call check_guess if valid
            check_guess(guess)
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")

# Call ask_for_input to test
ask_for_input()

