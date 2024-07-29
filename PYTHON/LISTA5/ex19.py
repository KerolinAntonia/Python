def matriz(x):
    l1= []
    for i in range (1,4):
        y = x
        l1.append(y)
    l2= []
    for i in range (1,4):
        y = x
        l2.append(y)
    l3= []
    for i in range (1,4):
        y = x
        l3.append(y)
    matriz = ([])
    matriz.append(l1)
    matriz.append(l2)
    matriz.append(l3)
    for i in matriz:
        print(i) 
        
        
matriz(int(input("Número: ")))
        
        
        