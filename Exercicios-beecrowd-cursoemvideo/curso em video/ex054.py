maior = 0
menor = 0
from datetime import date
for c in range(7):
    nascimento = int(input('Digite seu ano de nascimento: '))
    atual = date.today().year
    idade = atual - nascimento
    if idade < 21:
        menor += 1
    else:
        maior += 1
print(f'{maior} Ja são maiores de idade')
print(f'{menor} Pessoas ainda não são maiores de idade: ')