import turtle
from turtle import Turtle, Screen
import random
walk = Turtle()
colors = [
    "skyblue",
    "coral",
    "goldenrod",
    "mediumseagreen",
    "tomato",
    "slateblue",
    "orchid",
    "crimson",
    "turquoise",
    "salmon"
]
directions = [0,90,180,270]
walk.pensize(10)
walk.speed(15)
for _ in range(100):
    walk.color(random.choice(colors))
    walk.forward(25)
    walk.setheading(random.choice(directions))
screen = Screen()
screen.exitonclick()