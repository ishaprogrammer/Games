import random
from hangman_words import word_list
from hangman_art import logo
print(logo)
choice=random.choice(word_list)
word_length=len(choice)
end_of_game=False
lives=6
display=[]
for _ in range(word_length):
    display+="_"
    
while not end_of_game:
    
    print(display)
    guess=input("Guess a letter:").lower()
    if guess in display:
        print(f"you've already guessed the letter {guess}")
    for position in range(word_length):
        letter=choice[position]
        if guess==letter:
            display[position]=letter
    if guess not in display:
        print(f"you guessed {guess},which is not in the word,you lose a life")
        lives-=1
        if lives==0:
           end_of_game==True 
           print("you've lose") 
    print(f"{''.join(display)}")
    if "_" not in display:
        end_of_game==True
        print("you've won!")
    from hangman_art import stages
    print(stages[lives])
    