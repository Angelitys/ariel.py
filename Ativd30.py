valor_hora_trabalho = float(input("Digite o valor da hora de trabalho: "))
horas_trabalhadas_mes = int(input("Digite o número de horas trabalhadas no mês: "))
salario_mes = valor_hora_trabalho * horas_trabalhadas_mes
salario_total = salario_mes + (salario_mes * 0.10)
print("O valor a ser pago ao funcionário é:", salario_total)
