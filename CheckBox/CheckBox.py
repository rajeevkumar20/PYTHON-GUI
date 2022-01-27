from tkinter import *
app = Tk()

check = StringVar()
chk = Checkbutton(app,text='Checkbox',variable=check,onvalue='Yes',offvalue='Nope')
chk.deselect()
chk.pack()

def Show_msg():
    ab = check.get()
    msg = Label(app,text=ab,font=('Courier',12),relief='raised',width=15,borderwidth=4)
    msg.pack()

B = Button(app,text='Show', command=Show_msg,background='green',relief='groove',borderwidth=5)
B.pack()

app.mainloop()
