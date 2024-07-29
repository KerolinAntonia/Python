r1 = 0
r2 = 0

while True:
    r1 = int(input("Digite o valor do resistor 1: "))
    r2 = int(input("Digite o valor do resistor2: "))
    
    if r1 == 0 or r2 == 0:
        print ("Resultado igual a 0")
        break
    else:
        r = (r1 * r2) / (r1 + r2)
        print (r)
       
    