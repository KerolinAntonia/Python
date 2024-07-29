A = ([1,13,3],
     [4,45,67],
     [7,80,9])

B = ([100,8,7],
     [6,5,4],
     [3,25,10])

C = []

for i in  range (len(A)):
    l = []
    for i1 in range (len(B)):
        d = A[i][i1] + B[i][i1]
        l.append(d)
    C.append(l)
    
for i in C:
    print(i)  
