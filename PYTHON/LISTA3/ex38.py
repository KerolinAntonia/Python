n = int(input("Digite um número: "))
p = []
c = 1

while len(p) <= n:
    div = []
    for i in range(1, c + 1):
        if c % i == 0:
            div.append(i)
    if len(div) == 2:
        p.append(c)
    c += 1

print(sum(p))
        