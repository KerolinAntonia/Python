def pesca (peso, quantidade_peixe):
    valor = peso * quantidade_peixe
    multa = 4
    if valor < 50:
       valor_da_multa = multa * ( valor - 50)
       return print("Valor da Multa", valor_da_multa)
    elif valor == 50:
        return print ("Esta no limite!!!")
    elif valor < 50:
        return print ("Esta abaixo do limite", valor)
    
print(pesca(10,15))    
    

        
    