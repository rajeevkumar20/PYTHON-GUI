from tkinter import *
from PIL import Image, ImageTk

app = Tk()
app.title('App')
#app.iconbitmap(r'python.ico')

img = ImageTk.PhotoImage(Image.open(r'python.png'))
lbl = Label(app, image = img)
lbl.pack()
app.mainloop()
