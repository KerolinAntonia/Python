def numeros (*args: float):
    r = sum(args)/ len(args)
    return r

print(numeros(2,4,6,2,4,8,9))