from time import sleep
print('-='*20)
print('Analisador de Triangulos')
print('-='*20)
lado1 = int(input())
lado2 = int(input())
lado3 = int(input())
print('Processando...')
sleep(3)
s = lado1 + lado2 + lado3 

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    print('Formam um triangulo')
else:
    print('Não formam um triangulo')