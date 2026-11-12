import random
from time import sleep
print('-=' * 30)
print('\033[7;32;34mTente adivinhar o numero de 1 a 10 que estou pensando:\033[m ')
print('-=' * 30)
numero = random.randint(1, 10)
qual = int(input('Qual o numero que eu escolhi? '))
print('Processando...')
sleep(2)
while qual != numero:
    qual = int(input('Voce errou, digite o numero que eu estou pensando novamente: '))
    print('Processando...')
    sleep(2)
print(f'ACERTOU! eu escolhi exatamento o {qual}')
print('\033[7;32;34mFim\033[m')
print('-=' * 30)
