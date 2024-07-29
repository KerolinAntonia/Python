nss = []

ns = int (input("NUMERO:"))
for n in range (1,ns):
    if ns % n == 0:
        nss.append(ns)
        
print("SOMA:", sum(nss))
        