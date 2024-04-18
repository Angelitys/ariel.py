nome_vendedor = input("Digite o nome do vendedor: ")
carros_vendidos = int(input("Digite o número de carros vendidos: "))
valor_total_vendas = float(input("Digite o valor total das vendas: "))

salario_fixo = 500.00
comissao_carro = carros_vendidos * 50.00
comissao_vendas = valor_total_vendas * 0.05

salario_total = salario_fixo + comissao_carro + comissao_vendas
print("Salário do vendedor", nome_vendedor, "no mês é:", salario_total)
