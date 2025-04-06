import turtle
from turtle import Turtle, Screen
import random
walk = Turtle()
turtle.colormode(255)
def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return tuple((r,g,b))
directions = [0,90,180,270]
walk.pensize(10)
walk.speed(55)
for _ in range(100):
    walk.pencolor(random_color())
    walk.forward(20)
    walk.setheading(random.choice(directions))
screen = Screen()
screen.exitonclick()