print ("Bem-Vindo")

while True:
    print (" (1)Adição \n (2)Substração \n (3)Multiplicação \n (4)Divisão \n (5)Sair\n")
    f =(input ("Selecione oque deseja fazer:"))
    
    #Adição
    if f == "1" :
        n1 = int(input("Numero 1: "))
        n2 = int(input("Numero 2: "))
        n3 = n1 + n2
        print (n3)
        
    #Substração
    if f == "2" :
       n1 = int(input("Numero 1: "))
       n2 = int(input("Numero 2: "))
       n3 = n1 - n2
       print (n3)
        
    #Multiplicação
    if f == "3":
        n1 = int(input("Numero 1: "))
        n2 = int(input("Numero 2: "))
        n3 = n1 * n2
        print (n3)
        
    #Divisão
    if f == "4":
        n1 = int(input("Numero 1: "))
        n2 = int(input("Numero 2: "))
        n3 = n1 / n2
        print (n3)
        
    #Sair
    if f == "5":
        print ("Fim do Programa")
        break
    else:
        print("Voltando")