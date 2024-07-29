matriz = [[1,2,11,13],[4,15,16,60],[7,8,19,200],[20,100,5,3]]

cont = 0

for i in matriz: 
    for j in i:
        if j > 10:
            cont += 1
            
print (cont)