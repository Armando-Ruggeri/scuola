class Pila:
    def __init__(self) -> None:
        self.elementi = []
        self.dimensione = 0
        
    def add(self, elemento):
        self.elementi.append(elemento)
        self.dimensione = self.dimensione +1
        
    def elimina(self):
        if self.dimensione > 0:
            self.elementi.remove(self.elementi[self.dimensione-1])
            
    def leggi(self):
        return self.elementi[self.dimensione-1]
    
    def stampa(self):
        if self.dimensione > 0:
            print("coda")
            for i in range(0,self.dimensione, -1):
                print(self.elementi[i])
            
    def empty(self):
        return self.elementi == []