nss = []
ns = 1000

for n in range (1,ns):
    if n % 3 == 0:
        nss.append(n)
    elif n % 5 == 0:
            nss.append(n)
            print(nss)
            
print("SOMA:", sum(nss))