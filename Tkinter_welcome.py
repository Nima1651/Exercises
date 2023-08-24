 
from tkinter import *
window = Tk()

window.title("avaln barnamz agha nimaye gol")

def welcome():
    greeting_lbl.config(text="welcome {} {}".format(first_name.get(),last_name.get()))





Label(window,text="First name").pack()
first_name = Entry(window)
first_name.pack()

Label(window,text="Last name").pack()
last_name = Entry(window)
last_name.pack()

Button(window,text="Sign in",command=welcome).pack()

greeting_lbl = Label(text="")
greeting_lbl.pack()
window.minsize(700,900)

window.mainloop()