segundos = int(input("Digite um valor inteiro em segundos: "))
horas = segundos // 3600
segundos_rest = segundos % 3600
minutos = segundos_rest // 60
segundos_final = segundos_rest % 60
print("Horas:", horas)
print("Minutos:", minutos)
print("Segundos:", segundos_final)