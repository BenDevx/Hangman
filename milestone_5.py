import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        """
        Initializes the Hangman game with the given word list and number of lives.

        Parameters:
        - word_list (list): List of words for the game.
        - num_lives (int): Number of lives for the player (default is 5).
        """
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list).lower()  # Pick a random word
        self.word_guessed = ['_'] * len(self.word)  # Initialize with underscores
        self.num_letters = len(set(self.word))  # Count unique letters
        self.list_of_guesses = []  # Keep track of previous guesses

    def check_guess(self, guess):
        """
        Checks if the guessed letter is in the word and updates the game state accordingly.

        Parameters:
        - guess (str): The guessed letter.
        """
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! '{guess}' is in the word.")
            for index, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[index] = guess
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, '{guess}' is not in the word. Try again.")
            print(f"Lives remaining: {self.num_lives}")

    def ask_for_input(self):
        """
        Prompts the user to input a guess and checks its validity. Updates the game state accordingly.
        """
        while True:
            guess = input("Guess a letter: ")
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break


def play_game(word_list):
    """
    Runs the Hangman game.

    Parameters:
    - word_list (list): List of words to use in the game.
    """
    num_lives = 5  # Set the number of lives
    game = Hangman(word_list, num_lives)  # Create a Hangman instance

    while True:
        # Lose condition
        if game.num_lives == 0:
            print("You lost!")
            print(f"The word was: {game.word}")
            break
        # Continue playing
        elif game.num_letters > 0:
            print(f"Word guessed so far: {' '.join(game.word_guessed)}")
            game.ask_for_input()
        # Win condition
        else:
            print("Congratulations! You won the game!")
            print(f"The word was: {game.word}")
            break


# Start the game
if __name__ == "__main__":
    word_list = ["apple", "banana", "cherry", "grape", "orange"]  # Example word list
    play_game(word_list)
