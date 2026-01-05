import random
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.allcars=[]

    def createcar(self):
        new = Turtle("square")
        new.shapesize(stretch_wid=2, stretch_len=1)
        new.penup()
        new.color(random.choice(COLORS))
        randomy = random.randint(-250, 250)
        new.goto(300, randomy)
        new.setheading(180)  # Face left
        self.allcars.append(new)

    def move(self):
        for car in self.allcars:
            car.backward(STARTING_MOVE_DISTANCE)