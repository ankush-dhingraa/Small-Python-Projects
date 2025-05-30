import tkinter
font = ("Arial",14,"bold")
window = tkinter.Tk()
window.title("Miles to Km Convertor")
window.minsize(width=300,height=150)

def calculate():
    miles = float(miles_input.get())
    output_label["text"] = (miles*1.60934)
#miles label
miles_lable = tkinter.Label(text="Miles",font=font)
#Km lable
km_label = tkinter.Label(text="Km",font=font)
#is equale to lable
equale_lable = tkinter.Label(text="is equale to : ",font=font)
#output label
output_label = tkinter.Label(text="0",font=font)
#miles input
miles_input = tkinter.Entry(width=15)
#button for calculate
button = tkinter.Button(text="Calculate",command=calculate)


#grid
miles_input.grid(column=1,row=0)
miles_lable.grid(column=2,row=0)
equale_lable.grid(column=0,row=1)
output_label.grid(column=1,row=1)
km_label.grid(column=2,row=1)
button.grid(column=1,row=3)





window.mainloop()