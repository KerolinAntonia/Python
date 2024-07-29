def imprimir_numeros_crescentes(N):
    if N < 0 or  N %2 != 0:
        print ("POR FAVOR, INSIRA UM NUMERO POSITIVO")
    else:
        for i in range(0,N+1,2):
            print(i)

numero = int(input("DIGTE UM NUMERO INTEIRO:"))
imprimir_numeros_crescentes (numero)