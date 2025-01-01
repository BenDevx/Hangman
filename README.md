# Hangman Game

## Table of Contents
- [Description](#description)
- [Installation Instructions](#installation-instructions)
- [Usage Instructions](#usage-instructions)
- [File Structure](#file-structure)
- [License Information](#license-information)

## Description
The Hangman Game is a Python-based word-guessing game that allows users to guess a randomly selected word, one letter at a time. Players have a limited number of lives and must guess the word before their lives run out. This project aims to improve familiarity with Python programming concepts, including classes, methods, loops, and input handling.

### Features:
- Word guessing with dynamic feedback for each guess.
- Tracks guessed letters and ensures valid inputs.
- Win and lose conditions based on the guessed word and remaining lives.

### What I Learned:
- Designing and structuring Python classes and methods.
- Handling user inputs and validating them effectively.
- Implementing core game mechanics using loops and conditionals.
- Writing readable and maintainable code with clear documentation.

## Installation Instructions
1. Clone or download the repository from GitHub:
   ```bash
   git clone https://github.com/username/hangman-game.git
   ```
2. Navigate to the project directory:
   ```bash
   cd hangman-game
   ```
3. Ensure you have Python installed (version 3.6 or above). You can check by running:
   ```bash
   python3 --version
   ```
4. Run the game:
   ```bash
   python3 milestone_5.py
   ```

## Usage Instructions
1. When prompted, enter a single letter to guess a part of the word.
2. If the letter is correct, it will appear in the correct position(s) in the word.
3. If the letter is incorrect, you lose a life. You have five lives in total.
4. Keep guessing until you either complete the word or lose all your lives.
5. The game provides feedback after every guess and announces the result when the game ends.

### Example:
```bash
Guess a letter: a
Sorry, 'a' is not in the word. Try again.
Lives remaining: 4
Guess a letter: e
Good guess! 'e' is in the word.
Word guessed so far: _ e _ _ y
```

## File Structure
```
.
|-- milestone_4.py         # Contains the core Hangman class implementation
|-- milestone_5.py         # Combines all milestones and includes the game loop
|-- README.md              # Documentation file
```

## License Information
This project is open-source and is licensed under the MIT License. Feel free to use, modify, and distribute the code with attribution.

