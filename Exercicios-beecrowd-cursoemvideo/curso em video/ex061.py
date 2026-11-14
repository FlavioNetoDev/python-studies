termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razao da PA: '))
cont = 1
while cont <= 10:
    print(termo, end=' > ')
    cont += 1
    termo += razao
print('FIM')