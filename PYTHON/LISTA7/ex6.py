class Agenda:
    def __init__(self,dia,mes,ano,anotação):
        self.dia = dia
        self.mes = mes
        self.ano = ano
        self.anotação = anotação
        
    def validar_data(self):
        print (f"Data: {self.dia}/{self.mes}/{self.ano}")
        
    def Mostra_anotação(self):
        print(f"Anotação do dia: {self.anotação}")
        
    def anotar_tarefa(self):
        self.anotação = input("Qual a anotação:")
        print(f"Anotado: {self.anotação}")
        
agenda1 = Agenda(2,5,2024,"Comer pudim")
agenda1.validar_data()
agenda1.Mostra_anotação()
agenda1.anotar_tarefa()
        
        
        
        
        
        