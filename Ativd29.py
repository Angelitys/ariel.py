dias_trabalhados = int(input("Digite o número de dias trabalhados: "))
salario_bruto = dias_trabalhados * 30
previdencia = salario_bruto * 0.11
salario_liquido = salario_bruto - previdencia
imposto_renda = salario_liquido * 0.08
salario_final = salario_liquido - imposto_renda
print("A quantia líquida a ser paga é:", salario_final)
