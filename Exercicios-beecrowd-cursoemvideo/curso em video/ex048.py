s = 0
for numero in range(1, 501):
    if numero % 2 != 0 and numero % 3 == 0:
        s += numero
print(f'A soma de todos os 83 valores solicitados é {s}')