import typing 
import nodo as n
import arco as a
import queue as q
import pila as p
from collections import deque as d

class Grafo:
    def __init__(self, numNodi:int, orientato = False) -> None:
        self.nodi: list = []
        self.orientato = orientato
        for i in range(numNodi):
            self.nodi.append(n.Nodo(i))
            
        self.numNodi = numNodi
    
    
    def inserisciArco(self, da: int, a: int) -> None:
        if da >=0 and da < self.numNodi and a >=0 and a < self.numNodi:
            if not self.orientato:
                self.nodi[a].vicini.append(da)
            
            self.nodi[da].vicini.append(a)
                 
    def cercaArco(self, da: int, a:int)->bool:
        if a in self.nodi[da]:
            return True
        else:
            return False
            
    
    def stampa(self):
        for pos in range(self.numNodi):
            if self.nodi[pos]!= []:
                self.nodi[pos].stampa()
        
    def accettabile(self, arco, soluzione) -> bool:
        nodiDa = {arc.da for arc in soluzione.elementi}
        nodiA = {arc.a for arc in soluzione.elementi}
        ok1 = False
        ok2 = False
        
        if not (arco.da in nodiDa):
            ok1 = True
        if not (arco.a in nodiA):
            ok2 = True
        if ok1 and ok2 :
            print(f"accettato ({arco.da},{arco.a})")
        else:
            print(f"rifiutato ({arco.da},{arco.a})")
        
        return ok1 and ok2
    
    def soluzioneCompleta(self, soluzione):
        return soluzione.dimensione == (self.numNodi/2)
    
           
    def stampaSoluzione(self, sol):
        print("Soluzione")
        while not sol.empty():
            arco = sol.leggi()
            arco.stampa()
            sol.elimina()
# ----------------------------------------------------------------
    def ric(self,gruppo, nodoCorrenteice, sol):
        if self.soluzioneCompleta(sol):
            self.stampaSoluzione(sol)
        else:
            nodoCorrenteiceNodo = gruppo[nodoCorrenteice]
            nodoCistacorrenteicilistaVicini = self.nodi[nodoCorrenteiceNodo].listaVicini
            for vicino in nodoCistacorrenteicilistaVicini:
                arco = a.Arco(nodoCorrenteiceNodo, vicino)
                if self.accettabile(arco, sol):
                    sol.add(arco)
                    self.ric (gruppo, nodoCorrenteice + 1, sol)
                    sol.elimina()

                    
    def isBipart(self):
        visti : list = [None for _ in range(self.numNodi)]
        risultato = True
        pila = p.Pila() 
        
        for start in range(self.numNodi):
            if visti[start] == None:    
                pila.elementi = [start]
                head = 0
                visti[start] = True
                
                while not head == pila.dimensione:
                    nodoCorrente: int = pila.elementi[head]
                    head += 1
                    pila.stampa()
                    listaVicini = self.nodi[nodoCorrente].vicini
                    for vicino in listaVicini:
                        if visti[vicino] == None:
                            visti[vicino] = not visti[nodoCorrente]
                            pila.inCoda(vicino)
                        elif visti[nodoCorrente] == visti[vicino]:
                            print(nodoCorrente, vicino, visti)
                            return False
        return True
                