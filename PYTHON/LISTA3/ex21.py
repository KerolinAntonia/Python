ns = []
par = impar = 0

for n in range (1,2):
    n1 = int (input ("Numero: "))
    n2 = int (input ("Numero: "))
    
    if n1 % 2 == 0:
        par += 1
        ns.append(n1)
        if n2 % 2 == 0:
            par += 1
            ns.append(n2)
        
        print ("PAR:" ,sum(ns))
        print (f"Quantidade: {par}")
        
    else:
        if n1 % 2 == 1:
            impar += 1
            if n2 % 2 == 1:
                impar += 1
                n3 = n1*n2
                print ("IMPAR:", n3)
                print (f"Quantidade: {impar}")