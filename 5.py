from tkinter import *

window = Tk()
window.title("Scrollbar")

#Scrollbar widget
Scrollbar = Scrollbar(window)
Scrollbar.pack(side=RIGHT, fill=Y)

mylist = Listbox(window, yscrollcommand=Scrollbar.set)
for line in range(500):
    mylist.insert(END,"The line no: "+str(line))
mylist.pack(side= LEFT, fill=BOTH)
Scrollbar.config(command=mylist.yview)

window.mainloop()