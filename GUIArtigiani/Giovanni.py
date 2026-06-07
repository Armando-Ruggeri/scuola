import tkinter as tk

#interfaccia grafica
gui = tk.Tk()

etnome = tk.Label(gui, text="Nome")
bottone = tk.Button(gui, text= "Icriviti")

gui.geometry("300x300+300+300")
gui.resizable(height=False, width=True)
gui.configure(background = "white")

etNome = tk.Label(text="Nome",)
txtNome = tk.Entry(width=25)
etCognome = tk.Label(text="Cognome")
txtCognome = tk.Entry(width=25)
bottone= tk.Button(gui, text = "Iscriviti")
etNome.pack()
txtNome.pack()
etCognome.pack()
txtCognome.pack()
bottone.pack()

gui.mainloop()


class Partecipante:
  def __init__ (self, nome, cognome, reddito, statoOccupazione,statoIscrizione):
    self.nome = nome
    self.cognome = cognome
    self.reddito = reddito
    self.statoOccupazione = statoOccupazione
    self.statoIscrizione = statoIscrizione


#interfaccia grafica
gui = tk.Tk()

etnome = tk.Label(gui, text="Nome")
bottone = tk.Button(gui, text= "Icriviti")

gui.geometry("300x300+300+300")
gui.resizable(height=False, width=True)
gui.configure(background = "white")

etNome = tk.Label(text="Nome",)
txtNome = tk.Entry(width=25)
etCognome = tk.Label(text="Cognome")
txtCognome = tk.Entry(width=25)
bottone= tk.Button(gui, text = "Iscriviti")

etNome.pack()
txtNome.pack()
etCognome.pack()
txtCognome.pack()
bottone.pack()

gui.mainloop()

class Corso(Partecipante):
  def __init__(self, costoIscrizione, limiteIscritti):
    self.costoIsrizione = costoIscrizione
    self.limiteIscritti = limiteIscritti

  #metodo per aggiungere iscrizione ad un corso
  def aggiungiscritto(self, unPartecipante):
    self.iscritto = unPartecipante

  #metodo per rimuovere iscrizione da un corso
  def rimuoviIscritto(self, unPartecipante):
    self.iscritto = unPartecipante

class Ente(Corso):
  #metodo per calcolare il totale derivato dal costo delle iscrizioni
  def totaleCostoiscrizioni():



