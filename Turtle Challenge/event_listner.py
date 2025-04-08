from turtle import Turtle, Screen
obj = Turtle() 
screen = Screen()

def move():
    obj.forward(10)
screen.listen()
screen.onkey(key="space",fun=move)
screen.exitonclick()