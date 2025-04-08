from turtle import Turtle, Screen
screen = Screen()
screen.setup(width=500,height=400)
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
user_bet = screen.textinput(title="Make your bet",prompt="Which turtle will win the race? Enter color : ")
print(user_bet)
x = -230
y = -120
for color in colors:
    obj = Turtle(shape="turtle")
    obj.penup()
    obj.color(color)
    y+=30
    obj.goto(x=x,y=y)


screen.exitonclick()