import nodo as n
import grafo as g
import pila as p

def main():
    grafo = g.Grafo(8)

    grafo.inserisciArco(0,3)
 
    grafo.inserisciArco(0,5)
    grafo.inserisciArco(2,1)
    grafo.inserisciArco(2,5)
    grafo.inserisciArco(2,7)
    grafo.inserisciArco(4,3)
    grafo.inserisciArco(4,5)
    grafo.inserisciArco(6,1)
    grafo.inserisciArco(6,7)
    grafo.stampa()
    print (grafo.isBipart())
 
    
if __name__ == "__main__":
    main()