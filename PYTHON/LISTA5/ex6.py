def reverse(x):
    b = str(x) 
    a = b[::- 1]
    c = int(a)
    return c
        
print(reverse((int(input("Número: ")))))
        