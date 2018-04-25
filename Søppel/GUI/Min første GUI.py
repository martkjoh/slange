import tkinter
import tkinter.messagebox
from random import randint as r

class Window:
    def __init__(self):
        global a
        global b
        a = r(0, 1000)
        b = r(0, 1000)

        self.window = tkinter.Tk()
        self.frame1 = tkinter.Frame(self.window)
        self.label1 = tkinter.Label(self.frame1, text="Lurer du på hva " + str(a)+ "+" + str(b) + " er?")

        self.but = tkinter.Button(self.window, text="Klikk for svar", command=self.svar)

        self.label1.pack()
        self.frame1.pack()
        self.but.pack()

        tkinter.mainloop()

    def svar(self):
        tkinter.messagebox.showinfo("Svar", str(a + b))

window = Window()

