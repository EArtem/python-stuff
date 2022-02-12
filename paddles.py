from turtle import Turtle
PADDLE_SHAPE = 'square'
PADDLE_HEIGHT = 1
PADDLE_WIDTH = 5
PADDLE_COLOR = 'white'
RIGHT_PADDLE_POSITION = (380, 0)
LEFT_PADDLE_POSITION = (-390, 0)


class Paddle(Turtle):
    def __init__(self):
        super().__init__(PADDLE_SHAPE)
        self.shapesize(PADDLE_HEIGHT, PADDLE_WIDTH)
        self.color(PADDLE_COLOR)
        self.penup()
        self.seth(90)

    def move_paddle_to_start_position(self, position):
        if position == 'right':
            self.goto(RIGHT_PADDLE_POSITION)
        else:
            self.goto(LEFT_PADDLE_POSITION)

    def move_up(self):
        self.fd(20)

    def move_down(self):
        self.bk(20)