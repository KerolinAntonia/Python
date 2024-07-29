def financiamento (valor_do_carro, valor_entrada,juros,parcelas):
    valor_parcela = (valor_do_carro - valor_entrada) /parcelas
    parcela_juro = (valor_parcela * juros) + valor_parcela
    
    valor_total_pago = valor_entrada + (parcela_juro * parcelas)
    juros_pagos = ((parcela_juro * parcelas) - (valor_parcela * parcelas))
    
    return print ("Valor Total:", valor_total_pago,
                  "Valor da Parcela:", valor_parcela,
                  "valor da parcela com juros:", parcela_juro,
                  "Valor de juros",juros_pagos)
    
print(financiamento(60000,25000,0.05,24))