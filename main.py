from turtle import Screen
from paddles import Paddle
from ball import Ball
from scoreboard import Scoreboard

RIGHT_PADDLE_POSITION = (380, 0)
LEFT_PADDLE_POSITION = (-390, 0)

screen = Screen()
screen.title('PinPong')
screen.setup(800, 600)
screen.bgcolor('black')
screen.tracer(0)

score = Scoreboard()

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
    # top and bottom wall bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # collision with paddles
    if ball.xcor() >= (RIGHT_PADDLE_POSITION[0] - 20) and ball.distance(right_paddle.position()) < 50 \
            or ball.xcor() <= (LEFT_PADDLE_POSITION[0] + 20) and ball.distance(left_paddle.position()) < 50:
        ball.bounce_x()
    # paddle miss the ball
    if ball.xcor() > (RIGHT_PADDLE_POSITION[0] + 20):
        ball.reset_ball()
        score.l_point()
    if ball.xcor() < (LEFT_PADDLE_POSITION[0] - 20):
        ball.reset_ball()
        score.r_point()

screen.exitonclick()
