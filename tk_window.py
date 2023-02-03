from tkinter import*

# Calls a constructor to create a window object and labels it 
window = Tk()
window.title('Label Example')

# Calls a constructor to create a label object
label = Label(window,text = 'Hello World!')

# Adds label to the window with horizontal and vertical padding positioning
label.pack(padx=200,pady=50)

# Maintains the window by capturing events
window.mainloop()