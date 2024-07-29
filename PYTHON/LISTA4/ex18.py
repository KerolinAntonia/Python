def desconto(dia,**kwags):
    couvert = kwags['couvert']
    if dia == "terça-feira":
        conta = kwags['valor'] - (kwags['valor'] * 0.10)
        conta = conta + (conta * 0.10) + couvert
        return conta
    elif dia == "quarta-feira":
        conta = kwags['valor'] - (kwags['valor'] * 0.15)
        conta = conta + (conta * 0.10) + couvert
        return conta
    elif dia == "quinta-feira":
        conta = kwags['valor'] - (kwags['valor'] * 0.20)
        conta = conta + (conta * 0.10) + couvert
        return conta
    else:
        conta = kwags['valor']
        conta = conta + (conta * 0.10) + couvert
        return conta
    
x = desconto('segunda-feira',valor=150,couvert = 15)

print(x)
