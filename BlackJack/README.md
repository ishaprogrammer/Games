# Card Game: Blackjack

Welcome to the Blackjack card game! In this simple Python program, you can play against the computer and try to beat its score.

## How to Play

1. **Run the Game:**
   - Make sure you have Python installed.
   - Execute the `main.py` script in your terminal or IDE.

2. **Rules:**
   - You and the computer start with two random cards each.
   - The goal is to get a score as close to 21 as possible without going over.
   - An ace (11) can be counted as 1 if needed.
   - If your score exceeds 21, you lose.
   - If the computer's score exceeds 21, it loses.
   - If both scores are equal, it's a draw.
   - If either player has a blackjack (an ace and a 10-value card), they win instantly.

3. **Gameplay:**
   - Follow the prompts to draw additional cards or pass.
   - The computer will automatically draw cards until its score is at least 17.
   - The game will display the final hands and announce the winner.

## Example

```
$ python main.py
Your cards: [10, 7], current score: 17
Computer's first card: 4
Type 'y' to get another card, type 'n' to pass: y
Your cards: [10, 7, 3], current score: 20
Computer's first card: 4
Type 'y' to get another card, type 'n' to pass: n
Your final hand: [10, 7, 3], final score: 20
Computer's final hand: [4, 6, 10], final score: 20
Draw 🙃
```
