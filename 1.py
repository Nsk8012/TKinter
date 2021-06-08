from tkinter import *  #import Tkinter lib

window = Tk()   #Creating window
window.title("Print") #Giving name of the window
l1 = Label(window, text="Hello World!",font=('Arial Bold',50)) #label is used to print line of text on window gui
l1.grid(column=0,row=0) #grid set the position of label on window
window.geometry('500x500') #sets the size of window
window.mainloop()   #Runs the event loop untill x button is clicked
