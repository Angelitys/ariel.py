import math

altura_cilindro = float(input("Digite a altura do cilindro: "))
raio_cilindro = float(input("Digite o raio do cilindro: "))
volume_cilindro = math.pi * (raio_cilindro ** 2) * altura_cilindro
print("O volume do cilindro é:", volume_cilindro)