#Login
while True:
    matricula1 = input("Matrícula: ")
    matricula2 = ["000000","142421","141516","999999"]
    senha1 = input("Senha: ")
    senha2 = ["123456"]
    
    if matricula1 in matricula2:
        matricula2 = matricula1
    if  senha1 in senha2:
            senha2 = senha1
            print("Iniciando sistema...")
    else:
        print ("Usuario Inválido \n Cadastra-se agora")
        sem_cadastro = input("Cadastrar agora? ")
        if sem_cadastro == "sim" or "Sim":
            
            #Cadastro do Usuario
            nomes = []
            emails = []
            nome = input("Nome Completo: ")
            nomes.append(nome)
            matricula = int(input("Matrícula: "))
            matricula2.append(matricula)
            email = input("E-mail: ")
            emails.append (email)
            c_senha = input("Criar senha: ")
            conf_senha = input("Confirma senha: ")
            while conf_senha != c_senha:
                print("Senha inválida")
                conf_senha = input("Confirma senha: ")
                if conf_senha == c_senha:
                    print("Cadastrado!")
                    break

        else:
            if sem_cadastro == "não" or "Não":
                print("Fim do Programa")
                break
    #Pagina Incial
    print ("Bem-Vindo")

    produtos_disponiveis = ['Computador', 'Mouse', 'Teclado']
    quantidade = [5,6,9]
    while True:
        print ("Selecione oque deseja fazer:")
        f = input(" (A)Cadastrar Produto \n (B)Editar produto \n (C)Excluir \n (D)Registro_produtos_disponiveis \n (E)Sair\n")
        #Cadastrar produto
        if f == "A" :
            nome_produto = input("Nome do produto: ")
            produtos_disponiveis.append(nome_produto)
            quantidade_nova = int(input("Quantidade:"))
            quantidade.append(quantidade_nova)

        #Editar produto
        if f == "B" :
            nome_produto = input("Nome do Produto:")
            for item in range(len(produtos_disponiveis)):
                if produtos_disponiveis[item] == nome_produto:
                    quantidade_nova = int(input("Qual a quantidade total nova do produto:"))
                    quantidade[item] = quantidade_nova


        #Excluir produto
        if f == "C":
            nome_produto = input("Nome do produto:")
            for item in range(len(produtos_disponiveis)):
                if produtos_disponiveis[item] == nome_produto:
                    produtos_disponiveis.remove(nome_produto)
                    quantidade.pop(item)
                    print("Produtos atuais / Quantidade de cada um",produtos_disponiveis,quantidade)
                    break
        #Registro de produtos disponíveis
        if f == "D":
            print("Nome, Quantidade")
            for item in range(len(produtos_disponiveis)):
                print(produtos_disponiveis[item],quantidade[item])

        #Sair
        if f == "E":
            print ("Fim do Programa")
            break
        else:
            print("Voltando")