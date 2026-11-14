'''num = int(input('Digite o valor que deseja calcular a fatorial: '))
c = num
resultado = 1
print(f'Calculando {num}! = ', end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    resultado *= c
    c -= 1
print(resultado)'''

'''from math import factorial
n = int(input('Digite um numero para calcular seu fatorial: '))
f = factorial(n)
print(f'O fatorial de {n} eh {f}')'''

'''n = int(input('Digite o valor que deseja calcular seu fatorial '))
f = 1
print(f'Calculando {n}!', end=' = ')
for c in range(n, 1, -1):
    print('{}'.format(c), end= '')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
print(f)'''