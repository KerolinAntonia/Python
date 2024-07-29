def imprimir_numeros_decrescentes(N):
    if N < 0 or N % 2 != 0:
        print ("POR FAVOR, INSIRA UM NUMERO PAR")
    else:
        for i in range(N,-1,-2):
            print(i)

numero = int(input("DIGITE UM NÚMERO PAR:"))
imprimir_numeros_decrescentes (numero)