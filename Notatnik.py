from tkinter import *
import tkinter as tk

class Notatnik():
    counter = 0
    def __init__(self, master, width, height):
        self.master = master
        self.master.geometry("%sx%s+100+100" % (width, height))
        self.master.title("Notatnik")

        self.btn = Button(master, bg = "lightblue", text="DODAJ NOTATKĘ", font=('Calibri Light', 20), command=self.new_window)
        self.btn.pack(side=TOP, padx=0, pady=0)

        self.btn2 = Button(master, bg = "lightblue", text="ODCZYTAJ NOTATKĘ", font=('Calibri Light', 20))
        self.btn2.pack(side=TOP, padx=0, pady=10)

    def new_window(self):
        self.newWindow = tk.Toplevel(self.master)

 
 
root = tk.Tk()
Notatnik(root, "400", "300")
#top1 = Toplevel()
#top2 = Toplevel()
#TopLevelWindow(top1, "300", "300")
#TopLevelWindow(top2, "500", "250")
 
root.mainloop()