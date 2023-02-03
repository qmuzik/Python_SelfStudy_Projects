from tkinter import*
window = Tk()
window.title('Button Example')

# Creates an exit button
btn_end = Button(window,text = 'Close',command=exit)

# Function to toggle window's background color when another button is clicked 
def tog():
    if window.cget('bg') == 'yellow':
        window.configure(bg = 'gray')
    else:
        window.configure(bg = 'yellow')

# Creates a switch button
btn_tog = Button(window,text = 'Switch',command=tog)

# Adds button to window with padding for positioning
btn_tog.pack(padx = 150,pady = 20)
btn_end.pack(padx = 150,pady = 20)

window.mainloop()