from tkinter import *

FONT = ("Arial",16)
def miles_to_km():
    miles = int(input_miles.get())
    km = 1.6 * miles
    amount_label.config(text=round(km))


window = Tk()
window.title("Mile to KM Converter")
window.minsize(200,100)
window.config(pady=10,padx=10)



miles_label = Label(text="Miles",font=FONT)
miles_label.grid(column=3,row=0)


equal_to_label = Label(text="is equal to",font=FONT)
equal_to_label.grid(column=0,row=1)


Km_label = Label(text="KM",font=FONT)
Km_label.grid(column=3,row=1)


amount_label = Label(text="0",font=FONT)
amount_label.config(justify="center")
amount_label.grid(column=1,row=1)

input_miles = Entry(width=7)
input_miles.insert(END,string="0")
input_miles.grid(column=1,row=0)

calc_button = Button(text="Calculate",command=miles_to_km)
calc_button.grid(column=1,row=2)











window.mainloop()