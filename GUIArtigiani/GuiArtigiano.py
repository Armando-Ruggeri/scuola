import tkinter as tk
from tkinter import ttk

class GuiArtigiano:
    def __init__(self):
        gui = tk.Tk()
        gui.geometry("800x100+300+150")
        gui.resizable(height=False, width=False)
        gui.title("Anagrafica Artigiano")

        # creazione widget
        frmNome = ttk.Frame(gui, padding=2, borderwidth=4)
        frmNome.pack(side = tk.LEFT)

        etNome = tk.Label(frmNome, text="Nome")
        txtNome = tk.Entry(frmNome, width=53)
        etNome.pack(side = tk.LEFT)
        txtNome.pack(side = tk.LEFT)

        frmCognome = ttk.Frame(gui, padding=2, borderwidth=4)
        frmCognome.pack(side = tk.LEFT)
        etCognome = tk.Label(text="Cognome")
        txtCognome = tk.Entry(width=40)
        etCognome.pack(side = tk.LEFT, fill = tk.X)
        txtCognome.pack(side = tk.LEFT, fill = tk.X)

        self.nome = txtNome

        pulsante1 = tk.Button(gui, text = 'Invia', command=self.stampa)
        pulsante1["padx"]=20

        #print(pulsante1.config().keys())
        pulsante1.pack(side=tk.LEFT)

        self.gui = gui


    def stampa(self):
        print(self.nome.get())


    def esegui(self):
        self.gui.mainloop()

app = GuiArtigiano()
app.esegui()
