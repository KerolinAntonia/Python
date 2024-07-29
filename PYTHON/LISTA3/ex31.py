x = 4000  #2019
t = int(input("TEMPO DE EMPRESA:"))
r = 0.015

for i in range(1,t+1):
    r *= 2
    k = x * r
    d = k + x 
    print (d)