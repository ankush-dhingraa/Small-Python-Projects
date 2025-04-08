from turtle import Turtle, Screen
import random

def race_winner(turtle_color):
    if user_bet == turtle_color:
        print("you win")
    else:
        print("you lose")

is_race_on = False
screen = Screen()
screen.setup(width=500,height=400)
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
user_bet = screen.textinput(title="Make your bet",prompt="Which turtle will win the race? Enter color : ")
print(user_bet)
x = -230
y = -120
turtle_list = []
for color in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(color)
    y+=30
    new_turtle.goto(x=x,y=y)
    turtle_list.append(new_turtle)

if user_bet:
    is_race_on = True
while is_race_on:
    for turtle in turtle_list:
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
        if int(turtle.xcor()) == 100:
            race_winner(turtle.color()[0])
            is_race_on = False



screen.exitonclick()