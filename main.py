from turtle import Screen
from paddles import Paddle


screen = Screen()
screen.title('PinPong')
screen.setup(800, 600)
screen.bgcolor('black')

right_paddle = Paddle()
right_paddle.move_paddle_to_start_position('right')
left_paddle = Paddle()
left_paddle.move_paddle_to_start_position('left')

screen.listen()
screen.onkey(right_paddle.move_up, 'Up')
screen.onkey(left_paddle.move_up, 'a')
screen.onkey(right_paddle.move_down, 'Down')
screen.onkey(left_paddle.move_down, 'z')

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