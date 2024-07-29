l = []
t = 0
p = []
print("PARA QUANDO DIGITA 0")

while True:
    n = int(input("NUMERO: "))
    if n == 0:
        break
    if n > 0:
        l.append(n)
        t += 1
        if n % 2 == 0:
            p.append(n)

print(l)
print("SOMA DOS NUMEROS:",sum(l))
print(f"QUANTIDADE DE NUMEROS: {t}")
print("MEDIA DOS NUMEROS:",((sum(l))/2))
print("MAIOR DOS NUMEROS:",max(l))
print("MENOR DOS NUMEROS:",min(l))
print("NUMEROS PARES:", p)
print("MEDIA DOS NUMEROS PARES:",((sum(p))/2))