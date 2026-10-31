idade = int(input('Digite seu ano de nascimento: '))
idade1 = 2026 - idade

if idade1 < 18:
    print('Voce ainda vai se alistar ')
elif idade1 == 18:
    print('Ja eh hora de se alistar')
elif idade1 > 18:
    print('Ja passou da hora de se alistar ')