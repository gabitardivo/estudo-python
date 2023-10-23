def perguntar():
    resposta = input(
        "\n <I> para inserir usuário"
        "\n <P> para procurar usuário"
        "\n <L> Para localizar o usuário"
        "\n <E> Para excluir usuário"
        "\n Digite opção desejada: ").upper()
    return  resposta

def inserir(dicionario):
    chave = input("Digite o login: ").upper()
    dicionario[chave] = [
        input("Digite o nome: ").upper(),
        input("Digite a estação: ")
    ]
    print(dicionario)
