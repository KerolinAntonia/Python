try:
    conta = 200
    saque = int(input("SAQUE: "))
    r = conta - saque
    if saque < conta:
        print("SALDO:", r)
except:
    print("Você não tem tanto!")
    