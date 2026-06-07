def testaLista(diz, k, v):
    if k not in diz.keys():
        diz[k]=[]    
        
    diz[k].append(v)
    
d = dict()

def prova (a=1, b=2, c=3):
    print(a+b+c)
    
testaLista(d, "ok", 55)
testaLista(d, "ok", 665)
print(d)

prova()
prova(b=0)
prova(c=-5, b=4)

