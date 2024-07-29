def kwh (potencia, tempo, hora_kwh):
    consumo = potencia * tempo
    print ("Consumo foi:" ,consumo)
    conta = hora_kwh * consumo
    return print("Irar paga:",conta, "reais")

(kwh(5,8,25)) 
    