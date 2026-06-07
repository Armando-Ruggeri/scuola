# nodi già visitati
visitati = []

# classe Nodo
class Nodo:
    def __init__(self, v):
        self.valore = v
        self.collegati = []
        
    # collega il nodo con un latro
    def collega(self, nodo):
        self.collegati.append(nodo)
        
    # verifica se il nodoDest è raggiungibile
    def raggiungibile(self, nodoDest):
        trovato = False
        if nodoDest in self.collegati:
            return True
        else:
            for nodo in self.collegati:
                trovato = nodo.raggiungibile(nodoDest)
        
        return trovato
            
    # stampa il nodo e ricorsivamente quelli a lui collegati direttamente
    def stampa(self):
        if self not in visitati:
            print(f"{self.valore}", end=" ")
            visitati.append(self)
            
            for nodo in self.collegati:
                nodo.stampa()
                
        else:
            print()
                           
# classe Grafo
class Grafo:
    def __init__(self, nodoRadice):
        self.vertici = [nodoRadice]
          
    # verifica se due nodi sono raggiungibili tra di loro         
    def raggiungibile (self, nodoA, nodoB):
        if nodoA in self.vertici:
            return nodoA.raggiungibile(nodoB)  
              
    # stampa tutti i nodi del grafo a meno di cicli    
    def stampa(self):
        self.vertici[0].stampa()
                 
 
# programma      
n1 = Nodo(1)
n2 = Nodo(2)
n3 = Nodo(3)
n4 = Nodo(4)
n5 = Nodo(5)
n6 = Nodo(6)

n1.collega(n2)
n1.collega(n3)
n2.collega(n4)
n3.collega(n5)
n1.collega(n6)
n6.collega(n1)

g = Grafo(n1)
print(g.raggiungibile(n1,n6))
g.stampa()

