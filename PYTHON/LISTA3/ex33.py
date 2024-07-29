l = [10,1,90,60,2,3,5,7,2,5,]

x = int(input("VALOR PARA VERIFICAR: "))
if x in (l):
    print ("ERRO!")

else: 
    l.append (x)
    print (l)
   