from unittest import result
from funcoes_iventario import *
inventario = {}
opcao = chamarMenu()
while opcao > 0 and opcao < 4:
    if opcao == 1:
        registrar(inventario)
    elif opcao == 2:
        persistir(inventario)
    elif opcao == 3:
        resultado = (exibir())
        for linha in resultado:
            separacao = linha[linha.find(",")+1:-1]
            data = separacao[0:separacao.find(",")]
            separacao = separacao[separacao.find(",")+1:-1]
            descricao = separacao[0:separacao.find(",")]
            departamento = linha[linha.rfind(",")+1:-1]
            print("Data.........: ", data)
            print("Descrição....: ", descricao)
            print("Departamento.: ", departamento)
            print("---------------------------------")
    opcao = chamarMenu()
