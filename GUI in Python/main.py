from tkinter import *


def button_clicked():
    my_label.config(text=input.get())

window = Tk()
window.title("My first GUI Program")
window.minsize(500,300 )
window.config(padx=20,pady=20)

my_label = Label(text="I am a label",font=("Arial",24,"italic"))
my_label.grid(column=0,row=0)


new_button = Button(text="Click",command=button_clicked)
new_button.grid(column=2,row=0)


button = Button(text="Click Me",command=button_clicked)
button.grid(column=1,row=1)




input = Entry(width=10)
input.grid(column=3,row=2)










window.mainloop()
