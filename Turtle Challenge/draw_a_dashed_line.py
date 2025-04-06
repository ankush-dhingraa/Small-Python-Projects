from turtle import Turtle, Screen
line = Turtle()
# for _ in range(5):
#     line.forward(10)
#     line.color("white")
#     line.forward(10)
#     line.color("black")
for _ in range(10):
    line.forward(5)
    line.penup()
    line.forward(5)
    line.pendown()
screen = Screen()
screen.exitonclick()
