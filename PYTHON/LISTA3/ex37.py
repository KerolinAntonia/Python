while True:
    x = 1

    for n in range (1,x+1):
        n = int(input ("NUMERO: "))
        div = []
        for i in range(1, 1 + n):
            if n % i == 0:
                div.append(i) 
        if len(div) == 2:
            print(f"{n} é um número primo")  
        else:
            print(f"{n} não é um número primo")