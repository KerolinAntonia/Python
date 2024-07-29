ns = []
while True:
    n = int (input (f"NOTA: "))
    if n < 1 or n > 10:
        print("ERRO!")
        break
    else:
        ns.append(n)

print ("Media:",sum(ns)/ len (ns))