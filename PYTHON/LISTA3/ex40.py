n1 = int(input("Digite um número de inicio: "))
n2 = int(input("Digite um número final: "))

soma = 0
if n1 > n2:
    print("Intervalor Inválido! ")
else:
    while n1 <= n2:
        if n1 % 2 != 0:
            soma += n1
            n1 += 1
        else:
            n1 += 1

print(soma)
          
