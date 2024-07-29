n1 = int(input("Digite um número de inicio: "))
n2 = int(input("Digite um número final: "))
p = [0]
c = n1

while max(p) <= n2:
    div = []
    for i in range(1,  + 1):
        if c % i == 0:
            div.append(i)
    if len(div) == 2:
        p.append(c)
    c += 1
    
p.pop(0)
p.pop(-1)

print(p)