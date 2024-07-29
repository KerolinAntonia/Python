import random

def coitados(x):
    l = []
    for i in range (1,x+1):
        nome = input(f"Nome {i}: ")
        l.append(nome)
    l1 = random.randint(0,len(l))
    print(l)
    return l[l1]
    
print(coitados(6))