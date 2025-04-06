import turtle
from turtle import Turtle, Screen
import random

def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return tuple((r,g,b))

graph = Turtle()
graph.speed(1000)
turtle.colormode(255)
def draw_spirograph(gap_size):
    for _ in range(int(360/gap_size)):
        graph.pencolor(random_color())
        graph.circle(100)
        graph.setheading(graph.heading()+gap_size)
draw_spirograph(5)

screen = Screen()
screen.exitonclick()