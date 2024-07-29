class Aluno_academia:
    def __init__(self,nome,idade,peso,altura,mensalidade=120):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        self.mensalidade = mensalidade
        
    def calacular_imc(self):
        self.imc = self.peso * (self.altura**2)
        print(f"O aluno {self.nome} com imc: {self.imc}")
        
    def valor_desconto(self):
        if self.idade < 18:
            self.valor_final = self.mensalidade - (self.mensalidade * 0.2)
            print (f"Valor com deconto: {self.valor_final}")
        else:
            print(f"Paga mesmo: {self.mensalidade}")
            
aluno1 = Aluno_academia("Marcos",16,54,1.80)
aluno1.calacular_imc()
aluno1.valor_desconto()