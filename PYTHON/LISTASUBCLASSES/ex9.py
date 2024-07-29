class Compra:
    def __init__(self,numero,produto,valor):
        self.numero = numero
        self.produto = produto
        self.valor = valor
        
    def calcular_valor_total(self):
        self.valor = self.valor + (self.valor * 0.17) + (self.valor * 0.05)
        print(f"Valor: {self.valor}") 
        
class Avista(Compra):
    def __init__(self, numero, produto, valor=0):
        super().__init__(numero, produto, valor)
        
    def desconto (self):
        self.valor = self.valor - (self.valor * 0.20) 
        print(f"Valor a vista  é {self.valor} do {self.produto}")  
        
class Parcelado(Compra):
    def __init__(self, numero, produto, valor=0):
        super().__init__(numero, produto, valor)
        
    def pobre1 (self):
        self.parcela = int(input("Quantas parcelas: "))
        r = self.valor / (self.parcela + 0.5)
        print(f"Valor de cada parcela: {r}") 
        
        
compra1 = Avista(5555,"Fogão",600)
compra1.calcular_valor_total()
compra1.desconto()

compra2 = Parcelado(5555,"Tv Cara", 1999)
compra2.calcular_valor_total()
compra2.pobre1()

