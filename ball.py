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
        self.speed(0)
        self.x_start = self.xcor()
        self.y_start = self.ycor()
        self.x_move = 10
        self.y_move = 10
        self.speed_control = 0.1
        self.move()

    def move(self):
        new_y = self.ycor() + self.y_move
        new_x = self.xcor() + self.x_move
        time.sleep(self.speed_control)
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def reset_ball(self):
        self.speed_control = 0.1
        self.goto(self.x_start, self.y_start)
        self.bounce_x()
