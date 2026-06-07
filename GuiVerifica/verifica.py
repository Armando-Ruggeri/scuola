import tkinter as tk

class GUI:
    def __init__(self):
        self.finestra = tk.Tk()
        self.finestra.title("Esercizio")
        self.finestra.geometry("150x100")
        self.btn_plus = tk.Button(self.finestra, text="+1", width=5, command=self.incrementa1)
        self.btn_meno = tk.Button(self.finestra, text="-", width=5, command=self.togli1)
        self.btn_reset = tk.Button(self.finestra, text="Reset", width=5, command=self.azzera)

        self.numero = tk.IntVar(self.finestra)
        self.numero.set(0)
        self.etichetta = tk.Label(self.finestra, text="Numero")
        self.txt_numero = tk.Entry(self.finestra, textvariable= self.numero, width=4)

        self.etichetta.grid(row=0, column=0)
        self.txt_numero.grid(row=0, column=1)
        self.btn_plus.grid(row=0, column=2)
        self.btn_meno.grid(row=1, column=2)
        self.btn_reset.grid(row=2, column=2)

        self.finestra.mainloop()

    def incrementa1(self):
        self.numero.set(self.numero.get()+1)

    def togli1(self):
        self.numero.set(self.numero.get() - 1)

    def azzera(self):
        self.numero.set(0)

gui = GUI()
