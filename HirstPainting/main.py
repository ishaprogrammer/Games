import turtle as sammy
from turtle import colormode,Screen,screensize
import random
import colorgram
# rgb_colors=[]
# colors= colorgram.extract('hirst.py/download (1).jpg',20)
# for color in colors:
#     r=color.rgb.r
#     g=color.rgb.g
#     b=color.rgb.b
#     new_color=(r,g,b)
#     rgb_colors.append(new_color)
# print(rgb_colors)
color_list=[(213, 211, 210), (207, 214, 210), (199, 163, 119), (215, 208, 211), (210, 214, 218), (165, 187, 163), (38, 94, 115), (124, 38, 30), (52, 35, 34), (155, 76, 56), (113, 74, 83), (119, 163, 174), (195, 99, 73), (50, 130, 103), (124, 35, 42), (18, 56, 42), (8, 65, 84), (215, 197, 122), (102, 148, 74), (185, 153, 156)]
colormode(255)
sammy.speed("fastest")
sammy.penup()
sammy.hideturtle()
sammy.screensize(500,700)
sammy.setheading(225)#270-180 degrees
sammy.forward(250)#5 times 50
sammy.setheading(0)
num_of_dots=100
for dots in range(1,num_of_dots+1):
    sammy.dot(20,random.choice(color_list))
    sammy.forward(50)
    if dots%10==0:
        sammy.setheading(90)
        sammy.forward(50)
        sammy.setheading(180)
        sammy.forward(500)
        sammy.setheading(0)
    
    
sammy.exitonclick()

