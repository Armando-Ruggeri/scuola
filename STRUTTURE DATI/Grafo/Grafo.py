visitati = []


class Nodo:
    def __init__(self, valore):
        self.valore = valore
        self.nodi = []
        
    def connetti(self, nodo, nomeConn=""):
        self.nodi.append(nodo)
        self.nomeConnessione = nomeConn
        
    # verifica se un nodo è raggiungibile
    def raggiungibile(self, nodoDest):
        for nodo in self.nodi:
            if nodo.valore == nodoDest.valore:
                return True
            else:
                return nodo.raggiungibile(nodoDest)
            
        return False
        
    def visita(self):
        for nodo in self.nodi:           
            if (nodo in visitati):
                print(f"({self.valore},{nodo.valore}) già presente")
                break
            else:
               print(self.valore, "-->", nodo.valore)
               visitati.append(nodo)
               nodo.visita()
            
    def visitabile(self, esclusi):
        for nodo in self.nodi:
            if nodo in esclusi:
                return False
          
        
class Grafo:
    def __init__(self, nodo):
        self.radice = nodo
        
    def visita(self):
        self.radice.visita()

                
            
n1 = Nodo(10)
n2 = Nodo(20)
n3 = Nodo(25)
n4 = Nodo(30)
n5 = Nodo(35)
n6 = Nodo(40)
n7 = Nodo(28)
n8 = Nodo(38)

n1.connetti(n2)
n2.connetti(n3)
n2.connetti(n4)
n2.connetti(n5)
n3.connetti(n5)
n4.connetti(n6)
n4.connetti(n1)
n5.connetti(n2)


g = Grafo(n1)
n1.visita()
#print(n1.raggiungibile(n5))