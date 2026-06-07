import csv
from decimal import Decimal

# -----------------------------------------------------------------------------------------
# lettura e trasformazione dei dati nel file in lista di dizionari
# -----------------------------------------------------------------------------------------

def leggiDati(nomeFile: str)-> list:
    # apertura del file contenente i dati
    dati = open(nomeFile)
    
    # trasformazione del file in dizionario
    elencoDati = csv.DictReader(dati, delimiter=";")
    
    # lista dati da elaborare
    listaAnalisi: list = []
    
    # lettura dei dati del dizionario
    for dizDati in elencoDati:
        # verifico se la riga di dati si riferisce al settore Energia
        if dizDati["OC_TEMA_SINTETICO"] == "Energia":
            # aggiungo il dizionario letto alla lista di dati da analizzare successivamente
            listaAnalisi.append(dizDati)
            
            
    # chiudo il file
    dati.close()
    
    # restituisco i dati da analizzare successivamente
    return listaAnalisi

# -----------------------------------------------------------------------------------------
# elaborazione dei dati selezionati e restituzione del dizionario con i risultati
# -----------------------------------------------------------------------------------------
    
def elaboraDati(elencoDati: list) -> dict:
    comune = dict()
    for elemento in elencoDati:
        nome = elemento["OC_DENOMINAZIONE_SLL"]
        nome = nome.replace(" ", "_")
        costo = elemento["COSTO_REALIZZATO"]
        costo = costo.replace(",", ".")
        
        if nome in comune.keys():
            comune[nome] = comune[nome] + float(Decimal(costo))
        else:
            comune[nome] = float(costo)
            
    return comune

# -----------------------------------------------------------------------------------------
# salvataggio dei dati nel file risultati.txt per future elaborazioni
# -----------------------------------------------------------------------------------------

def salva_risultati(risultati: dict):
    dati = open(r"C:\Users\Armando\Documents\LABORATORIO\PythonLab\OpenData\risultati.txt", "wt")
    for città in risultati.keys():
        dati.write(città + " " + str(risultati[città]) + "\n")
        
    dati.close()
    
# -----------------------------------------------------------------------------------------
# visualizzazione formattata dei risultati
# -----------------------------------------------------------------------------------------

def visualizzaRisultati(risultati: dict):
    for città in risultati.keys():
        valore = risultati[città]
        print(f"{città} \t\t\tcosto\t{valore:.2f}")

# -----------------------------------------------------------------------------------------
# sequenza principale delle operazioni
# -----------------------------------------------------------------------------------------

def esegui():
    listaDati = leggiDati(r"C:\Users\Armando\Documents\LABORATORIO\PythonLab\OpenData\progetti.csv")
    dizRisultati = elaboraDati(listaDati)
    visualizzaRisultati(dizRisultati)
    salva_risultati(dizRisultati)
    

if __name__ == "__main__":
    esegui()