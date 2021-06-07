import tkinter  #import Tkinter lib
window = tkinter.Tk()   #Creating window
window.title("GUI") #Giving name of the window
label = tkinter.Label(window, text="Hello World!").pack() #label is used to print line of text on window gui
window.mainloop()   #Runs the event loop untill x button is clicked
