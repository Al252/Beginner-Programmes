import tkinter as tk
from tkinter import ttk


win = tk.Tk()
win.title("Python GUI")
win.resizable(0, 0)


def click():
    bt.configure(text = "Hello " + name.get() + age.get())

lbName = ttk.Label(win, text = "Name:").grid(column = 0, row = 0)
name = tk.StringVar()
nameEntered = ttk.Entry(win, width = 12, textvariable = name)
nameEntered.grid(column = 0, row = 1)
nameEntered.focus()

lbAge = ttk.Label(win, text = "Age:").grid(column = 1, row = 0)
age = tk.StringVar()
ageEntered = ttk.Combobox(win, width = 12, textvariable = age, state = 'readonly')
ageEntered.grid(column = 1, row = 1)
ageEntered['values'] = (10, 15, 20, 25, 30, 35, 40, 45, 50)
ageEntered.current(0)

bt = ttk.Button(win, text = "Submit", command = click)
bt.grid(column = 2, row = 1)

mcheckState = tk.IntVar()
chMale = tk.Checkbutton(win, text = "Male", variable = mcheckState)
chMale.deselect()
chMale.grid(column = 0, row = 2)

fcheckState = tk.IntVar()
chFemale = tk.Checkbutton(win, text = "Female", variable = fcheckState)
chFemale.deselect()
chFemale.grid(column = 1, row = 2)


win.mainloop()
