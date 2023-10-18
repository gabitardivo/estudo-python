equipamento =[]
valor = []
departamento = []
continuar = "S"

# cadastro equipamentos
while continuar =="S":
    equipamento.append(input("Equipamento: "))
    valor.append(float(input("Valor: ")))
    departamento.append(input("Departamento: "))
    continuar = (input("Continuar a cadastrar?: ")).upper()

# busca equipamento
#busca = input("Digite equipamento a ser encontrado: ")
#for x in range(0, len(equipamento)):
#    if busca == equipamento[x]:
#        print("\nEquipamento encontrado: ", equipamento[x])
#        print("Com valor de R$: ", valor[x])
#        print("Pertence ao Departamento: ", departamento[x])

# Equipamento desvalorizado
#abaixarValor = input("Digite o equipamento que irá abaixar valor: ")
#for x in range(0,len(equipamento)):
#    if abaixarValor == equipamento[x]:
#        print("Antigo valor R$: ", valor[x])
#       valor[x]= valor[x] * 0.9
#        print("Novo valor R$: ", valor[x])

# Deletar equipamento
deletarEquipamento = input("Digite equipamento a ser deletado: ")
for x in range(0,len(equipamento)):
    if equipamento[x] == deletarEquipamento:
        del equipamento[x]
        del valor[x]
        del departamento[x]
        break

# print da lista
for x in range(0,len(equipamento)):
    print("\tEquipamento:....:", equipamento[x])
    print("\tValor:........R$:", valor[x])
    print("\tDepartamento:...:", departamento[x])
    x=x+1