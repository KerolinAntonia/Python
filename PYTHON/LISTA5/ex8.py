def nota(n1,n2,n3,letra):
    if letra == "a":
        final = (n1+n2+n3)/3
        return final
    if letra == "p":
        final = (n1*0.5)+(n2*0.3)+(n3*0.2)
        return final
    
letra = input("Digite a letra: ")
print(nota((int(input("Nota 1: "))),(int(input("Nota 2: "))),(int(input("Nota 3: "))),letra))