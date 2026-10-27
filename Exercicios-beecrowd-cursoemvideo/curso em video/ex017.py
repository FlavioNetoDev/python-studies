from math import hypot
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))

hipotenusa = hypot(co, ca)
print('O valor da hipotenusa eh {:.2f}'.format(hipotenusa))