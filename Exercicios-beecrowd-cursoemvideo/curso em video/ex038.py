n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))

if n1 > n2:
    print('\033[0;35;46m{} eh maior que {}\033[m'.format(n1, n2))
elif n2 > n1:
    print('\033[0;41;47m{} eh maior que {}\033[m'.format(n2, n1))
else:
    print('\033[0;33;41mNao existe valor maior, os dois sao iguais\033[m ')