# Hangman Game

Welcome to the Hangman Game! In this Python program, you'll try to guess a hidden word by inputting individual letters. But be careful—you only have a limited number of lives!

## How to Play

1. **Run the Game:**
   - Make sure you have Python installed.
   - Execute the `main.py` script in your terminal or IDE.
   -import random module.
   -import word_list from hangman_words.
   -import logo from hangman_art.

2. **Rules:**
   - A random word is chosen from a predefined list.
   - You'll see underscores representing each letter in the word.
   - Guess a letter. If it's correct, the corresponding underscores will be replaced with the letter.
   - If you guess incorrectly, you lose a life.
   - The game ends when you either guess the entire word or run out of lives.

## Word List
The words for this game come from the `hangman_words.py` file, which contains a collection of words.

3. **Example:**
 ```
    | |
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |
                   |___/
['_', '_', '_', '_']
Guess a letter: m
you guessed m, which is not in the word, you lose a life
____

  +---+
  |   |
  O   |
      |
      |
      |
=========

['_', '_', '_', '_']
Guess a letter: t
you guessed t, which is not in the word, you lose a life
____

  +---+
  |   |
  O   |
  |   |
      |
      |
=========

['_', '_', '_', '_']
Guess a letter: w
you guessed w, which is not in the word, you lose a life
____

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========

['_', '_', '_', '_']
Guess a letter: p
you guessed p, which is not in the word, you lose a life
____

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========

['_', '_', '_', '_']
Guess a letter: t
you guessed t, which is not in the word, you lose a life
____

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========

['_', '_', '_', '_']
Guess a letter: m
you guessed m, which is not in the word, you lose a life
you've lost
____

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========

 ```

