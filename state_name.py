from turtle import Turtle
FONT = ('Arial', 14, 'normal')


class StateName:
    def __init__(self):
        self.state = Turtle()
        self.state.hideturtle()
        self.state.penup()

    def name_state(self, state_name: list):
        self.state.write(state_name[0], False, 'center', FONT)

    def place_state_name_on_map(self, x_cor, y_cor):
        self.state.goto(x_cor[0], y_cor[0])