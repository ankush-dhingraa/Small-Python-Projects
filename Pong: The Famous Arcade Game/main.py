from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong: The Famous Arcade Game")
screen.tracer(0)
l_paddle = Paddle((-350,0))
r_paddle = Paddle((350,0))
ball = Ball()
# paddle = Turtle()
# paddle.color("white")
# paddle.shape("square")
# paddle.shapesize(stretch_len=1,stretch_wid=5)
# paddle.penup()
# paddle.goto(x=350,y=0)

screen.listen()
# def up():
#     new_y = paddle.ycor()+10
#     paddle.goto(x=paddle.xcor(),y=new_y)
# def down():
#     new_y = paddle.ycor()-10
#     paddle.goto(x=paddle.xcor(),y=new_y)
screen.onkey(key="Up",fun=r_paddle.up)
screen.onkey(key="Down",fun=r_paddle.down)
screen.onkey(key="w",fun=l_paddle.up)
screen.onkey(key="s",fun=l_paddle.down)

game_is_on = True
while game_is_on:
    screen.update()
    ball.move()
screen.exitonclick()