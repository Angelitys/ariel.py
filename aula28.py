import math

# 1. Comparação de dois números
def maior_numero(num1, num2):
    if num1 > num2:
        return num1
    elif num2 > num1:
        return num2
    else:
        return "Números iguais"

# 2. Calcular a raiz quadrada se o número for positivo
def calcular_raiz_quadrada(numero):
    if numero >= 0:
        return math.sqrt(numero)
    else:
        return "Número inválido"

# 3. Imprimir a raiz quadrada se positivo, senão o número ao quadrado
def calcular_resultado(numero):
    if numero >= 0:
        return math.sqrt(numero)
    else:
        return numero ** 2

# 4. Calcular e mostrar o quadrado e a raiz quadrada se o número for positivo
def calcular_quadrado_e_raiz(numero):
    if numero >= 0:
        quadrado = numero ** 2
        raiz = math.sqrt(numero)
        return quadrado, raiz
    else:
        return "Número negativo"

# 5. Verificar se um número inteiro é par ou ímpar
def verificar_paridade(numero):
    if numero % 2 == 0:
        return "Par"
    else:
        return "Ímpar"

# 6. Mostrar o maior número e a diferença entre eles
def maior_e_diferenca(num1, num2):
    maior = max(num1, num2)
    menor = min(num1, num2)
    diferenca = maior - menor
    return maior, diferenca

# 7. Mostrar o maior número, ou se forem iguais, "Números iguais"
def maior_numero_ou_iguais(num1, num2):
    if num1 > num2:
        return num1
    elif num2 > num1:
        return num2
    else:
        return "Números iguais"

# 8. Calcular a média de duas notas, verificando se são válidas
def calcular_media(nota1, nota2):
    if 0 <= nota1 <= 10 and 0 <= nota2 <= 10:
        return (nota1 + nota2) / 2
    else:
        return "Notas inválidas"

# 9. Verificar se a prestação de um empréstimo é maior que 20% do salário
def verificar_emprestimo(salario, prestacao):
    if prestacao > (salario * 0.2):
        return "Empréstimo não concedido"
    else:
        return "Empréstimo concedido"

# 10. Calcular a soma dos algarismos de um número inteiro
def soma_algarismos(numero):
    if numero > 0:
        soma = 0
        while numero > 0:
            soma += numero % 10
            numero //= 10
        return soma
    else:
        return "Número inválido"

# 11. Calcular o logaritmo de um número positivo
def calcular_logaritmo(numero):
    if numero > 0:
        return math.log(numero)
    else:
        return "Número inválido"

# 12. Calcular a média ponderada de duas provas e verificar se o aluno foi aprovado
def media_ponderada_e_aprovacao(nota1, nota2):
    media = (nota1 + (nota2 * 2)) / 3
    if media >= 70:
        return "Aprovado"
    else:
        return "Reprovado"

# 13. Calcular a média final de um aluno e verificar sua situação
def verificar_situacao_aluno(nota_lab, nota_semestral, nota_final):
    media = (nota_lab * 2 + nota_semestral * 3 + nota_final * 5) / 10
    if media < 3:
        return "Reprovado"
    elif media < 5:
        return "Recuperação"
    else:
        return "Aprovado"

# 14. Imprimir o dia da semana correspondente a um número (1 a 7)
def dia_da_semana(numero):
    dias = {1: "Domingo", 2: "Segunda-feira", 3: "Terça-feira", 4: "Quarta-feira", 5: "Quinta-feira", 6: "Sexta-feira", 7: "Sábado"}
    return dias.get(numero, "Número inválido")

# 15. Imprimir o mês correspondente a um número (1 a 12)
def mes_do_ano(numero):
    meses = {1: "Janeiro", 2: "Fevereiro", 3: "Março", 4: "Abril", 5: "Maio", 6: "Junho", 7: "Julho", 8: "Agosto", 9: "Setembro", 10: "Outubro", 11: "Novembro", 12: "Dezembro"}
    return meses.get(numero, "Número inválido")

# 16. Calcular a área de um trapézio
def area_trapezio(base_maior, base_menor, altura):
    if base_maior > 0 and base_menor > 0:
        return ((base_maior + base_menor) * altura) / 2
    else:
        return "Valores inválidos"

# 17. Realizar uma operação matemática escolhida pelo usuário
def operacao_matematica(operacao, num1, num2):
    if operacao == "+":
        return num1 + num2
    elif operacao == "-":
        return num1 - num2
    elif operacao == "*":
        return num1 * num2
    elif operacao == "/":
        return num1 / num2
    else:
        return "Operação inválida"

# 18. Verificar se um número é divisível por 3 ou por 5, mas não por ambos
def verificar_divisibilidade(numero):
    if numero % 3 == 0 and numero % 5 == 0:
        return "Divisível por 3 e por 5"
    elif numero % 3 == 0:
        return "Divisível apenas por 3"
    elif numero % 5 == 0:
        return "Divisível apenas por 5"
    else:
        return "Não é divisível por 3 nem por 5"

# 19. Verificar se três números formam um triângulo e classificar seu tipo
def classificar_triangulo(a, b, c):
    if a < b + c and b < a + c and c < a + b:
        if a == b == c:
            return "Triângulo Equilátero"
        elif a ==  b or a == c or b == c:
            return "Triângulo Isósceles"
        else:
            return "Triângulo Escaleno"
    else:
        return "Não é possível formar um triângulo"
    
import math

# 20. Verificar se um trabalhador pode se aposentar
def verificar_aposentadoria(idade, tempo_servico):
    if idade >= 65 or tempo_servico >= 30 or (idade >= 60 and tempo_servico >= 25):
        return "Pode se aposentar"
    else:
        return "Não pode se aposentar"

# 21. Verificar se um ano é bissexto
def verificar_bissexto(ano):
    if (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0):
        return "Ano bissexto"
    else:
        return "Não é ano bissexto"

# 22. Calcular o preço final de um produto com base no estado e valor
def calcular_preco_final(valor, estado):
    impostos = {"MG": 0.07, "SP": 0.12, "RJ": 0.15, "MS": 0.08}
    if estado in impostos:
        preco_final = valor * (1 + impostos[estado])
        return preco_final
    else:
        return "Estado inválido"

# 23. Classificar atleta de bocha rolada em categorias de idade
def classificar_atleta(idade):
    if idade >= 5 and idade <= 7:
        return "Infantil A"
    elif idade >= 8 and idade <= 10:
        return "Infantil B"
    elif idade >= 11 and idade <= 13:
        return "Juvenil A"
    elif idade >= 14 and idade <= 17:
        return "Juvenil B"
    else:
        return "Sênior"

# 24. Calcular o preço de estacionamento com base no tempo
def calcular_preco_estacionamento(chegada, partida):
    horas_estacionadas = math.ceil((partida - chegada).total_seconds() / 3600)
    if horas_estacionadas <= 2:
        return horas_estacionadas * 1.00
    elif horas_estacionadas <= 4:
        return 2 * 1.00 + (horas_estacionadas - 2) * 1.40
    else:
        return 2 * 1.00 + 2 * 1.40 + (horas_estacionadas - 4) * 2.00

# 25. Verificar se um número inteiro é divisível por 3 ou por 5, mas não por ambos
def verificar_divisibilidade(numero):
    if numero % 3 == 0 and numero % 5 == 0:
        return "Divisível por 3 e por 5"
    elif numero % 3 == 0:
        return "Divisível apenas por 3"
    elif numero % 5 == 0:
        return "Divisível apenas por 5"
    else:
        return "Não é divisível por 3 nem por 5"

# 26. Verificar se três números formam um triângulo e classificar seu tipo
def classificar_triangulo(a, b, c):
    if a < b + c and b < a + c and c < a + b:
        if a == b == c:
            return "Triângulo Equilátero"
        elif a == b or a == c or b == c:
            return "Triângulo Isósceles"
        else:
            return "Triângulo Escaleno"
    else:
        return "Não é possível formar um triângulo"


