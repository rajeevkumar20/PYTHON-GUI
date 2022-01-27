from tkinter import *

app = Tk()
app.geometry('150x150')

menu_ch = StringVar()
options = ['Red','White','Black','Blue','Yellow']
menu = OptionMenu(app,menu_ch,*options)
menu.pack()
menu_ch.set('White')

def Show():
    msg = Label(app,text='          ',background=(menu_ch.get()).lower())
    msg.pack()

b = Button(app,text='Show',command=Show)
b.pack()

app.mainloop()
