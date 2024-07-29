matriz = ([],
          [],
          [],
          [],
          [])

cont = 0

for i in matriz:
    while len(i) < 4:
        i.append(0)
    i.insert (cont,1)
    cont += 1
    
for i in matriz:
    print(i)