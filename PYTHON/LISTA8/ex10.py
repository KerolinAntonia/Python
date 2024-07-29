class Transporte:
    def __init__(self,capacidade):
        self.capacidade = capacidade
        
class Aquatico(Transporte):
    def __init__(self, capacidade):
        super().__init__(capacidade)
        
class  Terrestre(Transporte):
    def __init__(self, capacidade,numeros_de_rodas):
        self.numeros_de_rodas = numeros_de_rodas
        super().__init__(capacidade)
        
class Aéreo(Transporte):
    def __init__(self, capacidade):
        super().__init__(capacidade)
        
class Barco(Aquatico):
    def __init__(self, capacidade):
        super().__init__(capacidade)
        
class Návio(Aquatico):
    def __init__(self, capacidade):
        super().__init__(capacidade)
        
class Avião(Aéreo):
    def __init__(self, capacidade):
        super().__init__(capacidade)

class Helicóptero(Aéreo):
    def __init__(self, capacidade):
        super().__init__(capacidade)
        
class Carro(Terrestre):
    def __init__(self, capacidade, numeros_de_rodas,cor,portas,placa):
        self.cor = cor
        self.portas = portas
        self.placa = placa
        super().__init__(capacidade, numeros_de_rodas)
        
    def modelo(self):
        print(f"{self.capacidade},{self.numeros_de_rodas},{self.cor},{self.portas},{self.placa}")
        
class Ônibus(Terrestre):
    def __init__(self, capacidade, numeros_de_rodas,cor,portas,placa):
        self.cor = cor
        self.portas = portas
        self.placa = placa
        super().__init__(capacidade, numeros_de_rodas)
        
    def modelo(self):
        print(f"{self.capacidade},{self.numeros_de_rodas},{self.cor},{self.portas},{self.placa}")
        
class Caminhão(Terrestre):
    def __init__(self, capacidade, numeros_de_rodas,cor,portas,placa):
        self.cor = cor
        self.portas = portas
        self.placa = placa
        super().__init__(capacidade, numeros_de_rodas)
        
    def modelo(self):
        print(f"{self.capacidade},{self.numeros_de_rodas},{self.cor},{self.portas},{self.placa}")
        
