def pessoa(**kwargs):
    for chave, valor in kwargs.items():
        print(f"{chave}:{valor}")

pessoa(Nome = "Kerolin",
       Sobrenome = "Antonia",
       Idade = "17",
       Email = "kerolinantonia123",
       Numero = "5555555555")
    