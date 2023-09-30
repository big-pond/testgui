#!/usr/bin/env python3
#-*-coding: utf-8-*-

import tkinter as tk
import tkinter.ttk as ttk
root = tk.Tk()
frame = tk.Frame(root)
frame.grid()
combobox = ttk.Combobox(frame, values = ["ОДИН", "ДВА", "ТРИ"], height=3)
combobox.set(u'ОДИН')
combobox.grid(column=0,row=0)
root.mainloop()

