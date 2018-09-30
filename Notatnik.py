from tkinter import *
import tkinter as tk
import tkinter.scrolledtext as tkscrolled
import sqlite3

conn = sqlite3.connect('python.db')


class Notatnik():

    def __init__(self, master, width, height):
        self.master = master
        self.master.geometry("%sx%s+100+100" % (width, height))
        self.master.title("Notatnik")

        self.btn = Button(master, bg="lightblue", text="DODAJ NOTATKĘ", font=(
            'Calibri Light', 20), command=self.new_note)
        self.btn.pack(fill=BOTH, expand=1)

        self.btn2 = Button(master, bg="lightblue",
                           text="ODCZYTAJ NOTATKĘ", font=('Calibri Light', 20))
        self.btn2.pack(fill=BOTH, expand=1)

        self.c = conn.cursor()
        self.c.execute('''CREATE TABLE IF NOT EXISTS notatki
             (data text, nazwa text, notatka text)''')

    def new_note(self):
        self.newWindow = tk.Toplevel(self.master)
        self.textfield = tkscrolled.ScrolledText(self.newWindow)
        self.textfield.pack()
        self.addButton = Button(
            self.newWindow, text="Dodaj!", command=self.dodaj)
        self.addButton.pack(side=BOTTOM)

    def dodaj(self):
        self.notka = self.textfield.get("1.0", END)
        print(self.notka)
        self.c.execute('''INSERT INTO notatki (data, nazwa, notatka) VALUES ('dzis', 'Notatka1', ?)''', (self.notka,))
        conn.commit()


root=tk.Tk()
Notatnik(root, "400", "300")
# top1 = Toplevel()
# top2 = Toplevel()
# TopLevelWindow(top1, "300", "300")
# TopLevelWindow(top2, "500", "250")

root.mainloop()
