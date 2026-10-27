velocidade = int(input('A quantos km voce ultrapassou o radar? '))
radar = 80

if velocidade >= 80:
    multa = (80 - velocidade) * 7
    print('O maximo de km/h foram ultrapassados, multa no valor de {}'.format(multa))

else:
    print('Voce esta no limite da via {}.'.format(velocidade))