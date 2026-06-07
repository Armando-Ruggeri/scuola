class Pila:
    def __init__(self) -> None:
        self.elementi = []
        self.dimensione = 0
        
    def inCoda(self, elemento) -> None:
        self.elementi.append(elemento)
        self.dimensione = self.dimensione + 1
        
    def inTesta(self, elemento) -> None:
        self.elementi.insert(0, elemento)
        self.dimensione = self.dimensione + 1
        
    def getCoda(self) -> int:
        if self.dimensione > 0:
            nodoEliminato = self.elementi[self.dimensione-1]
            self.elementi.remove(nodoEliminato)
            self.dimensione = self.dimensione - 1
            return nodoEliminato
        else:
            return -1
        
    def getTesta(self) -> int:
        if self.dimensione > 0:
            nodoEliminato = self.elementi[0]
            self.elementi.remove(nodoEliminato)
            self.dimensione = self.dimensione - 1
            return nodoEliminato
        else:
            return -1
            
    def leggi(self):
        if self.dimensione > 0:
            return self.elementi[self.dimensione - 1]
        else:
            print("pila vuota")
            return -1
    
    def stampa(self):
        if self.dimensione > 0:
            print("Pila")
            for i in range(self.dimensione-1, -1, -1):
                print(f"elemento {i}: {self.elementi[i]}")
        else:
            print("Pila vuota")
            
        print()
            
    def empty(self):
        return self.elementi == []
    
    def getPila(self):
        return self.elementi
    
    def svuota(self):
        self.elementi = []
        self.dimensione = 0