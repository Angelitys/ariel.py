investimento1 = float(input("Investimento do primeiro apostador: "))
investimento2 = float(input("Investimento do segundo apostador: "))
investimento3 = float(input("Investimento do terceiro apostador: "))
premio = float(input("Valor do prêmio: "))

total_investido = investimento1 + investimento2 + investimento3
porcentagem1 = investimento1 / total_investido
porcentagem2 = investimento2 / total_investido
porcentagem3 = investimento3 / total_investido

ganho1 = premio * porcentagem1
ganho2 = premio * porcentagem2
ganho3 = premio * porcentagem3

print("O primeiro apostador ganharia:", ganho1)
print("O segundo apostador ganharia:", ganho2)
print("O terceiro apostador ganharia:", ganho3)