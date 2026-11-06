peso1 = int(input('Digite seu peso: '))
maior = peso1
menor = peso1
for c in range(4):
    peso = int(input('Digite seu peso: '))
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print(f'O maior peso registrado foi {maior}')
print(f'O menor peso registrado foi {menor}')