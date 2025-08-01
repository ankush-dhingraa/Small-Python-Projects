from tkinter import *
import pandas as pd
import random
BC= "#B1DDC6"
current_card = {}
to_learn = {}
try:
    data = pd.read_csv("data/word_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/english_hindi.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_background, image=canvas_front_img)
    canvas.itemconfig(card_title,text="English",fill = "black")
    canvas.itemconfig(card_word, text=current_card["ENGLISH"],fill = "black")
    flip_timer = window.after(3000, func=card_flip)


def card_flip():
    canvas.itemconfig(card_title, text="Hindi",fill = "white")
    canvas.itemconfig(card_word, text=current_card["HINDI"],fill = "white")
    canvas.itemconfig(card_background, image=canvas_back_img)

def is_known():
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv("data/word_to_learn.csv",index=False)
    next_card()

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BC)

flip_timer = window.after(3000,func=card_flip)

canvas = Canvas(width=800, height=526)
canvas_front_img = PhotoImage(file = "images/card_front.png")
canvas_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400,263,image= canvas_front_img)
card_title = canvas.create_text(400,150,text="",font= ("Ariel",40,"italic"))
card_word = canvas.create_text(400,263,text="",font= ("Ariel",60,"bold"))
canvas.config(bg=BC, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0,command=is_known)
known_button.grid(row=1,column=1)
next_card()

window.mainloop()

