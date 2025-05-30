import tkinter
window = tkinter.Tk(screenName="new window")
window.title(string="My new GUI window")
window.minsize(width=500, height=300)

#label
my_label = tkinter.Label(text="lable text",font=("Time new roman",14,"bold"))
my_label.pack()
my_label["text"] = "new twxt 1"
my_label.config(text="new text")
def clicked_button():
    if inputv.get() != "":
        my_label.config(text=inputv.get())
    else:
        my_label.config(text="Button Clicked")
    print("click")
    # pass

#button 
my_button = tkinter.Button(text="Click me",command=clicked_button)
my_button.pack()

#entry input
inputv = tkinter.Entry(width=15)
inputv.pack()
window.mainloop()