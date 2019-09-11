from tkinter import *


root = Tk()

name = Label(root, text = "Name")
password = Label(root, text = "password")
name.grid(row = 0, column = 0)
password.grid(row = 1, column = 0)

pic = PhotoImage(filename = ['IMG_7702.jpg'])
pic.pack()

root.mainloop()
