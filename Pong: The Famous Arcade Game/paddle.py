from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.color("white")
        self.shapesize(stretch_len=1,stretch_wid=5)
        self.shape("square")
        self.penup()
        self.goto(position)
    
    def up(self):
        new_y = self.ycor() + 20
        self.goto(x=self.xcor(), y=new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(x=self.xcor(), y=new_y)