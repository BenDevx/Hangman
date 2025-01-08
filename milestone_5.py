import random

class Hangman:
    def __init__(self, word_list, num_lives=5): 
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list).lower()  # Code to pick a random word from word_list
        self.word_guessed = ['_'] * len(self.word)  # Here will create blanks for the guessed word
        self.num_letters = len(set(self.word))  # Count unique letters
        self.list_of_guesses = []  # Keep track of guessed letters

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:  # To check if the guess is correct
            print(f"Good guess! '{guess}' is in the word.")
            for index, letter in enumerate(self.word):
                if letter == guess:  # Replace blanks with the guessed letter
                    self.word_guessed[index] = guess
            self.num_letters -= 1  # Reduce the count of unique letters left
        else:  # Wrong guess
            self.num_lives -= 1
            print(f"Sorry, '{guess}' is not in the word.")
            print(f"Lives remaining: {self.num_lives}")

    def ask_for_input(self):
        while True:
            guess = input("Guess a letter: ")
            if len(guess) != 1 or not guess.isalpha():  # Check if input is not equal to 1 or not an alphabet
                print("Invalid input. Please enter one letter.")
            elif guess in self.list_of_guesses:  # Check if input has already being guessed
                print("You already tried that letter.")
            else:
                self.check_guess(guess)  # Check the guess
                self.list_of_guesses.append(guess)  # Add to guessed list
                break


def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)

    while True:
        if game.num_lives == 0:  # Check if player lost
            print("You lost!")
            print(f"The word was: {game.word}")
            break
        elif game.num_letters > 0:  # Continue the game if letters remain
            print(f"Word guessed so far: {' '.join(game.word_guessed)}")
            game.ask_for_input()
        else:  # Check if player won
            print("Congratulations! You won!")
            print(f"The word was: {game.word}")
            break


if __name__ == "__main__":
    word_list = ["apple"]
    play_game(word_list)
