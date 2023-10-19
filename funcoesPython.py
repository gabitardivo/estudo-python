inventario=[]

#adicionar item no inventario
def adicionarItem(lista):
  resposta = "S"  
  while resposta == "S":
    equipamento=[
      input("Equipamento: "),
      float(input("Valor: ")),
      int(input("Número Serial: ")),
      input("Departamento: ")]
    lista.append(equipamento)
    resposta = input("Digite \"S\" para continuar: ").upper()

#exibir dados do inventário
def exibirInventario(lista):
  for elemento in lista:
    print("Nome.........: ", elemento[0])
    print("Valor........: ", elemento[1])
    print("Serial.......: ", elemento[2])
    print("Departamento.: ", elemento[3])

#localizar um item no inventario
def buscarItem(lista):
  busca=input("Digite o nome do equipamento que deseja buscar: ")
  for elemento in lista:
    if busca==elemento[0]:
      print("Valor..: ", elemento[1])
      print("Serial.:", elemento[2])

#depreciar itens no inventario
def depreciarItem(lista):
  depreciacao=input("Digite o nome do equipamento que será depreciado: ")
  for elemento in lista:
    if depreciacao==elemento[0]:
      print("Valor antigo: ", elemento[1])
      elemento[1] = elemento[1] * 0.9
      print("Novo valor: ", elemento[1])

#excluir um item do inventario
def excluirItem(lista):
  serial=int(input("Digite o serial do equipamento que será excluído: "))
  for elemento in lista:
    if elemento[2]==serial:
      inventario.remove(elemento)

#resumo de valores do inventário
def resumoValores(lista):
  valores=[]
  for elemento in lista:
    valores.append(elemento[1])
  if len(valores)>0:
    print("O equipamento mais caro custa: ", max(valores))
    print("O equipamento mais barato custa: ", min(valores))
    print("O total de equipamentos é de: ", sum(valores))