i = 0
soma = 0 

while i < 10:
    try:
        num = int(input("NUMERO: "))
        soma += num
        i = i + 1
    except:
        print("Errado! De novo!")
        
print("Total:", num)
        