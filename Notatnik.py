from tkinter import *
from datetime import datetime
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
        self.dodtyt = tk.Label(self.newWindow, text="DODAJ TYTUŁ", font=('Calibri Light', 15))
        self.dodtyt.grid(column=0, row=0)
        self.tytul = tk.Entry(self.newWindow, width=40)
        self.tytul.grid(column=1, row=0)
        self.textfield = tkscrolled.ScrolledText(self.newWindow)
        self.textfield.grid(columnspan=2)
        self.addButton = Button(
            self.newWindow, text="Dodaj!", command=self.dodaj)
        self.addButton.grid(columnspan=2)

    def dodaj(self):
        self.notka = self.textfield.get("1.0", END)
        self.nazwanotki = self.tytul.get()
        print(self.notka)
        now = datetime.now()
        print(now)
        self.c.execute('''INSERT INTO notatki (data, nazwa, notatka) VALUES (?, ?, ?)''', (now, self.nazwanotki, self.notka,))
        conn.commit()


root=tk.Tk()
Notatnik(root, "400", "300")
# top1 = Toplevel()
# top2 = Toplevel()
# TopLevelWindow(top1, "300", "300")
# TopLevelWindow(top2, "500", "250")

root.mainloop()
