import tkinter as tk
from essentials import *

mainwindow = tk.Tk()

mainwindow.title("Betterpye")
mainwindow.minsize(424,340)
mainwindow.maxsize(670,340)

def copyurl(tocopy:str):
    mainwindow.clipboard_clear()
    mainwindow.clipboard_append(tocopy)

hello = tk.Label(master=mainwindow,text="Hello, World!")
hello.place(relx=0.5, rely=0.4, anchor="center")

textfield = tk.Entry(master=mainwindow)
textfield.place(relx=0.5, rely=0.5, anchor="center")

button = tk.Button(master=mainwindow, text="Replace", command=lambda: fixupurl(textfield))
button.place(relx=0.5, rely=0.6, anchor="center")

copybutton = tk.Button(master=mainwindow, text="Copy", command=lambda: copyurl(textfield.get()))
copybutton.place(relx=0.5, rely=0.7, anchor="center")

# :D
tk.mainloop()