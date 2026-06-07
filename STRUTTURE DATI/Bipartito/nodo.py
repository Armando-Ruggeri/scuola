import typing
import arco as a

class Nodo:
    def __init__(self, indice: int, etichetta = None) -> None:
        self.indice = indice
        self.vicini = []
        self.etichetta = etichetta
        
    def aggiungiArco(self, destinazione: int, peso: float = 0) -> None:
        self.vicini.append(destinazione)
        
    def eliminaArco(self, destinazione: int) -> None:
        if destinazione in self.vicini:
            del self.vicini[destinazione]
    
    def stampa(self) -> None:
        print(f"Nodo {self.indice} vicini: {self.vicini}")  
        
# ----------------------------------------------------------------        