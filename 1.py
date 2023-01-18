from tkinter import *

def sl(event):
    a = ent1.get()
    b = ent2.get()
    try :
        a = int(a)
        b = int(b)
        lab["text"] = a + b
    except ValueError:
        lab["text"] = "Ошибка"
def rz(event):
    a = ent1.get()
    b = ent2.get()
    try :
        a = int(a)
        b = int(b)
        lab["text"] = a - b
    except ValueError:
        lab["text"] = "Ошибка"
def dl(event):
    a = ent1.get()
    b = ent2.get()
    try :
        a = int(a)
        b = int(b)
        lab["text"] = a / b
    except ValueError:
        lab["text"] = "Ошибка"
def um(event):
    a = ent1.get()
    b = ent2.get()
    try :
        a = int(a)
        b = int(b)
        lab["text"] = a * b
    except ValueError:
        lab["text"] = "Ошибка"



ent1 = Entry(width=15, bg = 'gray')
ent2 = Entry(width=15, bg = 'gray')
but1 = Button(text="+",width=20)
but2 = Button(text="-",width=20)
but3 = Button(text="/",width=20)
but4 = Button(text="*",width=20)
lab = Label(width=15)

but1.bind("<Button-1>", sl)
but2.bind("<Button-1>", rz)
but3.bind("<Button-1>", dl)
but4.bind("<Button-1>", um)

ent1.pack()
ent2.pack()
but1.pack()
but2.pack()
but3.pack()
but4.pack()
lab.pack()

win = Tk()
win.geometry("150x170")
win.mainloop()