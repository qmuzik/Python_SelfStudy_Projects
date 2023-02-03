from msilib.schema import ListBox
from tkinter import*
import tkinter.messagebox as box
from typing import List

window = Tk()
window.title('Listbox Example')

frame = Frame(window)

# Create a listbox
listbox = Listbox(frame)
listbox.insert(1,'HTML5 in easy steps')
listbox.insert(2,'CSS3 in easy steps')
listbox.insert(3,'JavaScript in easy steps')

def dialog():
    box.showinfo('Selection','Your Choice: '+ listbox.get(listbox.curselection()))

btn = Button(frame,text='Choose',command=dialog)

btn.pack(side= RIGHT, padx=5)
listbox.pack(side =LEFT)
frame.pack(padx = 30,pady =30)

window.mainloop()