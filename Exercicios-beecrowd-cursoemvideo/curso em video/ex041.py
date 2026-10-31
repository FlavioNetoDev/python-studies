idade = int(input('Qual sua idade? '))

if idade >= 1 and idade <= 9:
    print('MIRIM')
elif idade >= 10 and idade <= 14:
    print('INFANTIL')
elif idade >= 14 and idade <= 19:
    print('JUNIOR')
elif idade >= 19 and idade <= 20:
    print('SENIOR')
else:
    print('MASTER')