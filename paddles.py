from turtle import Turtle
PADDLE_SHAPE = 'square'
PADDLE_HEIGHT = 1
PADDLE_WIDTH = 5
PADDLE_COLOR = 'white'


class Paddle(Turtle):
    def __init__(self, paddle_position):
        super().__init__(PADDLE_SHAPE)
        self.shapesize(PADDLE_HEIGHT, PADDLE_WIDTH)
        self.color(PADDLE_COLOR)
        self.penup()
        self.seth(90)
        self.move_paddle_to_start_position(paddle_position)

    def move_paddle_to_start_position(self, position):
        self.goto(position)

    def move_up(self):
        self.fd(20)

    def move_down(self):
        self.bk(20)