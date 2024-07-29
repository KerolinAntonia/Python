class Pessoa:
    def __init__(self,matricula,nome,idade):
        self.matricula = matricula
        self.nome = nome
        self.idade = idade
        
class Aluno(Pessoa):
    def __init__(self, matricula, nome, idade):
        super().__init__(matricula, nome, idade)
        
    def estudar(self):
        print(f"O aluno {self.nome} está estudando.")
        
    def nota (self,n1,n2,n3,n4):
        print("Notas:",n1,n2,n3,n4)
        m = n1 + n2 + n3 + n4
        self.nota1 = m/4
        print(f"Nota:{self.nota1}")
        
class Professor(Pessoa):
    def __init__(self, matricula, nome, idade):
        super().__init__(matricula, nome, idade)
        
    def Formação(self,disciplina):
        self.disciplina = disciplina
        print(f"A disciplina do {self.nome} é {self.disciplina}") 
        
    def salario (self, carga, salario):
        self.carga = carga
        self.salario1 = salario
        print(f"O {self.nome} tem a carga horario de {self.carga} e recebe {self.salario1}")  
        
pessoa_aluno = Aluno(21212, "João Antonio",17)
pessoa_professor = Professor(22222,"Thiago",35)

pessoa_aluno.estudar()
pessoa_aluno.nota(2,5,6,9)

pessoa_professor.Formação("Matematica")
pessoa_professor.salario(48,30000)