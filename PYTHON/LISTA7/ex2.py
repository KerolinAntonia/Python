class Livro:
    def __init__(self,nome,autor,editora,paginas):
        self.nome = nome
        self.autor = autor
        self.editora = editora
        self.paginas = paginas
        
    def setAlterar_editor(self,autor):
        self.autor = autor
        print (f"Editora: {self.autor}")
        
    def getListar_qtde_paginas(self):
        print (f"{self.paginas} paginas do livro {self.nome}")
        
livro1 = Livro("PEQUENO PRINCIPE", "Antoine","HarperCollins",96)
livro1.getListar_qtde_paginas()
livro1.setAlterar_editor("Brasil")