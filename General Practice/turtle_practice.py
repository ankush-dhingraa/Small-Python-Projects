from turtle import Turtle, Screen

obj = Turtle()
colours = ["red", "green", "black", "blue"]
obj.shape("turtle")
for i in colours:
    obj.color(i)
    obj.forward(150)
    obj.right(90)














screen = Screen()
screen.exitonclick()