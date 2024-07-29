matriz = [[1,2,3],
          [4,5,6],
          [7,8,9]]

matriz2 = []
l1 = []
l2 = []
l3 = []

for i in range(len(matriz)): #
    for j in range(len(matriz)):
        if j == 0:
            l1.append(matriz[i][j])
        elif j == 1:
            l2.append(matriz[i][j]) 
        elif j == 2:
            l3.append(matriz[i][j])
            
matriz2.append(l1)
matriz2.append(l2)
matriz2.append(l3)

for i in matriz2:
    print(i)