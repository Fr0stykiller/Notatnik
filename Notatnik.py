from tkinter import *
 
class Notatnik():
    def __init__(self, master, width, height):
        self.master = master
        self.master.geometry("%sx%s+100+100" % (width, height))
        self.master.title("Notatnik")

        self.btn = Button(master, text="Dodaj notatkę")
        self.btn.pack(side=TOP, padx=0, pady=0)
 
 
root = Tk()
Notatnik(root, "500", "500")
#top1 = Toplevel()
#top2 = Toplevel()
#TopLevelWindow(top1, "300", "300")
#TopLevelWindow(top2, "500", "250")
 
root.mainloop()