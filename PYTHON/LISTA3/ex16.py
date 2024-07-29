def imprimir_numeros_crescentes(N):
    if N < 0 or N %2 == 0.5:
        print ("POR FAVOR, INSIRA UM NUMERO IMPAR")
    else:
        for i in range(1,N+1,2):
            print(i)

numero = int(input("DIGITE UM NÚMERO IMPAR: "))
imprimir_numeros_crescentes (numero)