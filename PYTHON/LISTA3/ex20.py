par = impar = 0
#Repetição
while True:
    num = int(input("PARA QUANDO DIGITA 0.\n NUMERO:"))
    if num == 0:
        break
    if num % 2 == 0:
        par += 1
    if num % 2 == 1:
        impar += 1
        
print (f"Quantidade par: {par} \n Quantidade impar: {impar}" )

