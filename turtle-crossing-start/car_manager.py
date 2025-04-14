from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.all_cars = []
        self.add_car()        
    
    def add_car(self):
        new_car = Turtle()
        new_car.shape("square")
        new_car.color(random.choice(COLORS))
        new_car.shapesize(stretch_len=2,stretch_wid=1)
        new_car.setheading(180)
        new_car.penup()
        y = random.randint(-250,250)
        new_car.goto(300,y)
        self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.forward(STARTING_MOVE_DISTANCE)



