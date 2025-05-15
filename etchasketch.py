from turtle import Turtle,Screen



timmy = Turtle()
screen = Screen()

def w():
    timmy.forward(30)

def s():
    timmy.backward(30)

def a():
    timmy.left(10)

def d():
    timmy.right(10)

def c():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()

screen.listen()
screen.onkey(key="w", fun=w)
screen.onkey(key="a", fun=a)
screen.onkey(key="s", fun=s)
screen.onkey(key="d", fun=d)
screen.onkey(key="c", fun=c)
screen.exitonclick()