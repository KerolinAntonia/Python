def desenhaLinha(x):
    c = ""
    for n in range(1,x+1):
        c += "="
    return c
    
print(desenhaLinha(9999))