import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("black")

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.up, "Up")
screen.onkey(player.down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.createcar()
    car_manager.move()

    # 🚗 Check for collision with any car
    for car in car_manager.allcars:
        if car.distance(player) < 25:
            scoreboard.game_over()
            game_is_on = False

    # 🏁 Check if player reached finish line
    if player.is_at_finish_line():
        player.reset_position()
        car_manager.increase_speed()
        scoreboard.increase_level()

screen.exitonclick()
