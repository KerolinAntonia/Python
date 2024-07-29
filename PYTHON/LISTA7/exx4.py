class Funcionario:
    def __init__(self, nome,sobrenome,horas_trabalhadas,valor_hora,horas_extras):
        self.nome = nome 
        self.sobrenome = sobrenome
        self.horas_trabalhadas = horas_trabalhadas
        self.valor_hora = valor_hora
        self.horas_extras = horas_extras
        
    def getNomeCompleto(self):
        print(f"Nome completo do funcionario: {self.nome} {self.sobrenome}")  
        
    def calcular_salario (self):
        self.valor_do_salario = self.horas_trabalhadas * self.valor_hora
        print(f"Salario: {self.valor_do_salario}")
    
    def imprementar_horas(self):
        self.valor_do_salario = (self.horas_trabalhadas * self.valor_hora) + (self.horas_extras * self.valor_hora)
        self.extras = self.horas_extras * self.valor_hora
        print(f"Valor das horas extras: {self.extras}")
        print(f"Salario com horas extras: {self.valor_do_salario}")
        
Funcionario1 = Funcionario("João Paulo","dos Santos",40,50,5)
Funcionario1.getNomeCompleto()
Funcionario1.calcular_salario()
Funcionario1.imprementar_horas()