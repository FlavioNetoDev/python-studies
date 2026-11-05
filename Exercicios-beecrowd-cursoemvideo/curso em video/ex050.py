s = 0
for c in range(1, 7):
    prgnt = int(input('Digite um valor inteiro '))
    if prgnt % 2 == 0:
        s += prgnt
print(f'A soma de todos os numeros pares digitados são {s}')
    