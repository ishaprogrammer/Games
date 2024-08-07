import random
import os
from art import logo
from art import vs
from data import data
def game():
    def clear_console():
            os.system('cls' if os.name == 'nt' else 'clear') 
    
    print("Welcome to the game!👋")
    def function():
        answer=[(f"{A['name']},a {A['description']} from {A['country']}"),(f"{B['name']},a {B['description']} from {B['country']}")]
        return answer
    stop=False
    score=0
    A=random.choice(data)
    while not stop:
        print(logo)
        print(f"score:{score}")
        answer1=print(f"{A['name']},a {A['description']} from {A['country']}")
        print(vs)
        B=random.choice(data)
        answer2=print(f"{B['name']},a {B['description']} from {B['country']}")
        player=input(" Who has more followers? A or B:")
        
        if player=="A":
            if A['follower_count'] > B['follower_count']:
                print("you are right😎")
                score+=1
               
                A=B
                while A==B:
                    B=random.choice(data)
                clear_console()
                
            else: 
                print("you are wrong☹️")
                print(f"score:{score}")
                stop=True
                            
        elif player=="B":
            if B['follower_count'] > A['follower_count']:
                print("you are right😎")
                score+=1
                
                A=B
                while A==B:
                    B=random.choice(data)
                clear_console()
               
                
            else: 
                print("you are wrong☹️") 
                print(f"score:{score}")
                stop=True
game()
def clear_console():
            os.system('cls' if os.name == 'nt' else 'clear') 
again=input("Do you want to play the game again 😇? yes or no:")  
if again=="yes":
    clear_console()
    game()
elif again=="no":
    print("Thank you for playing, Goodbye!😄")
    exit()
else:
    print("invalid text")
    exit()
          