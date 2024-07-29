class Carro:
    def __init__(self,marca,cor,modelo,placa,ano):
        self.marca = marca
        self.cor = cor 
        self.modelo = modelo
        self.placa = placa
        self.ano = ano 
        
    def mostrar_carro(self):
        return print (f"Marca: {self.marca}, Cor: {self.cor}, Modelo: {self.modelo}, Placa: {self.placa}, Ano: {self.ano}")
    
Carro1 = Carro("Toyota","Preta","Corolla","KEL-2024","2021")
Carro2 = Carro("Chevrolet","Prata","Monsa","EKL-55555","1989")

Carro1.mostrar_carro()
Carro1.modelo = "HILUX"
Carro1.mostrar_carro()
Carro2.mostrar_carro()
Carro2.modelo = "Onix"
Carro2.mostrar_carro()


