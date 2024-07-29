def base(n):
    for i in range(1,n+1):
        x = 2 * i - 1
        y = n - i
        z = ' ' * y + '*' * x
        print (z)

(base(int(input("Número: "))))