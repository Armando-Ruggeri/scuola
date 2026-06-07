# definisce la scacchiera con cui iniziamo il gioco
def scacchieraIniziale():
    for riga in range( 0, 3 ):
        sottolista = []
        for colonna in range( 0, 3 ):
            sottolista.append( spazioVuoto )

        scacchiera.append( sottolista )

# stampa la scacchiera
def stampaScacchiera():
    for riga in range( 0, 3 ):
        stringaRiga = ""
        for colonna in range( 0, 3 ):
            stringaRiga = stringaRiga + scacchiera[riga][colonna]

        print( stringaRiga )

# giocatore attuale è colui che è di turno adesso
# giocatore prossimo è quello che diventa di turno
def cambiaTurno(giocatoreAttuale):
    if giocatoreAttuale == 1:
        giocatoreProssimo = 2
    else:
        giocatoreProssimo = 1

    return giocatoreProssimo

def effettuaMossa(giocatore):
    global contaMosse
    riga = int(input( "Quale riga?") )
    while ( riga >= 3 or riga < 0 ):
        riga = int( input( "Inserisci riga corretta" ) )

    colonna = int(input( "Quale colonna?") )
    while (colonna >= 3 or colonna < 0):
        colonna = int( input( "Inserisci colonna corretta" ) )

    if (scacchiera[riga][colonna] == spazioVuoto):
        if giocatore == 1:
            scacchiera[riga][colonna] = "X"
        else:
            scacchiera[riga][colonna] = "0"
    else:
        print("Ripeti la mossa")
        effettuaMossa(giocatore)

    contaMosse = contaMosse + 1

# verifica condizioni per il pareggio
def hoUnPareggio():
    if contaMosse == 10:
        return True
    else:
        return False

def vittoriaRiga ( riga ):
    col = 0
    uguali = True

    if scacchiera[riga][col] != spazioVuoto:
        simbolo = scacchiera[riga][0]

        while (col < 3) and uguali :
            if (scacchiera[riga][col] != simbolo):
                uguali = False
            else:
                col = col + 1
    else:
        uguali = False

    #print("Riga", riga, uguali)
    return uguali

def vittoriaColonna ( colonna ):
    riga = 0
    uguali = True

    if scacchiera[riga][colonna] != spazioVuoto:
        simbolo = scacchiera[0][colonna]

        while (riga < 3) and uguali :
            if (scacchiera[riga][colonna] != simbolo):
                uguali = False
            else:
                riga = riga + 1
    else:
        uguali = False

    #print("Colonna", colonna, uguali)
    return uguali

def vittoriaDiagonali():
    uguali = True

    if scacchiera[0][0] != spazioVuoto:
        simbolo = scacchiera[0][0]
        riga = 0
        colonna = 0

        while (riga < 3) and (colonna < 3) and uguali :
            if (scacchiera[riga][colonna] != simbolo):
                uguali = False
            else:
                riga = riga + 1
                colonna = colonna + 1

        if not uguali:
            riga = 2
            colonna = 2
            uguali = True

            while (riga >= 0) and (colonna >= 0) and uguali:
                if (scacchiera[riga][colonna] != simbolo):
                    uguali = False
                else:
                    riga = riga - 1
                    colonna = colonna - 1

        else:
            # la prima diagonale dà la vittoria
            return uguali

    # il carattere nella prima casella è lo spazio vuoto
    else:
        uguali = False

    # restituisce il risultato della seconda diagonale
    return uguali

def faiPartita():
    giocatoreAttuale = 1
    riga = 0
    colonna = 0
    partitaFinita = False

    scacchieraIniziale()
    effettuaMossa( giocatoreAttuale )

    while not partitaFinita:
        riga = 0
        colonna = 0
        while riga < 3:
            if vittoriaRiga( riga ):
                partitaFinita = True
                print( "Mossa n.", contaMosse, "Vittoria alla riga", riga )
                riga = 1000

            else:
                riga = riga + 1

        while colonna < 3:
            if vittoriaColonna(colonna):
                partitaFinita = True
                print("Mossa n.", contaMosse, "Vittoria alla colonna", colonna)
                colonna = 1000
            else:
                colonna = colonna + 1

        if vittoriaDiagonali():
            partitaFinita = True
            print( "Mossa n.", contaMosse, "Vittoria sulle diagonali" )


        if hoUnPareggio():
            partitaFinita = True
            print("Pareggio" )

        if not partitaFinita:
            stampaScacchiera()
            giocatoreAttuale = cambiaTurno(giocatoreAttuale)
            print("\nMuove il giocatore", giocatoreAttuale)
            effettuaMossa( giocatoreAttuale )

        else:
            print("\nScacchiera finale")
            stampaScacchiera()

# programma
scacchiera = []
contaMosse = 0
spazioVuoto = "*"

faiPartita()