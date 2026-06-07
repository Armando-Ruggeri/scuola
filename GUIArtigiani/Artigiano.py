class Artigiano:
    def __init__(self, nome, cognome, specializzazione):
        self.__nome = nome
        self.__cognome = cognome
        self.__spec = specializzazione
        self.__cassetta = None

    def aggCassetta(self, unaCassetta):
        self.__cassetta = unaCassetta

    def getCassetta(self):
        return self.__cassetta

    def usa(self, unMezzo):
        print("\n\nusa")
        unMezzo.stampa()
    def stampa(self):
        print(self.__nome, " ", self.__cognome, " ", self.__spec)
        if (self.__cassetta != None):
            self.__cassetta.stampa()
            #print("ha una cassetta")
        else:
            print("NON ha una cassetta")

class Cassetta:
    def __init__(self):
        self.__attrezzi = []

    def aggAttrezzo(self, unAttrezzo):
        self.__attrezzi.append(unAttrezzo)

    def stampa(self):
        for attrezzo in self.__attrezzi:
            attrezzo.stampa()

class Attrezzo:
    def __init__(self, nome, azione):
        self.__nome = nome
        self.__azione = azione

    def svolge(self):
        print(self.__azione)

    def stampa(self):
        print(self.__nome)
        self.svolge()

class Mezzo:
    def __init__(self, modello, targa):
        self.__modello = modello
        self.__targa = targa

    def stampa(self):
        print(self.__modello, " ", self.__targa)

class Auto (Mezzo):
    def __init__(self, modello, targa, colore):
        Mezzo.__init__(self, modello, targa)
        self.__colore = colore

    def stampa(self):
        super().stampa()
        print(self.__colore)

class AutoElettrica(Auto):
    def __init__(self, kw, modello, targa, colore):
        Auto.__init__(self, modello, targa, colore)
        self.__kw = kw

    def stampa(self):
        print("KW ", self.__kw)
        super().stampa()
