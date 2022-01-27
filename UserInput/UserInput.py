from tkinter import *
from random import randint
app = Tk()

app.title('User Input')
app.geometry('350x100')

inp = Entry(app)
inp.pack()

def Show_msg():
    ab = inp.get()
    msg = Label(app,text=ab)
    msg.pack()

B = Button(app,text='Show', command=Show_msg)
B.pack()

qt = Button(app,text='Quit', command=app.quit)
qt.pack()

app.mainloop()
