maior = 0
menor = 0
from datetime import date
for c in range(1, 8):
    nascimento = int(input(f'Em que a no a {c} nasceu?: '))
    atual = date.today().year
    idade = atual - nascimento
    if idade <= 21:
        menor += 1
    else:
        maior += 1
print(f'{maior} Ja são maiores de idade')
print(f'{menor} Pessoas ainda não são maiores de idade: ')