from tkinter import *
from random import randint
app = Tk()

app.title('User Input')
app.geometry('350x125')

inp = Entry(app,relief='raised',borderwidth=3)
inp.grid(row=0,column=0,columnspan=2,padx=25,pady=5)

def Show_msg():
    ab = inp.get()
    msg = Label(app,text=ab,font=('Courier',12),relief='raised',width=15,borderwidth=4)
    msg.grid(row=2,column=0,columnspan=2,padx=40,pady=5)

    if qt['state'] == DISABLED:
        qt['state'] = NORMAL

B = Button(app,text='Show', command=Show_msg,background='green',relief='groove',borderwidth=5)
B.grid(row=1,column=0,padx=25,pady=5)

qt = Button(app,text='Quit', command=app.quit, state=DISABLED,background='red',borderwidth=5)
qt.grid(row=1,column=1,padx=25,pady=5)

app.mainloop()
