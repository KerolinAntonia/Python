import random
 
s = random.randint(1, 100)
t = 0
 
print("Adivinhe o numero entre 1 a 100! ")
while True:
    c = int(input("Palpite: "))
    t += 1
 
    if c < s :
        print("Maior")
    elif c > s :
        print("Menor")
    else:
        print(f"Parabéns! você acertou o número {s} em {t} tentativa(s)")
        break