from turtle import Turtle,Screen
shape = Turtle()
angle = 360
sides = 3
for _ in range(10):
    for side in range(sides):
        shape.forward(50)
        shape.right(angle/sides)
    sides+=1
screen = Screen()
screen.exitonclick()