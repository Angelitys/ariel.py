hora_inicio = input("Digite o horário de início (HH:MM:SS): ").split(":")
duracao_segundos = int(input("Digite a duração em segundos: "))
hora_fim = int(hora_inicio[0]), int(hora_inicio[1]), int(hora_inicio[2]) + duracao_segundos