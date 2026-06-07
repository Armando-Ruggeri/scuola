import tkinter as tk

class GUI_Rubrica:
    def __init__(self, rub=None):
        self.rubrica = rub
        self.checkButtons = []
        gui = tk.Tk()
        gui.title("Rubrica")
        gui.geometry("600x300+500+200")
        gui.resizable(height=False, width=False)

        if (self.rubrica != None):
            cont = 0
            for cliente in self.rubrica:

                # mostra cliente
                v = tk.BooleanVar().set(False)
                self.checkButtons[cont] = tk.Checkbutton(gui, text=cliente.nome + " " + cliente.cognome, variable = v, onvalue= 1, offvalue=0)
                self.checkButtons[cont].select()
                print("risultato ", v)
                cont = cont + 1
                self.checkButtons[cont].pack()

            button = tk.Button(text="prova", command=self.test())
            button.pack()
        gui.mainloop()

    def test(self):
        for c in self.checkbuttons:
            print(c.state)



class Cliente:
    def __init__(self, n="", c=""):
        self.nome = n
        self.cognome = c

c1 = Cliente("Aldo", "Rossi")
c2 = Cliente("Mario" "rossi")
l = [c1, c2]
g = GUI_Rubrica(l)
