import re

def validar_senha(senha):
    if len(senha) < 8:
        print("A senha deve ter pelo menos 8 caracteres.")
        return False
    if not re.search("[a-z]", senha):
        print("A senha deve conter pelo menos uma letra minúscula.")
        return False
    if not re.search("[A-Z]", senha):
        print("A senha deve conter pelo menos uma letra maiúscula.")
        return False
    if not re.search("[0-9]", senha):
        print("A senha deve conter pelo menos um número.")
        return False
    return True

def obter_credenciais():
    nome_usuario = input("Digite o nome de usuário: ")
    senha_valida = False
    while not senha_valida:
        senha = input("Digite a senha: ")
        senha_valida = validar_senha(senha)
        if not senha_valida:
            print("Por favor, tente novamente.")
    print("Usuário e senha cadastrados com sucesso!")

if __name__ == "__main__":
    obter_credenciais()
