# visualizzare l'elenco degli studenti di una classe con debito

'''
- rappresentare uno studente come dizionario(nome, cognome, debiti)
+ inserire i dati corrispondenti ad uno studente
+ formare una classe di studenti
+ selezionare gli studenti con debiti
'''

# funzione per la creazione di un dizionario studente
def creaStudente():
    nome = input( "nome" )
    cognome = input( "cognome" )

    debiti = []

    finito = False
    while not finito:
        fine = input( "Finito?" )
        if fine == "f":
            finito = True

        else:
            materia = input( "Materia" )
            debiti.append( materia )

    studente = {"nome": nome, "cognome": cognome, "debiti": debiti}

    return studente

# funzione per formare una classe di n studenti
def formaClasse(n):
    classe = []

    for i in range( 0, n ):
        s = creaStudente()
        classe.append( s )

    return classe

# procedura per visualizzare i nominativi degli studenti con debito
def stampaDebiti(classe):
    for studente in classe:
        if len( studente["debiti"] ) > 0:
            print( studente["nome"], studente["cognome"] )
            for materia in studente["debiti"]:
                print( materia, end="+" )


classe = formaClasse( 3 )
stampaDebiti( classe )
