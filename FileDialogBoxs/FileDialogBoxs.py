from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

app = Tk()
app.title('App')
app.iconbitmap(r'python.png')

def img_select():
    global img
    
    app.frame = filedialog.askopenfilename(title='Select a image',filetypes=(
        ('PNG Images','*.png'),('Icon Files','*.ico'),('All files','*.*')
    ))
    b.destroy()
    img = ImageTk.PhotoImage(Image.open(app.frame))
    lbl = Label(app, image = img)
    lbl.pack()

b = Button(app, text='View',command=img_select)
b.pack()
app.mainloop()
