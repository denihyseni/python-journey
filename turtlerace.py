import turtle
from random import randint
from turtle import Turtle,Screen
import random
is_race = False


x = -225
y = -70
screen = Screen()
screen.setup(width=500,height=400)


user_bet = screen.textinput(title="Make your bet",prompt="Which turtle will win the race? Enter a color: ")
colors = ['red','green','blue','orange','yellow','purple']
all_turtles = []


for n in range(0,6):
    new_turtle = Turtle("turtle")
    new_turtle.penup()
    new_turtle.color(colors[n])
    new_turtle.goto(x, y)
    all_turtles.append(new_turtle)
    y+=30

if user_bet:
    is_race = True

while is_race:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race = False
            winnner = turtle.pencolor()
            if winnner == user_bet:
                print(f'{winnner} has won')
            else:
                print(f'{user_bet} has lost. The winning color is {winnner}')


        rnd_distance = random.randint(0,10)
        turtle.forward(rnd_distance)












screen.exitonclick()