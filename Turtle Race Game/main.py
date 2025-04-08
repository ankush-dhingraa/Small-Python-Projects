from turtle import Turtle, Screen
obj = Turtle()
screen = Screen()
screen.setup(width=500,height=400)
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
user_bet = screen.textinput(title="Make your bet",prompt="Which turtle will win the race? Enter color : ")
print(user_bet)
for color in colors:
    pass

screen.exitonclick()