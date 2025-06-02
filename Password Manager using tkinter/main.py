# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

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
canvas.grid(column=0,row=2)
#Labels
#website
website_label = Label(text="website: ")
#email and username
email_username_label = Label(text="Email\\Username: ")
#password
password_label = Label(text="Password: ")

#entry input 
website_input = Entry(width=50)
website_input.grid(column=1,row=1)

email_username_input = Entry(width=50)


password_input = Entry(width=50)




window.mainloop()