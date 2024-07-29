class Filme:
    def __init__(self, nome, duracao):
        self.nome = nome
        self.duracao = duracao

    def play(self):
        print(f"Iniciando o filme: {self.nome}, que tem duração de {self.duracao} minutos.")


class Acao(Filme):
    def __init__(self, nome, duracao):
        super().__init__(nome, duracao)

    def explodir(self):
        print(f"Explosão em {self.nome}!")


class Drama(Filme):
    def __init__(self, nome, duracao):
        super().__init__(nome, duracao)

    def chorar(self):
        print(f"Chorando durante o filme {self.nome}.")


class Suspense(Filme):
    def __init__(self, nome, duracao):
        super().__init__(nome, duracao)

    def assustar(self):
        print(f"Assustador! {self.nome} está te deixando na ponta da cadeira!")


filme_acao = Acao("Missão Impossível", 120)
filme_drama = Drama("A Procura da Felicidade", 117)
filme_suspense = Suspense("O Silêncio dos Inocentes", 118)

filme_acao.play()
filme_acao.explodir()

filme_drama.play()
filme_drama.chorar()

filme_suspense.play()
filme_suspense.assustar()
