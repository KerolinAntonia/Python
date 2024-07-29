def numeros(x,y):
    l = []
    for n in range (x,y+1):
       l.append(n)
    s =sum(l)
    return s

print(numeros((int(input("Número: "))),(int(input("Número: ")))))
