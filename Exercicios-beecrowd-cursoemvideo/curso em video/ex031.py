distancia = int(input('Quantos kms é a sua viagem?: '))

if distancia >= 200:
    preco = 0.50
    print('O preco da sua viagem baseado nos kms rodados foi {}'.format(preco * distancia))
elif distancia < 200:
    preco = 0.45
    print('O preco da sua viagem baseado nos kms rodados foi {}'.format(preco*distancia))