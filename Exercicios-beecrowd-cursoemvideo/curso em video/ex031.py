distancia = int(input('Quantos kms é a sua viagem?: '))

if distancia >= 200:
    preco = 0.45
    print('Sua viagem vai custar R$ {:.2f}'.format(preco * distancia))
else:
    preco = 0.50
    print('Sua viagem vai custar R$ {:.2f}'.format(preco * distancia))