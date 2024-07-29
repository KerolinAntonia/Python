n1 = int (input ("Numero: "))
c = 0

for i in range(n1,0,-1):
    print(i, end ="")
    c *= i
    if i ==1:
        print (end =" = ")
    else:
        print(end =" * ")

print (c)
    