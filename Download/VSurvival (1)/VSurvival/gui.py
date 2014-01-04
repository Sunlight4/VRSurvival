from Tkinter import *

root = Tk()

def textinput():
    text = Entry(master)
    text.pack
    return text.get()
