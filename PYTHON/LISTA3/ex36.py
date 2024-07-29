i = j = 0
medias = []
while i < 10:
    print(f"*** Aluno {i+1} *** ")
    n1 = int(input("N1: "))
    n2 = int(input("N2: "))
    n3 = int(input("N3: "))
    n4 = int(input("N4: "))

    med = (n1 + n2 + n3 + n4) / 4
    medias.append(med)
    i = i + 1

cont = 0
while j < len(medias):
    if medias[j] >= 7:
        cont = cont + 1
        j = j + 1
    else:
        j = j + 1
        
print("TOTAL DE NOTAS ACIMA DA MEDIA: ",cont)