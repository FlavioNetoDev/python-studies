import random
from time import sleep
print('-=-' * 20)
print('Tente adivinhar um número de 1 a 5 que eu estou pensando.')
print('-=-' * 20)
numero = random.randint(1, 5)
qual = int(input('Qual foi o numero que eu escolhi? '))
print('Processando...')
sleep(3)
if qual == numero:
    print('CORRETO! O numero que eu pensei foi exatamente o {}'.format(numero))
else:
    print('PERDEU! O numero que eu pensei foi o {} e não o {}'.format(numero, qual))