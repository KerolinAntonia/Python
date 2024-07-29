class Circulo:
    def __init__(self,raio,pi):
        self.raio = raio
        self.pi = pi
        
    def getRaio(self):
        print(f"Raio: {self.raio}")
        
    def calcular_area(self):
        self.resultado = self.pi * (self.raio**2)
        print(f"Area do circulo: {self.resultado}")
        
    def calcular_circuferencia(self):
        self.resultado = (self.pi**2) * self.raio
        print(f"Valor da circuferencia: {self.resultado}")
        
circulo1 = Circulo(5,3.14)
circulo1.getRaio()
circulo1.calcular_area()
circulo1.calcular_circuferencia()

