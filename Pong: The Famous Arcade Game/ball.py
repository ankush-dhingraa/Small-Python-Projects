from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_len=1,stretch_wid=1)
        self.penup()
        self.goto(0,0)

    def move(self):
        new_x = self.xcor() + 1
        new_y = self.ycor() + 1  
        self.goto(new_x,new_y)     
            