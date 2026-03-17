def selectionsort(lista: list):
    postoGiusto = 0
    lung = len(lista)
    while postoGiusto < lung:
        # cerco la posizione del massimo
        posMax = getPosMax( lista, postoGiusto)
        
        #scambia postoGiusto con posMax
        temp = lista[postoGiusto]
        lista[postoGiusto] = lista[posMax] 
        lista[posMax] = temp
        
        postoGiusto = postoGiusto + 1
        
    print(lista)


def getPosMax(lista: list, inizio: int): 
    lung: int = len(lista)
    if lung > 0 and inizio < lung:
        massimo = lista[inizio]
        posMax = inizio
        for pos in range (inizio, lung):
            if (lista[pos] > massimo):
                massimo = lista[pos]
                posMax = pos
                
    else:
        return -1
             
    return posMax
    
    
selectionsort([4,8, 12, 3, 7, 1, 5, 43, 6])