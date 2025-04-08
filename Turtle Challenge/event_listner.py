from turtle import Turtle, Screen
obj = Turtle() 
screen = Screen()

def move_forwards():
    obj.forward(10)
def move_backwards():
    obj.backward(10)
def clockwise():
    obj.right(10)
def counter_clockwise():
    obj.left(10)

screen.listen()
screen.onkey(key="w",fun=move_forwards)
screen.onkey(key="s",fun=move_backwards)
screen.exitonclick()