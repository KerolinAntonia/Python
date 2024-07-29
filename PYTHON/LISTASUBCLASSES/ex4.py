class Passagem:
    def __init__(self,preco,assento):
        self.preco = preco
        self.assento = assento
        
    def alterar_preco(self):
        print(f"Atual: {self.preco}")
        self.preco_atual = input("Preco: ")
        print(f"Preco Novo: {self.preco_atual}")
        
    def escolher_assento(self):
        print("Escolha entre em 1 á 40")
        self.escolha = input("Qual: ")
        print(f"Escolhido: {self.escolha}")
        
class PassagemBus(Passagem):
    def __init__(self, preco, assento,placa,leito):
        self.placa = placa
        self.leito = leito
        super().__init__(preco, assento)
        
    def abastacer(self):
        print("Abastace")
        
class PassagemAviao(Passagem):
    def __init__(self, preco, assento,dese,che):
        self.dese = dese
        self.che = che
        super().__init__(preco, assento)
        
    def decolar(self):
        print("Voou")
   
        
passagem_bus = PassagemBus(60,5,"555QWA","A2")
passagem_bus.alterar_preco()
passagem_bus.escolher_assento()
passagem_bus.abastacer()

passagem_Avião = PassagemAviao(1222,"90A","B5","4LLLLLL")
passagem_Avião.decolar()