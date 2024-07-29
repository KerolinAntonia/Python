class Triangulo:
    def __init__(self,ladoA,ladoB,ladoC):
        self.ladoA = ladoA
        self.ladoB = ladoB
        self.ladoC = ladoC
        
    def calcular_perimetro(self):
        self.resultado = self.ladoA + self.ladoB + self.ladoC
        print(f"Perímetro: {self.resultado}")
        
    def getMaior_lado(self):
        self.maior = max(self.ladoA,self.ladoB,self.ladoC)
        print(f"Maior: {self.maior}")

triangulo1 = Triangulo(2,5,8)
triangulo1.calcular_perimetro()
triangulo1.getMaior_lado()
        