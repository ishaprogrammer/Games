import turtle
from turtle import Screen,Turtle
import pandas
screen=Screen()
screen.title("INDIAN-STATE GAME")

image=r"C:\Users\isha\Desktop\python100Days\IndianStateGame.py\blank_map.gif"
screen.addshape(image)
turtle.shape(image)
csv_file=r"C:\Users\isha\Desktop\python100Days\IndianStateGame.py\Indian_States_Coordinates - Sheet1.csv"
data=pandas.read_csv(csv_file)
state=data.State.to_list()
x=data.x.to_list()
y=data.y.to_list()

sammy=Turtle()
sammy.penup()
sammy.hideturtle()

score=0
to_learn=[]
guessed_list=[]


def check_guess(guess):
    global score,x,y,guessed_list,to_learn
    normalized_guess = guess.lower()
    normalized_states = [state.lower() for state in state]
    if normalized_guess in normalized_states and normalized_guess not in guessed_list:
        score+=1
        print(guess.title())
        index=normalized_states.index(normalized_guess)
        sammy.goto(x[index],y[index])
        sammy.write(normalized_guess,align="center")
        guessed_list.append(normalized_guess)
    return True
    
screen.listen()
game_on=True
while game_on and len(guessed_list)<29:
    guess = screen.textinput(f"{score}/29 Guess the State", "Name a state?")
    if guess=="exit":
        break
    else:
        guessed_list.append(guess.title())
        game_on=check_guess(guess)
        
sammy.goto(0,220)
sammy.color("magenta")
sammy.write(f"final-score!: {score}/29",font=("Georgia",30),align="center")
missing_state=[states for states in state if states not in guessed_list]
data=pandas.DataFrame(missing_state)
data.to_csv("state_to_learn")
screen.mainloop()
