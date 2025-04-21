from turtle import Turtle,Screen,turtles
import turtle
from update_district import update
import pandas
data = pandas.read_csv(r'Haryana Districts Game\22_districts.csv')
total
obj = Turtle()
# update = Update_district()
screen = Screen()
screen.screensize(300,300)
screen.bgpic(r"Haryana Districts Game\haryana.gif")
obj.penup()
obj.hideturtle()
user_input = turtle.textinput("Guess ?","Guess the Districts name of haryana")
# update(16,135,"Ambala")
# update(-46,-2,'Jind')
# row = list(data[data['District Name']=='Yamunanagar'])
print(data.loc[1]['X'])
print(user_input)
# print(row)







screen.exitonclick()
