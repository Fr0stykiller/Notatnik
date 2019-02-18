from tkinter import *
from datetime import datetime
import tkinter as tk
import tkinter.scrolledtext as tkscrolled
import sqlite3
from tkcalendar import Calendar, DateEntry

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
                           text="ODCZYTAJ NOTATKĘ", font=('Calibri Light', 20), command=self.odczytaj)
        self.btn2.pack(fill=BOTH, expand=1)

        self.c = conn.cursor()
        self.c.execute('''CREATE VIRTUAL TABLE IF NOT EXISTS notatki USING FTS5
             (data, nazwa, notatka)''')

    def new_note(self):
        self.newWindow = tk.Toplevel(self.master)
        self.dodtyt = tk.Label(
            self.newWindow, text="TYTUŁ:", font=('Calibri Light', 20))
        self.dodtyt.grid(column=0, row=0, sticky='w')
        self.tytul = tk.Entry(self.newWindow, width=85)
        self.tytul.grid(column=1, row=0, sticky='w')
        self.textfield = tkscrolled.ScrolledText(self.newWindow)
        self.textfield.insert(INSERT, "kosjdksd")
        self.textfield.grid(columnspan=2)
        self.addButton = Button(
            self.newWindow, text="DODAJ!", bg="LIGHTPINK", font=('Calibri Light', 20), command=self.dodaj)
        self.addButton.grid(columnspan=2)

    def searchDatabase(self, searchQuery):
        self.c.execute(
            '''SELECT * FROM notatki WHERE nazwa = ? COLLATE NOCASE''', (searchQuery,))
        self.searchResult = self.c.fetchall()
        conn.commit()
        print(searchQuery)
        print(self.searchResult)
        return self.c.fetchall()

    def odczytaj(self):
        self.newWindow1 = tk.Toplevel(self.master)
        self.ramka1 = tk.Frame(self.newWindow1, bg='white', bd=10)
        self.ramka1.grid()
        self.szukajd = tk.Label(
            self.ramka1, text="SZUKAJ PO DACIE", font=('Calibri LIGHT', 25))
        self.szukajd.grid(column=0, row=1)
        self.szukajde = Calendar(self.ramka1)
        self.szukajde.grid(column=0, row=2)
        self.szukajdb = Button(self.ramka1, text="SZUKAJ!", bg="slategray2", font=('Calibri Light', 15))
        self.szukajdb.grid(column=0, row=4)
        self.separator = Frame(self.newWindow1, height=3, width=300, bg="slategray4")
        self.separator.grid(column=0, row=5)
        self.szukajt = tk.Label(
            self.newWindow1, text="SZUKAJ PO TYTULE", font=('Calibri Light', 25))
        self.newWindow1.grid_columnconfigure(0, minsize=300)
        self.szukajt.grid(column=0, row=6)
        self.szukajte = tk.Entry(self.newWindow1, width=40)
        self.szukajte.grid(column=0, row=7)
        self.szukajtb = Button(
            self.newWindow1, text="SZUKAJ!", bg="slategray2", font=('Calibri Light', 15), command=lambda: self.searchDatabase(self.szukajte.get()))
        self.szukajtb.grid(column=0, row=9)

        self.newWindow1.grid_rowconfigure(3, minsize=10)
        self.newWindow1.grid_rowconfigure(5, minsize=30)
        self.newWindow1.grid_rowconfigure(8, minsize=30)
        self.newWindow1.grid_rowconfigure(10, minsize=30)
        # self.labelOdczyt = tk.Label(self.newWindow1, text=data, font=('Calibri Light', 15))
        # self.labelOdczyt.grid(column=0, row=3)

    def dodaj(self):
        self.notka = self.textfield.get("1.0", END)
        self.nazwanotki = self.tytul.get()
        print(self.notka)
        now = datetime.now()
        print(now)
        self.c.execute('''INSERT INTO notatki (data, nazwa, notatka) VALUES (?, ?, ?)''',
                       (now, self.nazwanotki, self.notka,))
        conn.commit()
        self.newWindow.destroy()


root = tk.Tk()
Notatnik(root, "400", "300")
# top1 = Toplevel()
# top2 = Toplevel()
# TopLevelWindow(top1, "300", "300")
# TopLevelWindow(top2, "500", "250")

root.mainloop()
