import tkinter as tk

def fixupurl(text):
    url = text.get()
    #This will replace the i on "tiktok" turning it into "tnktok". 
    url = url.replace("i", "n", 1)
    #I will make one for X/Twitter soon.

    text.delete(0, tk.END)
    text.insert(0, url)
    
    return url