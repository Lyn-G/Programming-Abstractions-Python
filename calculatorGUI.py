# assignment: programming assignment 4
# author: Lynelle Goh
# date: 11/16/2022
# file: calculatorGUI.py is a program that acts as a makeshift calculator
# input: it takes in numbers and operations that the user presses with their respective buttons on the calculator's interface
# output: outputs what the user presses and can evaluate expressions

# create a GUI calculator using tkinter
from tkinter import *
from calculator import *

def calculator(gui):   
    # name the gui window
    gui.title("Calculator")
    # make a entry text box
    entrybox = Entry(gui, width=36, borderwidth=5)
    # position the entry text box in the gui window using the grid manager
    entrybox.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
    
    # create buttons: 1,2,3,4,5,6,7,8,9,0,+,-,*,/,c,= 
    b0 = addButton(gui,entrybox,'0')
    b1 = addButton(gui,entrybox,'1')
    b2 = addButton(gui,entrybox,'2')
    b3 = addButton(gui,entrybox,'3')
    b4 = addButton(gui,entrybox,'4')
    b5 = addButton(gui,entrybox,'5')
    b6 = addButton(gui,entrybox,'6')
    b7 = addButton(gui,entrybox,'7')
    b8 = addButton(gui,entrybox,'8')
    b9 = addButton(gui,entrybox,'9')
    b_add = addButton(gui,entrybox,'+')
    b_sub = addButton(gui,entrybox,'-')
    b_mult = addButton(gui,entrybox,'*')
    b_div = addButton(gui,entrybox,'/')
    b_clr = addButton(gui,entrybox,'c')
    b_eq = addButton(gui,entrybox,'=')

    # add buttons to the grid
    buttons =[ b7,    b8, b9,    b_clr, 
               b4,    b5, b6,    b_sub, 
               b1,    b2, b3,    b_add, 
               b_mult,b0, b_div, b_eq ]
    k = 4           
    for i in range(k):
        for j in range(k):
            buttons[i*k+j].grid(row=i+1, column=j, columnspan=1)

def addButton(gui, entrybox, value):
    return Button(gui, text=value, height=4, width=9, command = lambda: clickButton(entrybox, value))

# you need to modify the function clickButton and use the widget Entry and its methods insert and delete
# Your function should be named calculate and execute the code written for your calculator.py program.
def clickButton(entrybox, value):
    # the function clickButton() is not implemented!!!
    current = entrybox.get()
    # if clear has been pressed, delete everything
    print(current)
    if 'c' in value:
        entrybox.delete(0, END)
    # calculate the expression only if = has been pressed
    elif '=' in value:
        answer = calculate(str(current))
        entrybox.delete(0, END)
        entrybox.insert(0, answer)
    # just insert the stuff onto the interface if none of the above are pressed
    else:
        entrybox.delete(0, END)
        entrybox.insert(0, str(current) + str(value))
    print(value) # for debugging
    
# main program
# create the main window
gui = Tk()
# create the calculator layout
calculator(gui)
# update the window
gui.mainloop()