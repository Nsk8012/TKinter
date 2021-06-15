from tkinter import *
from PIL import ImageTk, Image

window = Tk()

#To add window icon widget.
window.call('wm', 'iconphoto', window._w, PhotoImage(file="/Users/Nsk/Desktop/Project/TKinter/tab.png"))

#To show image on window
my_image = ImageTk.PhotoImage(Image.open("/Users/Nsk/Desktop/Project/TKinter/pillow.png"))
l1 = Label(image=my_image)
l1.pack()

window.mainloop()