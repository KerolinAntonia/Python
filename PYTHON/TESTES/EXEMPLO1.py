class Gato:
    def __init__(self,nome,cor,idade):
        self.nome = nome
        self.cor = cor
        self.idade = idade
        
    def hello(self):
        print (f"{self.nome}: MIAU")
        
gato1 = Gato("Gato de botas","Laranja",5)
gato2 = Gato("Felix","Preto e Branco",10)

gato2.hello()
gato1.nome = "GATO"
gato1.hello()

print(gato2.cor)
gato2.cor = "Amarelo"
print(gato2.cor)

print("oi")