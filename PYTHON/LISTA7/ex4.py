class Conta:
    def __init__(self,nome,cpf,numero,saldo):
        self.nome = nome 
        self.cpf = cpf
        self.numero = numero
        self.saldo = saldo
        
    def depositar(self):
        self.saldo1 = self.numero + self.saldo
        print(f"Saldo Atual: {self.saldo1}")
        
    def sacar(self):
        if self.saldo < self.numero:
            self.saldo1 = self.numero - self.saldo
            print(f"Saldo Atual: {self.saldo1}")
        else:
            print (f"Valor menor!! \n Saldo Atual: {self.saldo}")
    
    def getImprimir_saldo(self):
        print(f"Saldo Atual: {self.saldo}")
        
conta1 = Conta("João Aparecido", 6666666666,50,100)
conta1.depositar()
conta1.getImprimir_saldo()
conta1.sacar()