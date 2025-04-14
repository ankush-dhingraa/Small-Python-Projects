from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        while game_is_on:
            self.shape("square")
            self.color(random.choice(COLORS))
            self.shapesize(stretch_len=2,stretch_wid=1)
            self.setheading(180)
            self.penup()
            self.x = random.choice([-1,1])*random.randint(0,270)
            self.y = random.choice([-1,1])*random.randint(0,270)
            self.goto(self.x, self.y)
    
    def add_car(self,game_status):
        
    def move(self):
        self.goto(self.xcor()-STARTING_MOVE_DISTANCE,self.y)



