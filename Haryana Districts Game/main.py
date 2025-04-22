from turtle import Turtle,Screen,turtles
import turtle
import tkinter as tk
from score import update
import pandas
data = pandas.read_csv(r'Haryana Districts Game\22_districts.csv')
total_districts = 22
SCORE = 21
user_guessed_districts = []
obj = Turtle()
screen = Screen()
screen.screensize(300,300)
screen.bgpic(r"Haryana Districts Game\haryana.gif")
obj.penup()
obj.hideturtle()

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

            if SCORE == 22:
                game_is_on = False
        
        elif user_input.lower() == 'exit':
            game_is_on = False

def show_win_popup():
    win_popup = tk.Tk()
    win_popup.title("Congratulations!")
    win_popup.geometry("400x150")
    
    label = tk.Label(win_popup, text="You Win!", font=("Arial", 24))
    label.pack(pady=20)

    button = tk.Button(win_popup, text="Close", command=win_popup.destroy)
    button.pack(pady=10)

    win_popup.mainloop()


game_is_on = True
#start
while game_is_on:
    user_input = turtle.textinput(f"{SCORE}/{total_districts} Districts Correct","What's another district name?")
    check(user_input)
else:
    screen.bye()
    if SCORE == 22:
        show_win_popup()

screen.exitonclick()
