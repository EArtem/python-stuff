from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Arial', 24, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.write(f'Score: {self.score} High Score: {self.high_score}', False, ALIGNMENT, FONT)

    def update_score(self):
        self.clear()
        self.write(f'Score: {self.score} High Score: {self.high_score}', False, ALIGNMENT, FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()
