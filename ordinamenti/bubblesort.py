def bubblesort(lista: list):
    lung: int = len(lista)
    if lung > 0:
        fattoScambi: bool = True
        i = 0
        
        while (fattoScambi):
            fattoScambi = False
            for i in range (lung - 1):
                if lista[i] > lista[i+1]:
                    # scambio gli elementi vicini
                    temp = lista[i]
                    lista[i] = lista[i+1]
                    lista[i+1] = temp
                    
                    fattoScambi = True
                    i = i + 1
    print(lista)
    
    
bubblesort([4,8, 12, 3, 7, 1, 5, 43, 6])