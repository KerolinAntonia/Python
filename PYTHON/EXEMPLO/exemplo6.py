pessoas = { 'Nome': 'Kerolin Antônia', 'Idade': '17 anos', 'Cidade':'Campo Grande', 'Estado': 'Mato Grosso do Sul'}

print (pessoas.keys())
print(pessoas['Nome'])
print(pessoas['Idade'])
print(pessoas['Cidade'])
print(pessoas['Estado'])

for i in pessoas.keys():
    print(i)
    print(pessoas[i])
    
print(pessoas['Cidade'])
pessoas['Cidade'] = 'Paris'
pessoas['Idade'] = '17 anos e 4 meses'
pessoas['Estado'] = 'Não sei'
 
print(pessoas['Nome'])
print(pessoas['Idade'])
print(pessoas['Cidade'])
print(pessoas['Estado'])