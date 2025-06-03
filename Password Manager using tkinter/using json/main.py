from tkinter import messagebox
from password_generator import create_password
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generate():
    password = create_password()
    password_input.delete(0,END)
    password_input.insert(0,password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
import json
def save_data():
    website = website_input.get()
    email_user = email_username_input.get()
    password = password_input.get()
    new_data = {
        website : {
            "email" : email_user,
            "password" : password
        }
    }

    if len(website) ==0 or len(password) ==0:
        messagebox.askretrycancel(title="Opps",message="Please make sure you haven't left any field empty.")
    else:

        try:
            with open(r"Password Manager using tkinter\using json\data.json","r") as file:
                data = json.load(file)
                data.update(new_data)
        except FileNotFoundError:
            with open(r"Password Manager using tkinter\using json\data.json","w") as file:
                json.dump(new_data,file,indent=4)
                website_input.delete(0,END)
                password_input.delete(0,END)
        else:
            with open(r"Password Manager using tkinter\using json\data.json","w") as file:
                json.dump(data,file,indent=4)
        website_input.delete(0,END)
        password_input.delete(0,END)
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
email_username_input.insert(0,"ankushkumar20024@gmail.com")


password_input = Entry(width=37)
password_input.grid(column=1,row=3)

#buttons

add_button = Button(text="Add",width=42,command=save_data)
add_button.grid(column=1,row=4,columnspan=2)

generate_button = Button(text="Generate",command=password_generate,padx=10)
generate_button.grid(column=2,row=3)



window.mainloop()