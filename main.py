import datetime
# import turtle as t
# import random
# from turtle import Screen
#
# timmy = t.Turtle()
# timmy.speed("fastest")
# timmy.shape("arrow")
# t.colormode(255)
#
# def random_color():
#     r = random.randint(0,255)
#     g = random.randint(0,255)
#     b = random.randint(0,255)
#     return r,g,b
#
#
#
#
# def draw_spirograph(size_of_gap):
#     for _ in range(int(360/size_of_gap)):
#         timmy.setheading(timmy.heading() + size_of_gap)
#         timmy.circle(100)
#         timmy.pencolor(random_color())
#
# draw_spirograph(5)
#
# screen = t.Screen()
# screen.exitonclick()
t = datetime.datetime.now().time().strftime()

print(t)