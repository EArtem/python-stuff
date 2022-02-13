from turtle import Screen
from paddles import Paddle
from ball import Ball
RIGHT_PADDLE_POSITION = (380, 0)
LEFT_PADDLE_POSITION = (-390, 0)

screen = Screen()
screen.title('PinPong')
screen.setup(800, 600)
screen.bgcolor('black')
screen.tracer(0)

right_paddle = Paddle(RIGHT_PADDLE_POSITION)
left_paddle = Paddle(LEFT_PADDLE_POSITION)
ball = Ball()

screen.listen()
screen.onkey(right_paddle.move_up, 'Up')
screen.onkey(right_paddle.move_down, 'Down')
screen.onkey(left_paddle.move_up, 'a')
screen.onkey(left_paddle.move_down, 'z')

game_is_on = True
while game_is_on:
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.xcor() >= (RIGHT_PADDLE_POSITION[0] - 20) and ball.distance(right_paddle.position()) < 50\
            or ball.xcor() <= (LEFT_PADDLE_POSITION[0] + 20) and ball.distance(left_paddle.position()) < 50:
        ball.bounce_x()


screen.exitonclick()

'''
1. class ball
    1.1 def start game - ball starts to move to randon x that = screen x, y that == y max or y min
    1.2 top and bottom edges should deflect the ball
    1.3 planks should reflect the ball
    1.4 respawn on the centre
2. Class planks - respawn on the left and right edges (might be under the same class with ball, as table elements)
    2.1 should have methods to move up and down;

3. class scoreboard should calculate score:
    3.1 should have left and right players
    3.2 If ball position < x.max_left
        right player score ++
    3.3 If ball position > x.max_right
        left player score ++

'''
