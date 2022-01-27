from tkinter import *

app = Tk()
app.geometry('150x150')

menu_ch = StringVar()
options = ['Red','White','Black','Blue','Yellow']
menu = OptionMenu(app,menu_ch,*options)
menu.pack()
menu_ch.set('White')

outwin = Toplevel()
outwin.title('OUTPUT')
outwin.geometry('150x150')

def Show():
    msg = Label(outwin,text='          ',background=(menu_ch.get()).lower())
    msg.pack()

b = Button(app,text='Show',command=Show)
b.pack()

app.mainloop()
