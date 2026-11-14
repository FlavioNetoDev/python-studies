resp = 'S'
media = soma = quant = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um numero: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
media = soma / quant
print(f'Voce digitou {quant} numeros')
print(f'A media foi {media}')
print(f'O maior valor foi {maior} e o menor foi {menor}')
