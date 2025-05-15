import json
from tkinter import *
from tkinter import messagebox
import random
import string
import pyperclip

SYMBOLS = ["!","@","#","$","%","^","&","*","_","+","-","=","|",";",":",".","<",">","?","/","~"]
random_pass = ''
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate(count = 0):
    global random_pass
    if count == 0:
        random_pass = ""
    if count < 3:
        lowercase = random.choice(string.ascii_lowercase)
        uppercase = random.choice(string.ascii_uppercase)
        rand_digits = random.choice(string.digits)
        rand_symbol = random.choice(SYMBOLS)

        random_pass += lowercase+uppercase+rand_digits+rand_symbol

        window.after(1,generate,count + 1 )
    else:
        password_entry.insert(0,random_pass)
    pyperclip.copy(random_pass)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():

    website_data = website_entry.get()
    email_username = em_us_entry.get()
    password_data = password_entry.get()
    new_data = {
        website_data: {
            "email": email_username,
            "password":password_data
    }
    }

    if len(website_data) == 0 or len(password_data) == 0:

        messagebox.showerror(title="Oops",message="Please dont leave any fields empty!")
    else:

        try:
            with open("data.json", 'r') as data_file:
                data = json.load(data_file)

        except FileNotFoundError:
                with open("data.json","w") as data_file:
                    json.dump(new_data,data_file,indent=4)
        else:
            data.update(new_data)

            with open("data.json", 'w') as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0,END)
            password_entry.delete(0, END)
# ---------------------------- FIND PASSWORD ---------------------------- #

def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error",message="No data file found")
    else:
            if website in data:
                email = data[website]["email"]
                password = data[website]["password"]
                messagebox.showinfo(title=website,message=f"Email: {email}\nPassword: {password}")
            else:
                messagebox.showinfo(title="Error",message=f"No details for {website} exists")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(pady=20,padx=20)


canvas = Canvas(width=200,height=200)
lock_image =PhotoImage(file="logo.png")
canvas.create_image(100,100,image = lock_image)
canvas.grid(column=1,row=0)

website_label = Label(text="Website: ")
website_label.grid(column=0,row=1)

website_entry =Entry(width=18)
website_entry.grid(column=1,row=1)
website_entry.focus()

email_username_label =Label(text="Email/Username: ")
email_username_label.grid(column=0,row=2)

em_us_entry = Entry(width=35)
em_us_entry.grid(column=1, row=2,columnspan=2)
em_us_entry.insert(0,"deni.hyseni@gmail.com")

password_label= Label(text="Password: ")
password_label.grid(column=0,row=3)

password_entry = Entry(width=18)
password_entry.grid(column=1, row=3)

gen_pass_button = Button(text="Generate Password",command=generate)
gen_pass_button.grid(column=2,row=3)

add_button = Button(width=33,text="Add",command=save)
add_button.grid(column=1,row=4,columnspan=2)

search_button = Button(text="Search",width=13,command=find_password)
search_button.grid(column=2,row=1)















window.mainloop()