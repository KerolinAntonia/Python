n = 1
d = 1
l = []

for i in range(1,51):
    f = n/d
    d += 1
    n += 2
    l.append (f)

print (sum(l))
