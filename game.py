# assignment: programming assignment 5
# author: Lynelle Goh
# date: 12/1/2022
# file: game.py is the main module that runs the game
# input: it accepts and handles events such as mouse clicks 
# output: will play the Fifteen Game and output it in the terminal

from tkinter import *
import tkinter.font as font
#from fifteen import Fifteen
          

def clickButton():
    global message
    if message.get()=='You clicked me!':
        message.set('Click me again!')
    else:
        message.set('You clicked me!')
    
if __name__ == '__main__':    

    # make tiles
    #tiles = Fifteen()

    # make a window
    gui = Tk()
    gui.title("Fifteen")

    # make font
    font = font.Font(family='Helveca', size='25', weight='bold')

    # make buttons
    text1 = StringVar()
    text1.set('1')
    name1 = 1
    button1 = Button(gui, textvariable=text1, name=str(name1),
                      bg='white', fg='black', font=font, height=2, width=5,
                      command = lambda : clickButton())
    button1.configure(bg='coral')
    
    # the key argument name is used to identify the button
    gui.nametowidget(name1).configure(bg='white')

    # add buttons to the window
    # use .grid() or .pack() methods
    button1.pack()
    # update the window
    gui.mainloop()
