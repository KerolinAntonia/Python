
lista1 = []
lista2 = []
lista3 = [] 

for i in range(1,4):
    n1 = int(input("LINHA 1: "))
    lista1.append(n1)
    
for i in range(1,4):
    n2 = int(input("LINHA 2: "))
    lista2.append(n2)

for i in range(1,4):
    n3 = int(input("LINHA 3: "))
    lista3.append(n3)
    
matriz = ([lista1], [lista2], [lista3])

print(matriz)