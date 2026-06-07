import tkinter as tk
from tkinter import ttk

master = tk.Tk()

# creating a Fra, e which can expand according
# to the size of the window
pane = tk.Frame(master)
pane.pack(fill = tk.BOTH, expand = True)

# button widgets which can also expand and fill
# in the parent widget entirely
# Button 1
b1 = tk.Button(pane, text = "Click me !",
            background = "red", fg = "white")
b1.pack(side = tk.TOP, expand = True, fill = tk.BOTH)

# Button 2
b2 = tk.Button(pane, text = "Click me too",
            background = "blue", fg = "white")
b2.pack(side = tk.TOP, expand = True, fill = tk.BOTH)

master.mainloop()
