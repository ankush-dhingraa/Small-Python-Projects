from turtle import Turtle, Screen
obj = Turtle()
screen = Screen()
# move_forward() is used for moving turtle forward by 10
def move_forwards():
    obj.forward(10)
# move_backward() is used for moving turtle forward by 10
def move_backwards():
    obj.backward(10)
# clockwise() is used for rotating turtle right by 10 degree angle
def clockwise():
    obj.right(10)
# counter_clockwise() is used for rotating turtle left by 10 degree angle
def counter_clockwise():
    obj.left(10)
#clear() is used for Delete the turtle’s drawings from the screen. 
def clear():
    obj.clear()

#Event listner
screen.listen()
#Set 'w' key to call move_forwards function.
screen.onkey(key="w",fun=move_forwards)
screen.onkey(key="s",fun=move_backwards)
screen.onkey(key="d",fun=clockwise)
screen.onkey(key="a",fun=counter_clockwise)
screen.onkey(key="c",fun=clear)
screen.exitonclick()