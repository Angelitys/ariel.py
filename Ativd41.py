comprimento = float(input("Digite o comprimento do terreno em metros: "))
largura = float(input("Digite a largura do terreno em metros: "))
preco_metro_tela = float(input("Digite o preço do metro de tela: "))
custo_cercamento = 2 * (comprimento + largura) * preco_metro_tela
print("O custo para cercar o terreno é:", custo_cercamento)
