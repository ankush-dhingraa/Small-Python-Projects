from turtle import Turtle, Screen
obj = Turtle()
screen = Screen()
# move_forward() is used for moving turtle forward by 10
def move_forwards():
    obj.forward(10)
# move_backward() is used for moving turtle forward by 10
def move_backwards():
    obj.backward(10)
# turn_right() is used for rotating turtle right by 10 degree angle
def turn_right():
    new_heading = obj.heading()+10
    obj.setheading(new_heading)
# turn_left() is used for rotating turtle left by 10 degree angle
def turn_left():
    new_heading = obj.heading()-10
    obj.setheading(new_heading)
#clear() is used for Delete the turtle’s drawings from the screen. 
def clear():
    obj.clear()
    obj.penup()
    obj.goto(0,0)
    obj.setheading(0)

#Event listner
screen.listen()
#Set 'w' key to call move_forwards() function.
screen.onkey(key="w",fun=move_forwards)

#Set 's' key to call move_backwards() function.
screen.onkey(key="s",fun=move_backwards)

#Set 'd' key to call clockwise() function.
screen.onkey(key="d",fun=clockwise)

#Set 'a' key to call counter_clockwise() function.
screen.onkey(key="a",fun=counter_clockwise)

#Set 'c' key to call clear() function.
screen.onkey(key="c",fun=clear)

screen.exitonclick()