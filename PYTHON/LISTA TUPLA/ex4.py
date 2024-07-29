tupla = (3,6,2,9,1,7,5)

l =[]
for i in tupla:
    if i % 2 == 0:
        print ("NUMERO PAR:",i)
        l.append(i)
    
print("SOMA:",sum(l))