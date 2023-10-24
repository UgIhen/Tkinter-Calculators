from tkinter import *
import tkinter


window = tkinter.Tk()
window.title("Simple Calculator")
window.geometry("300x100")
entry = tkinter.Entry(window, text="", width=100, borderwidth=10)
entry.pack()
label = tkinter.Label(window)
label.pack()


def calc(): 
    calculate = entry.get()
    label.config(text=" " + str(eval(calculate)))

button = tkinter.Button(window, text = "Calculate", command=calc).pack()
tkinter.mainloop()