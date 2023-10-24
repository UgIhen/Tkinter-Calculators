from tkinter import * 
import tkinter

window = tkinter.Tk()
window.title ("Calculator")
window.geometry("338x270+500+50")


entry = tkinter.Entry(window, width=47, borderwidth=10 )
entry.grid(row=0, column=0, columnspan=4)


def show(display_value): 
    present_value = entry.get()
    entry.delete(0, END)
    entry.insert(0, present_value + str(display_value))


def calc(): 
    equation = entry.get()
    result = str(eval(equation))
    entry.delete(0, END)
    entry.insert(0, result )  


def clear(): 
    entry.delete(0, END)

button_C = tkinter.Button(window, text="C", width=5, padx=20, pady=10, command= lambda: clear())
button_C.grid(row=1, column=0)
button_percent = tkinter.Button(window, text="%", width=5, padx=20, pady=10, command= lambda: show("/100"))
button_percent.grid(row=1, column=1)
button_bracket_open = tkinter.Button(window, text="(", width=5, padx=20, pady=10, command= lambda: show("("))
button_bracket_open.grid(row=1, column=2)
button_bracket = tkinter.Button(window, text=")", width=5, padx=20, pady=10, command= lambda: show(")"))
button_bracket.grid(row=1, column=3) 

button_1 = tkinter.Button(window, text="1", width=5, padx=20, pady=10, command= lambda: show("1"))
button_1.grid(row=4, column=0)
button_2 = tkinter.Button(window, text="2", width=5, padx=20, pady=10, command= lambda: show("2"))
button_2.grid(row=4, column=1)
button_3 = tkinter.Button(window, text="3", width=5, padx=20, pady=10, command= lambda: show("3"))
button_3.grid(row=4, column=2)
button_multiply = tkinter.Button(window, text="x", width=5, padx=20, pady=10, command= lambda: show("*"))
button_multiply.grid(row=4, column=3)

button_4 = tkinter.Button(window, text="4", width=5, padx=20, pady=10, command= lambda: show("4"))
button_4.grid(row=3, column=0)
button_5 = tkinter.Button(window, text="5", width=5, padx=20, pady=10, command= lambda: show("5"))
button_5.grid(row=3, column=1)
button_6 = tkinter.Button(window, text="6", width=5, padx=20, pady=10, command= lambda: show("6"))
button_6.grid(row=3, column=2)
button_subtract = tkinter.Button(window, text="-", width=5, padx=20, pady=10, command= lambda: show("-"))
button_subtract.grid(row=3, column=3)

button_7 = tkinter.Button(window, text="7", width=5, padx=20, pady=10, command= lambda: show("7"))
button_7.grid(row=2, column=0)
button_8 = tkinter.Button(window, text="8", width=5, padx=20, pady=10, command= lambda: show("8"))
button_8.grid(row=2, column=1)
button_9 = tkinter.Button(window, text="9", width=5, padx=20, pady=10, command= lambda: show("9"))
button_9.grid(row=2, column=2)
button_divide = tkinter.Button(window, text="/", width=5, padx=20, pady=10, command= lambda: show("//"))
button_divide.grid(row=2, column=3)

button_0 = tkinter.Button(window, text="0", width=5, padx=20, pady=10, command= lambda: show("0"))
button_0.grid(row=5, column=0)
button_point = tkinter.Button(window, text=".", width=5, padx=20, pady=10, command= lambda: show("."))
button_point.grid(row=5, column=1)
button_plus = tkinter.Button(window, text="+", width=5, padx=20, pady=10, command= lambda: show("+"))
button_plus.grid(row=5, column=2)
button_equalto = tkinter.Button(window, text="=", width=5, padx=20, pady=10, command= calc)
button_equalto.grid(row=5, column=3)

tkinter.mainloop()



