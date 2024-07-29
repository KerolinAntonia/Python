def soma_imposto (taxa_impostos, custos):
    total = custos + (taxa_impostos * custos)
    return total 

print(soma_imposto(0.02,666))
