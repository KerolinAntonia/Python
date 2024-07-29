class Funcionario:
    def __init__(self,nome,matricula,salario):
        self.nome = nome 
        self.matricula = matricula
        self.salario = salario
        
    def Bater_ponto(self,bate):
        self.bate = bate
        if self.bate == 1:
            print("Batou ponto!")
        elif self.bate == 0:
            print("Não bateu")
        else:
            print("De novo!")

class Vendedor(Funcionario):
    def __init__(self, nome, matricula, salario,vendido ,comissão):
        self.vendido = vendido
        self.comissão = comissão
        super().__init__(nome, matricula, salario)
        
    def Bater_meta(self):
        r = self.vendido * self.comissão
        print(f"Valor da comissão: {r}")
        print(f"Salario: {self.salario}")
        
class Gerente(Funcionario):
    def __init__(self, nome, matricula, salario,senha):
        self.senha1 = senha
        super().__init__(nome, matricula, salario)
        
    def senha(self):
        print(f"Senha para acesso: {self.senha1}")
        
funcionario_vendedor = Vendedor("Jessica",55555,1200,90000,0.002)
funcionario_vendedor.Bater_ponto(1)
funcionario_vendedor.Bater_meta()

funcionario_gerente = Gerente("Rose",555557,9000,696969)
funcionario_gerente.Bater_ponto(0)
funcionario_gerente.senha()