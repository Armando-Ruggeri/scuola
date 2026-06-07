def formaSet():
    pezzi = set()

    x = input( "inserisci un pezzo" )
    while x != "0":
        pezzi.add( x )
        x = input( "inserisci un pezzo" )

    return pezzi


def stampaPezzi(setPezzi):
    print( "Ci sono ", len( setPezzi ), "pezzi" )

    for elemento in setPezzi:
        print( elemento )


p = formaSet()
stampaPezzi( p )

p1 = formaSet()
stampaPezzi( p1 )










# aggiungere un elemento e ottenere il set risultato
# aggiungere una lista di elementi
# eliminare un elemento