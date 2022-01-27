from tkinter import *

app = Tk()
app.geometry('150x150')
var = IntVar()

sld = Scale(app,from_=0,to=100,variable=var,orient=HORIZONTAL)
sld.pack()

def Show():
    msg = Label(app,text=var.get())
    msg.pack()

b = Button(app,text='Show',command=Show)
b.pack()

app.mainloop()
