media_aprovacao = 7
primeira_avaliacao = float(input("Digite a nota da primeira avaliação: "))
segunda_avaliacao = (media_aprovacao * 3 - primeira_avaliacao) / 2
print("Nota necessária na segunda avaliação para aprovação:", segunda_avaliacao)