'''termo = int(input('Digite o primeiro termo da PA: '))
razão = int(input('Digite a razao da PA: '))
print(termo)
for c in range(1, 10):
    termo += razão
    print(termo)
print('Acabou')'''

termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razao da PA: '))
decima = termo + (10 - 1) * razao
for c in range(termo, decima + razao, razao):
    print(f'{c}', end= ' > ')
print('Acabou')