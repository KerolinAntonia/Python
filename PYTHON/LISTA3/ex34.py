ns = []
nsp = []
nsi = []
x = 20

for n in range (1,x+1):
    n = int(input (f"NUMERO {n}: "))
    ns.append(n)
    if n % 2 == 0:
        nsp.append(n)
    if n % 2 != 0:
        nsi.append (n)
    
print (ns)
print (nsp)  
print (nsi)                   