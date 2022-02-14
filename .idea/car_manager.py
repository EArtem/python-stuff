import time
from turtle import Turtle
import random
COLORS = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
Y_START = list(range(-250, 230))
X_START = 320
SHAPESIZE = (1, 2)

class CarManager():

    def __init__(self):
        self.all_cars = []
        self.move()

    def create_car(self):
        new_car = Turtle('square')
        new_car.color(random.choice(COLORS))
        new_car.shapesize(1, 2)
        new_car.penup()
        new_car.goto(X_START, random.choice(Y_START))
        self.all_cars.append(new_car)
        self.speed_increment = STARTING_MOVE_DISTANCE

    def move(self):
        for car in self.all_cars:
            car.backward(self.speed_increment)

    def increase_speed(self):
        self.speed_increment += MOVE_INCREMENT
