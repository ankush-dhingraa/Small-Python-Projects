from turtle import Turtle,Screen,turtles
import turtle
from score import update
import pandas
data = pandas.read_csv(r'Haryana Districts Game\22_districts.csv')
total_districts = 22
SCORE = 0
user_guessed_districts = []
obj = Turtle()
# update = Update_district()
screen = Screen()
screen.screensize(300,300)
screen.bgpic(r"Haryana Districts Game\haryana.gif")
obj.penup()
obj.hideturtle()
# print(SCORE)
# update(16,135,"Ambala")
# print(SCORE)
# update(-46,-2,'Jind')
# print(SCORE)
# # row = list(data[data['District Name']=='Yamunanagar'])
# print(data.loc[1]['X'])
# print(user_input)
# print(row)
def check(user_input):
    global game_is_on, SCORE
    for index in range(0,22):
        if user_input.lower() == data.loc[index]['District Name'].lower():
            x = data.loc[index]['X']
            y = data.loc[index]['Y']
            display = data.loc[index]['District Name']
            update(x=x,y=y,display=display)
            if user_input.lower() in user_guessed_districts:
                continue
            else:
                SCORE +=1
            user_guessed_districts.append(user_input.lower())

            if SCORE ==22:
                game_is_on = False
        
        elif user_input.lower() == 'exit':
            game_is_on = False

game_is_on = True
#start
while game_is_on:
    user_input = turtle.textinput(f"{SCORE}/{total_districts} Districts Correct","What's another district name?")
    check(user_input)
    if SCORE
else:
    screen.bye()








screen.exitonclick()
