s = 0
cont = 0
for c in range(1, 7):
    prgnt = int(input('Digite um valor inteiro '))
    if prgnt % 2 == 0:
        s += prgnt
        cont += 1
print(f'A soma de todos os {cont} numeros pares digitados são {s}')
    