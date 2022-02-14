from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE = 10
Y_FINISH = 280


class Player(Turtle):
    def __init__(self):
        super().__init__('turtle')
        self.color('green')
        self.seth(90)
        self.penup()
        self.to_starting_position()
        self.move()
        self.finish = Y_FINISH

    def move(self):
        self.fd(MOVE)

    def to_starting_position(self):
        self.goto(STARTING_POSITION)
