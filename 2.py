from tkinter import * 

#Enter function
def enter():
    capText = txt.get()
    res = "Hi, " + capText.capitalize()
    l2.config(text=res)

window = Tk()  
window.title("Print") 

#Label widget
l1 = Label(window, text="Welcome!", font=('Arial Bold',50))
l1.grid(column=0,row=0)

l2 = Label(window, text="", font=('Arial Bold',25))
l2.grid(column=0,row=2)

#Entry widget
txt = Entry(window,width=10)
txt.grid(column=0,row=1)

#Button widget, which has command function
bt =Button(window,text="Enter",fg="purple",command=enter)
bt.grid(column=1,row=1)

window.geometry('500x500')
window.mainloop()