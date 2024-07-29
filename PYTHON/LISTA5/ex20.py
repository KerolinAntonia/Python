
while True:
    
    def soma_matriz(x):
        matriz = ([10,20,30,40],
                [45,26,33,78],
                [19,18,17,16],
                [13,14,15,16])
        
        if x == 0:
            l = []
            for i in matriz[0]:
                l.append(i)
            z = sum(l)
            print(l)
            return z
        
        if x == 1:
                l = []
                for i in matriz[1]:
                    l.append(i)
                z = sum(l)
                print(l)
                return z
        if x == 2:
                l = []
                for i in matriz[2]:
                    l.append(i)
                z = sum(l)
                print(l)
                return z
        if x == 3:
                l = []
                for i in matriz[3]:
                    l.append(i)
                z = sum(l)
                print(l)
                return z
        else:
            print("De novo!!")
    
    print(soma_matriz(int(input("Número: "))))
    