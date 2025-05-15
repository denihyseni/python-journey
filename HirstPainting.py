import turtle
from turtle import Turtle , Screen
import random
import colorgram


color_list = [(140, 22, 67), (77, 107, 190), (142, 151, 43), (235, 211, 82),
              (218, 164, 56), (110, 151, 220), (232, 205, 218), (60, 128, 64),
              (178, 68, 142), (3, 67, 152), (207, 105, 56), (152, 99, 66), (149, 37, 36)]
#10x10
x = -275
y = -300
count = 0

timmy = Turtle()
turtle.colormode(255)
timmy.penup()
timmy.hideturtle()
timmy.goto(x, y)
for rows in range(10):
    for _ in range(10):
        timmy.pendown()
        timmy.dot(20,random.choice(color_list))
        timmy.penup()
        timmy.forward(50)
        count+=1
        if count == 10:
            y+=50
            timmy.goto(x,y)
            count = 0


screen = Screen()
screen.exitonclick()