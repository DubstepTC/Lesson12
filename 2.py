from tkinter import *

def pr(event, f):
    if f == 1:
        ent1.delete(0, END)
        lab["text"] = "Красный"
        ent1.insert(0, but1["bg"])
    elif f == 2:
        ent1.delete(0,END)
        lab["text"] = "Оранжевый"
        ent1.insert(0, but2["bg"])
    elif f ==3:
        ent1.delete(0, END)
        lab["text"] = "Жёлтый"
        ent1.insert(0, but3["bg"])
    elif f == 4:
        ent1.delete(0, END)
        lab["text"] = "Зелёный"
        ent1.insert(0, but4["bg"])
    elif f == 5:
        ent1.delete(0, END)
        lab["text"] = "Голубой"
        ent1.insert(0, but5["bg"])
    elif f == 6:
        ent1.delete(0, END)
        lab["text"] = "Синий"
        ent1.insert(0, but6["bg"])
    elif f == 7:
        ent1.delete(0, END)
        lab["text"] = "Фиолетовый"
        ent1.insert(0, but7["bg"])

win = Tk()
win.geometry("200x250")

lab = Label(width=15, justify = "center")
ent1 = Entry(width=15, justify = "center")
but1 = Button(width=20, bg = "#ff0000")
but2 = Button(width=20, bg = "#ff7d00")
but3 = Button(width=20, bg = "#ffff00")
but4 = Button(width=20, bg = "#00ff00")
but5 = Button(width=20, bg = "#007dff")
but6 = Button(width=20, bg = "#0000ff")
but7 = Button(width=20, bg = "#7d00ff")

but1.bind("<Button-1>", lambda event, f = 1 : pr(event, f))
but2.bind("<Button-1>", lambda event, f = 2 : pr(event, f))
but3.bind("<Button-1>", lambda event, f = 3 : pr(event, f))
but4.bind("<Button-1>", lambda event, f = 4 : pr(event, f))
but5.bind("<Button-1>", lambda event, f = 5 : pr(event, f))
but6.bind("<Button-1>", lambda event, f = 6 : pr(event, f))
but7.bind("<Button-1>", lambda event, f = 7 : pr(event, f))



lab.pack()
ent1.pack()
but1.pack()
but2.pack()
but3.pack()
but4.pack()
but5.pack()
but6.pack()
but7.pack()

win.mainloop()