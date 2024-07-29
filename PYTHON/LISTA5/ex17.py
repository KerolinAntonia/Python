
import random

def sort(x,y):
    l = []
    l1 = []
    for n in range (x,y+1):
        l.append(n)
    print(l)
    for i in l:
        n = random.randint(x,y)
        l1.append(n)
    print(l1)
    l2 = []
    for i in l1:
        if i % 2 == 0:
            l2.append(i)
            s =sum(l2)
    print(l2)
    return s

print(sort(int(input("inicio: ")),int(input("Fim: "))))
