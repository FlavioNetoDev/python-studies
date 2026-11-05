primo = int(input('Digite um numero inteiro: '))
total = 0
for c in range(1, primo + 1):
    if primo % c == 0:
        total += 1
if total == 2:
     print(f'{primo} = Primo')
else:
    print(f'{primo} = Nao eh primo')
