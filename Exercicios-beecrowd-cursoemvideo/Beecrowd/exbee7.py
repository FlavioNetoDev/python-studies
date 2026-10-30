segundos = int(input())
horas = segundos // 3600
minutos = (segundos % 3600) // 60
segundosrestantes = segundos % 60

print('{}:{}:{}'.format(horas, minutos, segundosrestantes))