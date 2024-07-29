class Pessoa:
    def __init__(self,nome,idade,endereço):
        self.nome = nome
        self.idade = idade
        self.endereço = endereço
        
    def getMostra_nome(self):
        print (f"Nome: {self.nome}")
    
    def setAltera_idade(self, idade):
        self.idade = idade
        print (f"Idade: {self.idade}")
        
    def getendereço(self):
        print (f"Endereço: {self.endereço}")
        
p1 = Pessoa("Joui",21,"Escola Nostradamus")
p1.getMostra_nome()
p1.setAltera_idade(16)
p1.getendereço()
                