from turtle import Turtle, Screen
shape = Turtle()
shape.color("orange")
for _ in range(360):
    shape.forward(1)
    shape.right(1)
screen = Screen()
screen.exitonclick()