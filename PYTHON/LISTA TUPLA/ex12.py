matriz = ([1,120,-3],
          [4,5,250],
          [7,0,9])
maior = 0
col = 0
lin = 0
menor = 0
col1 = 0
lin1 = 0

for i in matriz:
    for j in i:
      if j > maior:
        maior = j 
        col = i.index(j)
        lin = matriz.index(i)
        
for i in matriz:
    for j in i:
      if j < menor:
        menor = j 
        col1 = i.index(j)
        lin1= matriz.index(i)
        
for i in matriz:
    print(i)        

print("MAIOR:",maior)
print ("LINHA:", lin , "COLUNA:",col)
print("MENOR:",menor)
print ("LINHA:", lin , "COLUNA:",col)