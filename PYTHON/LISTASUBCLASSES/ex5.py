class Pessoa:
    def __init__(self,nome,telefone,email,endereço):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereço = endereço
        
    def negociar(self):
        print("Vamos gastar dinheiro?")
        
class PessoaFisica(Pessoa):
    def __init__(self, nome, telefone, email, endereço,cpf):
        self.cpf = cpf
        super().__init__(nome, telefone, email, endereço)
        
    def fechanegocio(self):
        print(f"Eu, {self.nome} portador do cpf {self.cpf},resido {self.endereço}, declaro que aceito os termos desse contrato.\n Email: {self.email}")
        
class PessoaJuridica(Pessoa):
    def __init__(self, nome, telefone, email, endereço,cnpj):
        self.cnpj = cnpj
        super().__init__(nome, telefone, email, endereço)
        
    def fechanegocio1(self):
        print(f"Eu, {self.nome} portador do cnpj {self.cnpj},resido {self.endereço}, declaro que aceito os termos desse contrato.\n Email: {self.email}")
            
        
pessoa_fisica = PessoaFisica("Kerolin",679944444444,"keroi123@gmail.com","Avendida Afonso Pena Numero 8888","05096478123")
pessoa_fisica.negociar()
pessoa_fisica.fechanegocio()

pessoa_juridica = PessoaJuridica("Kerolin",679944444444,"keroi123@gmail.com","Avendida Afonso Pena Numero 8888","099962316468-3123")
pessoa_juridica.negociar()
pessoa_juridica.fechanegocio1()