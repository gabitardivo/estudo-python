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

def pesquisar(dicionario, chave):
    lista=dicionario.get(chave)
    if lista!=None:
        print("Nome...........: " + lista[0])
        print("Última estação.: " + lista[1])

def excluir(dicionario, chave):
    if dicionario.get(chave)!=None:
        del dicionario[chave]
    print("Objeto Eliminado")

def listar(dicionario):
    for chave, valor in dicionario.items():
        print("Objeto......")
        print("Login: ", chave)
        print("Dados: ", valor)