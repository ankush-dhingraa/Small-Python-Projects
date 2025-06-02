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


password_input = Entry(width=25)
password_input.grid(column=1,row=3)

#buttons

add_button = Button(text="Add",width=42,command="")
add_button.grid(column=1,row=4,columnspan=2)

generate_button = Button(text="Generate",width=20,command="")
generate_button.grid(column=2,row=3)




window.mainloop()