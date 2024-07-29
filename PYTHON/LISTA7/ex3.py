class Aluno:
    
    def __init__(self, nome, ra,nota1,nota2,nota3,nota4):
        self.nome = nome
        self.ra = ra
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
        self.nota4 = nota4
        ns = []
        ns.append(nota1)
        ns.append(nota2)
        ns.append(nota3)
        ns.append(nota4)
        n = sum(ns)/len(ns)
        self.n = n
        
    def getMostrar_situacao(self):
        if self.n <= 5:
            print("Reprovou")
        elif self.n == 6:
            print("EXAME")
        elif self.n > 6:
            print("Aprovado")
            
            
aluno1 = Aluno("Marcos",5555,6,6,6,6)
aluno1.getMostrar_situacao()            
        
        