class Nf:
    def __init__(self,numero,tipo,serie,cnpj,razao,data,valor,icms,frete,ipi):
        self.numero1 = numero
        self.tipo = tipo
        self.serie = serie
        self.cnpj = cnpj
        self.razao = razao
        self.data1 = data
        self.valor_produto = valor
        self.icms = icms
        self.frete = frete
        self.ipi = ipi
        
    def numero(self):
        print(f"Numero da nota: {self.numero1}")
        
    def data(self):
        print(f"Data da emissão: {self.data1}")
        
    def setRazao(self):
        print(f"Razão atual: {self.razao}")
        self.atual = input("Alterar:")
        print(f"Razão alterada! Atual: {self.atual}")
        
    def cacular_valor(self):
        self.valor_total = self.valor_produto + self.frete + self.icms
        print(f"VAlor total: {self.valor_total}")
        
nf1 = Nf(55555,"entrada",5555,555555,8888,"02/02/2002",50,0.20,5,5,)
nf1.numero()
nf1.data()
nf1.setRazao()
nf1.cacular_valor()     