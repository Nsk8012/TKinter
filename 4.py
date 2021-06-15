from tkinter import *
from tkinter.ttk import *

window = Tk()
window.title("Radio Button")

#Radio button widget
rad1 = Radiobutton(window, text="Python", value = 1)
rad2 = Radiobutton(window, text="Java", value = 2)
rad3 = Radiobutton(window, text="C",value = 3)

rad1.grid(column=1,row=0)
rad2.grid(column=2,row=0)
rad3.grid(column=3,row=0)

window.geometry('200x200')
window.mainloop()