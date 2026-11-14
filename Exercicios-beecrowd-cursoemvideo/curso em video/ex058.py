import random
from time import sleep
print('-=' * 30)
print('\033[7;32;34mTente adivinhar o numero de 1 a 10 que estou pensando:\033[m ')
print('-=' * 30)
palpites = 0
numero = random.randint(1, 10)
acertou = False
while not acertou:
    qual = int(input('Qual numero estou pensando?: '))
    palpites += 1
    if qual == numero:
        acertou = True
    else:
        if qual > numero:
            print('Menos... Tente novamente')
        else:
            print('Mais... Tente novamente')
print(f'ACERTOU! com {palpites} palpites, parabéns! ')
