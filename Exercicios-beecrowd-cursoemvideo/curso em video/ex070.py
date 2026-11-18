print('-' * 20)
print('LOJA SUPER BARATA')
print('-' * 20)
total = mil = barato = 0
resp = 'S'
while True:
    produto = str(input('Nome do Produto: ')).strip()
    preço = float(input('Preço: '))

    if barato == 0 or preço < barato:
        barato = preço

    if preço >= 1000:
        mil += 1
    total += preço

    continuar = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if continuar == 'S':
        continue
    elif continuar == 'N':
        break
print(f'O total da compra foi {total:.2f}')
print(f'Temos {mil} produtos custando mais de 1000,00')
print(f'O produto mais barato foi de {barato:.2f}')