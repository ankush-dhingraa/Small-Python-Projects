from turtle import Turtle, Screen

shape = Turtle()
shape.color("green")
for i in range(4):
    shape.forward(100)
    shape.right(90)
screen = Screen()
screen.exitonclick()