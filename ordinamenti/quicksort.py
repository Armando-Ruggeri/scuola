import random 

def quicksort(lista: list):
  pass
    
def dividi(lista, primo, ultimo):
    if primo < ultimo:
        pivot = lista[ultimo -1]
        for i in range(primo, ultimo):
            if lista[i] > pivot:
                scambia(i, pivot, lista)
                pivot = i
            
    
def scambia(posX, posY, lista):
    temp = lista[posX]
    lista[posX] = lista[posY]
    lista[posY] = temp
    
    
x = [8, 4, 1, 9, 12, 7, 13, 24, 17]
ris = quicksort(x)
print(ris)