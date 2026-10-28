velocidade = int(input('A quantos km voce ultrapassou o radar? '))
if velocidade >= 80:
    print('MULTADO! Voce excedeu o limite permitido que é de 80km/h')
    multa = (velocidade - 80) * 7
    print('O maximo de km/h foram ultrapassados, multa no valor de R$ {}'.format(multa))
print('Voce esta no limite da via, tenha um bom dia. {}'.format(velocidade))