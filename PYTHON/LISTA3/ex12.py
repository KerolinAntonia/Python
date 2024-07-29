def imprimir_numeros_decrescentes(N):
    if N < 0:
        print ("POR FAVOR, INSIRA UM NUMERO POSITIVO")
    else:
        for i in range(N + 1):
            print(i)

numero = int(input("DIGTE UM NUMERO INTEIRO:"))
imprimir_numeros_decrescentes (numero)