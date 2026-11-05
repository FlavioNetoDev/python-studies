termo = int(input('Digite o primeiro termo da PA: '))
razão = int(input('Digite a razao da PA:'))
print(termo)
for c in range(1, 10):
    termo += razão
    print(termo)