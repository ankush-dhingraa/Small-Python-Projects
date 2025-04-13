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
    time.sleep(0.01)
    screen.update()
    ball.move()

    #top and bottom wall collition detection
    if ball.ycor() > 280 or ball.ycor() < -280:
        print("need bounce")
        ball.bounce_y()
    
    # detect collition with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 330 or ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_x()
    #detect R paddle missing
    if ball.xcor() > 380:
        ball.reset_position()
    #detect l paddle missing
    if ball.xcor() < -380:
        ball.reset_position()
screen.exitonclick()