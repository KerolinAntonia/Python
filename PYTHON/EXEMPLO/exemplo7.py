lista = []

empresa = {'nome':'','unidade':'','fone':'','email':'','cidade':'','UF':''}

cont = 0

while cont < 2:
    nome = input("Digite o nome da empresa: ")
    unid = input("Digite a unidade da empresa: ")
    fone = input("Digite o fone da empresa: ")
    email = input("Digite o email da empresa: ")
    cidade = input("Digite o cidade da empresa: ")
    estado = input("Digite o estado da empresa: ")
    
    empresa['nome'] = nome
    empresa['unidade'] = unid
    empresa['fone'] = fone
    empresa['email'] = email
    empresa['cidade'] = cidade
    empresa['UF'] = estado
    
    lista.append(empresa)
    
    cont = cont + 1
    

print (lista)
 
