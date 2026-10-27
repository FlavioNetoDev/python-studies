'''import math
angulo = float(input('Digite o valor do seu angulo: '))

seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print('O valor do seno do angulo {:.2f} eh equivalente a {:.2f}'.format(angulo, seno))
print('O valor do cosseno do angulo {:.2f} eh equivalente a {:.2f}'.format(angulo, cosseno))
print('O valor da tangente do angulo {:.2f} eh equivalente a {:.2f}'.format(angulo, tangente))'''

from math import radians, sin, cos, tan

angulo = float(input('Digite o angulo: '))

seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print('O seno do seu angulo {} eh {:.2f}'.format(angulo, seno))
print('O cosseno do seu angulo {} eh {:.2f}'.format(angulo, cosseno))
print('A tangente do seu angulo eh {} {:.2f}'.format(angulo, tangente))
