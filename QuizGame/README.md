# Quiz Game

Welcome to the Quiz Game! In this Python program, you'll answer a series of true/false questions. Let's see how well you know these fun facts!

## How to Play

1. **Run the Game:**
   - Make sure you have Python installed.
   - Execute the `main.py` script in your terminal or IDE.

2. **Rules:**
   - You'll be presented with a series of questions.
   - Answer each question as "True" or "False."
   - Your score will be displayed at the end.

## Questions Source
The questions for this quiz come from the `data.py` file, which contains interesting facts.

- **Question Class:**
  - The `Question` class encapsulates a single question and its corresponding answer.
  - It has two attributes:
    - `text`: The text of the question (e.g., "A slug's blood is green.").
    - `answer`: The correct answer (either "True" or "False").
  - This class allows you to create question objects and organize them into a list for the quiz.

- **QuizBrain Class:**
  - The `QuizBrain` class manages the flow of the quiz by handling questions, user input, and scoring.
  - It keeps track of the current question number, the list of questions, and the player's score.
  - Here are its key methods:
    - `__init__(self, q_list)`: Initializes the quiz with the provided question list.
    - `next_question(self)`: Displays the next question, collects the user's answer, and checks if it's correct.
    - `still_has_question(self)`: Determines if there are more questions to ask.
    - `check_answer(self, answer, correct_answer)`: Compares the user's answer with the correct answer and updates the score.

3. **Example:**
   ```
   Welcome to the game!👋
   Q.1: A slug's blood is green. (True/False) True
   correct
   ...
   you've completed the Quiz!
   your final score is 10/12
   ```

