def calcular_tempo(tempo):
     hora_paga = 9
     t = tempo / 60
     if t < 0.25:
         return print("Nenhum valor a ser pago")
     elif t == 1:
         return print ("Valor a ser pago:",hora_paga)
     elif t > 1:
        a = t - 1
        v = hora_paga + (a * 1.50)
        pis = v * 0.33
        cofins = v * 0.20
        icms = v * 0.17
        impostos = pis + cofins + icms
        vl = v + pis + cofins + icms
        return print("Valor a ser pago:", vl,
                     "Tempo:", t ,
                     "Pis R$", pis,
                     "Cofins R$", cofins,
                     "ICMS", icms,
                     "Impostos R$", impostos)
         
print (calcular_tempo(120))
