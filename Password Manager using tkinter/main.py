# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
import sqlite3
conn = sqlite3.connect(r"Password Manager using tkinter\sqlite.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS passwords (id INTEGER PRIMARY KEY AUTOINCREMENT,website varchar(250),email_user varchar(250),password varchar(250))")
def save_data(website,email_user,password):
    query = f"INSERT INTO passwords (website,email_user,password) values (\"{website}\",\"{email_user}\",\"{password}\")"
    cursor.execute(query)
    conn.commit()
# save_data("google.com","anku","1235ddd3424@$@#$@")
cursor.execute("select * from passwords")

print(cursor.fetchall())
# ---------------------------- UI SETUP ------------------------------- #
from tkinter import *
window = Tk()
window.title("Password Manager")
window.config(padx=20,pady=20)
# window.minsize(width=500,height=500)
#image canvas
password_image = PhotoImage(file=r"Password Manager using tkinter\logo.png")
canvas = Canvas(width=200,height=200)
canvas.create_image(100,100,image=password_image)
canvas.grid(column=1,row=0)
#Labels
#website
website_label = Label(text="website: ")
website_label.grid(column=0,row=1)
#email and username
email_username_label = Label(text="Email\\Username: ")
email_username_label.grid(column=0,row=2)
#password
password_label = Label(text="Password: ")
password_label.grid(column=0,row=3)

#entry input 
website_input = Entry(width=50)
website_input.grid(column=1,row=1,columnspan=2)

email_username_input = Entry(width=50)
email_username_input.grid(column=1,row=2,columnspan=2)


password_input = Entry(width=37)
password_input.grid(column=1,row=3)

#buttons

add_button = Button(text="Add",width=42,command="")
add_button.grid(column=1,row=4,columnspan=2)

generate_button = Button(text="Generate",command="",padx=10)
generate_button.grid(column=2,row=3)




window.mainloop()