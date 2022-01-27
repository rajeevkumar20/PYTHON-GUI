from tkinter import *
from random import randint
app = Tk()

app.title('Random Generator')
app.geometry('350x100')

def Show_msg():
    msg = Label(app,text=randint(1,100))
    msg.pack()
    
B = Button(app,text='Generate', command=Show_msg)
B.pack()

app.mainloop()
