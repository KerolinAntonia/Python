class Brinquedo:
    def __init__(self,nome,cor,tamanho,preço):
        self.nome = nome
        self.cor = cor 
        self.tamanho = tamanho
        self.preço = preço
        
    def brincar(self):
        print(f"Brincando com {self.nome}")
        
class Brinquedo1(Brinquedo):
    def __init__(self, nome, cor, tamanho, preço,habilidade):
        self.habilidade = habilidade
        super().__init__(nome, cor, tamanho, preço)
        
    def habilidades(self):
        print(f"O {self.nome} {self.habilidade}")
        
class Brinquedo2(Brinquedo):
    def __init__(self, nome, cor, tamanho, preço,habilidade):
        self.habilidade = habilidade
        super().__init__(nome, cor, tamanho, preço)
        
    def habilidades(self):
        print(f"O {self.nome} {self.habilidade}")
        
class Brinquedo3(Brinquedo):
    def __init__(self, nome, cor, tamanho, preço,habilidade):
        self.habilidade = habilidade
        super().__init__(nome, cor, tamanho, preço)
        
    def habilidades(self):
        print(f"O {self.nome} {self.habilidade}")
        
class Brinquedo4(Brinquedo):
    def __init__(self, nome, cor, tamanho, preço,habilidade):
        self.habilidade = habilidade
        super().__init__(nome, cor, tamanho, preço)
        
    def habilidades(self):
        print(f"O {self.nome} {self.habilidade}")
        
class Brinquedo5(Brinquedo):
    def __init__(self, nome, cor, tamanho, preço,habilidade):
        self.habilidade = habilidade
        super().__init__(nome, cor, tamanho, preço)
        
    def habilidades(self):
        print(f"O {self.nome} {self.habilidade}")

class Brinquedo6(Brinquedo):
    def __init__(self, nome, cor, tamanho, preço,habilidade):
        self.habilidade = habilidade
        super().__init__(nome, cor, tamanho, preço)
        
    def habilidades(self):
        print(f"O {self.nome} {self.habilidade}")
        
class Brinquedo7(Brinquedo):
    def __init__(self, nome, cor, tamanho, preço,habilidade):
        self.habilidade = habilidade
        super().__init__(nome, cor, tamanho, preço)
        
    def habilidades(self):
        print(f"O {self.nome} {self.habilidade}")
        
class Brinquedo8(Brinquedo):
    def __init__(self, nome, cor, tamanho, preço,habilidade):
        self.habilidade = habilidade
        super().__init__(nome, cor, tamanho, preço)
        
    def habilidades(self):
        print(f"O {self.nome} {self.habilidade}")

class Brinquedo9(Brinquedo):
    def __init__(self, nome, cor, tamanho, preço,habilidade):
        self.habilidade = habilidade
        super().__init__(nome, cor, tamanho, preço)
        
    def habilidades(self):
        print(f"O {self.nome} {self.habilidade}")
        
class Brinquedo10(Brinquedo):
    def __init__(self, nome, cor, tamanho, preço,habilidade):
        self.habilidade = habilidade
        super().__init__(nome, cor, tamanho, preço)
        
    def habilidades(self):
        print(f"O {self.nome} {self.habilidade}")
        
qualquer_Brinquedo = Brinquedo1("Buzz Lighyear","Branco","Medio",69.99,"Voaa")
qualquer_Brinquedo.brincar()
qualquer_Brinquedo.habilidades()

