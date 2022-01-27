from tkinter import *
from random import randint
app = Tk()

app.title('User Input')
app.geometry('350x100')
app['background'] = 'gray'

inp = Entry(app,background='white')
inp.grid(row=0,column=0,columnspan=2,padx=25,pady=5)

def Show_msg():
    ab = inp.get()
    msg = Label(app,text=ab,font=('Courier',12),background='white',foreground='black')
    msg.grid(row=2,column=0,columnspan=2,padx=40,pady=5)

    if qt['state'] == DISABLED:
        qt['state'] = NORMAL

B = Button(app,text='Show', command=Show_msg,background='green')
B.grid(row=1,column=0,padx=25,pady=5)

qt = Button(app,text='Quit', command=app.quit, state=DISABLED,background='red')
qt.grid(row=1,column=1,padx=25,pady=5)

app.mainloop()
