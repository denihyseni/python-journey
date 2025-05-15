from turtle import Screen

from scoreboard import Scoreboard
from player import Player
from car_manager import CarManager
import time


screen = Screen()
screen.setup(600,600)
screen.bgcolor("white")
screen.tracer(0)


scoreboard = Scoreboard()
player = Player()
car_manager = CarManager()


screen.listen()
screen.onkey(player.move_up,"Up")



game_on = True

while game_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_on = False
            scoreboard.game_over()

    if player.is_at_finish_line():
        player.go_to_start()
        scoreboard.increase_level()
        car_manager.level_up()





screen.exitonclick()