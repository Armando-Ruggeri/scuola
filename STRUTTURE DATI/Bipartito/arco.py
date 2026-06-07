class Arco:
    def __init__(self, da:int, a: int, peso:float = 0.0) -> None:
        self.da = da
        self.a = a
        self.peso = peso
        
    def stampa(self):
        print(f"Arco ({self.da}, {self.a})")
            
# ----------------------------------------------------------------            
