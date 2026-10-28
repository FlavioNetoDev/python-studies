numero1 = int(input('Digite um valor: '))
numero2 = int(input('Digite outro valor: '))
numero3 = int(input('Digite mais um valor: '))

if numero1 > numero2 and numero1 > numero3:
    if numero2 < numero3:
        print('o menor eh {} e o maior eh {}'.format(numero2, numero1))
    else:
        print('o menor eh {} e o maior eh {}'.format(numero3, numero1))
elif numero2 > numero1 and numero2 > numero3:
    if numero1 < numero3:
        print('o menor eh {} e o maior eh {}'.format(numero1, numero2))
    else:
        print('o menor eh {} e o maior eh {}'.format(numero3, numero2))
elif numero3 > numero1 and numero3 > numero2:
    if numero1 < numero2:
        print('o menor eh {} e o maior eh {}'.format(numero1, numero3))
    else:
        print('o menor eh {} e o maior eh {}'.format(numero2, numero3))