from turtle import Turtle, Screen
obj = Turtle()
screen = Screen()
screen.setup(width=500,height=400)
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
screen.textinput(title="Make your bet")
for color in colors:

screen.exitonclick()