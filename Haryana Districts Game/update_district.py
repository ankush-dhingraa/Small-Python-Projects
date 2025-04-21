from turtle import Turtle

t = Turtle()
t.hideturtle()
t.penup()
t.color('black')

def update(x,y,display):
    t.goto(x,y)
    t.write(display,align="center", font=("courier",15,"normal"))