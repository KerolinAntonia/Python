n = 1
l = []

for i in range(1,100):
    while n <= 100:
         v = n**2
         l.append(v)
         n += 1
        
print(l)
print("VALOR TOTAL: ", sum(l))
