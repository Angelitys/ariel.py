N1= float(input("Aplique o valor da nota 1 da prova= "))
N2= float(input("Aplique o valor da nota 2 da prova= "))

media= 7.0
resultado= N1 +(N2 * 2) /3

if resultado >= 7.0:
    print("Aprovado") #Espaçamento se  chama identação
else:
    print("Reprovado")
    print("Sua média é=" , resultado)