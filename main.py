from turtle import Screen
import time
import snake
from food import Food
from score import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor('black')
screen.title('Snake Game')

snake = snake.Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

game_is_on = True
score = 0
score_board = Scoreboard()
while game_is_on:
    screen.update()
    snake.move()
    time.sleep(0.15)

    # eat the food and extend the snake
    if snake.head.distance(food) < 15:
        food.refresh()
        score_board.increase_score()
        snake.extend()

    # Detect collision with walls
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        score_board.reset()
        snake.reset()

    # Detect collision with tail
    for segment in snake.snake[1:]:
        if snake.head.distance(segment) < 10:
            score_board.reset()
            snake.reset()
screen.exitonclick()
