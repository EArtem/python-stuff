from turtle import Turtle
import time
WIDTH = 1
HEIGHT = 1
COLOR = 'white'


class Ball(Turtle):
    def __init__(self):
        super().__init__('square')
        self.shapesize(WIDTH, HEIGHT)
        self.color(COLOR)
        self.penup()
        self.speed(9)
        self.x_move = 10
        self.y_move = 10
        self.move()

    def move(self):
        new_y = self.ycor() + self.y_move
        new_x = self.xcor() + self.x_move
        time.sleep(0.1)
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1
