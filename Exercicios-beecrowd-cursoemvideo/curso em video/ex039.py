from datetime import date
idade = int(input('Digite seu ano de nascimento: '))
genero = input('Qual o seu genero?: ').lower()
atual = date.today().year
idade1 = atual - idade
if genero == 'feminino':
    print('Voce não precisa se alistar.')
    exit()
else:
    print('Voce tem que se alistar.')

print('Quem nasceu em {} tem {} anos em {}.'.format(idade, idade1, atual))
if idade1 < 18:
    saldo = 18 - idade1
    print('Ainda faltam {} ano para o seu alistamento'.format(saldo))
    ano = atual + saldo
    print('O seu alistamento será em {} '.format(ano))
elif idade1 == 18:
    print('Voce precisa se alistar imediatamente.')
elif idade1 > 18:
    saldo = idade1 - 18
    print('Voce ja deveria ter se alistado há {} anos.'.format(saldo))
    ano = atual - saldo
    print(f'Seu alistamento deveria ter sido em {ano}.') 