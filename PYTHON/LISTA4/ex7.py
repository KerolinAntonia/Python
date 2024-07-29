def salario(horas):
    salario = 10
    if horas <= 40:
        valor = horas * salario
    else:
        valor = (horas * salario) + (salario/2) * (horas - 40)
    return valor

print(salario(50))
    
        
        
        
