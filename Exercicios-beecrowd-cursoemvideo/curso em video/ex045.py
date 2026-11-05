from random import choice
from time import sleep
print('======= JOKENPO =======')
maos = ['PEDRA', 'PAPEL', 'TESOURA']
eu = str(input('Escolha entre pedra, papel ou tesoura ')).upper()
aleatorio = choice(maos)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)
if eu not in maos:
    print('Escolha entre pedra, papel ou tesoura')
elif aleatorio == eu:
    print('EMPATE')
elif aleatorio == 'PEDRA' and eu == 'TESOURA':
    print('GANHEI, fui de {} e vc de {}'.format(aleatorio, eu))
elif aleatorio == 'TESOURA' and eu == 'PEDRA':
    print('VC GANHOU!, fui de {} e vc de {}'.format(aleatorio, eu))
elif aleatorio == 'PAPEL' and eu == 'PEDRA':
    print('GANHEI, fui de {} e vc de {}'.format(aleatorio, eu))
elif aleatorio == 'PEDRA' and eu == 'PAPEL':
    print('VC GANHOU!, fui de {} e vc de {}'.format(aleatorio, eu))
elif aleatorio == 'TESOURA' and eu == 'PAPEL':
    print('GANHEI, fui de {} e vc de {}'.format(aleatorio, eu))
elif aleatorio == 'PAPEL' and eu == 'TESOURA':
    print('VC GANHOU!, fui de {} e vc de {}'.format(aleatorio, eu))
