from random import randint
print('-' * 20)
print('VAMOS JOGAR PAR OU IMPAR')
print('-' * 20)
cont = 0
while True:
    valor = int(input('Diga um valor: '))
    computador = randint(1, 10)
    imparpar = str(input('Par ou Impar? [P/I] ')).upper().strip()[0]
    resultado = valor + computador
    if imparpar in 'Ii':
        if resultado % 2 != 0:
            print('-' * 20)
            print(f'Eu joguei {computador} e voce {valor}')
            print('Deu IMPAR voce GANHOU!')
            print('Vamos jogar novamente...')
            print('-' * 20)
            cont +=1
        else:
            print('-' * 20)
            print(f'Eu joguei {computador} e voce {valor}')
            print('Deu PAR, eu VENCI')
            print('-' * 20)
            break
    elif imparpar in 'Pp':
        if resultado % 2 == 0:
            print('-' * 20)
            print(f'Eu joguei {computador} e voce {valor}')
            print('Deu PAR voce GANHOU!')
            print('Vamos jogar novamente...')
            print('-' * 20)
            cont +=1
        else:
            print('-' * 20)
            print(f'Eu joguei {computador} e voce {valor}')
            print('Deu IMPAR, eu VENCI')
            print('-' * 20)
            break
print(f'Voce conquistou {cont} Vitorias consecutivas!')