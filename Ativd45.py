nome_aluno = input("Digite o nome do aluno: ")
nota_prova = float(input("Digite a nota da prova: "))
nota_qualitativa = float(input("Digite a nota qualitativa: "))
media = (nota_prova * 2 + nota_qualitativa) / 3
print("Média do aluno", nome_aluno, "na disciplina de ED:", media)
