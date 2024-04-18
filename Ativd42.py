custo_fabrica = float(input("Digite o custo de fábrica do carro: "))
porcentagem_distribuidor = 0.12
porcentagem_impostos = 0.45
custo_consumidor = custo_fabrica + (custo_fabrica * porcentagem_distribuidor) + (custo_fabrica * porcentagem_impostos)
print("O custo ao consumidor é:", custo_consumidor)
