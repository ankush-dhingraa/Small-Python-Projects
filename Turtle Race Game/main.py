from turtle import Turtle, Screen
import random

def race_winner(turtle):
    turtle_color = turtle.color()
    if user_bet == turtle_color[0]:
        print(f"You've won! The {turtle_color[0]} turtle is winner")
    else:
        print(f"You've lost! The {turtle_color[0]} turtle is winner")

#end line 
end_line = Turtle()
end_line.penup()
end_line.goto(x=230,y=180)
end_line.right(90)
end_line.pensize(10)
end_line.color("red")
end_line.pendown()
end_line.forward(350)


is_race_on = False
screen = Screen()
screen.setup(width=500,height=400)
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
user_bet = screen.textinput(title="Make your bet",prompt=f"Which turtle will win the race? \n{colors}\nEnter color : ")
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
        if int(turtle.xcor()) > 210:
            is_race_on = False
            race_winner(turtle)
            break
        
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)



screen.exitonclick()