class Ingresso:
    def __init__(self,preco,setor):
        self.preco = preco
        self.setor = setor
        
    def alterar_preco(self):
        print(f"Atual: {self.preco}")
        self.preco_atual = input("Preco: ")
        print(f"Preco Novo: {self.preco_atual}")
        
    def mostrar_setor(self):
        print(f"Setor:{self.setor}")
        
class IngressoVip(Ingresso):
    def __init__(self, preco, setor):
        super().__init__(preco, setor)
        
    def pagar_bebida(self,valor):
        self.valor = valor
        self.open_bar = True
        self.open_food = False
        self.camorote = True
        print(f"Pagando o valor do Todynho de {self.valor} ")
        
    def acessar_camorote(self,camarote):
        self.camorote = camarote
        print(f"Camarote: {self.camorote}")
        
ingressovip = IngressoVip(20,"A")
ingressovip.alterar_preco()
ingressovip.mostrar_setor()
ingressovip.pagar_bebida("12")
ingressovip.acessar_camorote("A")
        
