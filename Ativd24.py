import math

cateto_a = float(input("Digite o valor do cateto a: "))
cateto_b = float(input("Digite o valor do cateto b: "))
hipotenusa = math.sqrt(cateto_a ** 2 + cateto_b ** 2)
print("O valor da hipotenusa é:", hipotenusa)