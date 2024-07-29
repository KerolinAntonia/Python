class Carro:
    def __init__(self, modelo, cor, marca, val, ano, consumo ,nivel=5,):
        self.modelo = modelo
        self.cor = cor
        self.marca = marca
        self.valor = val
        self.ano = ano
        self.nivel = nivel
        self.consumo = consumo
        self.onoff = False
    def ligar(self):
        self.onoff = True
   
    def abastecer(self,add):
        self.nivel += add
   
    def andar(self,km):
        self.km = km
        if self.onoff == True:
            print(f"O carro andou {km} Km")
        else:
            print("O carro está desligado")
   
    def verificar_nivel(self,cgasto):
        ct = cgasto / self.km
    def calcular_imposto(self):
        self.ipva = self.valor*0.025
        