from turtle import Screen
from player import Player
import time
from car_manager import CarManager
from turtle import Turtle
from scoreboard import Scoreboard


screen = Screen()
screen.setup(600, 600)
screen.title('Capstone Crossing')
screen.listen()
screen.tracer(0)

scoreboard = Scoreboard()

player = Player()
screen.onkey(player.move, 'Up')

game_is_on = True
game_run = 0
car_manager = CarManager()
sleep_time = 0.1
while game_is_on:
    if game_run % 6 == 0:
        car_manager.create_car()
    time.sleep(sleep_time)
    screen.update()
    car_manager.move()
    if player.ycor() > player.finish:
        player.to_starting_position()
        sleep_time *= 0.9
        scoreboard.bump_score()
        scoreboard.update_scoreboard()
        car_manager.increase_speed()
    for car in car_manager.all_cars:
        if player.distance(car) < 24:
            game_is_on = False
            game_over = Turtle()
            game_over.write('Game Over', False, 'center', ('Courier', 16, 'normal'))
    game_run += 1

screen.exitonclick()
