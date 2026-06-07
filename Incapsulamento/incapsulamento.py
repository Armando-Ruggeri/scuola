class Persona:
    #costruttore
    def __init__(self, nome, cognome) -> None:
        # attributi
        self.nome = nome
        self.cognome = cognome
        
    def visualizza(self):
        print(f"La persona si chiama {self.nome} {self.cognome}")
        
        
# programma
# creo un oggetto Persona
p = Persona ("Giuseppe", "Garibaldi")

# stampo i suoi attributi
p.visualizza()