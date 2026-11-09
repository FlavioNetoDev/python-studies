peso1 = float(input('Digite o peso da 1 pessoa: '))
maior = peso1
menor = peso1
for c in range(2, 6):
    peso = float(input(f'Digite o peso da {c} pessoa: '))
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print(f'O maior peso registrado foi {maior}')
print(f'O menor peso registrado foi {menor}')