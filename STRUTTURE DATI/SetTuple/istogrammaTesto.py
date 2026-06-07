def scomponiTesto(testo):
    conteggi = [0] * 128

    for lettera in testo:
        posizione = ord( lettera )
        conteggi[posizione] = conteggi[posizione] + 1

    for posizione in range( 0, 128 ):
        print( chr( posizione ), conteggi[posizione] )

    return conteggi


def disegnaIst(contatori):
    for i in range( 0, 128 ):
        if (contatori[i] != 0):
            print( chr( i ), "*" * contatori[i] )


c = scomponiTesto( "allacciare le cinture prima del decollo" )
print( "-----------------------" )
disegnaIst( c )
