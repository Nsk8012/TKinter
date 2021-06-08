from tkinter import *
from tkinter.ttk import *

window = Tk()
window.title("Combo Tab")

l1 = Label(window, text = "Welcome!")
l1.grid(column=1,row=0)

combo = Combobox(window)
combo['values'] = (1,2,3,4,5,6,7,8,9,10,11,12)
combo.current(5)
combo.grid(column=1,row=1)

chk_state = BooleanVar()
chk_state.set(True)
chk = Checkbutton(window,text = 'Select', var=chk_state)
chk.grid(column=0,row=1)

window.geometry('500x500')
window.mainloop()