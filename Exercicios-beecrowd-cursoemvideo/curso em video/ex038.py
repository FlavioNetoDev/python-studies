n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))

if n1 > n2:
    print('{} eh maior que {}'.format(n1, n2))
elif n2 > n1:
    print('{} eh maior que {}'.format(n2, n1))
else:
    print('Nao existe valor maior, os dois sao iguais ')