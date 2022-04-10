"""Baby's first Python script"""

print('Hello, world!')

from tkinter import *
from tkinter import ttk

window = Tk()
window.title("Test Window")
frm = ttk.Frame(window, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=window.destroy).grid(column=1, row=0)
window.mainloop()
