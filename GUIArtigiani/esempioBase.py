import tkinter as tk


# creazione finestra
gui = tk.Tk()
#dimensioni finestra
gui.geometry("200x500+800+200")
gui.resizable(height=False, width=True)

#creazione widget
frame = tk.Frame(gui)
frame.pack(fill = tk.BOTH, expand = True)
etNome = tk.Label(frame,text="Nome", bg="red")
etNome.pack(side = tk.TOP, expand = True, fill = tk.BOTH)
txtNome = tk.Entry(frame,width=50)
txtNome.pack(side = tk.TOP, expand = True, fill = tk.BOTH)

etCognome = tk.Label(text="Cognome")
txtCognome = tk.Entry(width=50)
pulsante1 = tk.Button(gui, text = 'Invia')

#aggiungere widget a finestra
etNome.pack()
txtNome.pack()
etCognome.pack()
txtCognome.pack()
pulsante1.pack()
etNome.config(background="green")


#esegui
while True:
    nome = txtNome.get()
    print(nome)
    gui.mainloop()
