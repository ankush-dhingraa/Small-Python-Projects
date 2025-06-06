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
score = Scoreboard()

screen.listen()
screen.onkey(key="Up",fun=player.move_up)
screen.onkey(key="Down",fun=player.move_down)


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.add_car()
    car.move()

    #detect collition with cars 
    for cars in car.all_cars:
        if cars.distance(player) < 20:
            game_is_on = False
            score.game_over()
    #detect if player cross other side
    if player.ycor() > 295:
        score.score +=1
        score.update_scoreboard()
        player.starting_position()
        car.level_up()

screen.exitonclick()
