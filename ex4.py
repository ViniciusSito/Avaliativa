
"""
Nessa questão de cadastro de usuarios utilizo bando de dados e disponibilizado pelo professor, utilizo a opção 1 onde a função retorna o dicionário
gerado e armazenar no dicionário global chamado banco_usuarios
"""
banco_de_dados = []

def cadastrar_usuario(campos_obrigatorios):
    usuario = {}
    
    print("Cadastro de Usuário")
    for campo in campos_obrigatorios:
        valor = input(f"Digite o valor para '{campo}': ")
        usuario[campo] = valor
    
    while True:
        campo_adicional = input("Digite um campo adicional ou 'sair' para encerrar: ")
        if campo_adicional.lower() == "sair":
            break
        valor_adicional = input(f"Digite o valor para '{campo_adicional}': ")
        usuario[campo_adicional] = valor_adicional
    
    banco_de_dados.append(usuario)
    print("Usuário cadastrado com sucesso!")

def imprimir_usuarios():
    print("\nLista de Usuários Cadastrados:")
    for usuario in banco_de_dados:
        print("\n---")
        for campo, valor in usuario.items():
            print(f"{campo}: {valor}")

while True:
    print("\nMenu:")
    print("1 - Cadastrar Usuário")
    print("2 - Imprimir Usuários")
    print("0 - Encerrar")
    
    escolha = input("Digite a opção desejada: ")
    
    if escolha == "1":
        campos_obrigatorios = input("Digite os campos obrigatórios (separados por vírgula): ").split(",")
        cadastrar_usuario(campos_obrigatorios)
    elif escolha == "2":
        imprimir_usuarios()
    elif escolha == "0":
        break
    else:
        print("Opção inválida. Tente novamente.")