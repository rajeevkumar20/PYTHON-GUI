from tkinter import *

app = Tk()
app.geometry('150x150')
choice = StringVar()
rb1 = Radiobutton(app,text='Option-1',variable=choice,value='RB1 Selected')
rb2 = Radiobutton(app,text='Option-2',variable=choice,value='RB2 Selected')
rb1.deselect()
rb2.deselect()
rb1.pack()
rb2.pack()

def Show():
    msg = Label(app,text=choice.get())
    msg.pack()

b = Button(app,text='Show',command=Show)
b.pack()

app.mainloop()
