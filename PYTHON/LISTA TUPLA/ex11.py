matriz = ([1,2,11,13],
          [4,15,16,60],
          [7,8,19,200],
          [20,100,5,3])
maior = 0
col = 0
lin = 0

for i in matriz:
    for j in i:
      if j > maior:
        maior = j 
        col = i.index(j)
        lin = matriz.index(i)
        
for i in matriz:
    print(i)
    
print(maior)
print ("LINHA:", lin , "COLUNA:",col)
