num1 = int(input('Digite um numero inteiro: '))
print('-=' * 10)

for c in range(1, 11):
    tabuada = num1 * c
    print(f'{num1} x {c} = {tabuada}')
print('-=' * 10)