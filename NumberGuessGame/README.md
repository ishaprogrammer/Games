# Number Guessing Game

Welcome to the Number Guessing Game! In this Python program, you'll try to guess a randomly chosen number between 1 and 100. Let's see if you can beat the computer!

## How to Play

1. **Run the Game:**
   - Make sure you have Python installed.
   - Execute the `main.py` script in your terminal or IDE.
   - import random module.
   - import ascii art from art.py.
   - I have also imported os module to clear the console but its optional.

2. **Rules:**
   - You start with a certain number of lives (based on the difficulty level).
   - Guess a number, and the program will tell you if it's too high or too low.
   - Keep guessing until you find the correct number or run out of lives.
   - The game will display whether you've won or lost.

3. **Difficulty Levels:**
   - **Easy:** You have 10 lives.
   - **Hard:** You have 5 lives.

## Example

```
$ python main.py
                                    | | | |                                | |
   __ _ _   _  ___  ___ ___  | |_| |__   ___   _ __  _   _ _ __ ___ | |__   ___ _ __
  / _` | | | |/ _ \/ __/ __| | __| '_ \ / _ \ | '_ \| | | | '_ ` _ \| '_ \ / _ \ '__|
 | (_| | |_| |  __/\__ \__ \ | |_| | | |  __/ | | | | |_| | | | | | | |_) |  __/ |
  \__, |\__,_|\___||___/___/  \__|_| |_|\___| |_| |_|\__,_|_| |_| |_|_.__/ \___|_|
   __/ |
  |___/

Welcome to the Number Guessing Game!
I am thinking of a number between 1-100
Choose difficulty level 'easy' or 'hard': easy
Guess a number: 50
Too low
you've made a wrong choice, you lose a life! Remaining lives: 9
Guess a number: 75
Too high
you've made a wrong choice, you lose a life! Remaining lives: 8
...
Guess a number: 63
You've won!
Do you want to restart the game? 'yes' or 'no': no
Thank you for playing! Goodbye!
```
