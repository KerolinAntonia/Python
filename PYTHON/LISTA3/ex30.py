l = []
x = 1

while True:
    for n in range (1,x+1):
        n = int (input (f"Numero: "))
        l.append(n)
    if n == 1:
        break

print (max(l))
print (min(l))