def gasolina(km):
    if km <= 8:
        return print("Gasta muito!")
    if km <= 15:
        return print ("Econômico!")
    if km >= 15:
        return print("Super econômico!")  
    
(gasolina((int(input("Número: ")))))      