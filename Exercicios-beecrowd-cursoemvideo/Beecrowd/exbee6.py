valor = int(input())
original = valor

notas100 = valor // 100 
valor = valor % 100

notas50 = valor // 50
valor = valor % 50

notas20 = valor // 20
valor = valor % 20

notas10 = valor // 10
valor = valor % 10

notas5 = valor // 5
valor = valor % 5

notas2 = valor // 2
valor = valor % 2

notas1 = valor // 1
valor = valor % 1

print(original)
print('{} nota(s) de R$ 100,00'.format(notas100))
print('{} nota(s) de R$ 50,00'.format(notas50))
print('{} nota(s) de R$ 20,00'.format(notas20))
print('{} nota(s) de R$ 10,00'.format(notas10))
print('{} nota(s) de R$ 5,00'.format(notas5))
print('{} nota(s) de R$ 2,00'.format(notas2))
print('{} nota(s) de R$ 1,00'.format(notas1))
