class Conto:
    def __init__(self, numero:int) -> None:
        self.__iban = numero
        
    def get_Iban(self) -> int:
        return self.__iban
    
    def set_Iban(self, nuovoIban) -> None:
        self.__iban = nuovoIban
        
    def stampa(self) -> None:
        print(f"IBAN {self.__iban}")
        
        
        
conto = Conto(1234)   
conto.stampa()
#print("conto ", conto.__iban) 
conto.__iban = 5678
conto.set_Iban(9999)
conto.stampa()
