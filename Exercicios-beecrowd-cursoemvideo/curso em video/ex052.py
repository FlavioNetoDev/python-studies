num = int(input('Digite um numero inteiro: '))
total = 0
for c in range(1, num + 1):
    if num % c == 0:
        total += 1
        print('\033[33m', end=' ')
    else:
        print('\033[31m', end=' ')
    print(f'{c}', end=' ')
print(f'\n\033[mO numero {num} foi divisível {total} vezes')
if total == 2:
    print('Por isso ele é primo')
else:
    print('Por isso ele não é primo')