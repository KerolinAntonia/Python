def base(n):
    x = ""
    for i in range(1,n+1):
        x += "!"
        print(x)
    return x

print(base(int(input("Número: "))))