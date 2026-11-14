'''cont = -1
soma = 0
numero = 1
while numero != 999:
    cont += 1
    if numero != 999:
        numero = int(input('Digite um numero: '))
        if numero != 999:
            soma += numero
print(f'Voce digitou {cont} numeros')
print(f'A soma dos numeros digitados foi de {soma}')'''

núm = soma = cont = 0
núm = int(input('Digite um numero [999 para parar:] '))
while núm != 999:
    soma += núm
    cont += 1
    núm = int(input('Digite um numero [999 para parar:] '))
print(f'Voce digitou {cont} numeros e a soma entre eles eh {soma}')
print('Acabou')