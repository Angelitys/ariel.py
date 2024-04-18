salario_base = float(input("Digite o salário-base do funcionário: "))
gratificacao = salario_base * 0.05
imposto = salario_base * 0.07
salario_receber = salario_base + gratificacao - imposto
print("O salário a receber é:", salario_receber)