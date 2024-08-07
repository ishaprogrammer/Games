import random
import os
from art import logo
print(logo)
def clear_console():
        os.system('cls' if os.name == 'nt' else 'clear') 
choice=random.randint(1,100)
print("Welcome to the number Guessing Game!")
print("I am thinking of a number between 1-100")

def function():
    level=input("Choose difficulty level 'easy' or 'hard':")
    if level=="easy":
       lives=10   
    elif level=="hard":
       lives=5
    else:
        print("invalid choice")
    while lives>0:
        guess=int(input("Guess a number:"))
        if guess==choice:
            print("you've won!")
            break
        elif guess>choice:
            print("Too High")
        else:
            print("Too low")
       
        lives-=1
        print(f"you've made a wrong choice you lose a life! remaining lives:{lives}")
        if lives==0:
           print("You've lose")
           break 
function()
restart=input("Do you want to restart the game? 'yes' or 'no'")
if restart=="yes":
    clear_console()
    function()
elif restart=="no":
    print("Thank you for playing goodbye!")
    exit()
else:
    print("invalid choice")
    exit()
        
        
     
