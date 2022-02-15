from turtle import Turtle, Screen
MOVE_DISTANCE = 20
SNAKE_SPEED = 0
SNAKE_SIZE = 3


class Snake:

    def __init__(self):
        self.snake = []
        self.screen = Screen()
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        for _ in range(0, SNAKE_SIZE + 1):
            snake_element = Turtle('square')
            snake_element.color('white')
            snake_element.penup()
            snake_element.speed(SNAKE_SPEED)
            self.snake.append(snake_element)
        x_position = 0
        for segment in self.snake:
            segment.setx(x_position)
            x_position -= 20
        self.screen.update()

    def add_segment(self, position):
        new_segment = Turtle('square')
        new_segment.color('white')
        new_segment.penup()
        new_segment.goto(position)
        self.snake.append(new_segment)

    def reset(self):
        for segment in self.snake:
            segment.goto(1000, 1000)
        self.snake.clear()
        self.create_snake()
        self.head = self.snake[0]

    def extend(self):
        self.add_segment(self.snake[-1].position())

    def move(self):
        for segment_num in range(len(self.snake) - 1, 0, -1):
            self.snake[segment_num].goto(self.snake[segment_num - 1].position())
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() == 0:
            self.head.seth(90)
        if self.head.heading() == 180:
            self.head.seth(90)

    def down(self):
        if self.head.heading() == 0:
            self.head.seth(270)
        if self.head.heading() == 180:
            self.head.seth(270)

    def left(self):
        if self.head.heading() == 90:
            self.head.lt(90)
        if self.head.heading() == 270:
            self.head.rt(90)

    def right(self):
        if self.head.heading() == 90:
            self.head.rt(90)
        if self.head.heading() == 270:
            self.head.lt(90)
