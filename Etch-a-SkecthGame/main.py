from turtle import Turtle,Screen
sammy=Turtle()
def move_forward():
    sammy.forward(10)
def backwards():
    sammy.backward(10)
def counter_clockwise():
    sammy.left(90)
def clockwise():
    sammy.right(90)
    
def clear():
    sammy.clear()
    sammy.penup()
    sammy.home()
    sammy.pendown()
screen=Screen()
screen.listen()
screen.onkeypress(fun=move_forward,key="f")
screen.onkeypress(fun=backwards,key="b")
screen.onkeypress(fun=counter_clockwise,key="s")
screen.onkeypress(fun=clockwise,key="o")
screen.onkeypress(fun=clear,key="c")

screen.exitonclick()