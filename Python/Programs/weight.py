import tkinter as tk
from tkinter import ttk


win = tk.Tk()
win.title("Weight Converter")
win.resizable(0, 0)

#CONVERSION FUNCTIONS
def ktol():
    cweight = round(float(tkweight.get()) / 0.45)
    tkresult.set(f"Weight in Lbs: {cweight}Lbs")
def ltok():
    cweight = round(float(tkweight.get()) * 0.45)
    tkresult.set(f"Weight in Kg: {cweight}Kg")


#WEIGHT DETAILS: LABEL, ENTRY BOX
lbWeight = ttk.Label(win, text = "Weight:").grid(column = 0, row = 0)
tkweight = tk.IntVar()
weightEntered = ttk.Entry(win, width = 12, textvariable = tkweight)
weightEntered.grid(column = 0, row = 1)
weightEntered.focus()

#WEIGHT TYPE DETAILS: LABEL, COMBOBOX(KG AND LBS)
lbtype = ttk.Label(win, text = "Kg or Lbs:").grid(column = 1, row = 0)
weight_type = tk.StringVar()
typeEntered = ttk.Combobox(win, width = 12, textvariable = weight_type, state = 'readonly')
typeEntered.grid(column = 1, row = 1)
typeEntered['values'] = ("kilogrammes(Kg)", "Pounds(Lbs)")
typeEntered.current(0)

#CONVERSION RESULTS
tkresult = tk.StringVar()
ttk.Label(win, textvariable = tkresult).grid(column = 0, row = 2)

#BUTTON COMMAND SELECTOR
if weight_type.get() == "kilogrammes(Kg)":
    action = ktol
if weight_type.get() == "Pounds(Lbs)":
    action = ltok

bt = ttk.Button(win, text = "Convert", command = action)
bt.grid(column = 2, row = 1)


win.mainloop()

