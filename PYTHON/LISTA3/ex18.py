ns = []
x = int (input ("Digite quantas numeros vão ser calculadas: "))

for n in range (1,x+1):
    n = float (input (f"NUMERO {n}º: "))
    ns.append (n)
     
print (max(ns))