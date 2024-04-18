import math

altura_degrau = float(input("Digite a altura do degrau da escada: "))
altura_objetivo = float(input("Digite a altura que deseja alcançar subindo a escada: "))
quantidade_degraus = math.ceil(altura_objetivo / altura_degrau)
print("Quantidade de degraus a subir:", quantidade_degraus)