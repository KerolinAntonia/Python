class Imóvel:
    def __init__(self,incricao,aluguel,iptu):
        self.incriçãoMunicipal = incricao
        self.valoraluguel = aluguel
        self.iptu = iptu
        
    def Obter_parcela_Iptu(self):
        self.parcela = int(input("Quantas parcelas: "))
        r = self.iptu / self.parcela
        print(f"Valor de cada parcela: {r}") 
    
    def SetValorAluguel(self):
        print(f"Paga isso {self.valoraluguel}")   
        
class Casa(Imóvel):
    def __init__(self, incricao, aluguel, iptu):
        super().__init__(incricao, aluguel, iptu) 
        
    def Tem_na_casa(self):
        print(f"Tem Área de lazer, 2 quartos, 4 banheiros , Churrasqueira, louvor")
        
class Condominio(Imóvel):
    def __init__(self, incricao, aluguel, iptu):
        super().__init__(incricao, aluguel, iptu)
        
    def Tem_no_condomio(self):
        print("Tem elevador,piscina,segurança")
        
class Apartamento(Imóvel):
    def __init__(self, incricao, aluguel, iptu):
        super().__init__(incricao, aluguel, iptu)
        
    def Tem_no_apartamento(self):
        print("Tem 1 quarto, 1 banheiro, sala junto com a cozinha")
        
class Terreno(Imóvel):
    def __init__(self, incricao, aluguel, iptu):
        super().__init__(incricao, aluguel, iptu)
        
    def Terreno(self):
        print("Tem 23 de comprimento e 14 de largura ")
        
class Chácara(Imóvel):
    def __init__(self, incricao, aluguel, iptu):
        super().__init__(incricao, aluguel, iptu)
        
    def Tem_na_chácara(self):
        print("Tem piscina, churrasqueira,6 quartos,10 banheiros, área de lazer e com 40 metros")
        
        
casa_imovel = Casa(600972,600,500)
casa_imovel.Obter_parcela_Iptu()
casa_imovel.SetValorAluguel()
casa_imovel.Tem_na_casa()