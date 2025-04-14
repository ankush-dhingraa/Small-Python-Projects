from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.starting_position()
        self.setheading(90)
    def starting_position(self):
        self.goto(STARTING_POSITION)

    def move_up(self):
        x = self.xcor()
        y = self.ycor() + MOVE_DISTANCE
        self.goto(x,y)
    def move_down(self):
        x = self.xcor()
        y = self.ycor() - MOVE_DISTANCE
        self.goto(x,y)
    def relocate(self):
        self.goto(STARTING_POSITION)

