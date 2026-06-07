import tkinter as tk

class Vista:
    def __init__(self):
        self.fin = tk.Tk()
        self.fin.title("Esempio")
        self.fin.geometry('200x100+800+400')
        
        self.var1 = tk.StringVar()
        self.var2 = tk.StringVar()
       
        self.nome = tk.Entry(self.fin, textvariable= self.var1)
        self.cognome = tk.Entry(self.fin, textvariable= self.var2)
        
        self.salva = tk.Button(self.fin, text="Salva")
        
        # griglia
        self.etNome = tk.Label(self.fin, text="Nome")
        self.etNome.grid(row=0,column=0)
        self.etCognome = tk.Label(self.fin, text="Cognome")
        self.etCognome.grid(row=1,column=0)
        self.nome.grid(row=0,column=1)
        self.cognome.grid(row=1,column=1)
        self.salva.grid(row=2,column=1)
        
        self.fin.mainloop()
        
    
            
v = Vista()