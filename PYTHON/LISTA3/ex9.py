ns = []
x = 10

for n in range (1,x+1):
    n = int (input (f"Numero {n}: "))
    ns.append(n)
     
x = max (ns)
y = min (ns)

print ("Maior",x)
print ("Menor",y)