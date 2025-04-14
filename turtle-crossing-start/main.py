import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("white")
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()

screen.listen()
screen.onkey(key="Up",fun=player.move_up)
screen.onkey(key="Down",fun=player.move_down)


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    car.add_car()
    car.move()
