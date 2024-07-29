def potencia(x,z):
    r = 1
    for _ in range(z):
        r*=x
    return r
    
    
print (potencia((int(input("Número: "))),(int(input("Número: ")))))