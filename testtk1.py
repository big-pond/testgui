#!/usr/bin/env python3
#-*-coding: utf-8-*-

from tkinter import *

window = Tk()
window.title("Добро пожаловать в приложение Python Tkinter")
lbl = Label(window, text="Привет мир!")
lbl.grid(column=0, row=0)
window.mainloop()

