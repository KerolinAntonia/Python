def base(n):
    for i in range(1,n+1):
        print("*"*i)
    for i in range(n,1,-1):
        print("*"*i)


base(int(input("Número: ")))