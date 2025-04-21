from turtle import Turtle
t = Turtle()
t.hideturtle()
t.penup()
t.color('black')

def update(x,y,display):
    t.goto(x,y)
    t.write(display,align="center", font=("Arial",6,"normal"))