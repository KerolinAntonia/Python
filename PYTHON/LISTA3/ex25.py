ns = []
while True:
    n = int (input (f"IDADE: "))
    if n < 1 :
        break
    else:
        ns.append(n)

print ("MEDIA:",sum(ns)/ len (ns))